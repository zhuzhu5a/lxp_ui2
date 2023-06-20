import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page import Login_page
from page.Login_page import LoginPage
from common.element import Loctor
import datetime
class Task(LoginPage):
    def __init__(self,driver,url,user,pwd,org):

        self.driver=driver
        lp=LoginPage(driver)
        lp.login_successful(url,user,pwd,org)
    def task_before_momney(self):
        time.sleep(1)
        self.click('cs','#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div > div')
        self.locateElement('xpath','/html/body/ul')
        time.sleep(1)
        self.click('xpath','/html/body/ul/li[2]')
        # 进入账号设置页面
        config=self.driver.window_handles[1]
        self.driver.switch_to.window(config)
        time.sleep(1)
        self.click('xpath','//*[@class="el-submenu__title"]')
        time.sleep(1)
        self.click('cs','#app > div > section > div > section.app-nav > ul > div:nth-child(7) > li > ul > div:nth-child(1) > li')
        time.sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default el-button--small"]')
        ceter = self.driver.window_handles[-1]
        self.driver.switch_to.window(ceter)
        self.driver.implicitly_wait(5)
        self.beforetaskmoney=self.driver.find_element(By.CSS_SELECTOR,'#app > div > section > div > section.app-contain > div > div:nth-child(2) > div.tw-text-base.tw-text-primary.tw-mb-5 > span').text
        self.beforetaskmoney1 = round(float(self.beforetaskmoney.strip("\￥")))
        # print('发布任务前金额：', self.beforetaskmoney1)
        a=[self.beforetaskmoney,self.beforetaskmoney1]
        return a

    def task_after_momney(self):
        self.click('cs','#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div > div')
        self.locateElement('xpath', '/html/body/ul')
        zhanghaoshezhi=self.locateElement('xpath','/html/body/ul/li[2]')
        ActionChains(self.driver).move_to_element(zhanghaoshezhi).perform()
        self.click('xpath','/html/body/ul/li[2]')
        # 进入账号设置页面
        config = self.driver.window_handles[-1]
        self.driver.switch_to.window(config)
        self.click('xpath', '//*[@class="el-submenu__title"]')
        self.click('cs',
                   '#app > div > section > div > section.app-nav > ul > div:nth-child(7) > li > ul > div:nth-child(1) > li')
        self.click('xpath','//*[@class="el-button el-button--default el-button--small"]')
        ceter = self.driver.window_handles[-1]
        self.driver.switch_to.window(ceter)
        self.driver.implicitly_wait(5)
        aftertaskmoney = self.driver.find_element(By.CSS_SELECTOR,'#app > div > section > div > section.app-contain > div > div:nth-child(2) > div.tw-text-base.tw-text-primary.tw-mb-5 > span').text
        aftertaskmoney1 = round(float(aftertaskmoney.strip("\￥")))
        return aftertaskmoney1

    # aftertaskmoney=task_after_momney()
    #     招标模式
    def biddingtask(self,biaoti,momney):
        handles = self.driver.window_handles[0]
        self.driver.switch_to.window(handles)
        self.driver.implicitly_wait(5)

        try:
            creator = ('#v-step_creator')
            self.click('cs', creator)
        except:
            print('没有创作中心')
            time.sleep(5)
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.click('cs', '#app > section > aside > div > ul > div:nth-child(2) > li')
        self.click('xpath', '//*[@aria-controls="pane-task"]')
        time.sleep(2)
        # 点击创建任务按钮
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        # 进入创建任务页面
        window1= self.driver.window_handles[-1]
        self.driver.switch_to.window(window1)
        self.driver.implicitly_wait(5)
        self.dt=datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.driver.implicitly_wait(5)
        self.driver.back()
        self.driver.back()
        # self.click('cs', '#v-step_creator')
        # self.click('id', 'tab-task')
        # # 点击创建工单按钮
        # self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-1.tw-overflow-auto.custom-py-s2 > div.tw-flex.tw-flex-col.tw-flex-1.tw-h-full.tw-overflow-auto.tw-space-y-s4 > div:nth-child(1) > div > div > button')
        # # 进入创建工单页面
        # window1 = self.driver.window_handles[-1]
        # self.driver.switch_to.window(window1)
        # self.driver.implicitly_wait(5)
        # 输入工单标题     #app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div.el-form-item.is-success.is-required > div > div > input
        title=biaoti+self.dt
        self.input('cs','#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(1) > div > div > input',title)
        # 选择行业分类
        self.click('cs',
                   '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(4) > div > div > div > input')
        self.driver.implicitly_wait(5)
        self.locateElement('cs',
                           'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs',
                   'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
        # 选择岗位分类
        self.click('cs',
                   '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(5) > div > div > div.el-input.el-input--suffix > input')
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div')
        self.click('xpath', '/html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]')
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div[2]')
        self.click('xpath', '/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[6]/span')
        # 输入金额
        self.input('cs',
                   '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(10) > div > div > input',
                   momney)
        self.click('xpath','//*[text()="发布工单"]')

        return title
    def cpatask(self,biaoti,momney,password):
        handles = self.driver.window_handles[0]
        self.driver.switch_to.window(handles)
        self.driver.implicitly_wait(5)

        try:
            creator = ('#v-step_creator')
            self.click('cs', creator)
        except:
            print('没有创作中心')
            time.sleep(5)
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.click('cs', '#app > section > aside > div > ul > div:nth-child(2) > li')
        self.click('xpath', '//*[@aria-controls="pane-task"]')
        time.sleep(2)
        # 点击创建任务按钮
        self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')
        # 进入创建任务页面
        window1 = self.driver.window_handles[-1]
        self.driver.switch_to.window(window1)
        self.driver.implicitly_wait(5)
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.driver.implicitly_wait(5)
        self.driver.back()
        self.driver.back()
        self.input('cs','#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(1) > div > div > input',biaoti+self.dt)
#       选择比稿模式
        self.click('cs','#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(2) > div > div > div > div:nth-child(2) > div')
#       选择行业分类
        self.click('cs', '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(4) > div > div > div > input')
        self.driver.implicitly_wait(5)
        self.locateElement('cs', 'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs','body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
        self.click('cs', '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(5) > div > div > div.el-input.el-input--suffix > input')
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div')
        self.click('xpath','/html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]')
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div[2]')
        self.click('xpath', '/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[6]/span')
        self.input('cs', '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(10) > div > div > input',momney)
        self.click('cs', '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(17) > div > button.el-button.el-button--primary.is-round')
        self.driver.implicitly_wait(5)
        taskmoney = self.driver.find_element(By.CSS_SELECTOR, '#app > div.checkout-counter.tw-flex-1 > div.wrapper > div > div.order-wrap > div.item-order > div.order-total > p > span').text
        taskmoney1 = round(float(taskmoney.strip("\￥")))
        self.input('cs', '#pane-0 > form > div:nth-child(2) > div > div > input',password)
        self.click('cs', '#pane-0 > form > div:nth-child(3) > div > button.el-button.el-button--primary.is-round')
        # print('发布任务金额：',taskmoney1)
        return taskmoney1

    # taskmoney=task_after_momney()

    # taskmoney=cpatask()
        # 计件模式
    def pitask(self,biaoti,momney,password,zibiaoti,qty):
        handles = self.driver.window_handles[0]
        self.driver.switch_to.window(handles)
        self.driver.implicitly_wait(5)

        try:
            creator = ('#v-step_creator')
            self.click('cs', creator)
        except:
            print('没有创作中心')
            time.sleep(5)
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.click('cs','#app > section > aside > div > ul > div:nth-child(2) > li')
        self.click('xpath', '//*[@aria-controls="pane-task"]')
        time.sleep(2)
        # 点击创建任务按钮
        self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')
        # 进入创建任务页面
        window1 = self.driver.window_handles[-1]
        self.driver.switch_to.window(window1)
        self.driver.implicitly_wait(5)
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        self.driver.implicitly_wait(5)
        self.driver.back()
        self.driver.back()
        self.input('cs','#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(1) > div > div > input',biaoti+self.dt)
            #选择计件模式
        self.click('cs','#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(2) > div > div > div > div:nth-child(3) > div')
        #       选择行业分类
        self.click('cs',
                   '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(4) > div > div > div > input')
        self.driver.implicitly_wait(5)
        self.locateElement('cs',
                           'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs',
                   'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
        self.click('cs',
                   '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(5) > div > div > div.el-input.el-input--suffix > input')
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div')
        self.click('xpath', '/html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]')
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div[2]')
        self.click('xpath', '/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[6]/span')
        self.click('cs',
                   '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(14) > div > button.el-button.el-button--primary.is-round')
        self.driver.implicitly_wait(5)
        self.click('cs', '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.tw-flex.tw-flex-col.tw-space-y-4.custom-px-s2.tw-pb-4 > div.tw-flex.page-section.page_h.tw-items-center.tw-justify-between > button')
        self.driver.implicitly_wait(5)
        self.input('cs', '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.tw-flex.tw-flex-col.tw-space-y-4.custom-px-s2.tw-pb-4 > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > input',zibiaoti+self.dt)
        self.input('cs','#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.tw-flex.tw-flex-col.tw-space-y-4.custom-px-s2.tw-pb-4 > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div > div > input',qty)
        self.input('cs', '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.tw-flex.tw-flex-col.tw-space-y-4.custom-px-s2.tw-pb-4 > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(7) > div > div > input',momney)

        self.click('cs','#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.tw-flex.tw-flex-col.tw-space-y-4.custom-px-s2.tw-pb-4 > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(9) > div > button.el-button.el-button--primary.is-round')
        self.click('cs', '#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.tw-flex.tw-flex-col.tw-space-y-4.custom-px-s2.tw-pb-4 > div.page-section.tw-text-center > button')
        self.driver.implicitly_wait(5)
        taskmoney = self.driver.find_element(By.CSS_SELECTOR,'#app > div.checkout-counter.tw-flex-1 > div.wrapper > div > div.order-wrap > div.item-order > div.order-total > p > span').text
        taskmoney1 = round(float(taskmoney.strip("\￥")))
        self.input('cs', '#pane-0 > form > div:nth-child(2) > div > div > input',password)
        self.click('cs','#pane-0 > form > div:nth-child(3) > div > button.el-button.el-button--primary.is-round')
        return taskmoney1
    def delete_task(self):
        handles = self.driver.window_handles[0]
        self.driver.switch_to.window(handles)
        self.driver.implicitly_wait(5)
        try:
            creator = ('#v-step_creator')
            self.click('cs', creator)
        except:
            print('没有创作中心')
            time.sleep(1)
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        time.sleep(1)
        self.click('cs', '#app > section > aside > div > ul > div:nth-child(2) > li')
        time.sleep(1)
        self.click('xpath', '//*[@aria-controls="pane-task"]')
        time.sleep(3)
        i=0

        while i<=2:

            try:
                sandian = self.locateElement('xpath',
                                             '/html/body/section/section/main/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/i')
                ActionChains(self.driver).move_to_element(sandian).perform()
                self.locateElement('xpath', '/html/body/ul')
                time.sleep(1)
                self.click('xpath', '/html/body/ul/li[2]')
                # try:
                #     retunmoney1=self.text('xpath','/html/body/div[1]/div/div[2]/div[1]/div[2]/div/p[2]')
                #     returnmoney2 = round(float(retunmoney1.strip("\￥")))
                #
                #
                # except:
                #     returnmoney2=0
                time.sleep(1)
                self.click('xpath', '//*[@class="el-button el-button--default el-button--small el-button--primary "]')
                time.sleep(1)


                msg = self.text('cs', 'body > div.el-message.el-message--success.is-closable > p')
            except:
                pass

            # returnmoney = returnmoney + returnmoney2
            i=i+1

        # retunmoney=returnmoney

        # return returnmoney2


