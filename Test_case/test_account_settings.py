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

@ddt
class account_settings(unittest.TestCase, Loctor):
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
    @BeautifulReport.add_test_img('test_pd')
    def test_pd(self, url, username, password, org):
        ta = Personal_page(self.driver, url, username, password, org)
        ta.personal_data()

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "login.xlsx")
    @unittest.skip('1')

    @data(*GetData().getExcel(path, '修改密码'))
    @unpack
    @BeautifulReport.add_test_img('test_ss')
    def test_ss(self, url, username, password, org,old_code,new_code):
        ta = Personal_page(self.driver, url, username, password, org)
        ta.change_code(old_code,new_code)
        ta.change_code_back(new_code,old_code)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")
    unittest.skip('1')

    @data(*GetData().getExcel(path, 'Sheet3'))
    @unpack
    @BeautifulReport.add_test_img('test_authentication')
    def test_authentication(self, url, username, password, org):
        ta=Personal_page(self.driver, url, username, password, org)
        ta.authentication()



if __name__ == '__main__':
    unittest.main