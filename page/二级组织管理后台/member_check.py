import datetime
import time
from time import sleep
from page.Login_page import LoginPage
class Member_check(LoginPage):
    def __init__(self, driver, url, user, pwd,org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd,org)

    def member_check(self,org):
        self.click('cs',
                   '#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div > div')
        self.locateElement('xpath', '/html/body/ul')
        sleep(1)
        self.click('xpath', '//*[text()="切换组织"]')
        sleep(1)
        self.click('xpath',org)
        sleep(2)
        self.click('cs', '#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div > div')
        self.locateElement('xpath', '/html/body/ul')
        sleep(1)
        self.click('xpath', '//*[text()="组织管理"]')
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        sleep(1)
        self.click('id','tab-check')
        sleep(1)
        i = 0
        while i <= 100:
            try:
                self.click('xpath', '//*[text()="通过"]')
                sleep(1)
                self.click('xpath','//*[@placeholder="请选择分配的角色"]')
                self.locateElement('xpath','//*[@class="el-scrollbar__view el-select-dropdown__list"]')
                sleep(1)
                self.click('xpath','//*[text()="学生"]')
                sleep(1)
                self.click('xpath','//*[@class="el-dialog__footer"]')
                button=self.locateElement('xpath','/html/body/div[1]/div/section/div/section[2]/div/div[2]/div[5]/div/div[3]/span/button[2]')
                self.driver.execute_script("arguments[0].click();",button)
            except:
                pass
            i = i + 1
