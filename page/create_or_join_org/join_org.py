import datetime
from time import sleep
from page.Login_page import LoginPage
class Join_org(LoginPage):
    def __init__(self, driver, url, user, pwd,org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd,org)

    def join_org(self,org):
        self.click('cs',
                   '#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div > div')
        self.locateElement('xpath', '/html/body/ul')
        sleep(1)
        self.click('xpath', '//*[text()="加入或创建组织"]')
        sleep(1)
        self.click('xpath','/html/body/div[2]/div[1]/div[2]/div[1]/div[3]/a[1]/div')
        sleep(1)
        self.input('xpath','//*[@placeholder="输入组织域名或组织名称"]',org)
        self.click('xpath','//*[@class="search-btn"]')
        sleep(1)
        self.click('xpath','//*[@class="enter-btn"]')
        sleep(1)
        self.input('xpath','//*[@placeholder="请填写理由，非必填"]','加入理由')
        self.click('xpath','//*[@class="layui-layer-btn0"]')
        sleep(1)
        msg=self.text('xpath','/html/body/div[4]/div')
        return msg