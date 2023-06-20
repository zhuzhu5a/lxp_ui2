from time import sleep

from selenium.webdriver.common.action_chains import ActionChains

from common.element import Loctor
class Contestcheck(Loctor):

    def contestCheck(self):
        sleep(1)
        handles = self.driver.window_handles[-2]
        self.driver.switch_to.window(handles)
        self.click('cs',
                   '#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div > div')
        self.locateElement('xpath', '/html/body/ul')
        try:
            tuichudenglu = self.locateElement('xpath', '/html/body/ul/li[10]/span')
            ActionChains(self.driver).move_to_element(tuichudenglu).perform()
            self.click('xpath', '/html/body/ul/li[10]/span')

        except:
            tuichudenglu2 = self.locateElement('xpath', '/html/body/ul/li[7]/span')
            ActionChains(self.driver).move_to_element(tuichudenglu2).perform()
            self.click('xpath', '/html/body/ul/li[7]/span')
        self.click('xpath','//*[@class="el-button login-btn el-button--primary is-round"]')
        sleep(1)
        self.input('cs', '#pass-login > div:nth-child(1) > input', 'luke')
        self.input('cs', '#pass-login > div:nth-child(2) > input', '123456')
        self.click('cs', '#pass-login > div.form-group.password-box > button')
        sleep(1)
        self.click('xpath', '//*[text()="技能盒子"]')
        sleep(1)
        self.click('cs',
                   '#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div > div')
        self.locateElement('xpath', '/html/body/ul')
        guanlihoutai = self.locateElement('xpath', '/html/body/ul/li[8]')
        ActionChains(self.driver).move_to_element(guanlihoutai).perform()
        self.click('xpath', '/html/body/ul/li[8]')
        houtai = self.driver.window_handles[-1]
        self.driver.switch_to.window(houtai)
        sleep(1)
        self.click('cs', '#app > section > header > div > div.center > ul > li:nth-child(4)')
        self.click('cs','#app > section > section > div > div.left-content.tw-border-\[\#dce1e6\].tw-border-r.scroll-bar > ul > div:nth-child(6) > a > li')
        self.click('xpath','/html/body/div/section/section/div/div[2]/div/div[2]/div/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/a[2]/span')
        sleep(1)
        self.click('xpath','//*[@class="el-button el-button--primary el-button--small"]')
