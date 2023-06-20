import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page.Login_page import LoginPage
from common.element import Loctor
import datetime
class do_study(LoginPage):
    def __init__(self,driver,url,user,pwd,org,name):
        self.driver=driver
        lp=LoginPage(driver)
        lp.login_successful(url,user,pwd,org)
        try:
            self.click('cs', 'body > div.el-dialog__wrapper > div > div.el-dialog__header > button')
        except:
            pass
        self.input('xpath', '//input[@placeholder="请输入关键词"]', name)
        self.input('xpath', '//input[@placeholder="请输入关键词"]', Keys.ENTER)
        time.sleep(2)
        self.click('xpath',
                   '//*[@class="tw-border tw-border-[#e6e6e6] common-card tw-relative tw-max-w-full tw-responsive-card tw-flex-shrink-0 tw-rounded-md img-lazyload tw-relative tw-cursor-pointer tw-flex tw-bg-white tw-w-[254px] tw-flex-col"]')
        time.sleep(1)
    def do_study_exam(self):
        # 选择考试         #app > div.tw-w-full.tw-h-full.tw-relative.tw-overflow-hidden.tw-bg-\[\#f7f7f7\].tw-flex-1 > div > div > div.tw-w-full.md\:tw-w-\[25\%\].tw-h-full.tw-min-w-\[200px\].tw-bg-white.tw-flex.tw-flex-col.tw-mt-\[10px\].md\:tw-mt-0 > div.tw-w-full.tw-px-2.tw-flex.tw-flex-col.tw-flex-1.scroll-bar > div.el-tree.dirTree.tw-px-2 > div.el-tree-node.is-expanded.is-current.is-focusable.is-checked
        self.click('cs','#app > div.tw-w-full.tw-h-full.tw-relative.tw-overflow-hidden.tw-bg-\[\#f7f7f7\].tw-flex-1 > div > div > div.tw-w-full.md\:tw-w-\[25\%\].tw-h-full.tw-min-w-\[200px\].tw-bg-white.tw-flex.tw-flex-col.tw-mt-\[10px\].md\:tw-mt-0 > div.tw-w-full.tw-px-2.tw-flex.tw-flex-col.tw-flex-1.scroll-bar > div.el-tree.dirTree.tw-px-2 > div:nth-child(2)')
        # 点击开始考试按钮
        time.sleep(1)
        self.click('xpath','/html/body/section/div[1]/div/div/div[1]/div[1]/div/div/div/div[3]/button')
        self.click('xpath',
                   '//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(1)
        self.click('xpath','/html/body/section/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/label')
        self.click('xpath', '//*[@class="el-button el-button--primary is-round"]')
        time.sleep(1)
        self.click('xpath', '/html/body/div[1]/div/div[3]/button[2]')

    def do_study_work(self):
        #         选择作业
        self.click('cs','#app > div.tw-w-full.tw-h-full.tw-relative.tw-overflow-hidden.tw-bg-\[\#f7f7f7\].tw-flex-1 > div > div > div.tw-w-full.md\:tw-w-\[25\%\].tw-h-full.tw-min-w-\[200px\].tw-bg-white.tw-flex.tw-flex-col.tw-mt-\[10px\].md\:tw-mt-0 > div.tw-w-full.tw-px-2.tw-flex.tw-flex-col.tw-flex-1.scroll-bar > div.el-tree.dirTree.tw-px-2 > div:nth-child(1)')
        time.sleep(1)
        self.click('xpath','/html/body/section/div[1]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]')
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        time.sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default el-button--small el-button--primary "]')
    def do_study_video(self):
        self.click('cs','#app > div.tw-w-full.tw-h-full.tw-relative.tw-overflow-hidden.tw-bg-\[\#f7f7f7\].tw-flex-1 > div > div > div.tw-w-full.md\:tw-w-\[25\%\].tw-h-full.tw-min-w-\[200px\].tw-bg-white.tw-flex.tw-flex-col.tw-mt-\[10px\].md\:tw-mt-0 > div.tw-w-full.tw-px-2.tw-flex.tw-flex-col.tw-flex-1.scroll-bar > div.el-tree.dirTree.tw-px-2 > div:nth-child(3)')
        time.sleep(1)
        self.click('xpath','//*[@class="vjs-big-play-button"]')

    def do_study_question(self):
        self.click('cs','#app > div.tw-w-full.tw-h-full.tw-relative.tw-overflow-hidden.tw-bg-\[\#f7f7f7\].tw-flex-1 > div > div > div.tw-w-full.md\:tw-w-\[25\%\].tw-h-full.tw-min-w-\[200px\].tw-bg-white.tw-flex.tw-flex-col.tw-mt-\[10px\].md\:tw-mt-0 > div.tw-w-full.tw-px-2.tw-flex.tw-flex-col.tw-flex-1.scroll-bar > div.el-tree.dirTree.tw-px-2 > div:nth-child(7)')
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        iframe=self.driver.find_element('xpath','/html/body/section/div[1]/div/div/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/div[2]/div[1]/iframe')
        self.driver.switch_to.frame(iframe)
        self.dt=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        self.input('id','tinymce',self.dt)
        self.driver.switch_to.default_content()
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        time.sleep(2)
        msg=self.text('xpath','//*[@class="el-message__content"]')
        return msg
    def do_study_link(self):
        self.click('cs','#app > div.tw-w-full.tw-h-full.tw-relative.tw-overflow-hidden.tw-bg-\[\#f7f7f7\].tw-flex-1 > div > div > div.tw-w-full.md\:tw-w-\[25\%\].tw-h-full.tw-min-w-\[200px\].tw-bg-white.tw-flex.tw-flex-col.tw-mt-\[10px\].md\:tw-mt-0 > div.tw-w-full.tw-px-2.tw-flex.tw-flex-col.tw-flex-1.scroll-bar > div.el-tree.dirTree.tw-px-2 > div:nth-child(8)')
        self.click('xpath','//*[@class="tw-text-skillbox-blue tw-font-semibold"]')
        handle=self.driver.window_handles[-1]
        self.driver.switch_to.window(handle)
        time.sleep(1)
        self.locateElement('id','kw')



