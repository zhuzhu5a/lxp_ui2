import time
import unittest
import datetime

from ddt import ddt, data ,unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from common.getdata import GetData
from page.Login_page import LoginPage
from common.element import Loctor
class Work(LoginPage):
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
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        handles = driver.window_handles[-1]
        driver.switch_to.window(handles)
        time.sleep(1)
        self.click('id','tab-work')
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
    def work(self):
        time.sleep(1)
        self.input('xpath','//*[@placeholder="请输入作业标题"]','作业'+self.dt)
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--primary is-plain is-round"]')
        time.sleep(1)
        self.click('xpath', '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/span[2]')
        handles1 = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles1)
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        self.select_all_clean('cs',
                              '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div.tw-flex-1.tw-relative.scroll-bar.custom-px-s1 > div.el-table.el-table--fit.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_1_column_2.el-table__cell > div > div > div > div.tw-w-\[200px\].el-input.el-input--small > input',
                              )
        self.input('cs',
                   '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div.tw-flex-1.tw-relative.scroll-bar.custom-px-s1 > div.el-table.el-table--fit.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_1_column_2.el-table__cell > div > div > div > div.tw-w-\[200px\].el-input.el-input--small > input',
                   '作业' + self.dt)
        self.click('xpath',
                   '/html/body/section/section/main/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div[2]/i')
        time.sleep(1)
        self.click('xpath',
                   '/html/body/section/section/main/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div/a/span')
        time.sleep(1)
        self.click('xpath', '/html/body/section/section/main/div/div[2]/div/div[1]/div/div[3]/div[1]/button[2]')
        time.sleep(1)
        iframe = self.driver.find_element('xpath',
                                          '/html/body/div[2]/div/div[2]/div/form/div[1]/div/div/div/div[1]/div[2]/div[1]/iframe')
        self.driver.switch_to.frame(iframe)
        self.input('id', 'tinymce', '这是题干')
        self.driver.switch_to.default_content()
        iframe2 = self.locateElement('xpath',
                                     '/html/body/div[2]/div/div[2]/div/form/div[2]/div/div/div/div[1]/div[2]/div[1]/iframe')
        self.driver.switch_to.frame(iframe2)
        self.input('id', 'tinymce', '这是选项A')
        self.driver.switch_to.default_content()
        iframe3 = self.locateElement('xpath',
                                     '/html/body/div[2]/div/div[2]/div/form/div[3]/div/div/div/div[1]/div[2]/div[1]/iframe')
        self.driver.switch_to.frame(iframe3)
        self.input('id', 'tinymce', '这是选项b')
        self.driver.switch_to.default_content()
        iframe4 = self.locateElement('xpath',
                                     '/html/body/div[2]/div/div[2]/div/form/div[4]/div/div/div/div[1]/div[2]/div[1]/iframe')
        self.driver.switch_to.frame(iframe4)
        self.input('id', 'tinymce', '这是选项c')
        self.driver.switch_to.default_content()
        iframe4 = self.locateElement('xpath',
                                     '/html/body/div[2]/div/div[2]/div/form/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
        self.driver.switch_to.frame(iframe4)
        self.input('id', 'tinymce', '这是选项d')
        self.driver.switch_to.default_content()
        self.click('xpath', '/html/body/div[2]/div/div[2]/div/form/div[7]/div/div/label[4]/span[1]/span')
        button = self.locateElement('xpath', '/html/body/div[2]/div/div[2]/div/div[2]/button[2]')
        ActionChains(self.driver).move_to_element(button).perform()
        self.click('xpath', '/html/body/div[2]/div/div[2]/div/div[2]/button[2]')
        time.sleep(1)
        handles1 = self.driver.window_handles[-2]
        self.driver.switch_to.window(handles1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        self.click('xpath', '//*[@class="el-button el-button--primary is-plain is-round"]')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-checkbox__inner"]')

        self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')
        self.input('xpath',
                   '/html/body/section/main/div/div/div[2]/div/div[1]/div[1]/div/div[2]/form/div/div/div/input',
                   '1')

        self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')
    def delete_work(self):
        time.sleep(1)
        self.click('xpath','/html/body/section/section/main/div/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr[3]/td[4]/div/a[4]/span')
        self.click('xpath', '//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(2)
        msg=self.text('cs','body > div.el-message.el-message--success.is-closable')
        return msg