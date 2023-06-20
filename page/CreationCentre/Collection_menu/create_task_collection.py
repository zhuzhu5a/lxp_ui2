import time
from page.Login_page import LoginPage
import datetime
class Task_collection(LoginPage):
    def __init__(self,driver,url,user,pwd,org):
        self.driver=driver
        lp=LoginPage(driver)
        lp.login_successful(url,user,pwd,org)

        try:
            creator = ('#v-step_creator')
            self.click('cs', creator)
        except:
            print('没有创作中心')
        self.dt=datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        time.sleep(2)
        self.click('cs','#app > section > aside > div > ul > div:nth-child(3) > li')
        time.sleep(1)
        self.click('id','tab-task_collection')
    def task_collcetion(self):
        self.click('xpath','/html/body/section/section/main/div/div[2]/div[1]/div[1]/div/div/button')
        time.sleep(1)
        self.input('xpath','//*[@maxlength="25"]','工单合集'+self.dt)
        self.click('xpath', '//input[@placeholder="请选择行业分类"]')
        self.driver.implicitly_wait(5)
        self.locateElement('xpath','//*[@class="el-scrollbar__view el-cascader-menu__list"]')

        self.click('xpath',
                   '/html/body/div/div[1]/div/div[1]/ul/li[2]')
        self.click('xpath', '//input[@placeholder="请选择职位分类"]')
        self.locateElement('xpath','//*[@class="el-scrollbar__view el-cascader-menu__list"]')
        self.click('xpath', '/html/body/div[2]/div[1]/div/div[1]/ul/li[3]')
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]')
        self.click('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[3]')
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div[3]/div[1]')
        self.click('xpath', '/html/body/div[2]/div[1]/div[3]/div[1]/ul/li[3]')
        self.click('xpath', '//*[@class="el-button el-button--primary is-plain is-round"]')
        time.sleep(1)
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(3) > div:nth-child(1) > div.tpop-item-right > span > i')
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.show-btn > button.el-button.el-button--primary.is-round')
        self.click('xpath', '//*[@class="el-button el-button--primary el-button--medium is-round"]')
        msg = self.text('xpath', '//*[@class="el-message el-message--success"]')
        return msg
    def delete(self):
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div.tw-flex.tw-flex-col.tw-flex-1.tw-h-full.tw-space-y-s3.tw-overflow-auto > div.tw-flex-1.tw-relative.scroll-bar.custom-pl-s1.tw-pr-4 > div > div:nth-child(1) > div.tw-flex.tw-absolute.tw-right-0.tw-top-0.tw-w-full.tw-h-10.tw-items-center.tw-justify-end.tw-pr-2\.5.linear-gradient > span')
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.edit-camp.tw-mx-auto.tw-bg-white > form > div:nth-child(8) > div > div > a > span')
        time.sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default el-button--small el-button--primary "]')
        time.sleep(1)
        msg=self.text('xpath','//*[@class="el-message el-message--success is-closable"]')
        return msg
