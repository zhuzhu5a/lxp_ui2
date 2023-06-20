import datetime
import time
import unittest
from ddt import ddt, data ,unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from common.getdata import GetData
from page.Login_page import LoginPage
from common.element import Loctor
class Class1(LoginPage):
    def __init__(self,driver,url,user,pwd,org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd,org)
        r=driver.current_window_handle
        # 点击创作中心按钮
        try:
            driver.find_element(By.CSS_SELECTOR, '#v-step_creator').click()
        except:
            print("没有创作中心")
        # 进入创作中心
        handles = driver.window_handles[-1]
        driver.switch_to.window(handles)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, '#app > section > aside > div > ul > div:nth-child(4) > li').click()
        a = driver.current_window_handle
        # f = driver.find_element(By.CSS_SELECTOR,
        #                         '#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > span').text
        # print(f)
        # driver.implicitly_wait(5)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@class="el-button el-button--primary is-round"]').click()
        time.sleep(2)
        o = driver.window_handles
        for curg in o:
            if curg != a and curg != r:
                driver.switch_to.window(curg)
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    def Cloud_class(self,className):
        self.driver.implicitly_wait(5)
        time.sleep(1)
         #         输入班级名称
        self.input('cs','#app > section > main > div > div.content > form > div:nth-child(3) > div > div > input',className+self.dt)
        time.sleep(1)
        # 选择行业分类
        self.click('xpath','//input[@placeholder="请选择行业"]')
        self.driver.implicitly_wait(5)
        self.locateElement('cs',
                           'body > div > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs',
                   'body > div > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
        # 点击保存按钮
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.content > form > div:nth-child(8) > div > div > button.el-button.el-button--primary.is-round')
        time.sleep(1)
        self.first_name = self.text('cs', '#app > section > aside > div > div.tw-flex.tw-flex-col.tw-space-y-2.tw-p-6 > p')
        return self.first_name

    def Cloud_chuangye(self,className,number):
        # 选择云创业模块
        self.click('cs','#app > section > main > div > div.content > form > div:nth-child(1) > div > div > div > div:nth-child(2)')
        # 输入班级名称
        self.input('cs', '#app > section > main > div > div.content > form > div:nth-child(3) > div > div > input', className + self.dt)
        # 选择行业分类
        time.sleep(1)
        self.click('xpath','//input[@placeholder="请选择行业"]')
        self.driver.implicitly_wait(5)
        self.locateElement('cs',
                           'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs',
                   'body > div > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
        # 填写分组成员上限
        self.input('cs','#app > section > main > div > div.content > form > div:nth-child(6) > div > div.el-input > input',number)
        # 点击保存按钮

        self.click('cs','#app > section > main > div > div.content > form > div:nth-child(9) > div > div > button.el-button.el-button--primary.is-round')
        time.sleep(1)
        zi = self.text('cs', '#app > section > aside > div > ul > div:nth-child(7) > li')
        return zi

    def Cloud_shixi(self,className,number):
        # 选择云实习模块
        self.click('cs','#app > section > main > div > div.content > form > div:nth-child(1) > div > div > div > div:nth-child(3)')
        # 输入班级名称
        self.input('cs', '#app > section > main > div > div.content > form > div:nth-child(3) > div > div > input',
                   className + self.dt)
        # 选择行业分类
        self.click('xpath','//input[@placeholder="请选择行业"]')
        self.driver.implicitly_wait(5)
        self.locateElement('cs',
                           'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs',
                   'body > div > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
        # 填写分组成员上限
        self.input('cs',
                   '#app > section > main > div > div.content > form > div:nth-child(6) > div > div.el-input > input',
                   number)
        # 点击保存按钮

        self.click('cs','#app > section > main > div > div.content > form > div:nth-child(9) > div > div > button.el-button.el-button--primary.is-round')
        time.sleep(1)
        zi = self.text('cs', '#app > section > aside > div > ul > div:nth-child(7) > li')
        return zi

    def private_class(self,className):
        #         输入班级名称
        self.input('cs', '#app > section > main > div > div.content > form > div:nth-child(3) > div > div > input', className + self.dt)
        # 选择行业分类
        self.click('xpath','//input[@placeholder="请选择行业"]')
        self.driver.implicitly_wait(5)
        self.locateElement('cs',
                           'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs',
                   'body > div > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
       # 点击私密
        self.click('cs','#app > section > main > div > div.content > form > div:nth-child(7) > div > div > label:nth-child(2) > span.el-radio__label')
        # 点击保存按钮
        self.click('cs','#app > section > main > div > div.content > form > div:nth-child(8) > div > div > button.el-button.el-button--primary.is-round')
        time.sleep(1)
        zi=self.text('cs','#app > section > aside > div > ul > div:nth-child(7) > li')
        return zi
    def delete_class(self):
        self.click('cs','#app > section > aside > div > ul > div:nth-child(7) > li')
        self.driver.find_element(By.LINK_TEXT,'删除班级').click()
        time.sleep(1)
        self.click('xpath','//button[@class="el-button el-button--default el-button--small el-button--primary "]')
        time.sleep(1)
        msg=self.text('cs','body > div.el-message.el-message--success.is-closable > p')
        return msg
    def class_plan(self,planname,barrier):
        time.sleep(1)
        self.click('cs','#app > section > aside > div > ul > div:nth-child(2) > li')
        time.sleep(1)
        self.click('xpath', '//button[@class="el-button el-button--primary is-round"]')
        self.input('xpath', '//input[@placeholder="填写名称"]',planname+self.dt)
        self.click('xpath','/html/body/section/section/main/div[2]/div[2]/div/div[2]/div/form/div[4]/button')
        # ac=ActionChains(self.driver)
        # button=self.locateElement('xpath', '//button[@type="button"]')
        # ac.move_to_element(button).perform()
        # ac.click(button).perform()
        # self.driver.execute_script("arguments[0].click();",button)
        time.sleep(1)
        self.click('xpath','//*[@class="project-item"]')
        time.sleep(1)
        self.click('xpath', '//button[@class="el-button el-button--primary is-round"]')
        self.input('xpath', '//input[@placeholder="填写名称"]', barrier)
        self.click('xpath', '/html/body/section/section/main/div[2]/div[2]/div/div[2]/div/form/div[3]/button')
        self.click('xpath', '/html/body/section/section/main/div[2]/div[1]/div[3]/div[3]/div/div[1]/div[2]/span/span/button')
        nr=self.locateElement('xpath','//*[@class="add-course"]')
        ActionChains(self.driver).move_to_element(nr).perform()
        self.click('xpath','/html/body/div/ul/li[6]')

        self.click('xpath','/html/body/section/section/main/div[2]/div[1]/div[3]/div[3]/div/div[4]/div/div[2]/div/div/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/label')
        self.click('xpath','/html/body/section/section/main/div[2]/div[1]/div[3]/div[3]/div/div[4]/div/div[2]/div/div/div[4]/button[2]')
        time.sleep(2)
        self.click('xpath','/html/body/section/section/main/div[2]/div[1]/div[3]/div[3]/div/div[1]/div[1]/button')

    def exam(self):

        time.sleep(1)
        self.click('id', 'tab-file')
        self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')
        self.click('xpath',
                   '/html/body/section/section/main/div[2]/div[2]/div/div/div[4]/div/div[2]/div[2]/ul/li[1]')
        self.input('xpath', '//*[@placeholder="填写试卷名称"]', '班级创建考试' + self.dt)
        self.input('xpath', '//*[@placeholder="填写答题时长"]', '1')
        self.click('xpath', '/html/body/section/section/main/div/div/div/div/div/div/button[2]')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--primary is-plain is-round"]')
        time.sleep(1)
        self.click('xpath', '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/span[2]')
        handles1 = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles1)
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        self.select_all_clean('cs',
                              '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div.tw-flex-1.tw-relative.scroll-bar.custom-px-s1 > div.el-table.el-table--fit.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_1_column_2.el-table__cell > div > div > div > div.tw-w-\[200px\].el-input.el-input--small > input',
                              )
        self.input('cs','#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div.tw-flex-1.tw-relative.scroll-bar.custom-px-s1 > div.el-table.el-table--fit.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_1_column_2.el-table__cell > div > div > div > div.tw-w-\[200px\].el-input.el-input--small > input','班级'+self.dt)
        self.click('xpath', '/html/body/section/section/main/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div[2]/i')
        time.sleep(1)
        self.click('xpath',
                   '/html/body/section/section/main/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div/a/span')
        self.click('xpath', '/html/body/section/section/main/div/div[2]/div/div[1]/div/div[3]/div[1]/button[2]')
        time.sleep(1)
        iframe=self.driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/form/div[1]/div/div/div/div[1]/div[2]/div[1]/iframe')
        self.driver.switch_to.frame(iframe)
        self.input('id','tinymce','这是题干')
        self.driver.switch_to.default_content()
        iframe2=self.locateElement('xpath','/html/body/div[2]/div/div[2]/div/form/div[2]/div/div/div/div[1]/div[2]/div[1]/iframe')
        self.driver.switch_to.frame(iframe2)
        self.input('id','tinymce','这是选项A')
        self.driver.switch_to.default_content()
        iframe3=self.locateElement('xpath','/html/body/div[2]/div/div[2]/div/form/div[3]/div/div/div/div[1]/div[2]/div[1]/iframe')
        self.driver.switch_to.frame(iframe3)
        self.input('id','tinymce','这是选项b')
        self.driver.switch_to.default_content()
        iframe4=self.locateElement('xpath','/html/body/div[2]/div/div[2]/div/form/div[4]/div/div/div/div[1]/div[2]/div[1]/iframe')
        self.driver.switch_to.frame(iframe4)
        self.input('id','tinymce','这是选项c')
        self.driver.switch_to.default_content()
        iframe4 = self.locateElement('xpath',
                                 '/html/body/div[2]/div/div[2]/div/form/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
        self.driver.switch_to.frame(iframe4)
        self.input('id', 'tinymce', '这是选项d')
        self.driver.switch_to.default_content()
        self.click('xpath','/html/body/div[2]/div/div[2]/div/form/div[7]/div/div/label[4]/span[1]/span')
        button=self.locateElement('xpath','/html/body/div[2]/div/div[2]/div/div[2]/button[2]')
        ActionChains(self.driver).move_to_element(button).perform()
        self.click('xpath','/html/body/div[2]/div/div[2]/div/div[2]/button[2]')
        time.sleep(1)
        handles1 = self.driver.window_handles[-2]
        self.driver.switch_to.window(handles1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        self.click('xpath','//*[@class="el-button el-button--primary is-plain is-round"]')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-checkbox__inner"]')

        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        self.input('xpath', '/html/body/section/main/div/div/div[2]/div/div[1]/div[1]/div/div[2]/form/div/div/div/input','1')
        self.input('xpath',
                   '/html/body/section/main/div/div/div[1]/div/div[2]/form/div/div/div/input', '1')
        self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')

    def connect_task(self):
        time.sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(3) > div:nth-child(1) > div > div.tw-flex.tw-flex-row.tw-text-neutral.tw-cursor-pointer > div.tw-flex.tw-flex-col.tw-flex-1.md\:tw-ml-4.tw-justify-between > div.tw-flex.tw-text-base.tw-items-center.tw-text-primary.tw-justify-between > div.tpop-item-right > span > i')
        button=self.locateElement('xpath','/html/body/div[2]/div/div[2]/div/div[5]/button[2]')
        # ActionChains(self.driver).move_to_element(button).perform()
        self.driver.execute_script('arguments[0].click();',button)
        self.locateElement('xpath','//*[@class="tw-font-bold tw-text-primary tw-line-clamp-2 tw-break-all tw-leading-5"]')

    def connect_train_camp(self):
        self.click('id','tab-camp')
        time.sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-wrap.tw-card-container.tw-content-start.tw-card-2 > div:nth-child(1)')
        button=self.locateElement('xpath','/html/body/div[2]/div/div[2]/div/div[5]/button[2]')
        ActionChains(self.driver).move_to_element(button).perform()
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg=self.text('xpath','//*[@class="el-message__content"]')
        self.locateElement('xpath','//*[@class="common-card-title"]')
        return msg

    def connect_study(self):
        self.click('id','tab-study_resource')
        time.sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-wrap.tw-card-container.tw-content-start.tw-card-3 > div:nth-child(1)')
        button = self.locateElement('xpath','/html/body/div[2]/div/div[2]/div/div[5]/button[2]')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        self.locateElement('xpath', '//*[@class="common-card-title"]')
        return msg

    def connect_teach(self):
        self.click('id', 'tab-teaching_resource')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('cs',
                   'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-wrap.tw-card-container.tw-content-start.tw-card-3 > div:nth-child(1)')
        button = self.locateElement('xpath', '/html/body/div[2]/div/div[2]/div/div[5]/button[2]')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        self.locateElement('xpath', '//*[@class="common-card-title"]')
        return msg

    def conncet_standard(self):
        self.click('id','tab-standard')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-wrap.tw-card-container.tw-content-start.tw-card-3 > div:nth-child(1)')
        button = self.locateElement('xpath', '/html/body/div[2]/div/div[2]/div/div[5]/button[2]')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        self.locateElement('xpath', '//*[@class="common-card-title tw-text-center"]')
        return msg

    def connect_channel(self):
        self.click('id','tab-channel')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-wrap.tw-card-container.tw-content-start.tw-card-3 > div:nth-child(1)')
        button = self.locateElement('xpath', '/html/body/div[2]/div/div[2]/div/div[5]/button[2]')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        self.locateElement('xpath', '//*[@class="common-card-title"]')
        return msg

    def connect_contest(self):
        self.click('cs','#app > section > aside > div > ul > div:nth-child(3) > li')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
        time.sleep(1)
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.tw-flex.tw-flex-col.tw-space-y-5.list-container > div:nth-child(1) > div')
        time.sleep(1)
        button = self.locateElement('xpath', '/html/body/div[2]/div/div[2]/div/div[5]/button[2]')
        self.driver.execute_script('arguments[0].click();', button)
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        self.locateElement('xpath', '//*[@class="tw-text-left tw-text-primary tw-line-clamp-2 tw-mr-3 tw-flex-1 tw-leading-5"]')
        return msg

    def add_member(self):
        self.click('cs','#app > section > aside > div > ul > div:nth-child(6) > li')
        time.sleep(1)
        self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')
        time.sleep(2)
        iframe = self.locateElement('xpath','/html/body/div/iframe')
        self.driver.switch_to.frame(iframe)
        self.input('xpath','//*[@placeholder="请输入内容"]','朱宇2')
        time.sleep(1)
        self.click('cs','#tree_container > div > div.el-tree-node.is-expanded > div.el-tree-node__children > div:nth-child(406) > div.el-tree-node__content')
        self.click('xpath','//*[@class="el-button confirm el-button--default"]')
        self.driver.switch_to.default_content()
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message__content"]')
        print("11",msg)
        # self.locateElement('cs','#\33 97 > div.content.tw-flex.tw-justify-between.tw-space-x-5.custom-p-s3 > div.tw-flex-1.tw-w-0.tw-space-y-5 > div.member-box > div > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(2) > td.el-table_3_column_18.is-left.el-table__cell > div > div > span')
        self.click('xpath','//*[@class="el-icon-plus tw-mr-1"]')
        time.sleep(1)
        self.input('xpath','//*[@placeholder="输入名称"]','学习小组')
        self.click('xpath','/html/body/div[2]/div/div[2]/form/div[2]/button')
        return msg

    def basic_info(self):
        self.click('cs', '#app > section > aside > div > ul > div:nth-child(7) > li')
        time.sleep(1)
        self.dt=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        self.select_all_clean('xpath','/html/body/section/section/main/div[2]/div[3]/form/div[3]/div/div/input')
        self.input('xpath','/html/body/section/section/main/div[2]/div[3]/form/div[3]/div/div/input',self.dt)
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        time.sleep(1)
        msg = self.text('cs','body > div.el-message.el-message--success.is-closable > p')
        sec_name=self.text('cs', '#app > section > aside > div > div.tw-flex.tw-flex-col.tw-space-y-2.tw-p-6 > p')
        time.sleep(5)
        print('第一个名称', self.first_name)
        print('第二个名称', sec_name)
        if self.first_name != sec_name:
            print('修改名称成功')
        else:
            print('修改名称失败')
        return msg






