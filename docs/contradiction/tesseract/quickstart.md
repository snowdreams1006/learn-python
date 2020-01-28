# 快速上手

> 下载地址: [https://digi.bib.uni-mannheim.de/tesseract/](https://digi.bib.uni-mannheim.de/tesseract/)

单独使用

```bash
tesseract test.png result
```

```python
# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image

def clear_image(image):
    image = image.convert('RGB')
    width = image.size[0]
    height = image.size[1]
    noise_color = get_noise_color(image)
    
    for x in range(width):
        for y in  range(height):
            #清除边框和干扰色
            rgb = image.getpixel((x, y))
            if (x == 0 or y == 0 or x == width - 1 or y == height - 1 
                or rgb == noise_color or rgb[1]>100):
                image.putpixel((x, y), (255, 255, 255))
    return image

def get_noise_color(image):
    for y in range(1, image.size[1] - 1):
        # 获取第2列非白的颜色
        (r, g, b) = image.getpixel((2, y))
        if r < 255 and g < 255 and b < 255:
            return (r, g, b)

image = Image.open('code4.png')
image = clear_image(image)
#转化为灰度图
imgry = image.convert('L')
code = pytesseract.image_to_string(imgry)

imgry.save("imgry1.png")
with open("code.txt", "w") as f:
    print(code)
    f.write(str(code))
```


## 图像处理库 Pillow

> Pillow

```bash
pip install Pillow
```

> pip3 install Pillow

## OCR 识别库 Tesseract-OCR

> pytesseract

```bash
pip install pytesseract
```

> pip3 install pytesseract

## 快速体验

```python
from PIL import Image
'''
获取图片
'''
def getImage():
    fileName = '16.jpg'
    img = Image.open()
    # 打印当前图片的模式以及格式
    print('未转化前的: ', img.mode, img.format)
    # 使用系统默认工具打开图片
    # img.show()
    return img
```

### 预处理

```python
'''
1) 将图片进行降噪处理, 通过二值化去掉后面的背景色并加深文字对比度
'''
def convert_Image(img, standard=127.5):
    '''
    【灰度转换】
    '''
    image = img.convert('L')

    '''
    【二值化】
    根据阈值 standard , 将所有像素都置为 0(黑色) 或 255(白色), 便于接下来的分割
    '''
    pixels = image.load()
    for x in range(image.width):
        for y in range(image.height):
            if pixels[x, y] > standard:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return image
```

### 识别

```python
import pytesseract
'''
使用 pytesseract 库来识别图片中的字符
'''
def change_Image_to_text(img):
    '''
    如果出现找不到训练库的位置, 需要我们手动自动
    语法: tessdata_dir_config = '--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
    '''
    testdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    textCode = pytesseract.image_to_string(img, lang='eng', config=testdata_dir_config)
    # 去掉非法字符，只保留字母数字
    textCode = re.sub("\W", "", textCode)
    return textCode
```

```
def main():
    img = convert_Image(getImage(fileName))
    print('识别的结果：', change_Image_to_text(img))

if __name__ == '__main__':
    main()
```

## 参考文档

- [Python 实现识别弱图片验证码](https://www.jianshu.com/p/bc6774723003)
- [Python之验证码识别](https://my.oschina.net/moluyingxing/blog/2996786)
- [selenium自动化测试+获取验证码图片](https://my.oschina.net/moluyingxing/blog/2997353)