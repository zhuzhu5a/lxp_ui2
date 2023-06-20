import os
import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.sup_space.manager_page import space_manger
from common.element import Loctor
from BeautifulReport import BeautifulReport
@ddt
class sup_spac_manager(unittest.TestCase,Loctor):
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
    @unittest.skip('1')
    @data(*GetData().getExcel(path, '超级空间'))
    @unpack
    @BeautifulReport.add_test_img('test_connect_content')
    def test_connect_content(self,url,username,password,org):
        ta=space_manger(self.driver,url,username,password,org)
        msg=ta.connect_channel()
        msg2=ta.connect_standard()
        msg3=ta.connet_class()
        msg4=ta.connect_study()
        msg5=ta.connect_teach()
        ta.connect_task()
        msg6=ta.connect_train()
        msg7=ta.connect_contest()
        ta.connect_vi_task()
        self.assertEqual('关联成功',msg)
        self.assertEqual('关联成功', msg2)
        self.assertEqual('关联成功', msg3)
        self.assertEqual('关联成功', msg4)
        self.assertEqual('关联成功', msg5)
        self.assertEqual('关联成功', msg6)
        self.assertEqual('关联成功', msg7)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "login.xlsx")
    unittest.skip('1')

    @data(*GetData().getExcel(path, '超级空间'))
    @unpack
    @BeautifulReport.add_test_img('test_basic')
    def test_basic(self,url,username,password,org):
        ta = space_manger(self.driver, url, username, password, org)
        msg=ta.basic_info()
        self.assertEqual('保存成功',msg)





if __name__ == '__main__':
    unittest.main