# -*- coding: utf-8 -*-
# import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from PIL import Image,ImageEnhance

class LoginCode(object):

    # 用户名框元素
    telephone_loc = (By.NAME,"username")
    # 密码框元素
    password_loc = (By.NAME,"password")
    # 验证码框元素
    code_loc = (By.NAME,"captcha")
    # 登录按钮元素
    button_loc = (By.XPATH,'*[@id="btn_login"]')
    # 验证码图片元素
    img_el_loc = (By.XPATH, "*[@id='captchaImage']")
    # 验证码错误提示元素
    codeErrMsg_loc = (By.CSS_SELECTOR, ".el-message__content")

    imgPath = "img.png"
    # driver = webdriver.Chrome("/Users/zhangc/zh/111/test/chromedriver")
    driver = webdriver.Chrome()


    def remove(self,string):
        '''字符串去除空格'''

        return string.replace(" ","")


    def find_element(self,*loc):
        # 实验得知方法中的参数loc↑加上*，定位会更稳定
        '''定位单个元素'''

        return self.driver.find_element(*loc)


    def open(self):
        '''打开浏览器'''

        url = 'https://ph.zui56.net/login'
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        # 获取验证码图片
        self.getCodeImg()
        self.driver.save_screenshot('test-printscreen.png')


    def getCodeImg(self):
        '''获取验证码图片'''

        # 验证码图片的元素定位
        # img_el = self.find_element(*self.img_el_loc)
        img_el = self.driver.find_element_by_xpath('//*[@id="captchaImage"]')
        # 获取整个浏览器的size
        chromeSize = self.driver.get_window_size()
        print("页面的总size:"+str(chromeSize))               
        # 页面的总size:{'width': 1202, 'height': 1129}
        
        # 获取图片的坐标
        self.location = img_el.location
        print("页面坐标点的size:"+str(self.location))         
        # 页面坐标点的size:{'x': 959, 'y': 518} x:指的图片左边距；y:指的图片上边距
        
        # 获取图片的大小
        imgSize = img_el.size
        print("验证码的size:"+str(imgSize))                  
        # 验证码的size:{'height': 28, 'width': 70}
        
        # 左边距占整个浏览器的百分比
        left = self.location['x']/chromeSize['width']
        # 上边距占整个浏览器的百分比
        top = self.location['y']/chromeSize['height']
        # 右边距占整个浏览器的百分比
        right = (self.location['x'] + imgSize['width'])/chromeSize['width']
        # 下边距占整个浏览器的百分比
        bottom = (self.location['y'] + imgSize['height'])/chromeSize['height']  
        print(left,top,right,bottom)                        
        # 0.7978369384359401 0.4588131089459699 0.8560732113144759 0.48361381753764393

        # 浏览器截屏操作
        self.driver.get_screenshot_as_file(self.imgPath)
        screenshotImgSize = Image.open(self.imgPath).size
        print("截图的size:"+str(screenshotImgSize))          
        # 截图的size:(2404, 1950)    宽：2404，高：1950
        self.driver.get_screenshot_as_file('imgPath-origin.png')

        sleep(2)


        img = Image.open(self.imgPath).crop((
            # left*screenshotImgSize[0],
            # top*screenshotImgSize[1]+100,
            # right*screenshotImgSize[0]+20,
            # bottom*screenshotImgSize[1]+150

            # 左边距百分比*截图的高≈截图左边距，再加上微调的距离+350
            left * screenshotImgSize[0],
            # 上边距百分比*截图的宽≈截图上边距，再加上微调的距离-100
            top * screenshotImgSize[1],
            # 右边距百分比*截图的高≈截图右边距，再加上微调的距离+400
            right * screenshotImgSize[0],
            # 上边距百分比*截图的宽≈截图下边距，再加上微调的距离-50
            bottom * screenshotImgSize[1]                
        ))
        img.save('save-origin.png')


        # 从文件读取截图，截取验证码位置再次保存
        img = Image.open(self.imgPath).crop((
            # left*screenshotImgSize[0],
            # top*screenshotImgSize[1]+100,
            # right*screenshotImgSize[0]+20,
            # bottom*screenshotImgSize[1]+150

            # 左边距百分比*截图的高≈截图左边距，再加上微调的距离+350
            left * screenshotImgSize[1]+350,
            # 上边距百分比*截图的宽≈截图上边距，再加上微调的距离-100
            top * screenshotImgSize[0]-100,
            # 右边距百分比*截图的高≈截图右边距，再加上微调的距离+400
            right * screenshotImgSize[1]+400,
            # 上边距百分比*截图的宽≈截图下边距，再加上微调的距离-50
            bottom * screenshotImgSize[0]-50                
        ))
        img.save('save.png')

        img = img.convert('L')                              # 转换模式：L | RGB
        img = ImageEnhance.Contrast(img)                    # 增强对比度
        img = img.enhance(2.0)                              # 增加饱和度
        img.save(self.imgPath)                              # 再次保存图片


    def getCode(self):
        '''获取图片的code'''

        # 再次读取识别验证码
        img = Image.open(self.imgPath)
        # code = pytesseract.image_to_string(img).strip()
        # print("=============输出的验证码为：" + self.remove(code))
        # return code


    def loopGetCode(self):
        '''循环判断获取正确的图片code'''

        code = self.remove(self.getCode())
        # 循环前获取code字数
        codeNumBf = len(code)

        # 如果获取图片的code值为空或者不满足4位数进行循环
        while (code == "") | (codeNumBf != 4):

            # 重新获取验证码
            self.find_element(*self.img_el_loc).click()
            self.getCodeImg()       # 获取验证码图片
            code = self.remove(self.getCode())
            # 循环后获取code字数
            codeNumAf = len(code)
            if code == "":
                print("code获取为空值=================")
                continue
            elif codeNumAf != 4:
                print("code获取不是4位数字=============")
                continue
            else:
                print("识别成功！")
            # 识别成功退出循环
            break
        print("=============输出的验证码为：" + code)
        # 输出满足条件的code
        return code


    def login(self,code):
        '''进行登录操作'''

        # 输入用户名
        telephone = self.find_element(*self.telephone_loc)
        telephone.clear()
        telephone.send_keys("cheng")
        # 输入密码
        password = self.find_element(*self.password_loc)
        password.clear()
        password.send_keys("123456")
        # 输入验证码
        code_loc = self.find_element(*self.code_loc)
        code_loc.clear()
        code_loc.send_keys(code)
        # 点击登录按钮
        button = self.find_element(*self.button_loc)
        button.click()
        sleep(1)
        # try:
        #     # 后台获取验证码校验内容
        #     codeErrMsg = self.find_element(*self.codeErrMsg_loc).text
        #     print("打印后台："+codeErrMsg)
        #     if codeErrMsg == "验证码不正确":
        #         print("验证码不正确111")
        #         self.find_element(*self.img_el_loc).click()
        #         self.getCodeImg()
        #         self.loopGetCode_action()
        #     else:
        #         print("登陆成功！")
        # except:
        #     print("进入首页！！！！")
        #     pass


    def loopGetCode_action(self):
        '''循环验证code的正确性'''

        resultCode = self.loopGetCode()
        self.login(resultCode)


    def login_action(self):
        '''执行验证码登录操作'''

        # 打开浏览器并获取验证码图片
        self.open()
        # self.loopGetCode_action()

if __name__ == '__main__':
    LoginCode().login_action()