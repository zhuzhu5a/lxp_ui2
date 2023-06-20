import os
import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.CreationCentre.Content_menu.create_standard import Standard
from common.element import Loctor
from BeautifulReport import BeautifulReport

@ddt
class create_standard(unittest.TestCase,Loctor):
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
    path = os.path.join(dir_path, "data", "study.xlsx")
    @data(*GetData().getExcel(path, 'Sheet2'))
    @unpack
    @unittest.skip("1")
    @BeautifulReport.add_test_img('test_create_standard')
    def test_create_standard(self,url,username,password,org,name):
        ta=Standard(self.driver,url,username,password,org)
        ta.create_standard()





    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "study.xlsx")
    @data(*GetData().getExcel(path, 'Sheet2'))
    @unpack
    @unittest.skip("1")
    @BeautifulReport.add_test_img('test_delete_standard')
    def test_delete_standard(self,url,username,password,org,name):
        ta=Standard(self.driver,url,username,password,org)
        msg=ta.delete_standeard()
        self.assertEqual('删除成功',msg)
if __name__ == '__main__':
    unittest.main