import os
import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from BeautifulReport import BeautifulReport

from page.CreationCentre.Collection_menu.create_task_collection import Task_collection
from common.element import Loctor
@ddt
class create_Exam(unittest.TestCase,Loctor):
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
    @BeautifulReport.add_test_img('test_01_create_task_collection')
    def test_01_create_task_collection(self,url,username,password,org):
        ta=Task_collection(self.driver,url,username,password,org)

        msg=ta.task_collcetion()
        self.assertEqual('发布成功',msg)





    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "login.xlsx")
    @data(*GetData().getExcel(path, '通用'))
    @unpack
    @BeautifulReport.add_test_img('test_02_create_task_collection')
    def test_02_create_task_collection(self, url, username, password, org):
        ta=Task_collection(self.driver,url,username,password,org)
        msg=ta.delete()
        self.assertEqual('删除成功',msg)

if __name__ == '__main__':
    unittest.main
