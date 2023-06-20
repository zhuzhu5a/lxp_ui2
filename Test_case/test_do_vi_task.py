import os
import unittest
import warnings
from ddt import ddt, data,unpack
from common.element import Loctor
from common.getdata import GetData
from page.CreationCentre.Content_menu.create_virtual_task import vi_Task
from page.do_vi_task import Do_vi_task
from BeautifulReport import BeautifulReport
global vi_task_title
@ddt
class do_vi_task(unittest.TestCase,Loctor):
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
    path = os.path.join(dir_path, "data", "vi_task.xlsx")

    @unittest.skip('1')
    @data(*GetData().getExcel(path, '带软件'))
    @unpack
    @BeautifulReport.add_test_img('test_01_add_software_vi_task')
    def test_01_add_software_vi_task(self, url, username, password,org, title, yonghudengji):
        ta = vi_Task(self.driver, url, username, password, org)
        yonghudengji1 = ta.add_software(title)
        self.assertEqual(yonghudengji, yonghudengji1[0])
        title=yonghudengji1[1]
        print('mingcheng',yonghudengji1)
        globals()['vi_task_title']=yonghudengji1[1]



    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")
    unittest.skip('1')
    @data(*GetData().getExcel(path, 'Sheet3'))
    @unpack
    @BeautifulReport.add_test_img('test_02_do_vi_task')
    def test_02_do_vi_task(self,url, username, password, org):
        task=vi_task_title
        ta=Do_vi_task(self.driver,url,username,password,org)
        msg=ta.do_vi_task(task)
        self.assertEqual('投稿成功',msg)

if __name__ == '__main__':
    unittest.main