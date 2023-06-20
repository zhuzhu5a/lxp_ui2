import os
import unittest
import warnings
from ddt import ddt, data,unpack
from common.element import Loctor
from common.getdata import GetData
from page.Admin.task_check import Taskcheck
from page.CreationCentre.Content_menu.create_task_page import Task
from page.do_task import Do_task
global biddingtask
from BeautifulReport import BeautifulReport

@ddt
class do_task(unittest.TestCase,Loctor):
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
    path = os.path.join(dir_path, "data", "tasky.xlsx")
    unittest.skip('1')

    @data(*GetData().getExcel(path, '招标'))
    @unpack
    @BeautifulReport.add_test_img('test_01_biddingtask')
    def test_01_biddingtask(self, url, username, password, org, title, amount):
        ta = Task(self.driver, url, username, password, org)
        ta.task_before_momney()
        task = ta.biddingtask(title, amount)
        print('11',task)
        sh = Taskcheck(self.driver)
        sh.taskCheck()
        globals()['biddingtask']=task

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet3'))
    @unpack
    @BeautifulReport.add_test_img('test_02_do_biddingtask')
    def test_02_do_biddingtask(self,url, username, password, org):
        task=biddingtask
        ta=Do_task(self.driver,url,username,password,org)
        msg=ta.do_biddingtask(task,'1')
        self.assertEqual('投稿成功',msg)


if __name__ == '__main__':
    unittest.main