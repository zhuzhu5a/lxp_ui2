import datetime
import os
import time
import unittest
from ddt import ddt, data ,unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from common.getdata import GetData
from page.Login_page import LoginPage
from common.element import Loctor
class Article(LoginPage):
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
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        driver.switch_to.window(handles)
        time.sleep(1)
        self.click('id','tab-article')
        self.click('xpath','//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
    def local_article(self):
        self.click('xpath','//*[@class="el-upload--text"]')
        time.sleep(1)
        self.input('xpath','//*[@placeholder="请输入文章标题"]','文章标题'+self.dt)
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        return msg
    def delete_article(self):
        self.click('xpath','/html/body/section/section/main/div/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[6]/div/a[4]/span')
        self.click('xpath','//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        msg=self.text('cs','body > div.el-message.el-message--success.is-closable')
        return msg
    def upload_article(self):
        dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

        path = os.path.join(dir_path, "data", "SAAS官网文案(1).docx")
        self.input('xpath','//*[@name="file"]',path)
        time.sleep(2)
        self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        return msg