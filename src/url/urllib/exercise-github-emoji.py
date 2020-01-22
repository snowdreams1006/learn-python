# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
import os
import random
import time
import PIL.Image as Image
import os

def download_all_emojis_on_github_with_urllib():
    '''
    Lists all the emojis available to use on GitHub and then download them.
    '''
    response = urllib2.urlopen('https://api.github.com/emojis')
    result = response.read()
    result = json.loads(result)
    for key,value in result.items():
        filename = key + value[value.rindex('.'):value.rindex('?')]
        filename = './images/github-emoji-{filename}'.format(filename=filename)
        existFile = os.path.exists(filename)
        print '文件: {filename},是否存在: {existFile}'.format(filename=filename,existFile=existFile)
        if os.path.exists(filename) is False:
            urllib.urlretrieve(value,filename)
            print '正在下载{value}到{filename}'.format(value=value,filename=filename)
            time.sleep(random.randint(30, 300))

    compose_image()

def compose_image():
    '''
    Compose multiple small images to one large image.
    '''
    # 已合并大图片的一行用多少个小图片填充,当行数大于列数时新图片是竖版,否则是横版
    IMAGE_LARGE_ROW_COUNT = 3
    # 已合并大图片的一列用多少个小图片填充,当行数大于列数时新图片是竖版,否则是横版
    IMAGE_LARGE_COLUMN_COUNT = 10
    # 已合并大图片路径
    IMAGE_LARGE_PATH = './images/emoji.png'

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

if __name__ == '__main__':
    # print '>>>Download all the emojis available to use on GitHub.<<<'
    # download_all_emojis_on_github_with_urllib() 

    print '>>>Compose multiple small images to one large image.<<<'
    compose_image()





