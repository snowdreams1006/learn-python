# -*- coding: utf-8 -*-
from PIL import Image
from selenium import webdriver
import time


def get_verify_code_img():
    url = 'http://www.scliangfu.com/Themes/Manages/Login.aspx'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    driver.save_screenshot('printscreen.png')
    
    imgelement = driver.find_element_by_xpath('//*[@id="Image3"]')  # 定位验证码
    location = imgelement.location
    size = imgelement.size


    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']

    # 713 363 813 399
    print(left,top,right,bottom)
    i = Image.open("printscreen.png") 
    frame4 = i.crop((2*int(left), 2*int(top), 2*int(right),2*int(bottom) ))  # 按照验证码的长宽，切割验证码
    frame4.save('code.png') # 保存我们接下来的验证码图片 进行打码
    frame4.show()
    
    driver.close()

'''
self.driver.get('https://ph.zui56.net/login')  # 打开登陆页面
        self.driver.save_screenshot('pictures.png')  # 全屏截图
        page_snap_obj = Image.open('pictures.png')
        img = self.find_element('#captchaImage')  # 验证码元素位置
        print(img.get_attribute('src'))

        time.sleep(1)
        location = img.location
        print('location',location)

        size = img.size  # 获取验证码的大小参数
        print('size',size)

        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']

        print(left,top,right,bottom)

        image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
        image_obj.show()  # 打开切割后的完整验证码
        self.driver.close()  # 处理完验证码后关闭浏览器
        return image_obj
'''

def main():
    print('main')
    get_verify_code_img()

if __name__ == '__main__':
    main()

