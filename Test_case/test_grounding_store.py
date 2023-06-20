import os
import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from common.element import Loctor
from page.CreationCentre.创收中心.grounding_store import Grounding_store
from BeautifulReport import BeautifulReport
@ddt
class grounding_store(unittest.TestCase, Loctor):
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
    @unittest.skip('1')
    @data(*GetData().getExcel(path, '通用'))
    @unpack
    @BeautifulReport.add_test_img('test_teach')
    def test_teach(self, url, username, password, org):
        ta = Grounding_store(self.driver, url, username, password, org)
        ta.tc()

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "login.xlsx")
    unittest.skip('1')

    @data(*GetData().getExcel(path, '通用'))
    @unpack
    @BeautifulReport.add_test_img('test_study')
    def test_study(self, url, username, password, org):
        ta = Grounding_store(self.driver, url, username, password, org)
        ta.sc()


if __name__ == '__main__':
    unittest.main