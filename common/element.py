from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Loctor():
    def __init__(self, driver):
        self.ActionChains = ActionChains
        self.driver = driver
    def locateElement(self, type, value):
        if type=='id':
            el=self.driver.find_element(By.ID,value)
            return el
        elif type=='cs':
            el=self.driver.find_element(By.CSS_SELECTOR,value)
            return el
        elif type=='xpath':
            el=self.driver.find_element(By.XPATH,value)
            return el
        elif type=='name':
            el= self.driver.find_element(By.NAME,value)
            return el
        elif type=='link_text':
            el=self.driver.find_element(By.LINK_TEXT,value)
            return el
        else:
            print('不支持的元素定位类型')
    def shili(self,path):
        self.driver=webdriver.Chrome(path)
    def open(self,url):
        self.driver.get(url)
    def quit(self):
        self.driver.quit()
    def input(self, type, value, text):
        self.locateElement(type, value).send_keys(text)
    def click(self, type,value):
        self.locateElement(type,value).click()
    def text(self,type,value):
        return self.locateElement(type,value).text
    def ac(self,type,value):
        self.ActionChains.move_to_element(type,value).perform()
    def select_all_clean(self,type,value):
        self.input(type=type,value=value,text=(Keys.CONTROL,'a'))
        self.input(type=type,value=value,text=(Keys.BACKSPACE))
    def clean_with_send(self,type,value,text):
        self.select_all_clean(type=type,value=value)
        self.input(type=type,value=value,text=text)
