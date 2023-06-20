import os
import unittest
import warnings
from BeautifulReport import BeautifulReport

from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.CreationCentre.Content_menu.create_train import Train
from common.element import Loctor
from page.CreationCentre.Collection_menu.create_train_camp import Train_camp
from page.Train_camp_page.do_train import Do_train_camp

global campname
@ddt
class Do_train(unittest.TestCase, Loctor):
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
    unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet2'))
    @unpack
    @BeautifulReport.add_test_img('test_01_create_train')
    def test_01_create_train(self, url, username, password,org, name):
        train=Train(self.driver,url, username, password,org)
        train.with_software('训练')




    unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet2'))
    @unpack
    @BeautifulReport.add_test_img('test_02_create_train_camp')
    def test_02_create_train_camp(self,url, username, password,org,name):
        train_camp=Train_camp(self.driver,url, username, password,org)
        self.hhh=train_camp.open_train_camp('训练营')
        globals()["campname"] = self.hhh
        train_camp.link_train()
        return self.hhh



    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet2'))
    @unpack
    @BeautifulReport.add_test_img('test_03_do_train')
    def test_03_do_train(self,url, username, password,org):
        ta1=campname
        print('ta1:',ta1)
        ta=Do_train_camp(self.driver,url,username,password,org)
        ta.do_free_train(ta1)


if __name__ == '__main__':
    unittest.main