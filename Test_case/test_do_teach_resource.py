import os
import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.CreationCentre.Collection_menu.create_teach_collection import teach_collection
from page.study_collection_page.join_study_collection_ import join_study
from common.element import Loctor
from page.study_collection_page.do_study_exam import do_study
global resoucername
from BeautifulReport import BeautifulReport

@ddt
class Do_teach(unittest.TestCase, Loctor):
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
    @BeautifulReport.add_test_img('test_01_create_teach_resource')
    def test_01_create_teach_resource(self, url, username, password,org,name):
        ta=teach_collection(self.driver, url, username, password,org)
        self.hhh=ta.open_resource(name)
        print(self.hhh)
        ta.teach_work()
        ta.study_exam()
        # self.assertEqual('删除成功',msg)
        ta.teach_video()
        ta.teach_local_office()
        ta.teach_upload_office()
        ta.teach_img()
        ta.teach_question()

        ta.teach_link()
        globals()["resoucername"] = self.hhh
        return self.hhh

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet2'))
    @unpack
    @BeautifulReport.add_test_img('test_02_jion_teach_resouce')
    def test_02_jion_teach_resouce(self, url, username, password,org):
        ta1 = resoucername
        print("ta1:", ta1)
        ta = join_study(self.driver, url, username, password,org)
        ta.join_study_resource(ta1)
    unittest.skip('1')

    @data(*GetData().getExcel(path, 'Sheet2'))
    @unpack
    @BeautifulReport.add_test_img('test_03_do_teach_resouce')
    def test_03_do_teach_resouce(self, url, username, password,org):
        ta1 = resoucername
        print("ta1:", ta1)
        ta = do_study(self.driver, url, username, password,org,ta1)
        ta.do_study_exam()
        ta.do_study_work()
        msg2 = ta.do_study_question()
        self.assertEqual('提交成功', msg2)
        ta.do_study_link()

if __name__ == '__main__':
    unittest.main