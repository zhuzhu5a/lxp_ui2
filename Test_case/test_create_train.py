import os
import unittest
from ddt import ddt, data ,unpack
from page.CreationCentre.Content_menu.create_train import Train
from common.element import Loctor
from common.get_path import Get_path
from BeautifulReport import BeautifulReport

import warnings
from common.getdata import GetData
@ddt
class create_train(unittest.TestCase,Loctor):
    def save_img(self,test_method):
        root_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\','/')
        print(root_dir)
        img_path = root_dir + '/img'
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), test_method))
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 要读取data路径下的login.xlsx文件
        path =os.path.join(dir_path,'chromedriver.exe')
        self.shili(path)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "train.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet1'))
    @unpack
    @BeautifulReport.add_test_img('test_01_train')
    def test_01_train(self,url,username,password,org,title):
        ta=Train(self.driver,url,username,password,org)
        ta.train(title)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "train.xlsx")
    unittest.skip('1')

    @data(*GetData().getExcel(path, 'Sheet3'))
    @unpack
    @BeautifulReport.add_test_img('test_02_train_with_software')
    def test_02_train_with_software(self, url, username, password, org, title):
        ta = Train(self.driver, url, username, password, org)
        ta.with_software(title)


    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "train.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, 'delete'))
    @unpack
    @BeautifulReport.add_test_img('test_delete_train')
    def test_delete_train(self,url,username,password,org):
        ta=Train(self.driver,url,username,password,org)
        # 删除
        msg=ta.delete_train()
        self.assertEqual('删除成功',msg)

if __name__ == '__main__':
    unittest.main