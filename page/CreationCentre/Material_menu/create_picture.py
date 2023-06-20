import datetime
import os.path
import time
import unittest
from ddt import ddt, data ,unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from common.getdata import GetData
from page.Login_page import LoginPage
from common.element import Loctor
class Picture(LoginPage):
    def __init__(self,driver,url,user,pwd,org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd,org)
        r=driver.current_window_handle
        # 点击创作中心按钮
        try:
            creator = ('#v-step_creator')
            self.click('cs', creator)
        except:
            print('没有创作中心')
        # 进入创作中心
        handles = driver.window_handles[-1]
        driver.switch_to.window(handles)
        time.sleep(1)
        self.click('id','tab-picture')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
    def picture(self):
        time.sleep(2)
        # 获取当前的文件绝对地址
        os.path.realpath(__file__)
        # 获取当前文件所在目录的路径
        os.path.dirname(os.path.realpath(__file__))
        # 获取当前文件所在目录的上一级目录  os.path.dirname()可以使用多次，直到到达要读写文件的上一级目录为止
        dir_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
        # 要读取img路径下的661-600文件
        path=os.path.join(dir_path,"img","661-600x420.jpg")
        self.input('xpath','//input[@name="file"]',path)
        time.sleep(2)
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        time.sleep(2)
    def create_pictrure_msg(self):
        msg=self.text('cs','body > div')
        return msg
    def delete_picture(self):
        self.input('xpath','//*[@placeholder="搜索关键词"]','661-600x420.jpg')
        self.click('xpath','/html/body/section/section/main/div/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/a[3]/span')
        self.click('xpath','//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        msg=self.text('cs','body > div.el-message.el-message--success.is-closable')
        return msg


