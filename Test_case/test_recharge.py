import os
import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from common.element import Loctor
global ammount
global account1
from BeautifulReport import BeautifulReport

from page.头像下拉账号设置.personal_page import Personal_page
from page.Admin.recharge_check import Rechargecheck
@ddt
class recharge(unittest.TestCase, Loctor):
    def save_img(self,test_method):
        root_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\','/')
        print(root_dir)
        img_path = root_dir + '/img'
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), test_method))
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 要读取data路径下的login.xlsx文件
        path = os.path.join(dir_path, "chromedriver.exe")
        self.shili(path)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")

    @unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet3'))
    @unpack
    @BeautifulReport.add_test_img('test_01_recharge')
    def test_01_recharge(self, url, username, password, org):
        ta=Personal_page(self.driver,url,username,password,org)
        account1=ta.get_account_balance()
        m='100'
        ta.recharge(m)
        globals()['ammount']=m
        globals()['account1']=account1

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")
    @unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet3'))
    @unpack
    @BeautifulReport.add_test_img('test_02_recharge_check')
    def test_02_recharge_check(self,url, username, password, org):
        ta=Rechargecheck(self.driver,url,username,password,org)
        ta.recgargeCheck()


    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")

    @unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet3'))
    @unpack
    @BeautifulReport.add_test_img('test_03_ammount')
    def test_03_ammount(self,url, username, password, org):
        ta=Personal_page(self.driver,url,username,password,org)
        account2=ta.get_account_balance()
        cha=account2-account1
        try:
            cha == ammount
            print('充值到账余额正常')
        except:
            print('充值到账余额错误')

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")

    unittest.skip('1')

    @data(*GetData().getExcel(path, 'Sheet3'))
    @unpack
    @BeautifulReport.add_test_img('test_pd')
    def test_pd(self,url, username, password, org):
        ta=Personal_page(self.driver,url,username,password,org)
        ta.personal_data()

if __name__ == '__main__':
    unittest.main