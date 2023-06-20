import os
import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.CreationCentre.Collection_menu.create_class import Class1
from page.class_manage_page.do_class_plan import Do_plan
from common.element import Loctor
from page.class_manage_page.check_join_class import Check
from BeautifulReport import BeautifulReport

global classname
@ddt
class Do_class_plan(unittest.TestCase, Loctor):
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
    path = os.path.join(dir_path, "data", "classdata1.xlsx")
    unittest.skip('v')
    # 创建班级和考试
    @data(*GetData().getExcel(path, '有计划'))
    @unpack
    @BeautifulReport.add_test_img('test_01_create_class_1')
    def test_01_create_class_1(self, url, username, password,org, className,planname,barrier):
        ta = Class1(self.driver, url, username, password,org)
        self.hhh=ta.Cloud_class(className)
        print(self.hhh)
        ta.exam()
        globals()["classname"]=self.hhh
        ta.class_plan(planname,barrier)
        return self.hhh

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")
    unittest.skip('v')
    # 申请加入班级
    @data(*GetData().getExcel(path, 'Sheet2'))
    @unpack
    @BeautifulReport.add_test_img('test_02_jion_class_2')
    def test_02_jion_class_2(self,url,username,password,org):
        ta1 = classname
        print("ta1:", ta1)
        ta=Do_plan(self.driver,url,username,password,org)
        ta.join_class(ta1)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "login.xlsx")
    unittest.skip('1')
    # 群管理员审核
    @data(*GetData().getExcel(path, '通用'))
    @unpack
    @BeautifulReport.add_test_img('test_03_check_join')
    def test_03_check_join(self, url, username, password,org):
        ta=Check(self.driver, url, username, password,org)
        ta.check_join_class()

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet2'))
    @unpack
    @BeautifulReport.add_test_img('test_04_do_plan')
    def test_04_do_plan(self,url,username,password,org):
        ta1=classname
        print("ta1:", ta1)
        ta=Do_plan(self.driver,url,username,password,org)
        result=ta.do_plan(ta1)
        self.assertEqual('得分0分',result)

if __name__ == '__main__':
    unittest.main
