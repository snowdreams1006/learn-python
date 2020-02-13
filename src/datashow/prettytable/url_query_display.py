# -*- coding: utf-8 -*-
from urllib.parse import urlparse, parse_qs, parse_qsl
from prettytable import PrettyTable
import numpy as np 

def simple_table_demo():
    ''''
    展示美化表格简单示例
    '''
    table = PrettyTable()
    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_row(["Adelaide",1295, 1158259, 600.5])
    table.add_row(["Brisbane",5905, 1857594, 1146.4])
    table.add_row(["Darwin", 112, 120900, 1714.7])
    table.add_row(["Hobart", 1357, 205556,619.5])

    print('>>>simple_table_demo<<<')
    print(table)

def sorted_table_demo():
    '''
    展示按照指定字段排序后的表格
    '''
    table = PrettyTable()
    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_row(["Adelaide",1295, 1158259, 600.5])
    table.add_row(["Brisbane",5905, 1857594, 1146.4])
    table.add_row(["Darwin", 112, 120900, 1714.7])
    table.add_row(["Hobart", 1357, 205556,619.5])

    print('>>>sorted_table_demo<<<')
    print(table)

    # 按照人口进行正向排序
    sorted_table = table.get_string(sortby="Population", reversesort=False)

    print('>>>按照人口进行正向排序(sortby="Population", reversesort=False)<<<')
    print(sorted_table)

def selected_table_demo():
    '''
    筛选出特定表格进行美化展示
    '''
    table = PrettyTable()
    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_row(["Adelaide",1295, 1158259, 600.5])
    table.add_row(["Brisbane",5905, 1857594, 1146.4])
    table.add_row(["Darwin", 112, 120900, 1714.7])
    table.add_row(["Hobart", 1357, 205556,619.5])

    print('>>>selected_table_demo<<<')
    print(table)

    # 按照标题进行筛选
    selected_table = table.get_string(fields=["Area", "Population"])

    print('>>>按照标题进行筛选["Area", "Population"]<<<')
    print(selected_table)

def simple_url_parse_demo():
    '''
    解析 url 链接参数简单示例
    '''
    # get 查询 url
    url_get = 'https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=dDNClw4tBKGU7hAZx-XpOBq5DoWF5WJ2TK8edBMLq4o&FMQw=0&q4f3=zh-CN&VySQ=FGEMmxz6TAvkuerBSuVfLd-w01fSfGxM&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581465946282'

    # 解析 url参数信息,主要提取请求路径,查询参数
    path = urlparse(url_get).path
    query = urlparse(url_get).query

    print(">>>simple_url_parse_demo<<<")
    print(path,query)

    # 查询参数解析成字典形式
    query_dict = parse_qs(query)

    print(">>>query_dict<<<")
    print(query_dict)

    # 查询参数解析成列表形式
    query_list = parse_qsl(query)

    print(">>>query_list<<<")
    print(query_list)

def get_urls_with_query_params(urls):
    # 提取有效链接
    valid_urls = []

    # 无效请求数据
    if not urls:
        return valid_ulrs

    # 先去除首尾空格再按照换行符分隔
    urls = urls.strip().split('\n')
    # 针对单个链接剔除首尾空格
    for url in urls:
        valid_url = url.strip()
        if valid_url:
            valid_urls.append(valid_url)
    return valid_urls

def parse_urls_with_query_params(urls):
    '''
    批量解析有效 url 并处理成 prettytable的表头和数据
    '''
    # 提取有效链接
    valid_urls = get_urls_with_query_params(urls)
    if not valid_urls or len(valid_urls) == 0:
        return None

    # 全部url 查询参数列表
    origin_query_param_list = []
    for valid_url in valid_urls: 
        # url 查询参数可能不完全相同
        query = urlparse(valid_url).query
        query_list = parse_qsl(query)
        # 不论解析结果,直接添加到原始解析列表
        origin_query_param_list.append(query_list)

    # 查询参数标题,即提取出最长查询参数列表
    query_param_list = []
    longest_query_param_set = set()
    for origin_query_param_item in origin_query_param_list: 
        for origin_query_param_detail_item in origin_query_param_item: 
            longest_query_param_set.add(origin_query_param_detail_item[0])
    query_param_list = list(longest_query_param_set)

    # 查询参数数据,注意顺序保持一致!
    query_value_list = []
    for origin_query_param_item in origin_query_param_list:
        query_value_item = []
        for query_param_item in query_param_list: 
            has_find_valid_param_value_flag = False
            for origin_query_param_detail_item in origin_query_param_item: 
                name = origin_query_param_detail_item[0]
                value = origin_query_param_detail_item[1]
                if query_param_item == name:
                    has_find_valid_param_value_flag = True
                    query_value_item.append(value)
                    break
            # 参数不足时补齐""
            if not has_find_valid_param_value_flag:
                query_value_item.append('')
        query_value_list.append(query_value_item)

    return query_param_list,query_value_list

def show_with_prettytable(table_names_list,table_values_list):
    '''
    展示美化表格
    '''
    # 美化展示请求参数
    table = PrettyTable()
    table.field_names = table_names_list
    for query_values in table_values_list:
        table.add_row(query_values)

    return table

def show_urls_with_query_params(urls):
    '''
    表格化展示url查询参数
    '''
    # 表头和数据
    query_names_list,query_values_list = parse_urls_with_query_params(urls)

    # 美化展示请求参数
    table = show_with_prettytable(query_names_list,query_values_list)

    print('>>>表格化展示查询参数<<<')
    print(table)
    print()

def show_diff_urls_with_query_params(urls):
    '''
    表格化展示差异性查询参数
    '''
    # 表头和数据
    query_names_list,query_values_list = parse_urls_with_query_params(urls)

    # 美化展示请求参数
    table = show_with_prettytable(query_names_list,query_values_list)

    print('>>>表格化展示全部查询参数<<<')
    print(table)
    print()

    # 按列提取出相同类型的数据
    query_param_dict = {}
    for query_name_index, query_name in enumerate(query_names_list):
        query_name_values = []
        for query_value in query_values_list:
            query_name_values.append(query_value[query_name_index])
        query_param_dict[query_name] = query_name_values

    # 字段字典转set集合去重得到差异性字段
    exclude_query_names_list = ['timestamp']
    diff_query_names_list = []
    for query_param_name in query_param_dict:
        diff_param_value_set = set(query_param_dict.get(query_param_name))
        if len(diff_param_value_set) > 1 and (query_param_name not in exclude_query_names_list):
            diff_query_names_list.append(query_param_name)

    # 展示筛选字段列表
    selected_table = table.get_string(fields=diff_query_names_list)

    print('>>>仅展示差异性查询表格<<<')
    print(selected_table)
    print()

def filter_diff_urls_with_query_params(urls,code_name_relation_map={}):
    '''
    先过滤差异性数据再表格化展示查询参数
    '''
    # 表头和数据
    query_names_list,query_values_list = parse_urls_with_query_params(urls)

    # 按列提取出相同类型的数据
    query_param_dict = {}
    for query_name_index, query_name in enumerate(query_names_list):
        query_name_values = []
        for query_value in query_values_list:
            query_name_values.append(query_value[query_name_index])
        query_param_dict[query_name] = query_name_values

    # 字段字典转set集合去重得到差异性字段
    diff_query_names_list = []
    exclude_query_names_list = ['timestamp']
    for query_param_name in query_param_dict:
        diff_param_value_set = set(query_param_dict.get(query_param_name))
        if len(diff_param_value_set) > 1 and (query_param_name not in exclude_query_names_list):
            diff_query_names_list.append(query_param_name)

    # 查找差异性字段在原标题中的顺序
    diff_query_names_index_list = []
    for diff_query_name in diff_query_names_list:
        for query_name_index, query_name in enumerate(query_names_list):
            if diff_query_name == query_name:
                diff_query_names_index_list.append(query_name_index)
                break

    # 翻译差异性标题
    diff_query_names_title_list = []
    for diff_query_names in diff_query_names_list:
        diff_query_names_title = code_name_relation_map.get(diff_query_names) or diff_query_names
        diff_query_names_title_list.append(diff_query_names_title) 

    # 查找差异性数据
    diff_query_names_data_list = []
    for query_value in query_values_list:
        diff_query_names_data_item_list = []
        for diff_query_names_index in diff_query_names_index_list:
            diff_query_names_data_item_list.append(query_value[diff_query_names_index])
        diff_query_names_data_list.append(diff_query_names_data_item_list)

    # 美化展示请求参数
    table = show_with_prettytable(diff_query_names_title_list,diff_query_names_data_list)

    print('>>>表格化展示差异性参数<<<')
    print(table)
    print()

def main():
    # 原始 get 参数 url 链接
    urls = '''
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=dDNClw4tBKGU7hAZx-XpOBq5DoWF5WJ2TK8edBMLq4o&FMQw=0&q4f3=zh-CN&VySQ=FGEMmxz6TAvkuerBSuVfLd-w01fSfGxM&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581465946282
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=dDNClw4tBKGU7hAZx-XpOBq5DoWF5WJ2TK8edBMLq4o&FMQw=0&q4f3=zh-CN&VySQ=FGEMmxz6TAvkuerBSuVfLd-w01fSfGxM&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581466048309
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=dDNClw4tBKGU7hAZx-XpOBq5DoWF5WJ2TK8edBMLq4o&FMQw=0&q4f3=zh-CN&VySQ=FGEMmxz6TAvkuerBSuVfLd-w01fSfGxM&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581466073940
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=dDNClw4tBKGU7hAZx-XpOBq5DoWF5WJ2TK8edBMLq4o&FMQw=0&q4f3=zh-CN&VySQ=FGEMmxz6TAvkuerBSuVfLd-w01fSfGxM&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581466097372
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=dDNClw4tBKGU7hAZx-XpOBq5DoWF5WJ2TK8edBMLq4o&FMQw=0&q4f3=zh-CN&VySQ=FGEMmxz6TAvkuerBSuVfLd-w01fSfGxM&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581466118828
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=dDNClw4tBKGU7hAZx-XpOBq5DoWF5WJ2TK8edBMLq4o&FMQw=0&q4f3=zh-CN&VySQ=FGEMmxz6TAvkuerBSuVfLd-w01fSfGxM&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581466153163
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=dDNClw4tBKGU7hAZx-XpOBq5DoWF5WJ2TK8edBMLq4o&FMQw=0&q4f3=zh-CN&VySQ=FGEMmxz6TAvkuerBSuVfLd-w01fSfGxM&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581473766043
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=z2EaI5kkCkW-jslnKmsffnYfiBdVG-JaQA6zDzT4lAU&FMQw=0&q4f3=zh-CN&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581473820005
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=z2EaI5kkCkW-jslnKmsffnYfiBdVG-JaQA6zDzT4lAU&FMQw=0&q4f3=zh-CN&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581474320091
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=z2EaI5kkCkW-jslnKmsffnYfiBdVG-JaQA6zDzT4lAU&FMQw=0&q4f3=zh-CN&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581501834959
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=z2EaI5kkCkW-jslnKmsffnYfiBdVG-JaQA6zDzT4lAU&FMQw=0&q4f3=zh-CN&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581501961805
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=t8mrq_YnAbyQUU7lmiJFNOysQGlKAykjpl6Kp_R4PXw&FMQw=0&q4f3=zh-CN&VySQ=FGHCXcWAgMnEuDfL881oOTbrF1iJfANK&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581508561749
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=1vWFUu6c8X&hashCode=z2EaI5kkCkW-jslnKmsffnYfiBdVG-JaQA6zDzT4lAU&FMQw=0&q4f3=zh-CN&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_2)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/80.0.3987.87%20Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581508957149
    https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=MFjuxmgU5M&hashCode=Obi2jdJnLWjGFx-xg8YrzljCaNGizhOypETrKR_L1JM&FMQw=0&q4f3=zh-CN&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36&E3gR=9f7fa43e794048f6193187756181b3b9&timestamp=1581509113202


    '''

    code_name_relation_map = {
            "FMQw": "adblock",
            "TeRS": "scrAvailSize",
            "qBVW": "appMinorVersion",
            "qmyu": "scrColorDepth",
            "hLzX": "userLanguage",
            "j5po": "hasLiedLanguages",
            "e6OK": "systemLanguage",
            "5Jwy": "scrHeight",
            "ks0Q": "plugins",
            "kU5z": "historyList",
            "Fvje": "storeDb",
            "q5aJ": "timeZone",
            "qT7b": "appcodeName",
            "3neK": "hasLiedResolution",
            "2xC5": "hasLiedBrowser",
            "VEek": "doNotTrack",
            "3sw-": "indexedDb",
            "jp76": "mimeTypes",
            "VPIf": "cookieEnabled",
            "9vyE": "online",
            "-UVA": "browserName",
            "88tV": "scrAvailHeight",
            "E-lJ": "scrAvailWidth",
            "VySQ": "cookieCode",
            "ci5c": "hasLiedOs",
            "0aew": "userAgent",
            "3jCe": "scrDeviceXDPI",
            "E3gR": "webSmartID",
            "Md7A": "cpuClass",
            "XM7l": "localStorage",
            "ssI5": "scrWidth",
            "EOQP": "jsFonts",
            "d435": "browserVersion",
            "lEnu": "localCode",
            "hAqN": "os",
            "V8vl": "openDatabase",
            "q4f3": "browserLanguage",
            "dzuS": "flashVersion",
            "tOHY": "srcScreenSize",
            "yD16": "javaEnabled",
            "wNLf": "touchSupport",
            "HVia": "sessionStorage"
        }

    filter_diff_urls_with_query_params(urls,code_name_relation_map=code_name_relation_map)

if __name__ == '__main__':
    main()