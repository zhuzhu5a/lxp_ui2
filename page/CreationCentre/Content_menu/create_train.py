import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page import Login_page
from page.Login_page import LoginPage
from common.element import Loctor
import datetime

class Train(LoginPage):
    def __init__(self,driver,url,user,pwd,org):
        self.driver=driver
        lp=LoginPage(driver)
        lp.login_successful(url,user,pwd,org)
        try:
            creator = ('#v-step_creator')
            self.click('cs', creator)
        except:
            print('没有创作中心')
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d——%H:%M')
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.driver.implicitly_wait(5)
        self.click('cs', '#app > section > aside > div > ul > div:nth-child(2) > li')
        self.click('id','tab-training')


    def train(self,title):
        self.click('xpath', '//button[@class="el-button el-button--primary is-round"]')
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        title1=title+self.dt
        self.input('xpath','//*[@placeholder="请输入标题"]',title1)
        dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
        path = os.path.join(dir_path, "img", "1.jpeg")
        self.input('xpath','//input[@type="file"]',path)
        self.input('xpath','//input[@accept=".mp4"]',r'C:\Users\91621\Videos\1.mp4')
        time.sleep(1)
        self.click('xpath','//button[@class="el-button add-tool el-button--default el-button--small is-round"]')
        self.input('xpath','//*[@placeholder="输入步骤内容" and @index="0"]','步骤1')
        self.input('xpath','//input[@multiple="multiple"]',r'C:\Users\91621\Pictures\12.png')
        self.click('xpath','//button[@class="el-button add-tool el-button--default el-button--small is-round"]')
        self.input('xpath','//*[@placeholder="输入步骤内容" and @index="1"]','步骤2')
        self.input('xpath','//input[@multiple="multiple"]',r'C:\Users\91621\Pictures\123.png')
        self.click('xpath', '//*[@placeholder="选择评价维度"]')
        time.sleep(0.5)
        self.locateElement('xpath', '//*[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath', '/html/body/div/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.click('xpath', '//*[@placeholder="选择评价标准"]')
        self.locateElement('xapth', '[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.input('xpath', '//*[@maxlength="3"]', '100')
        self.click('cs','#app > section > main > div > div.content > div > form > div:nth-child(12) > div > div > form > div:nth-child(2) > div > div.tw-flex.tw-flex-col.tw-space-y-5.el-col.el-col-16 > div > div.tw-flex.tw-justify-between.tw-items-center.tw-h-10.tw-pl-2\.5.el-col.el-col-4 > span:nth-child(2) > i')
        self.click('xpath','//button[@class="el-button el-button--primary is-round"]')
    def with_software(self,title):
        self.click('xpath', '//button[@class="el-button el-button--primary is-round"]')
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        title1 = title + self.dt
        self.input('xpath', '//*[@placeholder="请输入标题"]', title1)
        dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
        path = os.path.join(dir_path, "img", "1.jpeg")
        self.input('xpath', '//input[@type="file"]', path)
        self.input('xpath', '//input[@accept=".mp4"]', r'C:\Users\91621\Videos\1.mp4')
        time.sleep(1)
        self.click('xpath', '//button[@class="el-button add-tool el-button--default el-button--small is-round"]')
        self.input('xpath', '//*[@placeholder="输入步骤内容" and @index="0"]', '步骤1')
        self.input('xpath', '//input[@multiple="multiple"]', r'C:\Users\91621\Pictures\12.png')
        self.click('xpath', '//button[@class="el-button add-tool el-button--default el-button--small is-round"]')
        self.input('xpath', '//*[@placeholder="输入步骤内容" and @index="1"]', '步骤2')
        self.input('xpath', '//input[@multiple="multiple"]', r'C:\Users\91621\Pictures\123.png')
        self.click('xpath','//*[@class="el-button el-button--primary is-plain is-round"]')
        time.sleep(0.5)
        try:
            self.click('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[1]')
            time.sleep(1)
            self.click('xpath', '/html/body/div[2]/div/div[2]/div/div[2]/button')
        except:
            print('当前组织没有被分配的软件')
        self.click('xpath', '//*[@placeholder="选择评价维度"]')
        time.sleep(0.5)
        self.locateElement('xpath', '//*[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath', '/html/body/div/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.click('xpath', '//*[@placeholder="选择评价标准"]')
        self.locateElement('xapth', '[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.input('xpath', '//*[@maxlength="3"]', '100')
        self.click('cs',
                   '#app > section > main > div > div.content > div > form > div:nth-child(12) > div > div > form > div:nth-child(2) > div > div.tw-flex.tw-flex-col.tw-space-y-5.el-col.el-col-16 > div > div.tw-flex.tw-justify-between.tw-items-center.tw-h-10.tw-pl-2\.5.el-col.el-col-4 > span:nth-child(2) > i')
        self.click('xpath', '//button[@class="el-button el-button--primary is-round"]')
    def delete_train(self):
        i = 0
        while i <= 1:
            try:
                sandian=self.locateElement('xpath','/html/body/section/section/main/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div/i')
                ActionChains(self.driver).move_to_element(sandian).perform()
                self.locateElement('xpath','/html/body/ul')
                time.sleep(1)
                self.click('xpath','/html/body/ul/li[2]')
                self.click('xpath','/html/body/div[1]/div/div[3]/button[2]')
                msg=self.locateElement('cs','body > div.el-message.el-message--success.is-closable.el-message-fade-leave-active.el-message-fade-leave-to')
            except:
                pass
            i = i + 1
        msg1=msg.text
        return msg1




