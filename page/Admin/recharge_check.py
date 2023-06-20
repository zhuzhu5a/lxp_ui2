from time import sleep
from common.element import Loctor
from page.Login_page import LoginPage


class Rechargecheck(Loctor):
    def __init__(self, driver, url, user, pwd,org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd,org)
    def recgargeCheck(self):
        sleep(1)
        self.click('cs','#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div > div')
        sleep(1)
        self.click('xpath','//*[text()="退出登录"]')
        sleep(1)
        try:
            self.click('cs','#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > button > span')
            sleep(1)
        except:
            pass
        sleep(1)
        self.input('cs', '#pass-login > div:nth-child(1) > input', 'luke')
        self.input('cs', '#pass-login > div:nth-child(2) > input', '123456')
        self.click('cs', '#pass-login > div.form-group.password-box > button')
        sleep(1)
        self.click('xpath', '//*[text()="技能盒子"]')
        sleep(1)
        self.click('cs','#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div > div')
        sleep(1)
        self.click('xpath','//*[text()="管理后台"]')
        sleep(1)
        handles2=self.driver.window_handles
        self.driver.switch_to.window(handles2[-1])
        sleep(1)
        self.click('xpath','/html/body/div/section/header/div/div[2]/ul/li[6]')
        sleep(1)
        self.click('id','tab-recharge')
        sleep(1)
        self.click('xpath','/html/body/div/section/section/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/a[2]/span')
        sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default el-button--small el-button--primary confirm-del-btn"]')
