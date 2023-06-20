import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.CreationCentre.Collection_menu.create_class import Class1
from common.element import Loctor
from BeautifulReport import BeautifulReport

import os
@ddt
class create_Class(unittest.TestCase,Loctor):
    def save_img(self,test_method):
        root_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\','/')
        print(root_dir)
        img_path = root_dir + '/img'
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), test_method))
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 要读取data路径下的login.xlsx文件
        path = os.path.join(dir_path,  "chromedriver.exe")
        self.shili(path)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "classdata1.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, '云班级'))
    @unpack
    @BeautifulReport.add_test_img('test_class')
    def test_class(self,url, username, password,org,className):
        ta=Class1(self.driver,url, username, password,org)
        ta.Cloud_class(className)
        ta.connect_task()
        msg=ta.connect_train_camp()
        msg2=ta.connect_study()
        msg3=ta.connect_teach()
        msg4=ta.conncet_standard()
        msg5=ta.connect_channel()
        msg6=ta.connect_contest()
        msg7=ta.add_member()
        msg8=ta.basic_info()
        self.assertEqual('保存成功',msg8)
        self.assertEqual('操作成功',msg7)
        self.assertEqual('关联成功',msg6)
        self.assertEqual('关联成功',msg5)
        self.assertEqual('关联成功',msg4)
        self.assertEqual('关联成功',msg3)
        self.assertEqual('关联成功',msg2)
        self.assertEqual('关联成功',msg)

        msg=ta.delete_class()
        self.assertEqual('删除成功',msg)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path = os.path.join(dir_path, "data", "classdata1.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, '云创业'))
    @unpack
    @BeautifulReport.add_test_img('test_yunchuangye')
    def test_yunchuangye(self,url, username, password,org,className,number):
        ta=Class1(self.driver,url, username, password,org)
        ta.Cloud_chuangye(className,number)
        msg = ta.delete_class()
        self.assertEqual('删除成功', msg)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "classdata1.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, '云实习'))
    @unpack
    @BeautifulReport.add_test_img('test_yunshixi')
    def test_yunshixi(self, url, username, password,org, className,number):
        ta = Class1(self.driver, url, username, password,org)
        ta.Cloud_shixi(className,number)
        msg = ta.delete_class()
        self.assertEqual('删除成功', msg)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "classdata1.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, '私密'))
    @unpack
    @BeautifulReport.add_test_img('test_private')
    def test_private(self, url, username, password,org, className):
        ta = Class1(self.driver, url, username, password,org)
        zi=ta.private_class(className)
        self.assertEqual('基本信息',zi)
        # 删除
        msg = ta.delete_class()
        self.assertEqual('删除成功', msg)



if __name__ == '__main__':
    unittest.main
