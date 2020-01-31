# 图像处理

- [http://pythonware.com/products/pil/](http://pythonware.com/products/pil/)
- [https://python-pillow.org/](https://python-pillow.org/)

## 图片素材


## open 打开图像

```python
from PIL import Image             ##调用库，包含图像类
im = Image.open("3d.jpg")  ##文件存在的路径，如果没有路径就是当前目录下文件
im.show()
```


## 参考文档

- [Python图像处理PIL各模块详细介绍](https://blog.csdn.net/zhangziju/article/details/79123275)