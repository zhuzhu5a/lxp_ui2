import os
import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.CreationCentre.Collection_menu.create_contest import Contest
from common.element import Loctor
from BeautifulReport import BeautifulReport

@ddt
class create_contest(unittest.TestCase,Loctor):
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
    path = os.path.join(dir_path, "data", "login.xlsx")

    @data(*GetData().getExcel(path, '通用'))
    @unpack
    @BeautifulReport.add_test_img('test_task_team_contest')
    def test_task_team_contest(self,url,username,password,org):
        ta=Contest(self.driver,url,username,password,org)
        msg=ta.create_task_team_contest(3,username,password,org)
        self.assertEqual('托管成功',msg)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "login.xlsx")

    @data(*GetData().getExcel(path, '通用'))
    @unpack
    @BeautifulReport.add_test_img(' test_task_solo_contest')
    def test_task_solo_contest(self, url, username, password, org):
        ta = Contest(self.driver, url, username, password, org)
        msg=ta.create_task_solo_contest(username,password,org)
        self.assertEqual('托管成功',msg)


if __name__ == '__main__':
    unittest.main