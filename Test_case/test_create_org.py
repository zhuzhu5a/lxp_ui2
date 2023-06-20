import os
import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from common.element import Loctor
from page.create_or_join_org.create_org import Create_org
from page.create_or_join_org.join_org import Join_org
from page.二级组织管理后台.member_check import Member_check
global org_name
from page.头像下拉账号设置.personal_page import Personal_page
from BeautifulReport import BeautifulReport

@ddt
class org(unittest.TestCase, Loctor):
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
    @unittest.skip('组织无法删除避免创建大量组织先将该条用例跳过')
    @data(*GetData().getExcel(path, '通用'))
    @unpack
    @BeautifulReport.add_test_img('test_create_org')
    def test_create_org(self, url, username, password,org):
        ta=Create_org(self.driver,url, username, password,org)
        name=ta.create_org()
        self.assertEqual(name[0],name[1])
        globals()['org_name']=name[0]

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")
    @unittest.skip('组织无法删除避免创建大量组织先将该条用例跳过')
    @data(*GetData().getExcel(path, 'Sheet2'))
    @unpack
    @BeautifulReport.add_test_img('test_join_org')
    def test_join_org(self,url, username, password,org):
        ta1=org_name
        ta=Join_org(self.driver,url,username, password ,org)
        msg=ta.join_org(org_name)
        self.assertEqual('申请成功，等待审核',msg)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "login.xlsx")
    @unittest.skip('组织无法删除避免创建大量组织先将该条用例跳过')
    @data(*GetData().getExcel(path, '通用'))
    @unpack
    @BeautifulReport.add_test_img('test_member_check')
    def test_member_check(self,url, username, password,org):
        ta1=('//*[text()="{}"]').format('自动化创建组织2023-03-02-25')
        ta=Member_check(self.driver,url,username, password ,org)
        ta.member_check(ta1)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "join_class.xlsx")

    unittest.skip('组织无法删除避免创建大量组织先将该条用例跳过')
    @data(*GetData().getExcel(path, 'Sheet2'))
    @unpack
    @BeautifulReport.add_test_img('test_org_quit')
    def test_org_quit(self,url, username, password,org):
        ta=Personal_page(self.driver,url,username, password ,org)
        ta.org_quit()

if __name__ == '__main__':
    unittest.main()