import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page import Login_page
from page.Login_page import LoginPage
from common.element import Loctor
import datetime
class Train_camp(LoginPage):
    def __init__(self,driver,url,user,pwd,org):
        self.driver=driver
        lp=LoginPage(driver)
        lp.login_successful(url,user,pwd,org)

        try:
            creator = ('#v-step_creator')
            self.click('cs', creator)
        except:
            print('没有创作中心')

        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        time.sleep(2)
        self.click('cs','#app > section > aside > div > ul > div:nth-child(3) > li')
        self.driver.implicitly_wait(5)
        self.click('id','tab-training_camp')
                        # '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div.tw-flex.tw-flex-col.tw-flex-1.tw-h-full.tw-space-y-s3.tw-overflow-auto > div:nth-child(1) > div > div > button'
                        # '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div.tw-flex.tw-flex-col.tw-flex-1.tw-h-full.tw-space-y-s3.tw-overflow-auto > div:nth-child(1) > div > div > button'
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')
    def open_train_camp(self,campname):
        self.input('xpath','//*[@placeholder="请输入名称"]',campname+self.dt)
        self.click('xpath', '//input[@placeholder="行业筛选"]')
        self.driver.implicitly_wait(5)
        self.locateElement('cs','body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs',
                   'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
        self.click('cs',
                   'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div > button')
        time.sleep(1)
        zi=self.text('cs','#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div.tw-flex.tw-flex-col.tw-flex-1.tw-h-full.tw-space-y-s3.tw-overflow-auto > div.tw-flex-1.tw-relative.scroll-bar.custom-pl-s1.tw-pr-4 > div > div:nth-child(1) > div.tw-flex.tw-flex-col.tw-flex-1.custom-px-s2.custom-py-s4.tw-w-0 > p')
        return zi

    def link_train(self):
        # 点击管理按钮
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div.tw-flex.tw-flex-col.tw-flex-1.tw-h-full.tw-space-y-s3.tw-overflow-auto > div.tw-flex-1.tw-relative.scroll-bar.custom-pl-s1.tw-pr-4 > div > div:nth-child(1) > div.tw-flex.tw-absolute.tw-right-0.tw-top-0.tw-w-full.tw-h-10.tw-items-center.tw-justify-end.tw-pr-2\.5.linear-gradient > span')
        # 点击关联按钮
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-col.scroll-bar.tw-mb-2\.5.tw-w-full.tw-bg-white.tw-flex-1.custom-px-s2 > div.tw-flex.tw-justify-between.tw-items-center.tw-mb-5 > div > button.el-button.el-button--default.is-round')
        # 点击＋号
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div > ul > li:nth-child(2) > span')
        # 点击确认按钮
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div > div.tw-p-5.tw-text-right > button.el-button.el-button--primary.is-round')
