# -*- coding: utf-8 -*-
from urllib.parse import urlparse, parse_qs, parse_qsl
from prettytable import PrettyTable

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

    # 查询参数名称列表,其中以第一个链接为准设置表格标题
    query_names_list = []
    query_names_url = valid_urls[0]
    query = urlparse(query_names_url).query
    query_list = parse_qsl(query)
    for query_item in query_list:
        query_names_list.append(query_item[0])

    # 解析全部请求设置表格数据
    query_values_list = []
    for valid_url in valid_urls:
        # 美化表格参数列表
        query_values_item_list = []

        # 查询参数
        query = urlparse(valid_url).query
        query_list = parse_qsl(query)
        for query_item in query_list:
            query_values_item_list.append(query_item[1])
        # 参数不足时以参数标题为准补齐数据
        while len(query_values_item_list) < len(query_names_list):
            query_values_item_list.append('')

        query_values_list.append(query_values_item_list)

    return query_names_list,query_values_list

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

def show_urls_with_query_params():
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
    
    '''

    # 表头和数据
    query_names_list,query_values_list = parse_urls_with_query_params(urls)

    # 美化展示请求参数
    table = show_with_prettytable(query_names_list,query_values_list)

    # 筛选指定标题
    selected_table = table.get_string(fields=['algID','hashCode','VySQ'])

    print('>>>展示美化查询参数表格<<<')
    print(selected_table)

def main():
    show_urls_with_query_params()

if __name__ == '__main__':
    main()