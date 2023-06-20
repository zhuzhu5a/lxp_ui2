import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page.Login_page import LoginPage
from common.element import Loctor
import datetime
class Do_plan(LoginPage):
    def __init__(self,driver,url,user,pwd,org):
        self.driver=driver
        lp=LoginPage(driver)
        lp.login_successful(url,user,pwd,org)
    def join_class(self,classname):
        try:
            self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__header > button')
        except:
            pass
        self.input('xpath','//input[@placeholder="请输入关键词"]',classname)
        time.sleep(1)
        self.input('xpath','//input[@placeholder="请输入关键词"]',Keys.ENTER)
        time.sleep(2)
        self.click('xpath','//*[@class="tw-border tw-border-[#e6e6e6] common-card tw-relative tw-max-w-full tw-responsive-card tw-flex-shrink-0 tw-rounded-md img-lazyload tw-flex tw-flex-col tw-w-[254px] tw-bg-white"]')
        time.sleep(1)
        self.click('xpath','//button[@class="el-button el-button--primary is-round"]')

    def do_plan(self,classname):
        try:
            self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__header > button')
        except:
            pass
        self.input('xpath','//input[@placeholder="请输入关键词"]',classname)
        time.sleep(1)
        self.input('xpath','//input[@placeholder="请输入关键词"]',Keys.ENTER)
        time.sleep(2)
        self.click('xpath','//*[@class="tw-border tw-border-[#e6e6e6] common-card tw-relative tw-max-w-full tw-responsive-card tw-flex-shrink-0 tw-rounded-md img-lazyload tw-flex tw-flex-col tw-w-[254px] tw-bg-white"]')
        time.sleep(1)
        self.click('cs','#app > div.tw-w-full.tw-bg-skillbox-white.scroll-bar.tw-flex-1 > div > div.content > div.bottom > div.left > div.view-container > div > div > div.map-container > a')
        guanqia=self.locateElement('cs','#app > div.tw-w-full.tw-bg-skillbox-white.scroll-bar.tw-flex-1 > div > div.content > div.bottom > div.left > div.view-container')
        ActionChains(self.driver).move_to_element(guanqia).perform()#app > div.tw-w-full.tw-bg-skillbox-white.scroll-bar.tw-flex-1 > div > div.content > div.bottom > div.left > div.view-container > div > div > div.map-wrapper > div.map-container-out > div.map-container > div.point
        guanqia1=self.locateElement('cs','#app > div.tw-w-full.tw-bg-skillbox-white.scroll-bar.tw-flex-1 > div > div.content > div.bottom > div.left > div.view-container > div > div > div.map-wrapper > div.map-container-out > div.map-container > span > span > div')
        ActionChains(self.driver).move_to_element(guanqia1).perform()
        self.click('xpath','/html/body/div/div[1]/div[3]/button')
        time.sleep(3)
        a = self.driver.current_window_handle
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.click('cs','#app > div.stage-detail-container.tw-bg-skillbox-white.tw-flex-1 > div > div.content > div.view-container.custom-p-s1 > div > div > div.el-tree-node.is-expanded.is-focusable > div.el-tree-node__content > div > div')
        b=self.driver.current_window_handle
        o = self.driver.window_handles
        print(o)
        for curg in o:
            if curg != a and curg != b:
                self.driver.switch_to.window(curg)
        print(curg)
        time.sleep(1)


        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        self.click('cs','body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary')
        time.sleep(1)
        self.click('xpath','/html/body/section/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/label')
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        time.sleep(1)
        self.click('xpath','/html/body/div[1]/div/div[3]/button[2]')
        time.sleep(1)
        self.driver.switch_to.window(o[1])
        result=self.text('xpath','//*[@class="primary"]')
        return result

