import os
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page.Login_page import LoginPage
from common.element import Loctor
import datetime
class Do_train_camp(LoginPage):
    def __init__(self, driver, url, user, pwd,org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd,org)
    def do_free_train(self,name):
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        try:
            self.click('cs', 'body > div.el-dialog__wrapper > div > div.el-dialog__header > button')
        except:
            pass
        self.input('xpath', '//input[@placeholder="请输入关键词"]', name)
        self.input('xpath', '//input[@placeholder="请输入关键词"]', Keys.ENTER)
        time.sleep(2)
        self.click('xpath','//*[@class="tw-border tw-border-[#e6e6e6] common-card tw-relative tw-max-w-full tw-responsive-card tw-flex-shrink-0 tw-rounded-md img-lazyload tw-flex tw-w-[530px] tw-bg-white tw-relative"]')
        time.sleep(3)
        # '#app > div.tw-w-full.tw-h-full.tw-mx-auto.custom-p-s4.scroll-bar.tw-bg-\[\#f7f7f7\].tw-flex-1 > div.tw-flex.tw-justify-between.tw-w-full.md\:tw-flex-row.tw-flex-col.tw-flex-wrap.tw-items-stretch.md\:tw-h-full.md\:tw-min-h-\[700px\] > div.tw-w-full.md\:tw-w-\[25\%\].tw-h-full.tw-min-w-\[200px\].tw-bg-white.tw-flex.tw-flex-col.tw-mt-\[10px\].md\:tw-mt-0 > div.tw-w-full.tw-h-\[58px\].tw-min-h-\[58px\].tw-flex.tw-justify-center.tw-items-center > button'
        self.click('xpath', '//*[@class="tw-text-skillbox-blue tw-cursor-pointer tw-text-sm"]')
        time.sleep(1)
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.locateElement('xpath','//*[@class="title"]')
        handles1 = self.driver.window_handles[0]
        self.driver.switch_to.window(handles1)
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        self.input('xpath','//*[@placeholder="请填写作品标题"]','作品'+self.dt)
        time.sleep(1)
        # 获取当前的文件绝对地址
        os.path.realpath(__file__)
        # 获取当前文件所在目录的路径
        os.path.dirname(os.path.realpath(__file__))
        # 获取当前文件所在目录的上一级目录  os.path.dirname()可以使用多次，直到到达要读写文件的上一级目录为止
        dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        # 要读取img路径下的661-600文件
        path = os.path.join(dir_path, "img", "661-600x420.jpg")
        self.input('xpath','//*[@accept=".jpg, .png, .jpeg"]',path)
        time.sleep(1)
        self.input('xpath','//*[@multiple="multiple"]',path)
        time.sleep(1)
        self.click('cs','body > div.el-dialog__wrapper.works > div > div.el-dialog__body > form > div:nth-child(5) > div > button')


