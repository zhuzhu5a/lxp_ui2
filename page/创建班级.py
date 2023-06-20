from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from ddt import ddt,file_data

driver =webdriver.Chrome(executable_path=r'C:\Users\91621\PycharmProjects\lxp项目\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
driver.maximize_window()
# 使用朱宇账号登录lxp
driver.get('https:lxp.v2.dev.skillbox.cn')
driver.find_element(By.CSS_SELECTOR,'#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > button > span').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#pass-login > div:nth-child(1) > input').send_keys('18805920129')
driver.find_element(By.CSS_SELECTOR,'#pass-login > div:nth-child(2) > input').send_keys('123456')
driver.find_element(By.CSS_SELECTOR,'#pass-login > div.form-group.password-box > button').click()
driver.implicitly_wait(5)
# 选择鹿课组织
driver.find_element(By.XPATH,'//*[text()="技能盒子"]').click()
# 跳过新用户指引
driver.find_element(By.CSS_SELECTOR,'body > div.introjs-tooltipReferenceLayer > div > div.introjs-tooltip-header > a').click()
r=driver.current_window_handle
print("首页:",r)
# 点击创作中心按钮
driver.find_element(By.CSS_SELECTOR,'#v-step_creator').click()
# 进入创作中心
handles=driver.window_handles[-1]
driver.switch_to.window(handles)
driver.find_element(By.CSS_SELECTOR,'#app > section > aside > div > ul > div:nth-child(3) > li').click()
a=driver.current_window_handle
print("创作中心:",a)
f=driver.find_element(By.CSS_SELECTOR,'#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > span').text
print(f)
# driver.implicitly_wait(5)
time.sleep(1)
driver.find_element(By.XPATH,'//*[@class="el-button el-button--primary is-round"]').click()
h=driver.current_window_handle
print("创建班级:",h)
# handle=driver.window_handles[-1]
# driver.switch_to.window(handle)
# print("c:",handle)
time.sleep(2)
o=driver.window_handles
print('o:',o)
for curg in o:
    if curg!=a and curg!=r:
        driver.switch_to.window(curg)
        print(curg)
# g=driver.find_element(By.CSS_SELECTOR,'#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > span').text
# print(g)
k=driver.find_element(By.CSS_SELECTOR,'#app > section > main > div > div:nth-child(1) > div > span:nth-child(1) > span').text
print(k)
driver.find_element(By.CSS_SELECTOR,'#app > section > main > div > div.content > form > div:nth-child(3) > div > div > input').send_keys('123')
time.sleep(3)
driver.close()
driver.quit()