import os
import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.CreationCentre.Collection_menu.create_study_collection import Study_collection
from page.study_collection_page.join_study_collection_ import join_study
from common.element import Loctor
from BeautifulReport import BeautifulReport

from page.study_collection_page.do_study_exam import do_study
global name

@ddt
class Do_study(unittest.TestCase, Loctor):
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
    @data(*GetData().getExcel(path, 'Sheet1'))
    @unpack
    @BeautifulReport.add_test_img('test_01_create_study_resource')
    def test_01_create_study_resource(self, url, username, password,org,name):
        ta=Study_collection(self.driver, url, username, password,org)
        self.name=ta.open_resource(name)
        print(self.name)
        ta.study_work()
        ta.study_exam()
        # self.assertEqual('删除成功',msg)
        ta.study_video()
        ta.study_local_office()
        ta.study_upload_office()
        ta.study_img()
        ta.study_question()

        ta.study_link()
        globals()["name"] = self.name



    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet3'))
    @unpack
    @BeautifulReport.add_test_img('test_02_jion_study_resouce')
    def test_02_jion_study_resouce(self, url, username, password,org):
        ta1 = name
        print("ta1:", ta1)
        ta = join_study(self.driver, url, username, password,org)
        ta.join_study_resource(name)



    unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet3'))
    @unpack
    @BeautifulReport.add_test_img('test_03_do_study_resouce')
    def test_03_do_study_resouce(self, url, username, password,org):
        ta1 = name
        print("ta1:", ta1)
        ta = do_study(self.driver, url, username, password,org,ta1)
        ta.do_study_exam()
        ta.do_study_work()
        msg2=ta.do_study_question()
        self.assertEqual('提交成功',msg2)
        ta.do_study_link()
if __name__ == '__main__':
    unittest.main
