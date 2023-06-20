import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.CreationCentre.Material_menu.create_question import Question
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

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "login.xlsx")
    @data(*GetData().getExcel(path, '通用'))
    @unpack
    @BeautifulReport.add_test_img('test_question')
    def test_question(self,url,username,password,org):
        ta=Question(self.driver,url,username,password,org)

        ta.question()
        msg =ta.create_question_msg()
        self.assertEqual('操作成功',msg)
        msg2=ta.delete_question()
        self.assertEqual('操作成功',msg2)


if __name__ == '__main__':
    unittest.main