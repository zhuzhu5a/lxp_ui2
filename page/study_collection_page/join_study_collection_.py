import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page.Login_page import LoginPage
from common.element import Loctor
import datetime
class join_study(LoginPage):
    def __init__(self,driver,url,user,pwd,org):
        self.driver=driver
        lp=LoginPage(driver)
        lp.login_successful(url,user,pwd,org)

    def join_study_resource(self,name):
        try:
            self.click('cs', 'body > div.el-dialog__wrapper > div > div.el-dialog__header > button')
        except:
            pass
        self.input('xpath', '//input[@placeholder="请输入关键词"]', name)
        time.sleep(1)
        self.input('xpath', '//input[@placeholder="请输入关键词"]', Keys.ENTER)
        time.sleep(2)
        self.click('xpath',
                   '//*[@class="tw-border tw-border-[#e6e6e6] common-card tw-relative tw-max-w-full tw-responsive-card tw-flex-shrink-0 tw-rounded-md img-lazyload tw-relative tw-cursor-pointer tw-flex tw-bg-white tw-w-[254px] tw-flex-col"]')
        time.sleep(1)
        self.click('xpath', '//button[@class="el-button tw-ml-auto el-button--primary el-button--mini is-round"]')