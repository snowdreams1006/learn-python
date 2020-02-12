# 表格美化展示

```bash
virtualenv  -p python3 .env
```

```bash
source .env/bin/activate
```

```bash
pip install prettytable
```

```python
# -*- coding: utf-8 -*-
from prettytable import PrettyTable

def simple_demo():
    tb = PrettyTable()
    tb.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    tb.add_row(["Adelaide",1295, 1158259, 600.5])
    tb.add_row(["Brisbane",5905, 1857594, 1146.4])
    tb.add_row(["Darwin", 112, 120900, 1714.7])
    tb.add_row(["Hobart", 1357, 205556,619.5])

    print(tb)

def main():
    simple_demo()

if __name__ == '__main__':
    main()
```

- [github:prettytable](https://github.com/jazzband/prettytable)
- [python prettytable 打印表格](https://www.jianshu.com/p/82689c1e3247)
- [Python PrettyTable 模块(美化库）](https://blog.csdn.net/u013630675/article/details/78773356)