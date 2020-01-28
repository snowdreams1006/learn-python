# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image
import os

def use_simple_text_image(image_name,lang='eng'):
    image = Image.open(image_name)
    image = image.convert("1")
    code = pytesseract.image_to_string(image,lang=lang)
    print(code)

def convert_gray_image(image_name):
    '''
    灰度化处理图片
    '''
    image = Image.open(image_name)
    # 转灰度
    gray_image = image.convert("L")
    gray_image_name = get_covert_image(image_name,'gray-')
    # 保存灰度图
    gray_image_name.save(gray_image_name)

def convert_binarization_image(image_name):
    '''
    二值化处理图片
    '''
    image = Image.open(image_name)
    # 二值化
    binarization_image = image.convert("1")
    binarization_image_name = get_covert_image(image_name,'binarization-')
    # 保存二值图
    binarization_image.save(binarization_image_name)

def get_covert_image(image_name,covert_prefix):
    '''
    获取转换后文件名,支持文件名称,相对路径和绝对路径
    '''
    # 分割目录和文件名,形如: ('/Users/snowdreams1006/Downloads', 'zui56-code.jpeg')
    split_image_name = os.path.split(image_name)
    print(split_image_name)

    dir_split_image_name = split_image_name[0]
    file_split_image_name = split_image_name[1]

    # 分离文件名称和后缀名称,形如: ('zui56-code', '.jpeg')
    splitext_image_name = os.path.splitext(file_split_image_name)
    print(splitext_image_name)

    name_splitext_image_name = splitext_image_name[0]
    suffix_splitext_image_name = splitext_image_name[1]

    # 添加转换前缀并拼接形成新路径,形如: /Users/snowdreams1006/Downloads/binarization-zui56-code.jpeg
    binarization_image_name = ''.join([covert_prefix,name_splitext_image_name,suffix_splitext_image_name])
    if dir_split_image_name:
        binarization_image_name = ''.join([dir_split_image_name,os.sep,binarization_image_name])
    return binarization_image_name

def main():
    # /Users/snowdreams1006/Downloads/zui56-code.jpeg
    # convert_binarization_image('/Users/snowdreams1006/Downloads/zui56-code.jpeg')

    # use_simple_text_image('zhihu-code.jpeg')

    # use_simple_text_image('snowdreams1006.png')
    # use_simple_text_image('雪之梦技术驿站.png',lang='chi_sim')

if __name__ == '__main__':
    main()