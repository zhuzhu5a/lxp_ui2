import sys
import unittest
import datetime,os
from BeautifulReport import BeautifulReport
from selenium import webdriver
from page.report_page import *
from common.send_email_file import Email


if __name__ == '__main__':
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    parent_directory_path= os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\','/')
    test_suite=unittest.defaultTestLoader.discover('Test_case',pattern='test_*.py')
    result= BeautifulReport(test_suite)
    result.report(filename='测试报告',description='测试报告',log_path=parent_directory_path+ "\\lxp项目\\TestResult\\Report\\")
    try:
        driver= webdriver.Chrome()
        dir_path = os.path.dirname(os.path.realpath(__file__))

        report_path = os.path.join(dir_path, "TestResult\Report", "测试报告.html")
        driver.get("file:///"+report_path)
        driver.maximize_window()
        rp=report(driver)
        fail_count=rp.report_fail()
        skip_count=rp.report_skip()
        print('错误用例条数：',fail_count)
        print('跳过用例条数：',skip_count)
        driver.close()
        driver.quit()
        if str(fail_count)>="1":
            Email.sendTest(self=Email,file=report_path)
            print("有不通过的测试，发送邮件成功")
        else:
            print("测试通过，不发送邮件")
    except Exception as e :
        print('判断过程出现异常')
        raise e



