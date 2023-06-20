import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page.Login_page import LoginPage
import datetime

class space_manger(LoginPage):
    def __init__(self,driver,url,user,pwd,org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd, org)
        time.sleep(1)
        self.click('cs','#app > section > aside > div > div.tw-flex-1 > div.tw-flex.tw-flex-col.tw-justify-between > div:nth-child(2) > div > a')
        handle=self.driver.window_handles[-1]
        self.driver.switch_to.window(handle)
        time.sleep(1)

    def connect_channel(self):
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('id','tab-my')
        time.sleep(1)
        self.click('cs',
                   'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-wrap.tw-card-container.tw-content-start.tw-card-3 > div:nth-child(1)')
        button = self.locateElement('xpath', '/html/body/div[2]/div/div[2]/div/div[5]/button[2]')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        self.click('xpath','//*[@class="el-icon-more tw-text-3xl tw-cursor-pointer tw-text-gray-400 el-dropdown-selfdefine"]')
        time.sleep(1)
        self.click('xpath','//*[@class="el-dropdown-menu__item"]')
        time.sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(1)

        return msg

    def connect_standard(self):
        self.click('id', 'tab-standard')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('id', 'tab-my')
        time.sleep(1)
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-wrap.tw-card-container.tw-content-start.tw-card-3 > div:nth-child(1)')
        button = self.locateElement('cs', 'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(5) > button.el-button.el-button--primary.is-round')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        self.click('xpath','//*[@class="el-icon-more tw-text-3xl tw-cursor-pointer tw-text-gray-400 el-dropdown-selfdefine"]')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-dropdown-menu__item"]')
        time.sleep(1)
        self.click('xpath',
                   '//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(1)
        return msg

    def connet_class(self):
        self.click('id','tab-group')
        time.sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('id','tab-my')
        time.sleep(1)
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-wrap.tw-card-container.tw-content-start.tw-card-3 > div:nth-child(1)')
        button = self.locateElement('cs',
                                    'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(5) > button.el-button.el-button--primary.is-round')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        self.click('xpath',
                   '//*[@class="el-icon-more tw-text-3xl tw-cursor-pointer tw-text-gray-400 el-dropdown-selfdefine"]')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-dropdown-menu__item"]')
        time.sleep(1)
        self.click('xpath',
                   '//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(1)
        return msg

    def connect_study(self):
        self.click('id', 'tab-study_resource')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('id', 'tab-my')
        time.sleep(1)
        self.click('cs',
                   'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-wrap.tw-card-container.tw-content-start.tw-card-3 > div:nth-child(1)')
        button = self.locateElement('cs',
                                    'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(5) > button.el-button.el-button--primary.is-round')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        self.click('xpath',
                   '//*[@class="el-icon-more tw-text-3xl tw-cursor-pointer tw-text-gray-400 el-dropdown-selfdefine"]')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-dropdown-menu__item"]')
        time.sleep(1)
        self.click('xpath',
                   '//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(1)
        return msg

    def connect_teach(self):
        self.click('id', 'tab-teaching_resource')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('id', 'tab-my')
        time.sleep(1)
        self.click('cs',
                   'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-wrap.tw-card-container.tw-content-start.tw-card-3 > div:nth-child(1)')
        button = self.locateElement('cs',
                                    'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(5) > button.el-button.el-button--primary.is-round')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        self.click('xpath',
                   '//*[@class="el-icon-more tw-text-3xl tw-cursor-pointer tw-text-gray-400 el-dropdown-selfdefine"]')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-dropdown-menu__item"]')
        time.sleep(1)
        self.click('xpath',
                   '//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(1)
        return msg

    def connect_task(self):
        self.click('id', 'tab-task')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('id', 'tab-my')
        time.sleep(1)
        self.click('cs',
                   'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(3) > div:nth-child(1) > div > div.tw-flex.tw-flex-row.tw-text-neutral.tw-cursor-pointer')
        button = self.locateElement('cs',
                                    'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(5) > button.el-button.el-button--primary.is-round')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        self.click('xpath',
                   '//*[@class="el-icon-more tw-text-3xl tw-cursor-pointer tw-text-gray-400 el-dropdown-selfdefine"]')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-dropdown-menu__item"]')
        time.sleep(1)
        self.click('xpath',
                   '//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(1)

    def connect_train(self):
        self.click('id', 'tab-training')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('id', 'tab-my')
        time.sleep(1)
        self.click('cs',
                   'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-wrap.tw-card-container.tw-content-start.tw-card-2 > div:nth-child(1)')
        button = self.locateElement('cs',
                                    'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(5) > button.el-button.el-button--primary.is-round')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        self.click('xpath',
                   '//*[@class="el-icon-more tw-text-3xl tw-cursor-pointer tw-text-gray-400 el-dropdown-selfdefine"]')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-dropdown-menu__item"]')
        time.sleep(1)
        self.click('xpath',
                   '//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(1)
        return msg

    def connect_contest(self):
        self.click('id', 'tab-contest')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('id', 'tab-my')
        time.sleep(1)
        self.click('cs',
                   'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-col.tw-space-y-5.list-container > div:nth-child(1) > div')
        button = self.locateElement('cs',
                                    'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(5) > button.el-button.el-button--primary.is-round')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        self.click('xpath',
                   '//*[@class="el-icon-more tw-text-3xl tw-cursor-pointer tw-text-gray-400 el-dropdown-selfdefine"]')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-dropdown-menu__item"]')
        time.sleep(1)
        self.click('xpath',
                   '//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(1)
        return msg

    def connect_vi_task(self):
        self.click('id', 'tab-virtual_task')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('id', 'tab-my')
        time.sleep(1)
        self.click('cs',
                   'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(3) > div:nth-child(1) > div > div.tw-flex.tw-flex-row.tw-text-neutral.tw-cursor-pointer')
        button = self.locateElement('cs',
                                    'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(5) > button.el-button.el-button--primary.is-round')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        self.click('xpath',
                   '//*[@class="el-icon-more tw-text-3xl tw-cursor-pointer tw-text-gray-400 el-dropdown-selfdefine"]')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-dropdown-menu__item"]')
        time.sleep(1)
        self.click('xpath',
                   '//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(1)

    def basic_info(self):
        img_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        self.click('cs', '#app > section > aside > div > ul > div:nth-child(3) > li')
        time.sleep(1)
        self.input('xpath','/html/body/section/section/main/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div/input',img_path+'\\img/1.jpeg')
        time.sleep(1)
        self.input('xpath','/html/body/section/section/main/div[2]/div[2]/div/div[1]/form/div[2]/div/div/div/div/input',img_path+'\\img/1720x150.jpg')
        time.sleep(3)
        self.dt=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        self.input('xpath','/html/body/section/section/main/div[2]/div[2]/div/div[1]/form/div[4]/div/div/input',self.dt)
        self.input('xpath','//*[@maxlength="300"]',self.dt+'修改')
        time.sleep(1)
        self.click('xpath','//*[@class="el-button tw-w-[150px] el-button--primary is-round"]')
        time.sleep(1)
        msg=self.text('xpath','//*[@class="el-message el-message--success is-closable"]')
        return msg
