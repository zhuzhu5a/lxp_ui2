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
# 点击创作中心按钮
driver.find_element(By.CSS_SELECTOR,'#v-step_creator').click()
# 进入创作中心
handles=driver.window_handles[-1]
driver.switch_to.window(handles)
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,'#tab-task').click()
# 点击创建任务按钮
driver.find_element(By.CSS_SELECTOR,'#app > section > main > div > div.tw-flex.tw-flex-1.custom-py-s2.tw-overflow-auto > div.tw-flex.tw-flex-col.tw-flex-1.tw-h-full.tw-space-y-s4.tw-overflow-auto > div:nth-child(1) > div > div > button').click()
# 进入创建任务页面
window=driver.window_handles[-1]
driver.switch_to.window(window)
driver.implicitly_wait(5)
# 任务标题
driver.find_element(By.CSS_SELECTOR,'#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(1) > div > div > input').send_keys('比稿1')
# 选择比稿模式
driver.find_element(By.CSS_SELECTOR,'#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(2) > div > div > div > div:nth-child(2) > div').click()
# 选择行业分类
driver.find_element(By.CSS_SELECTOR,'#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(4) > div > div > div > input').click()
time.sleep(1)
hangye= driver.find_element(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')

hangye.find_element(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
driver.find_element(By.CSS_SELECTOR,'#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(5) > div > div > div.el-input.el-input--suffix > input').click()
time.sleep(1)
# 选择岗位分类
gangwei=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div')
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]').click()
gangwei2=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]')
driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[6]/span').click()
# 输入金额
driver.find_element(By.CSS_SELECTOR,'#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(10) > div > div > input').send_keys('100')

driver.find_element(By.CSS_SELECTOR,'#app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(17) > div > button.el-button.el-button--primary.is-round').click()
driver.implicitly_wait(5)            #app > section > main > div > div.tw-flex-1.tw-space-y-4.tw-bg-white.tw-shadow-card > div.custom-px-s2.tw-pb-4 > form > div:nth-child(18) > div > button.el-button.el-button--primary
# 进入到托管赏金页面
driver.find_element(By.CSS_SELECTOR,'#pane-0 > form > div:nth-child(2) > div > div > input').send_keys('123456')
driver.find_element(By.CSS_SELECTOR,'#pane-0 > form > div:nth-child(3) > div > button.el-button.el-button--primary.is-round').click()
time.sleep(1)
# 使用luke账号审核
driver.find_element(By.CSS_SELECTOR,'#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div.tw-w-\[38px\].tw-h-\[38px\].el-dropdown').click()
driver.find_element(By.XPATH,'/html/body/ul')
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/ul/li[7]/span').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#pass-login > div:nth-child(1) > input').send_keys('luke')
driver.find_element(By.CSS_SELECTOR,'#pass-login > div:nth-child(2) > input').send_keys('123456')
driver.find_element(By.CSS_SELECTOR,'#pass-login > div.form-group.password-box > button').click()
jinenghezi=(driver.find_element(By.XPATH, '//*[text()="技能盒子"]')).click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#app > header > div > div.tw-flex-1.tw-flex.tw-justify-between.tw-items-center > div.tw-flex.tw-items-center.custom-space-x-s2 > div.tw-flex.tw-items-center.tw-space-x-2.custom-ml-s2 > div.tw-w-\[38px\].tw-h-\[38px\].el-dropdown').click()
driver.find_element(By.XPATH,'/html/body/ul')
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/ul/li[6]/span').click()
houtai =driver.window_handles[-1]
driver.switch_to.window(houtai)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#app > section > header > div > div.center > ul > li:nth-child(4)').click()
driver.find_element(By.CSS_SELECTOR,'#app > section > section > div > div.left-content.tw-border-\[\#dce1e6\].tw-border-r > ul > div:nth-child(3) > a > li').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div/section/section/div/div[2]/div/div[2]/div/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/a[2]/span').click()
driver.find_element(By.CSS_SELECTOR,'#app > section > section > div > div.scroll-bar.tw-flex-1 > div > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > button.el-button.el-button--primary.el-button--small').click()
