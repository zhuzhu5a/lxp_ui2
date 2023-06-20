import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page import Login_page
from page.Login_page import LoginPage
from common.element import Loctor
import datetime
class vi_Task(LoginPage):
    def __init__(self,driver,url,user,pwd,org):
        self.driver=driver
        lp=LoginPage(driver)
        lp.login_successful(url,user,pwd,org)

        try:
            creator = ('#v-step_creator')
            self.click('cs', creator)
        except:
            print('没有创作中心')
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.driver.implicitly_wait(5)
        self.click('cs', '#app > section > aside > div > ul > div:nth-child(2) > li')
        self.click('id','tab-virtual_task')
        time.sleep(2)

    def beginner(self,title):
        self.click('cs',
                   '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div:nth-child(1) > div > div > button')
        handles=self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.input('xpath','//*[@t_role="title"]',title+self.dt)
        self.click('xpath','//*[@t_role="profession"]')
        self.locateElement('cs','body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs','body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
        # 选择岗位
        self.click('xpath','//*[@placeholder="请选择"]')
        self.locateElement('xpath','/html/body/div[2]/div[1]/div')
        self.driver.implicitly_wait(5)
        self.click('xpath','html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]')
        self.locateElement('xpath','/html/body/div[2]/div[1]/div[2]')
        self.click('xpath','/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[6]/span')
        self.click('xpath', '//input[@type="text" and @placeholder="请选择数量等级"]')
        self.locateElement('cs',
                           'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        yonghudengji = self.locateElement('cs',
                                          'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)')
        self.click('cs',
                   'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)')
        yonghudengji1 = yonghudengji.text
        print(yonghudengji1)
        amount=self.locateElement('xpath','//span[@class="el-radio__label"]')
        amount1  =amount.text
        amount2=round(float(amount1.strip('\技能币')))
        self.click('xpath', '//*[@placeholder="选择评价维度"]')
        time.sleep(0.5)
        self.locateElement('xpath', '//*[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.click('xpath', '//*[@placeholder="选择评价标准"]')
        self.locateElement('xapth', '[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.input('xpath', '//*[@maxlength="3"]', '100')
        self.click('cs',
                   '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(14) > div > div > form > div:nth-child(2) > div > div.tw-flex.tw-flex-col.tw-space-y-5.el-col.el-col-16 > div > div.tw-flex.tw-justify-between.tw-items-center.tw-h-10.tw-pl-2\.5.el-col.el-col-4 > span:nth-child(2) > i')
        self.click('xpath', '//*[@t_role="button"]')
        time.sleep(1)
        self.locateElement('xpath', '//*[@class="tw-text-base tw-font-bold tw-text-primary"]')
        return yonghudengji1
    def primary(self,title):
        self.click('cs',
                   '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div:nth-child(1) > div > div > button')
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.input('xpath', '//*[@t_role="title"]', title + self.dt)
        self.click('xpath', '//*[@t_role="profession"]')
        self.locateElement('cs',
                           'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs',
                   'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
        # 选择岗位
        self.click('xpath', '//*[@placeholder="请选择"]')
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div')
        self.driver.implicitly_wait(5)
        self.click('xpath', 'html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]')
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div[2]')
        self.click('xpath', '/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[6]/span')

        self.click('xpath','//input[@type="text" and @placeholder="请选择数量等级"]')
        self.locateElement('cs','body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        yonghudengji =self.locateElement('cs','body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
        self.click('cs','body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
        yonghudengji1=yonghudengji.text
        print(yonghudengji1)
        # js='document.querySelector("#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div.el-form-item.no-bottom.is-required > div > div > div > div > div > input").removeAttribute("readonly");'
        # self.driver.execute_script(js)
        # self.clean_with_send('cs','#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div.el-form-item.no-bottom.is-required > div > div > div > div > div > input','初级职称')
        # self.input('cs','#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div.el-form-item.no-bottom.is-required > div > div > div > div > div > input','初级职称')
        amount = self.locateElement('xpath', '//span[@class="el-radio__label"]')
        amount1 = amount.text
        amount2 = round(float(amount1.strip('\技能币')))
        print(amount2)
        self.click('xpath','//*[@placeholder="选择评价维度"]')
        time.sleep(0.5)
        self.locateElement('xpath','//*[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath','/html/body/div[5]/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.click('xpath', '//*[@placeholder="选择评价标准"]')
        self.locateElement('xapth','[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath','/html/body/div[6]/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.input('xpath','//*[@maxlength="3"]','100')
        self.click('cs','#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(14) > div > div > form > div:nth-child(2) > div > div.tw-flex.tw-flex-col.tw-space-y-5.el-col.el-col-16 > div > div.tw-flex.tw-justify-between.tw-items-center.tw-h-10.tw-pl-2\.5.el-col.el-col-4 > span:nth-child(2) > i')
        self.click('xpath', '//*[@t_role="button"]')
        time.sleep(1)
        self.locateElement('xpath','//*[@class="tw-text-base tw-font-bold tw-text-primary"]')

        return yonghudengji1

    def intermediate(self,title):
        self.click('cs',
                   '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div:nth-child(1) > div > div > button')
        handles=self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.input('xpath','//*[@t_role="title"]',title+self.dt)
        self.click('xpath','//*[@t_role="profession"]')
        self.locateElement('cs','body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs','body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
        # 选择岗位
        self.click('xpath','//*[@placeholder="请选择"]')
        self.locateElement('xpath','/html/body/div[2]/div[1]/div')
        self.driver.implicitly_wait(5)
        self.click('xpath','html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]')
        self.locateElement('xpath','/html/body/div[2]/div[1]/div[2]')
        self.click('xpath','/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[6]/span')
        self.click('xpath', '//input[@type="text" and @placeholder="请选择数量等级"]')
        self.locateElement('cs',
                           'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        yonghudengji = self.locateElement('cs',
                                          'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
        self.click('cs',
                   'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
        yonghudengji1 = yonghudengji.text
        print(yonghudengji1)
        amount=self.locateElement('xpath','//span[@class="el-radio__label"]')
        amount1  =amount.text
        amount2=round(float(amount1.strip('\技能币')))
        self.click('xpath', '//*[@placeholder="选择评价维度"]')
        time.sleep(0.5)
        self.locateElement('xpath', '//*[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.click('xpath', '//*[@placeholder="选择评价标准"]')
        self.locateElement('xapth', '[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.input('xpath', '//*[@maxlength="3"]', '100')
        self.click('cs',
                   '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(14) > div > div > form > div:nth-child(2) > div > div.tw-flex.tw-flex-col.tw-space-y-5.el-col.el-col-16 > div > div.tw-flex.tw-justify-between.tw-items-center.tw-h-10.tw-pl-2\.5.el-col.el-col-4 > span:nth-child(2) > i')
        self.click('xpath', '//*[@t_role="button"]')
        time.sleep(1)
        self.locateElement('xpath', '//*[@class="tw-text-base tw-font-bold tw-text-primary"]')

        return yonghudengji1

    def senior(self,title):
        self.click('cs',
                   '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div:nth-child(1) > div > div > button')
        handles=self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.input('xpath','//*[@t_role="title"]',title+self.dt)
        self.click('xpath','//*[@t_role="profession"]')
        self.locateElement('cs','body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs','body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
        # 选择岗位
        self.click('xpath','//*[@placeholder="请选择"]')
        self.locateElement('xpath','/html/body/div[2]/div[1]/div')
        self.driver.implicitly_wait(5)
        self.click('xpath','html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]')
        self.locateElement('xpath','/html/body/div[2]/div[1]/div[2]')
        self.click('xpath','/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[6]/span')
        self.click('xpath', '//input[@type="text" and @placeholder="请选择数量等级"]')
        self.locateElement('cs',
                           'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        yonghudengji = self.locateElement('cs',
                                          'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(4)')
        self.click('cs',
                   'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(4)')
        yonghudengji1 = yonghudengji.text
        print(yonghudengji1)
        amount=self.locateElement('xpath','//span[@class="el-radio__label"]')
        amount1  =amount.text
        amount2=round(float(amount1.strip('\技能币')))
        self.click('xpath', '//*[@placeholder="选择评价维度"]')
        time.sleep(0.5)
        self.locateElement('xpath', '//*[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.click('xpath', '//*[@placeholder="选择评价标准"]')
        self.locateElement('xapth', '[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.input('xpath', '//*[@maxlength="3"]', '100')
        self.click('cs',
                   '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(14) > div > div > form > div:nth-child(2) > div > div.tw-flex.tw-flex-col.tw-space-y-5.el-col.el-col-16 > div > div.tw-flex.tw-justify-between.tw-items-center.tw-h-10.tw-pl-2\.5.el-col.el-col-4 > span:nth-child(2) > i')
        self.click('xpath', '//*[@t_role="button"]')
        time.sleep(1)
        self.locateElement('xpath', '//*[@class="tw-text-base tw-font-bold tw-text-primary"]')
        return yonghudengji1
    def add_software(self,title):
        self.click('cs',
                   '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div:nth-child(1) > div > div > button')
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.input('xpath', '//*[@t_role="title"]', title + self.dt)
        self.click('xpath', '//*[@t_role="profession"]')
        self.locateElement('cs',
                           'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs',
                   'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
        # 选择岗位
        self.click('xpath', '//*[@placeholder="请选择"]')
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div')
        self.driver.implicitly_wait(5)
        self.click('xpath', 'html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]')
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div[2]')
        self.click('xpath', '/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[6]/span')

        self.click('xpath', '//input[@type="text" and @placeholder="请选择数量等级"]')
        self.locateElement('cs',
                           'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        yonghudengji = self.locateElement('cs',
                                          'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)')
        self.click('cs',
                   'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)')
        yonghudengji1 = yonghudengji.text

        # js='document.querySelector("#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div.el-form-item.no-bottom.is-required > div > div > div > div > div > input").removeAttribute("readonly");'
        # self.driver.execute_script(js)
        # self.clean_with_send('cs','#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div.el-form-item.no-bottom.is-required > div > div > div > div > div > input','初级职称')
        # self.input('cs','#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div.el-form-item.no-bottom.is-required > div > div > div > div > div > input','初级职称')
        amount = self.locateElement('xpath', '//span[@class="el-radio__label"]')
        amount1 = amount.text
        self.click('xpath','/html/body/section/section/main/div/div[2]/div[2]/form/div[8]/div/div/button')
        time.sleep(0.5)
        try:
            self.click('xpath','/html/body/div[6]/div/div[2]/div/div[1]/div[1]')
            time.sleep(1)
            self.click('xpath','/html/body/div[6]/div/div[2]/div/div[2]/button')
        except:
            print('当前组织没有被分配的软件')
        time.sleep(3)
        amount2 = round(float(amount1.strip('\技能币')))

        self.click('xpath', '//*[@placeholder="选择评价维度"]')
        time.sleep(0.5)
        self.locateElement('xpath', '//*[@class="el-scrollbar__view el-select-dropdown__list"]')
        self.click('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.click('xpath', '//*[@placeholder="选择评价标准"]')
        self.locateElement('xapth', '[@class="el-scrollbar__view el-select-dropdown__list"]')
        time.sleep(1)
        self.click('xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[1]')
        time.sleep(0.5)
        self.input('xpath', '//*[@maxlength="3"]', '100')
        self.click('cs',
                   '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(14) > div > div > form > div:nth-child(2) > div > div.tw-flex.tw-flex-col.tw-space-y-5.el-col.el-col-16 > div > div.tw-flex.tw-justify-between.tw-items-center.tw-h-10.tw-pl-2\.5.el-col.el-col-4 > span:nth-child(2) > i')
        self.click('xpath', '//*[@t_role="button"]')
        time.sleep(1)
        title=self.text('xpath','//*[@class="tw-text-base tw-font-bold tw-text-primary"]')
        self.locateElement('xpath', '//*[@class="tw-text-base tw-font-bold tw-text-primary"]')
        self.locateElement('xpath', '//*[@class="tw-text-skillbox-blue tw-cursor-pointer tw-text-sm"]')
        all=(yonghudengji1,title)
        return all
    def delete(self):
        i = 0
        while i <= 5:
            try:
                sandian = self.locateElement('xpath',
                                             '/html/body/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/i')
                ActionChains(self.driver).move_to_element(sandian).perform()
                self.locateElement('xpath', '/html/body/ul')
                time.sleep(1)
                self.click('xpath', '/html/body/ul/li[2]')
                time.sleep(1)
                self.click('xpath', '//*[@class="el-button el-button--default el-button--small el-button--primary "]')
                time.sleep(1)
                msg = self.text('cs', 'body > div.el-message.el-message--success.is-closable > p')
            except:
                pass
            i = i + 1
        return msg





