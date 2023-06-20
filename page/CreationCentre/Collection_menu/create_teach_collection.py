import time
from selenium.webdriver.common.action_chains import ActionChains
from page.Login_page import LoginPage
import datetime
from page.CreationCentre.Collection_menu.create_study_collection import Study_collection
class teach_collection(LoginPage):
    def __init__(self,driver,url,user,pwd,org):
        self.driver=driver
        lp=LoginPage(driver)
        lp.login_successful(url,user,pwd,org)

        try:
            creator = ('#v-step_creator')
            self.click('cs', creator)
        except:
            print('没有创作中心')

        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        time.sleep(1)
        self.click('cs','#app > section > aside > div > ul > div:nth-child(3) > li')
        self.driver.implicitly_wait(5)
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div:nth-child(1) > div > button')
        time.sleep(1)
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    def open_resource(self,resourcename):
        self.input('xpath','//*[@placeholder="请输入名称"]',resourcename+self.dt)
        self.click('xpath', '//input[@placeholder="行业筛选"]')
        self.driver.implicitly_wait(5)
        self.locateElement('cs',
                           'body > div > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        self.click('cs',
                   'body > div > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)')
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div.tw-flex.tw-justify-between.tw-items-center > div > button.el-button.el-button--primary.is-round')
        time.sleep(5)
        zi = self.text('cs',
                       '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div.tw-flex-1.tw-relative.scroll-bar.custom-px-s1 > div > div:nth-child(1) > div.tw-flex.tw-flex-col.custom-p-s4.custom-space-y-s4.tw-flex-1 > p')
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div.tw-flex-1.tw-relative.scroll-bar.custom-px-s1 > div > div:nth-child(1) > div.tw-flex.tw-absolute.tw-right-0.tw-top-0.tw-w-full.tw-h-10.tw-items-center.tw-justify-end.tw-pr-2\.5.linear-gradient > span')
        return zi

    def study_exam(self):
        Study_collection.study_exam(self)
    def teach_video(self):
        Study_collection.study_video(self)

    def teach_local_office(self):
        Study_collection.study_local_office(self)

    def teach_upload_office(self):
        Study_collection.study_upload_office(self)
    def teach_img(self):
        Study_collection.study_img(self)

    def teach_work(self):
        Study_collection.study_work(self)

    def teach_link(self):
        Study_collection.study_link(self)
    def teach_question(self):
        Study_collection.study_question(self)