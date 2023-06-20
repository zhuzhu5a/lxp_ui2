import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.CreationCentre.Material_menu.create_picture import Picture
from common.element import Loctor
import os
from BeautifulReport import BeautifulReport

@ddt
class create_picture(unittest.TestCase,Loctor):
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
    # 获取当前的文件绝对地址
    os.path.realpath(__file__)
    # 获取当前文件所在目录的路径
    os.path.dirname(os.path.realpath(__file__))
    # 获取当前文件所在目录的上一级目录  os.path.dirname()可以使用多次，直到到达要读写文件的上一级目录为止
    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "login.xlsx")
    @data(*GetData().getExcel(path, '通用'))
    @unpack
    @BeautifulReport.add_test_img('test_picture')
    def test_picture(self,url,username,password,org):
        ta=Picture(self.driver,url,username,password,org)

        ta.picture()
        msg=ta.create_pictrure_msg()
        self.assertEqual('操作成功',msg)
        msg2=ta.delete_picture()
        self.assertEqual('操作成功',msg2)


if __name__ == '__main__':
    unittest.main