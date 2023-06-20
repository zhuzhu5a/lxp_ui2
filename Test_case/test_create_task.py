import os
import unittest
import warnings
from ddt import ddt, data ,unpack
from common.getdata import GetData
from page.CreationCentre.Content_menu.create_task_page import Task
from page.Admin.task_check import Taskcheck
from common.element import Loctor
from BeautifulReport import BeautifulReport

@ddt
class create_task(unittest.TestCase,Loctor):
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
    @BeautifulReport.add_test_img('test_03_biddingtask')
    def test_03_biddingtask(self, url,username,password,org,title,amount):
        ta = Task(self.driver,url, username, password,org)
        ta.task_before_momney()
        task=ta.biddingtask(title, amount)
        sh=Taskcheck(self.driver)
        sh.taskCheck()
        return task

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "tasky.xlsx")
    @unittest.skip('1')
    @data(*GetData().getExcel(path, '比稿'))
    @unpack
    @BeautifulReport.add_test_img('test_02_cpatask')
    def test_02_cpatask(self, url,username, password,org, title, amount):
        # driver= webdriver.Chrome(r'C:\Users\91621\PycharmProjects\lxp项目\chromedriver.exe')
        ta=Task(self.driver,url,username, password,org)
        money1=ta.task_before_momney()
        print('发布任务前金额',money1)
        taskmoney=ta.cpatask(title, amount, password)
        print('任务金额',taskmoney)
        money2=ta.task_after_momney()
        print('发布后金额',money2)
        cha = (money1[1]) - (taskmoney)
        try:

            money2==cha
            print('发布任务后金额正确')
        except Exception as e :
            print('金额不对')
        sh = Taskcheck(self.driver)
        sh.taskCheck()

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "tasky.xlsx")
    @unittest.skip('1')
    @data(*GetData().getExcel(path, '计件'))
    @unpack
    @BeautifulReport.add_test_img('test_01_pitask')
    def test_01_pitask(self,url,username,password,org,title,amount,zititle,qty):
        # driver= webdriver.Chrome(r'C:\Users\91621\PycharmProjects\lxp项目\chromedriver.exe')
        ta= Task(self.driver,url,username,password,org)
        money1=ta.task_before_momney()
        print('发布任务前金额', money1)
        taskmoney=ta.pitask(title,amount,password,zititle,qty)
        print('任务金额', taskmoney)
        money2 = ta.task_after_momney()
        print('发布后金额', money2)
        cha = (money1[1]) - (taskmoney)
        try:
            money2 == cha
            print('发布任务后金额正确')
        except Exception as e:
            print('金额不对')
        sh = Taskcheck(self.driver)
        sh.taskCheck()

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 要读取data路径下的login.xlsx文件
    path = os.path.join(dir_path, "data", "tasky.xlsx")
    @unittest.skip('1')
    @data(*GetData().getExcel('C:\\Users\\91621\\PycharmProjects\\lxp项目\\data/tasky.xlsx', '招标'))
    @unpack
    @BeautifulReport.add_test_img('test_04_delete')
    def test_04_delete(self, url, username, password, org, title, amount):
        ta = Task(self.driver, url, username, password, org)
        # money=ta.task_before_momney()
        money2 = ta.delete_task()
        print(money2)
        # money3 = ta.task_after_momney()
        # cha=(money3)-(money)
        # try:
        #     money2 == cha
        #     print('删除任务后金额正确')
        # except Exception as e:
        #     print('删除任务金额不对')



if __name__ == '__main__':
    unittest.main





