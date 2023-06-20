import os
from time import sleep

from selenium.webdriver import Keys

from page.Login_page import LoginPage
class Do_task(LoginPage):
    def __init__(self, driver, url, user, pwd,org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd,org)


    def do_biddingtask(self,task,ammount):
        self.input('xpath','//*[@placeholder="请输入关键词"]',task)
        sleep(1)
        self.input('xpath', '//input[@placeholder="请输入关键词"]', Keys.ENTER)
        sleep(2)
        self.click('xpath','/html/body/section/section/main/div/div[2]/div[1]/div/div[2]/div')
        sleep(1)
        self.click('xpath','//*[text()="马上交稿"]')
        self.input('xpath','//*[@placeholder="请输入投标报价"]',ammount)
        # 获取当前的文件绝对地址
        os.path.realpath(__file__)
        # 获取当前文件所在目录的路径
        os.path.dirname(os.path.realpath(__file__))
        # 获取当前文件所在目录的上一级目录  os.path.dirname()可以使用多次，直到到达要读写文件的上一级目录为止
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 要读取img路径下的661-600文件
        path = os.path.join(dir_path, "img", "661-600x420.jpg")
        sleep(1)
        self.input('xpath','/html/body/div[2]/div/div[2]/div/form/div[3]/div[3]/div/div/div/input',path)
        sleep(1)
        self.input('xpath','/html/body/div[2]/div/div[2]/div/form/div[3]/div[4]/div/div/div/input',path)
        sleep(1)
        self.click('xpath','//*[text()="提交"]')
        sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default el-button--small el-button--primary customConfirmButton"]')
        sleep(1)
        msg=self.text('xpath','//*[@class="el-message el-message--success"]')
        return msg