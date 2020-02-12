# -*- coding: utf-8 -*-
from prettytable import PrettyTable

def simple_table_demo():
    table = PrettyTable()
    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_row(["Adelaide",1295, 1158259, 600.5])
    table.add_row(["Brisbane",5905, 1857594, 1146.4])
    table.add_row(["Darwin", 112, 120900, 1714.7])
    table.add_row(["Hobart", 1357, 205556,619.5])

    print(table)

def sorted_table_demo():
    table = PrettyTable()
    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_row(["Adelaide",1295, 1158259, 600.5])
    table.add_row(["Brisbane",5905, 1857594, 1146.4])
    table.add_row(["Darwin", 112, 120900, 1714.7])
    table.add_row(["Hobart", 1357, 205556,619.5])

    print(">>>simple_table_demo<<<")
    print(table)

    sorted_table = table.get_string(sortby="Population", reversesort=False)
    
    print(">>>sorted_table_demo<<<")
    print(sorted_table)

def main():
    sorted_table_demo()

if __name__ == '__main__':
    main()