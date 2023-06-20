from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from ddt import ddt,file_data
import datetime
dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
driver =webdriver.Chrome(executable_path=r'C:\Users\91621\PycharmProjects\lxp项目\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
driver.maximize_window()
# 使用朱宇账号登录lxp
driver.get('https://lxp.v2.dev.skillbox.cn')
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
# 点击创作中心按钮
driver.find_element(By.CSS_SELECTOR,'#v-step_creator').click()
# 进入创作中心
handles=driver.window_handles[-1]
driver.switch_to.window(handles)
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="tab-virtual-task"]').click()
driver.find_element(By.CSS_SELECTOR,'#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div > div:nth-child(1) > div > div > button').click()
handles=driver.window_handles[-1]
driver.switch_to.window(handles)
driver.find_element(By.XPATH,'//*[@t_role="title"]').send_keys('sssss')
# driver.find_element(By.CSS_SELECTOR,"*[t_role=title]").send_keys('vvvvv')
# driver.find_element(By.CSS_SELECTOR,'#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(1) > div > div > input').send_keys('111')
driver.find_element(By.XPATH,'//*[@t_role="profession"]').click()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
driver.find_element(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()
driver.find_element(By.XPATH,'//*[@placeholder="请选择"]').click()
# driver.find_element(By.CSS_SELECTOR,'#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(5) > div > div > div.el-input.el-input--suffix > input').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div')
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]')
driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[6]/span').click()
driver.find_element(By.XPATH,'//*[@t_role="button"]').click()