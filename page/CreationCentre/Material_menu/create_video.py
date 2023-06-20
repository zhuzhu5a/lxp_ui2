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
class Video(LoginPage):
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
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@class="el-button el-button--default is-round"]').click()
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    def video(self):
        time.sleep(1)
        dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
        path = os.path.join(dir_path, "video", "1.mp4")
        print(path)
        self.input('xpath','//input[@name="file"]',path)
        time.sleep(5)
        self.input('xpath','//input[@placeholder="请输入视频名称"]',"自动化创建视频"+self.dt)
        name=self.text('xpath','//input[@placeholder="请输入视频名称"]')
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        time.sleep(2)
        msg=self.locateElement('cs','body > div')
        msg2=msg.text
        a=(name,msg2)
        return a
    def delete_video(self,name):
        self.input('xpath','//*[@placeholder="搜索关键词"]',name)
        self.click('xpath','/html/body/section/section/main/div/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/a[4]/span')
        self.click('xpath', '//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(1)
        msg = self.locateElement('cs',
                                 'body > div.el-message.el-message--success.is-closable')
        msg1 = msg.text
        return msg1