from common.element import Loctor
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
class report(Loctor):
    test_case_fail_xpath='//*[@id="testFail"]'
    test_case_skip_xpath='//*[@id="testSkip"]'
    def report_fail(self):
        return self.locateElement('xpath',self.test_case_fail_xpath).text
    def report_skip(self):
        return self.text('xpath',self.test_case_skip_xpath)
