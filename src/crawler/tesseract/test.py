# -*- coding: utf-8 -*-
import tesserocr
from PIL import Image

def main():
    #新建Image对象
    image = Image.open("sina-code.png")
    #调用tesserocr的image_to_text()方法，传入image对象完成识别
    result = tesserocr.image_to_text(image)
    print(result)

if __name__ == '__main__':
    main()


