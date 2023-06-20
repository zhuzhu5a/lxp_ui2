import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page.Login_page import LoginPage
from common.element import Loctor
class Check(LoginPage):
    def __init__(self, driver, url, user, pwd,org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd,org)

    def check_join_class(self):

        # self.click('cs','#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div:nth-child(5) > div')
        # time.sleep(1)
        # xiaoxitongzhi=self.locateElement('xpath','/html/body/ul')
        # ActionChains(self.driver).move_to_element(xiaoxitongzhi).perform()
        # self.click('xpath','/html/body/ul/div[2]/li[1]')
        # time.sleep(2)

        #     time.sleep(1)
        #     self.click('cs','#app > section > aside > div > ul > div:nth-child(7) > li')
        #     # self.click('cs','#\32 89 > div.content > div.member-box.tw-mt-s4.custom-px-s1 > div > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_1_column_6.is-center.operate-box.el-table__cell > div > a.el-link.el-link--primary > span')
        #     self.click('xpath','//*[class="el-button el-button--default el-button--small el-button--primary "]')
        #     time.sleep(1)
        try:
            self.driver.find_element(By.CSS_SELECTOR, '#v-step_creator').click()
        except:
            print("没有创作中心")
        # 进入创作中心
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        time.sleep(2)
        self.click('cs', '#app > section > aside > div > ul > div:nth-child(4) > li')
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div.tw-flex-1.tw-relative.scroll-bar.custom-px-s1 > div > div:nth-child(1) > div.tw-flex.tw-absolute.tw-right-0.tw-top-0.tw-w-full.tw-h-10.tw-items-center.tw-justify-end.tw-pr-2\.5.linear-gradient > span')
        time.sleep(2)
        self.click('cs','#app > section > aside > div > ul > div:nth-child(6) > li')
        time.sleep(1)
        self.click('cs','#tab-check')
        time.sleep(1)
        i=0
        while i<= 100:
            try:
                self.click('link_text','同意')
                time.sleep(1)
                self.click('cs', 'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button')
                time.sleep(1)
            except:
                pass
            i=i+1

