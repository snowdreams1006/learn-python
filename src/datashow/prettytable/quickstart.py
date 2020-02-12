# -*- coding: utf-8 -*-
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

def main():
    simple_table_demo()

if __name__ == '__main__':
    main()