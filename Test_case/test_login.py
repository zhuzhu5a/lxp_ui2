import os
import unittest
from ddt import ddt, file_data ,data ,unpack
from selenium.webdriver.common.by import By
from BeautifulReport import BeautifulReport

from BeautifulReport import BeautifulReport
from common.element import Loctor
from page.Login_page import LoginPage
from selenium import webdriver
import warnings
from common.getdata import GetData
@ddt
class Login(unittest.TestCase,Loctor):
    def save_img(self,img_name):
        root_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\','/')
        print(root_dir)
        img_path = root_dir + '/img'
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 要读取data路径下的login.xlsx文件
        path = os.path.join(dir_path, "chromedriver.exe")
        self.shili(path)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "login.xlsx")
    @data(*GetData().getExcel(path,'Sheet1'))
    @unpack
    @BeautifulReport.add_test_img('test_login_successful')
    def test_login_successful(self,url,username,password,casename,org,truename):

        lp = LoginPage(self.driver)
        lp.login_successful(url,username, password,org)
        self.assertEqual(truename,self.driver.find_element(By.CSS_SELECTOR,'#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div > div > div > span.tw-text-sm.tw-truncate').text)
        print(casename)


    unittest.skip('1')
    @data(*GetData().getExcel(path,'Sheet2'))
    @unpack
    @BeautifulReport.add_test_img('test_login_userError')
    def test_login_userError(self,url,username,password,casename):

        lg = LoginPage(self.driver)
        user_error=lg.login_user_error(url,username,password)
        self.assertEqual(casename,user_error)
        print(casename)


    unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet3'))
    @unpack
    @BeautifulReport.add_test_img('test_login_passwordError')
    def test_login_passwordError(self,url,username,password,casename):

        lg=LoginPage(self.driver)
        password_error=lg.login_pwd_error(url,username,password)
        self.assertEqual(casename,password_error)
        print(casename)







if __name__ == '__main__':
    unittest.main
