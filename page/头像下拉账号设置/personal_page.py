import datetime
import os.path
from time import sleep
from page.Login_page import LoginPage
class Personal_page(LoginPage):
    def __init__(self, driver, url, user, pwd,org):
        self.driver = driver
        lp = LoginPage(driver)
        lp.login_successful(url, user, pwd,org)
        self.click('cs',
                   '#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div > div')
        self.locateElement('xpath', '/html/body/ul')
        sleep(1)
        self.click('xpath', '//*[text()="账号设置"]')
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)
        sleep(1)
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    def personal_data(self):
        self.click('xpath', '//*[text()="账号设置"]')
        sleep(1)
        img_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.input('xpath','//*[@accept=".jpg,.png,.jpeg"]',img_path+'\\img/头像.jpg')
        sleep(1)
        self.input('xpath','/html/body/div/div/section/div/section[2]/div/div[2]/div/form/div[2]/div/div/input',self.dt)
        self.input('xpath','/html/body/div/div/section/div/section[2]/div/div[2]/div/form/div[4]/div/div/input',self.dt)
        self.input('xpath','//*[@maxlength="100"]',self.dt)
        sleep(1)
        self.click('xpath','//*[@class="el-button el-button--primary"]')
    def change_code(self,old_code,new_code):
        self.click('xpath', '//*[text()="账号设置"]')
        self.click('xpath','//*[text()="安全设置"]')
        sleep(1)
        self.click('xpath','//*[text()="修改"]')
        sleep(1)
        self.input('xpath','//*[@placeholder="请输入旧密码"]',old_code)
        self.input('xpath', '//*[@placeholder="请输入新密码"]', new_code)
        self.input('xpath', '//*[@placeholder="请再次输入新密码"]', new_code)
        self.click('xpath','//*[text()="确定"]')
    def change_code_back(self,new_code,old_code):
        self.click('xpath', '//*[text()="账号设置"]')
        self.click('xpath', '//*[text()="安全设置"]')
        sleep(1)
        self.click('xpath', '//*[text()="修改"]')
        sleep(1)
        self.input('xpath', '//*[@placeholder="请输入旧密码"]', new_code)
        self.input('xpath', '//*[@placeholder="请输入新密码"]', old_code)
        self.input('xpath', '//*[@placeholder="请再次输入新密码"]', old_code)
        self.click('xpath', '//*[text()="确定"]')
    def authentication(self):
        self.click('xpath', '//*[text()="账号设置"]')
        self.click('xpath', '//*[text()="身份认证"]')
        sleep(1)
        self.select_all_clean('xpath','/html/body/div/div/section/div/section[2]/div/div[2]/div/form/div[1]/div/div/input')
        self.input('xpath','/html/body/div/div/section/div/section[2]/div/div[2]/div/form/div[1]/div/div/input',self.dt)
        self.select_all_clean('xpath','//*[@maxlength="18"]')
        self.input('xpath','//*[@maxlength="18"]','350322199702050847')
        img_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.input('xpath','/html/body/div/div/section/div/section[2]/div/div[2]/div/form/div[3]/div/div/div/div/input',img_path+'\\img/1.jpeg')
        self.input('xpath','/html/body/div/div/section/div/section[2]/div/div[2]/div/form/div[4]/div/div/div/div/input',img_path+'\\img/1.jpeg')
        sleep(1)
        self.click('xpath','//*[text()="确定并发送审核"]')
    def org_quit(self):
        self.click('xpath','//*[text()="我的组织"]')
        sleep(1)
        self.click('xpath','/html/body/div/div/section/div/section[2]/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/a[2]/span')
        sleep(1)
        self.click('xpath','//*[@class="el-button el-button--danger"]')
        sleep(1)
        msg=self.text('xpath','//*[@class="el-message__content"]')
        return msg

    def get_my_credits(self):
        self.click('xpath','//*[text()="我的积分"]')
        sleep(1)
        my_credits=self.text('xpath','//*[@class="balance"]')
        my_credits2=round(float(my_credits.strip("\我的积分:")))
        return my_credits2

    def get_my_coins(self):
        self.click('xpath', '//*[text()="我的技能币"]')
        sleep(1)
        my_coins=self.text('xpath','//*[@class="balance"]')
        my_coins2=round(float(my_coins.strip("\我的技能币:")))
        return my_coins2
    def get_account_balance(self):
        self.click('xpath', '//*[text()="财务管理"]')
        sleep(1)
        self.click('xpath', '//*[text()="账户中心"]')
        sleep(1)
        balance=self.text('xpath','//*[@class="tw-text-lg tw-text-primary"]')
        balance2=round(float(balance.strip("\￥")))
        return balance2

    def recharge(self,amount):
        sleep(1)
        self.click('xpath','//*[text()="充值"]')
        sleep(1)
        self.input('xpath','//*[@placeholder="请填写充值金额"]',amount)
        sleep(1)
        self.click('xpath','//*[text()="确认充值"]')
        sleep(1)
        self.click('xpath','/html/body/div/div/div[2]/div[2]/div[3]/div/div')
        sleep(1)
        self.click('xpath','//*[text()="确定"]')
        sleep(1)
        self.click('xpath','//*[@class="el-button el-button--default el-button--small el-button--primary confirm-del-btn"]')
