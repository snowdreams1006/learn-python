# -*- coding: utf-8 -*-
import PIL.Image as Image
import os
 
# IMAGES_PATH = 'E:\picture\新垣结衣\\'  # 图片集地址
# IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
# IMAGE_SIZE = 64  # 每张小图片的大小
# IMAGE_ROW = 4  # 图片间隔，也就是合并成一张图后，一共有几行
# IMAGE_COLUMN = 4  # 图片间隔，也就是合并成一张图后，一共有几列
# IMAGE_SAVE_PATH = 'E:\\picture\\新垣结衣\\final.jpg'  # 图片转换后的地址
 
# # 获取图片集地址下的所有图片名称
# image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
#                os.path.splitext(name)[1] == item]
 
# # 简单的对于参数的设定和实际图片集的大小进行数量判断
# if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
#     raise ValueError("合成图片的参数和要求的数量不能匹配！")
 
# 定义图像拼接函数
def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE)) #创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE, IMAGE_SIZE),Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
    return to_image.save(IMAGE_SAVE_PATH) # 保存新图

# 定义图像拼接函数
def list_image():
    # 已合并大图片的一行用多少个小图片填充,当行数大于列数时新图片是竖版,否则是横版
    IMAGE_LARGE_ROW_COUNT = 3
    # 已合并大图片的一列用多少个小图片填充
    IMAGE_LARGE_COLUMN_COUNT = 10
    # 已合并大图片路径
    IMAGE_LARGE_PATH = 'large.png'

    # 待合并的小图片所在目录,用于方便批量读取小图片
    IMAGES_SMALL_PATH = './images/'
    # 待合并的小图片像素大小
    IMAGE_SMALL_COLUMN_SIZE = 64
    IMAGE_SMALL_ROW_SIZE = 64

    # 读取待合并的图片:当前 images 目录下类似于 github-emoji-*.png的图片
    images = []
    for name in os.listdir(IMAGES_SMALL_PATH):
        if os.path.splitext(name)[0].startswith('github-emoji-') and os.path.splitext(name)[1].endswith('.png'):
            images.append(name)
    
    # 双重循环粘贴到已合并图片的指定位置: 先逐行行粘贴,未填充满时用空白图像代替
    to_image = Image.new('RGBA', (IMAGE_LARGE_COLUMN_COUNT * IMAGE_SMALL_COLUMN_SIZE, IMAGE_LARGE_ROW_COUNT * IMAGE_SMALL_ROW_SIZE)) 
    for y in range(1, IMAGE_LARGE_ROW_COUNT + 1):
        for x in range(1, IMAGE_LARGE_COLUMN_COUNT + 1):
            from_image_index = IMAGE_LARGE_COLUMN_COUNT * (y - 1) + x - 1
            if from_image_index < len(images):
                from_image_name = IMAGES_SMALL_PATH + images[from_image_index]
                if os.path.exists(from_image_name):
                    from_image = Image.open(from_image_name).resize((IMAGE_SMALL_ROW_SIZE, IMAGE_SMALL_COLUMN_SIZE),Image.ANTIALIAS)
                    to_image.paste(from_image, ((x - 1) * IMAGE_SMALL_ROW_SIZE, (y - 1) * IMAGE_SMALL_COLUMN_SIZE))
    return to_image.save(IMAGE_LARGE_PATH) 

# 定义图像拼接函数
def multiple_image_compose():
    #创建一个新图
    to_image = Image.new('RGB', (2 * 64, 2 * 64)) 
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, 2 + 1):
        for x in range(1, 2 + 1):
            from_image = Image.open('./images/four.png').resize(
                (64, 64),Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * 64, (y - 1) * 64))
    # 保存新图
    return to_image.save('multiple_image_compose.png') 

if __name__ == '__main__':
    # multiple_image_compose() 
    list_image()


