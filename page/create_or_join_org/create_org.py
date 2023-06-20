import datetime

from time import sleep

from page.Login_page import LoginPage

class Create_org(LoginPage):
    def __init__(self, driver, url, user, pwd,org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd,org)

    def create_org(self):
        self.click('cs',
                   '#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div > div')
        self.locateElement('xpath', '/html/body/ul')
        sleep(1)
        self.click('xpath','/html/body/ul/li[7]')
        sleep(1)
        self.click('xpath','/html/body/div[2]/div[1]/div[2]/div[1]/div[3]/a[2]/div')
        sleep(1)
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        name=('自动'+self.dt)
        self.input('xpath','//*[@placeholder="请输入真实组织名称"]',name)
        sleep(1)
        self.click('xpath','//*[@class="cate-select category"]')
        self.click('xpath','/html/body/div[2]/div[1]/div[2]/div/div[3]/div[2]/select/option[2]')
        sleep(1)
        self.click('xpath','//*[@class="branch-input create-btn"]')
        sleep(1)
        self.click('xpath','/html/body/div[2]/div[1]/div[2]/div[1]/div[3]/div/div[1]')
        sleep(2)
        name2=self.text('xpath','//*[@class="tw-truncate"]')
        name3=(name,name2)
        return name3