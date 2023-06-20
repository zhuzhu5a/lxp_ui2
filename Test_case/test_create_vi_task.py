import unittest, os
import warnings
from selenium import webdriver
from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.CreationCentre.Content_menu.create_virtual_task import vi_Task
from common.element import Loctor
from BeautifulReport import BeautifulReport
@ddt
class create_vi_task(unittest.TestCase,Loctor):
    def save_img(self,test_method):
        root_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\','/')
        print(root_dir)
        img_path = root_dir + '/img'
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), test_method))
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 要读取data路径下的login.xlsx文件
        path = os.path.join(dir_path, "chromedriver.exe")
        self.shili(path)


#第一条用例
    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "vi_task.xlsx")
    unittest.skip("1")
    @BeautifulReport.add_test_img('test_01_primarytask')
    @data (*GetData().getExcel(path, '初级职称'))
    @unpack
    def test_01_primarytask(self,url,username,password,org,title,yonghudengji):
        ta=vi_Task(self.driver,url,username,password,org)
        yonghudengji1=ta.primary(title)
        self.assertEqual(yonghudengji, yonghudengji1)




    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "vi_task.xlsx")
    unittest.skip("1")
    @data (*GetData().getExcel(path, '初学者'))
    @unpack
    @BeautifulReport.add_test_img('test_02_beginner')
    def test_02_beginner(self, url, username, password,org, title, yonghudengji):
        ta = vi_Task(self.driver, url, username, password,org)
        yonghudengji1 = ta.beginner(title)
        self.assertEqual(yonghudengji, yonghudengji1)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "vi_task.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, '中级职称'))
    @unpack
    @BeautifulReport.add_test_img('test_03_intermediate')
    def test_03_intermediate(self, url, username, password,org, title, yonghudengji):
        ta = vi_Task(self.driver, url, username, password,org)
        yonghudengji1 = ta.intermediate(title)
        self.assertEqual(yonghudengji, yonghudengji1)

    unittest.skip("1")
    @data(*GetData().getExcel(path, '高级职称'))
    @unpack
    @BeautifulReport.add_test_img('test_04_senior')
    def test_04_senior(self, url, username, password,org, title, yonghudengji):
        ta = vi_Task(self.driver, url, username, password,org)
        yonghudengji1 = ta.senior(title)
        self.assertEqual(yonghudengji, yonghudengji1)


    unittest.skip("1")
    @data(*GetData().getExcel(path, '带软件'))
    @unpack
    @BeautifulReport.add_test_img('test_05_add_software')
    def test_05_add_software(self, url, username, password, org, title, yonghudengji):
        ta = vi_Task(self.driver, url, username, password, org)
        yonghudengji1 = ta.add_software(title)
        self.assertEqual(yonghudengji, yonghudengji1)


    unittest.skip('1')
    @data(*GetData().getExcel(path, '高级职称'))
    @unpack
    @BeautifulReport.add_test_img('test_06_delete')
    def test_06_delete(self, url, username, password,org, title, yonghudengji):
        ta=vi_Task(self.driver, url, username, password,org)
        msg=ta.delete()
        self.assertEqual('操作成功',msg)
if __name__ == '__main__':
    unittest.main
