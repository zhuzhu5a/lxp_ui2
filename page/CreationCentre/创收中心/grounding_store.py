import datetime
import os.path
from time import sleep
from page.Login_page import LoginPage
class Grounding_store(LoginPage):
    def __init__(self, driver, url, user, pwd, org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd, org)
        self.click('xpath','//*[text()="创作中心"]')
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        sleep(2)
        self.click('xpath','//*[text()="创收中心"]')
        sleep(1)
        self.click('xpath','//*[text()="上架应用"]')
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    #选择教学资源上架
    def tc(self):
        self.click('xpath','//*[text()="应用商店（官方平台）"]')
        sleep(1)
        self.click('xpath','//*[text()="11.9"]')
        self.click('xpath','//*[text()="确定"]')
        sleep(1)
        self.click('xpath','//*[@placeholder="请选择分类"]')
        self.locateElement('xpath','//*[@class="el-scrollbar__view el-cascader-menu__list"]')
        sleep(1)
        self.click('xpath','/html/body/div[2]/div[1]/div/div[1]/ul/li[1]')
        sleep(1)
        self.locateElement('xpath','/html/body/div[2]/div[1]/div[2]/div[1]/ul')
        sleep(1)
        self.click('xpath','/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[1]')
        iframe=self.locateElement('xpath','//*[@frameborder="0"]')
        self.driver.switch_to.frame(iframe)
        self.select_all_clean('id','tinymce')
        self.input('id','tinymce',self.dt)
        self.driver.switch_to.default_content()
        self.input('xpath','//*[@placeholder="请填写申请上架理由"]',self.dt)    #填写上架理由

        self.select_all_clean('xpath','//*[@class="el-input__inner"]')
        self.input('xpath','//*[@class="el-input__inner"]','10')
        self.click('xpath','//*[text()="提交申请"]')
        sleep(1)
        self.locateElement('xpath','//*[@class="el-message-box customConfirm el-message-box--center"]')
        self.locateElement('xpath','//*[@class="el-message-box__message"]')
    #选择学习资源上架
    def sc(self):
        self.click('xpath', '//*[text()="应用商店（官方平台）"]')
        sleep(1)
        self.locateElement('xpath','//*[@aria-label="选择上架内容"]')
        self.click('id','tab-study_resource')
        sleep(1)
        self.click('xpath', '//*[text()="方法"]')   #根据资源名称查找
        self.click('xpath', '//*[text()="确定"]')
        sleep(1)
        self.click('xpath', '//*[@placeholder="请选择分类"]')
        self.locateElement('xpath', '//*[@class="el-scrollbar__view el-cascader-menu__list"]')
        sleep(1)
        self.click('xpath', '/html/body/div[2]/div[1]/div/div[1]/ul/li[1]')
        sleep(1)
        self.locateElement('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/ul')
        sleep(1)
        self.click('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[1]')
        iframe = self.locateElement('xpath', '//*[@frameborder="0"]')
        self.driver.switch_to.frame(iframe)
        self.select_all_clean('id', 'tinymce')
        self.input('id', 'tinymce', self.dt)
        self.driver.switch_to.default_content()
        self.input('xpath', '//*[@placeholder="请填写申请上架理由"]', self.dt)  # 填写上架理由

        self.select_all_clean('xpath', '//*[@class="el-input__inner"]')
        self.input('xpath', '//*[@class="el-input__inner"]', '10')
        self.click('xpath', '//*[text()="提交申请"]')
        sleep(1)
        self.locateElement('xpath', '//*[@class="el-message-box customConfirm el-message-box--center"]')
        self.locateElement('xpath', '//*[@class="el-message-box__message"]')





