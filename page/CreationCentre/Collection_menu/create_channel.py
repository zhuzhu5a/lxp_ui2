import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from page.Login_page import LoginPage
import datetime
class Channel(LoginPage):
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
        self.click('id','tab-channel')
    def channel(self):
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        self.input('xpath','//*[@placeholder="请输入职业路径标题"]',self.dt)
        self.click('cs','body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div.el-form-item.btn-center > div > button.el-button.el-button--primary.is-round')
        time.sleep(1)
        self.one_name = self.text('cs',
                                  '#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div.tw-flex-1.tw-relative.scroll-bar.custom-px-s1 > div > div:nth-child(1) > div.tw-flex.tw-flex-col.custom-p-s4.custom-space-y-s4.tw-flex-1 > span')

    def conctent_standard(self):
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div.tw-flex-1.tw-relative.scroll-bar.custom-px-s1 > div > div:nth-child(1) > div.tw-flex.tw-absolute.tw-right-0.tw-top-0.tw-w-full.tw-h-10.tw-items-center.tw-justify-end.tw-pr-2\.5.linear-gradient > span')
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.channel-assess-container.tw-w-full.tw-bg-white.tw-flex-1.custom-px-s1.custom-py-s2 > div.tw-flex.tw-justify-between.tw-items-center > div > button.el-button.el-button--primary.el-button--medium.is-plain.is-round')
        time.sleep(1)
        self.click('cs','body > div.el-dialog__wrapper.popupChosen > div > div.el-dialog__body > div.grid > div:nth-child(1)')
        queding=self.locateElement('cs','body > div.el-dialog__wrapper.popupChosen > div > div.el-dialog__body > div.dialog-footer > div.footer-btn > button.el-button.el-button--primary.is-round')
        ActionChains(self.driver).move_to_element(queding).perform()
        self.click('cs','body > div.el-dialog__wrapper.popupChosen > div > div.el-dialog__body > div.dialog-footer > div.footer-btn > button.el-button.el-button--primary.is-round')
        time.sleep(1)
        msg=self.text('xpath','//*[@class="el-message__content"]')
        return msg
    def add_classify(self):
        self.click('xpath','//*[@class="el-button el-button--primary el-button--medium is-round"]')
        time.sleep(1)
        self.input('xpath','//*[@placeholder="请输入名称"]',self.dt)
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        time.sleep(1)
        self.click('cs','#app > section > main > div > div.channel-assess-container.tw-w-full.tw-bg-white.tw-flex-1.custom-px-s1.custom-py-s2 > div.el-tree.job-tree.tw-mt-5 > div:nth-child(2) > div.el-tree-node__content > div > span.operate-box.tw-space-x-4.tw-hidden.md\:tw-block > span:nth-child(2)')
        time.sleep(1)
        self.click('cs','body > div.el-dialog__wrapper.popupChosen > div > div.el-dialog__body > div.grid > div:nth-child(2)')
        queding = self.locateElement('cs','body > div.el-dialog__wrapper.popupChosen > div > div.el-dialog__body > div.dialog-footer > div.footer-btn > button.el-button.el-button--primary.is-round')
        ActionChains(self.driver).move_to_element(queding).perform()
        self.click('cs','body > div.el-dialog__wrapper.popupChosen > div > div.el-dialog__body > div.dialog-footer > div.footer-btn > button.el-button.el-button--primary.is-round')
        time.sleep(1)
        msg = self.text('xpath', '//*[@class="el-message el-message--success is-closable"]')
        return msg
    def basic_information_menu(self):
        self.click('cs','#app > section > aside > div > ul > div:nth-child(2) > li')
        time.sleep(1)
        dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
        path = os.path.join(dir_path, "img", "1.jpeg")
        print(path)
        self.input('cs','#app > section > main > div > form > div:nth-child(1) > div > div > div > input',path)
        time.sleep(1)
        self.input('cs','#app > section > main > div > form > div:nth-child(2) > div > div > div > input',path)
        time.sleep(1)
        self.select_all_clean('xpath','//*[@maxlength="20"]')
        self.dt2 = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        self.input('xpath','//*[@maxlength="20"]',self.dt2)
        self.click('xpath','//*[@class="el-button tw-py-4 custom-px-s2 tw-rounded-full el-button--primary is-round"]')
        time.sleep(1)
        second_name = self.text('cs',
                                '#app > section > aside > div > div.tw-flex.tw-flex-col.tw-px-7.tw-space-y-2 > span')
        if self.one_name != second_name:
            print('名称修改成功')
        else:
            print('名称修改失败')

        msg=self.text('xpath','//*[@class="el-message__content"]')
        return msg
    def delete_channel(self):
        time.sleep(1)
        self.click('xpath','//*[@class="el-link--inner"]')
        time.sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default el-button--small el-button--primary confirm-danger-btn"]')
        time.sleep(1)
        msg=self.text('xpath','//*[@class="tw-text-base tw-text-[#333]"]')
        return msg





