import os
import time
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

from page.Login_page import LoginPage
class Do_vi_task(LoginPage):
    def __init__(self, driver, url, user, pwd,org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd,org)

    def do_vi_task(self,task):
        self.input('xpath', '//*[@placeholder="请输入关键词"]', task)
        sleep(1)
        self.input('xpath', '//input[@placeholder="请输入关键词"]', Keys.ENTER)
        sleep(2)
        self.click('xpath', '/html/body/section/section/main/div/div[2]/div[1]/div/div[2]/div')
        sleep(1)
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        time.sleep(0.5)
        self.clean_with_send('xpath','/html/body/div[2]/div/div[2]/div/form/div[2]/div/div/div/input','1')
        self.click('xpath','//*[text()="我知道了，确认接单"]')
        sleep(1)
        element=self.locateElement('xpath','/html/body/div[2]/div/div[1]/button')
        self.driver.execute_script("arguments[0].click();",element)
        sleep(2)
        self.click('xpath','//*[@class="el-button el-button--primary is-round"]')
        # 获取当前的文件绝对地址
        os.path.realpath(__file__)
        # 获取当前文件所在目录的路径
        os.path.dirname(os.path.realpath(__file__))
        # 获取当前文件所在目录的上一级目录  os.path.dirname()可以使用多次，直到到达要读写文件的上一级目录为止
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 要读取img路径下的661-600文件
        path = os.path.join(dir_path, "img", "661-600x420.jpg")
        sleep(0.5)
        self.input('xpath', '/html/body/div[2]/div/div[2]/div/form/div[2]/div[3]/div/div/div/input', path)
        self.input('xpath','/html/body/div[2]/div/div[2]/div/form/div[2]/div[4]/div/div/div/input',path)
        sleep(1)
        self.click('xpath', '//*[text()="提交"]')
        sleep(3)
        self.click('xpath',
                   '//*[@class="el-button el-button--default el-button--small el-button--primary customConfirmButton"]')
        sleep(1)
        msg = self.text('xpath', '//*[@class="el-message el-message--success"]')
        self.click('id','tab-description')
        sleep(0.5)
        self.click('xpath','//*[text()="去操作>"]')
        handle=self.driver.window_handles[-1]
        self.driver.switch_to.window(handle)
        sleep(1)
        self.locateElement('xpath','//*[@class="title"]')
        return msg