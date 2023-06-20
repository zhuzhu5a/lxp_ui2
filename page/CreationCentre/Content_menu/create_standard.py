import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page import Login_page
from page.Login_page import LoginPage
from common.element import Loctor
import datetime
class Standard(LoginPage):
    def __init__(self,driver,url,user,pwd,org):
        self.driver=driver
        lp=LoginPage(driver)
        lp.login_successful(url,user,pwd,org)

        try:
            creator = ('#v-step_creator')
            self.click('cs', creator)
        except:
            print('没有创作中心')
    def create_standard(self):
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.driver.implicitly_wait(5)
        self.click('cs', '#app > section > aside > div > ul > div:nth-child(2) > li')
        self.click('id','tab-standard')
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        # time.sleep()
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M')
        self.input('xpath','/html/body/section/div[1]/div[2]/div/form/div[2]/div/div/input','测评'+self.dt)
        # 选择按行业
        self.click('cs','#app > div.app-container.tw-flex-1 > div.create-container > div > form > div:nth-child(3) > div > div > div > input')
        self.locateElement('xpath','//*[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('cs','body > div > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
        # 选择岗位
        self.click('cs','#app > div.app-container.tw-flex-1 > div.create-container > div > form > div:nth-child(4) > div > div > div.el-input.el-input--suffix > input')
        self.locateElement('xpath','//*[@class="el-scrollbar__view el-cascader-menu__list"]')
        self.click('xpath','/html/body/div[2]/div[1]/div/div[1]/ul/li[3]')
        self.locateElement('xpath','/html/body/div[2]/div[1]/div[2]/div[1]')
        self.click('xpath','/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[3]')
        self.locateElement('xpath','/html/body/div[2]/div[1]/div[3]/div[1]')
        self.click('xpath','/html/body/div[2]/div[1]/div[3]/div[1]/ul/li[3]')
        self.input('cs','#app > div.app-container.tw-flex-1 > div.create-container > div > form > div:nth-child(5) > div > div > textarea','测评描述描述')
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        time.sleep(1)
        self.click('xpath','//*[@class="el-button add el-button--primary el-button--small is-plain is-round"]')
        self.input('xpath','//*[@placeholder="请输入技能名称"]','技能'+self.dt)
        self.click('xpath','/html/body/section/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/div[1]/div/div/button')
        self.click('xpath','/html/body/section/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/div[2]/button[2]')
        el = self.locateElement('xpath','//*[name()="rect"][@y="0"] and[]')
        ActionChains(self.driver).click(el).perform()
        self.input('xpath','//*[@placeholder="请输入技能点名称"]','技能点')
        self.input('xpath','//*[placeholder="分数"]','1')

        time.sleep(3)
    def delete_standeard(self):
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.driver.implicitly_wait(5)
        self.click('cs','#app > section > aside > div > ul > div:nth-child(2) > li')
        self.click('id', 'tab-standard')
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div.tw-flex.tw-flex-col.tw-flex-1.tw-h-full.tw-space-y-s3.tw-overflow-auto > div.tw-flex-1.tw-relative.scroll-bar.custom-pl-s1.tw-pr-4 > div > div:nth-child(1) > div.tw-absolute.tw-right-5.tw--top-2\.5.el-dropdown > i')
        self.locateElement('xpath','//*[@class="el-dropdown-menu el-popper"]')
        time.sleep(1)
        self.click('xpath','/html/body/ul/li[2]')
        time.sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default el-button--small el-button--primary "]')
        msg=self.text('cs','body > div.el-message.el-message--success.is-closable.el-message-fade-leave-active.el-message-fade-leave-to')
        return msg


