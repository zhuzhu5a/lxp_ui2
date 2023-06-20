import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.CreationCentre.Collection_menu.create_channel import Channel
from common.element import Loctor
import os
from BeautifulReport import BeautifulReport

@ddt
class create_Channel(unittest.TestCase,Loctor):
    def save_img(self,test_method):
        root_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\','/')
        print(root_dir)
        img_path = root_dir + '/img'
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), test_method))
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

        path = os.path.join(dir_path, "chromedriver.exe")
        self.shili(path)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path = os.path.join(dir_path, "data", "login.xlsx")
    @data(*GetData().getExcel(path, '通用'))
    @unpack
    @BeautifulReport.add_test_img('test_01_create_channel')
    def test_01_create_channel(self,url,username,password,org):
        ta=Channel(self.driver,url,username,password,org)

        ta.channel()
        msg=ta.conctent_standard()
        self.assertEqual('添加成功',msg)
        msg2=ta.add_classify()
        self.assertEqual('添加成功',msg2)
        msg3=ta.basic_information_menu()
        self.assertEqual('保存成功',msg3)
        msg4=ta.delete_channel()
        self.assertEqual('朱宇',msg4)

if __name__ == '__main__':
    unittest.main