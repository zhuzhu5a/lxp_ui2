import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page import Login_page
from page.Login_page import LoginPage
from common.element import Loctor
from page.CreationCentre.Material_menu.create_picture import Picture
from page.CreationCentre.Material_menu.create_question import Question
from page.CreationCentre.Material_menu.create_work import Work
import datetime
class Study_collection(LoginPage):
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
        self.click('cs','#app > section > aside > div > ul > div:nth-child(2) > li')
        self.driver.implicitly_wait(5)
        driver.find_element(By.CSS_SELECTOR, '#app > section > aside > div > ul > div:nth-child(3) > li').click()
        self.click('id','tab-study_resource')
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
        time.sleep(1)

        zi=self.text('cs','#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div.tw-flex-1.tw-relative.scroll-bar.custom-px-s1 > div > div:nth-child(1) > div.tw-flex.tw-flex-col.custom-p-s4.custom-space-y-s4.tw-flex-1 > p')
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div.tw-flex-1.tw-relative.scroll-bar.custom-px-s1 > div > div:nth-child(1) > div.tw-flex.tw-absolute.tw-right-0.tw-top-0.tw-w-full.tw-h-10.tw-items-center.tw-justify-end.tw-pr-2\.5.linear-gradient > span')

        return zi
    def study_exam(self):

        time.sleep(1)
        a = 1
        while a <= 1:
            self.click('cs',
                       '#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.operate > button:nth-child(3)')
            self.click('xpath', '/html/body/section/section/main/div/div[2]/div/div[4]/div/div[2]/div[2]/ul/li[2]')

            self.input('xpath', '//*[@placeholder="填写试卷名称"]', '学习资源创建考试' + self.dt)
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
            self.input('cs',
                       '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div.tw-flex-1.tw-relative.scroll-bar.custom-px-s1 > div.el-table.el-table--fit.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_1_column_2.el-table__cell > div > div > div > div.tw-w-\[200px\].el-input.el-input--small > input',
                       '学习资源' + self.dt)
            self.click('xpath',
                       '/html/body/section/section/main/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div[2]/i')
            time.sleep(1)
            self.click('xpath',
                       '/html/body/section/section/main/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div/a/span')
            self.click('xpath', '/html/body/section/section/main/div/div[2]/div/div[1]/div/div[3]/div[1]/button[2]')
            time.sleep(1)
            iframe = self.driver.find_element('xpath',
                                              '/html/body/div[2]/div/div[2]/div/form/div[1]/div/div/div/div[1]/div[2]/div[1]/iframe')
            self.driver.switch_to.frame(iframe)
            self.input('id', 'tinymce', '这是题干')
            self.driver.switch_to.default_content()
            iframe2 = self.locateElement('xpath',
                                         '/html/body/div[2]/div/div[2]/div/form/div[2]/div/div/div/div[1]/div[2]/div[1]/iframe')
            self.driver.switch_to.frame(iframe2)
            self.input('id', 'tinymce', '这是选项A')
            self.driver.switch_to.default_content()
            iframe3 = self.locateElement('xpath',
                                         '/html/body/div[2]/div/div[2]/div/form/div[3]/div/div/div/div[1]/div[2]/div[1]/iframe')
            self.driver.switch_to.frame(iframe3)
            self.input('id', 'tinymce', '这是选项b')
            self.driver.switch_to.default_content()
            iframe4 = self.locateElement('xpath',
                                         '/html/body/div[2]/div/div[2]/div/form/div[4]/div/div/div/div[1]/div[2]/div[1]/iframe')
            self.driver.switch_to.frame(iframe4)
            self.input('id', 'tinymce', '这是选项c')
            self.driver.switch_to.default_content()
            iframe4 = self.locateElement('xpath',
                                         '/html/body/div[2]/div/div[2]/div/form/div[5]/div/div/div/div[1]/div[2]/div[1]/iframe')
            self.driver.switch_to.frame(iframe4)
            self.input('id', 'tinymce', '这是选项d')
            self.driver.switch_to.default_content()
            self.click('xpath', '/html/body/div[2]/div/div[2]/div/form/div[7]/div/div/label[4]/span[1]/span')
            button = self.locateElement('xpath', '/html/body/div[2]/div/div[2]/div/div[2]/button[2]')
            ActionChains(self.driver).move_to_element(button).perform()
            self.click('xpath', '/html/body/div[2]/div/div[2]/div/div[2]/button[2]')
            time.sleep(1)
            handles1 = self.driver.window_handles[-3]
            self.driver.switch_to.window(handles1)
            self.click('xpath', '//*[@class="el-button el-button--default is-round"]')
            self.click('xpath', '//*[@class="el-button el-button--primary is-plain is-round"]')
            time.sleep(1)
            self.click('xpath', '//*[@class="el-checkbox__inner"]')

            self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')
            self.input('xpath',
                       '/html/body/section/main/div/div/div[2]/div/div[1]/div[1]/div/div[2]/form/div/div/div/input',
                       '1')
            self.input('xpath',
                       '/html/body/section/main/div/div/div[1]/div/div[2]/form/div/div/div/input', '1')
            self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')
            # handles2=self.driver.window_handles[-1]
            # self.driver.switch_to.window(handles2)
            # self.click('xpath','//*[@class="hover:tw-text-[#409EFF]"]')
            # time.sleep(1)
            # self.click('xpath','/html/body/section/section/main/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div/div/a[2]/span')
            # time.sleep(1)
            # self.click('xpath','//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
            # msg=self.text('xpath','//*[@class="el-message__content"]')
            # handles1 = self.driver.window_handles[-2]
            # self.driver.switch_to.window(handles1)
            a = a + 1
            # return msg

    def study_video(self):
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.operate > button:nth-child(3)')
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div:nth-child(4) > div > div.el-dialog__body > div:nth-child(1) > ul > li:nth-child(1)')
        dir_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
        path=os.path.join(dir_path,"video",'1.mp4')
        print(path)
        self.input('xpath','//*[@class="el-upload__input"]',path)
        time.sleep(1)
        self.dt1=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        self.select_all_clean('xpath','//*[@placeholder="请输入视频名称"]')
        self.input('xpath','//*[@placeholder="请输入视频名称"]',self.dt1)
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        time.sleep(1)
        self.locateElement('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.el-tree > div:nth-child(2) > div > div > div > div.activity-title > div > div > span')

    def study_local_office(self):
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.operate > button:nth-child(3)')
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div:nth-child(4) > div > div.el-dialog__body > div:nth-child(1) > ul > li:nth-child(2)')
        self.click('xpath', '//*[@class="el-upload--text"]')
        time.sleep(1)
        self.input('xpath', '//*[@placeholder="请输入文章标题"]', '文章标题' + self.dt)
        self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')
        time.sleep(1)

        self.locateElement('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.el-tree > div:nth-child(3) > div > div > div > div.activity-title > div > div > span')

    def study_upload_office(self):
        self.click('cs',
                   '#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.operate > button:nth-child(3)')
        time.sleep(1)
        self.click('cs',
                   '#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div:nth-child(4) > div > div.el-dialog__body > div:nth-child(1) > ul > li:nth-child(2)')
        dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

        path = os.path.join(dir_path, "data", "SAAS官网文案(1).docx")
        self.input('xpath', '//*[@name="file"]', path)
        time.sleep(2)
        self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')
        time.sleep(1)
        self.locateElement('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.el-tree > div:nth-child(4) > div > div > div > div.activity-title > div > div > span')

    def study_img(self):
        self.click('cs',
                   '#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.operate > button:nth-child(3)')
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div:nth-child(4) > div > div.el-dialog__body > div:nth-child(1) > ul > li:nth-child(3)')
        Picture.picture(self)
        self.locateElement('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.el-tree > div:nth-child(5) > div > div > div > div.activity-title > div > div > span')

    def study_question(self):
        self.click('cs',
                   '#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.operate > button:nth-child(3)')
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div:nth-child(4) > div > div.el-dialog__body > div:nth-child(2) > ul > li:nth-child(1)')
        Question.question(self)
        self.locateElement('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.el-tree > div:nth-child(6) > div > div > div > div.activity-title > div > div > span')

    def study_work(self):
        self.click('cs',
                   '#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.operate > button:nth-child(3)')
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div:nth-child(4) > div > div.el-dialog__body > div:nth-child(2) > ul > li:nth-child(3)')
        Work.work(self)

    def study_link(self):
        self.click('cs',
                   '#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.operate > button:nth-child(3)')
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div:nth-child(4) > div > div.el-dialog__body > div:nth-child(3) > ul > li')
        time.sleep(1)
        self.input('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div:nth-child(7) > div > div.el-dialog__body > form > div.el-form-item.is-required > div > div > input','https://www.baidu.com')

        self.input('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div:nth-child(7) > div > div.el-dialog__body > form > div:nth-child(3) > div > div > input','百度')
        self.click('xpath','//*[@class="el-select"]')
        self.locateElement('xpath','//*[@class="el-scrollbar__view el-select-dropdown__list"]')
        time.sleep(1)
        self.click('cs','body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)')
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        self.locateElement('cs','#app > section > main > div > div.tw-flex.tw-flex-col.tw-w-full.tw-bg-white.tw-flex-1 > div > div.el-tree > div:nth-child(7) > div > div > div > div.activity-title > div > div > span')






