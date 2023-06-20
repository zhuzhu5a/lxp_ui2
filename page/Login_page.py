import time
from time import sleep
from common.element import Loctor
from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage(Loctor):
    def __init__(self,driver):
        #页面元素
        self.driver=driver
        self.loginbutton=('#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > button > span')
        self.username = ('#pass-login > div:nth-child(1) > input')
        self.password = ('#pass-login > div:nth-child(2) > input')
        self.button = ('#pass-login > div.form-group.password-box > button')


    def login_successful(self,url,user,pwd,org):
        self.open(url)
        self.driver.maximize_window()
        sleep(1)
        try:
            self.click('cs','body > div > div > div.el-dialog__body > a > i')
            self.click('cs', self.loginbutton)
        except:
            self.click('cs',self.loginbutton)
        sleep(1)
        username = self.input('cs',self.username,user)
        password = self.input('cs',self.password,pwd)
        button = self.click('cs',self.button)
        sleep(1)
        try:
            self.click('id','verifybtn')
            time.sleep(1)
            self.shouji=self.text('xpath','//*[@class="layui-layer-content layui-layer-padding"]')
            self.shouji2=round(float(self.shouji.strip("\发送成功")))
            print('手机验证码：',self.shouji2)
            self.input('xpath','//*[@class="form-control verifycode"]',self.shouji2)
            self.click('xpath','//*[@class="login-btn"]')
            time.sleep(1)
            try:
                self.click('xpath',org)
                sleep(1)
                self.click('cs','body > div.introjs-tooltipReferenceLayer > div > div.introjs-tooltip-header > a')
            except:
                try:
                    self.click('cs', 'body > div.introjs-tooltipReferenceLayer > div > div.introjs-tooltip-header > a')
                    self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__header > button > i')
                except:
                    self.click('cs', 'body > div.introjs-tooltipReferenceLayer > div > div.introjs-tooltip-header > a')
        except:
            try:
                self.click('xpath',org)
                sleep(1)
                self.click('cs','body > div.introjs-tooltipReferenceLayer > div > div.introjs-tooltip-header > a')
            except:
                self.click('cs', 'body > div.introjs-tooltipReferenceLayer > div > div.introjs-tooltip-header > a')
    def login_user_error(self,url,user,pwd):
        self.open(url)
        self.driver.maximize_window()
        try:
            self.click('cs', 'body > div > div > div.el-dialog__body > a > i')
            self.click('cs', self.loginbutton)
        except:
            login = self.click('cs', self.loginbutton)
        sleep(1)
        self.input('cs',self.username,user)
        self.input('cs',self.password,pwd)
        self.click('cs',self.button)
        sleep(1)
        error_msg=self.driver.find_element('id','username-tip').text
        return error_msg
    def login_pwd_error(self,url,user,pwd):
        self.open(url)
        self.driver.maximize_window()
        try:
            self.click('cs', 'body > div > div > div.el-dialog__body > a > i')
            self.click('cs', self.loginbutton)
        except:
            login = self.click('cs', self.loginbutton)
        sleep(1)
        self.input('cs', self.username, user)
        self.input('cs', self.password, pwd)
        self.click('cs', self.button)
        sleep(1)
        error_msg=self.driver.find_element('xpath','//*[@id="password-tip"]').text
        return error_msg








