from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

service = Service(executable_path = 'chromedriver.exe')
driver = webdriver.Chrome(service = service)

driver.get('https://sts.sifycorp.com/adfs/ls/idpinitiatedsignon.aspx')
input_element = driver.find_element(By.CLASS_NAME, 'submit')
input_element.send_keys(Keys.ENTER)
# 7b28e58e-b188-e811-a2c0-af6ffbecc3f4
select = Select(driver.find_element(By.TAG_NAME, 'select'))
select.select_by_value('df0fae88-9842-ee11-a2d6-00155dda2400')
body = driver.find_element(By.TAG_NAME, 'body')
body.send_keys(Keys.TAB + Keys.ENTER)
driver.implicitly_wait(600)

attendance = driver.find_element(By.CLASS_NAME, 'inpfont')
attendance.click()
 
#in_time = driver.find_element(By.ID, 'btnhrintime_bu-button-2011-btnInnerEl')
#in_time.click()
 
#out_time = driver.find_element(By.ID, 'btnhrouttime_bu-button-2013-btnInnerEl')
#out_time.click()
 
confirmation = driver.find_element(By.ID, 'ok-button-1056-btnInnerEl')
confirmation.click()
 
time.sleep(1000)
driver.quit()
 
 
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# button = WebDriverWait(input_element1, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit')))
# input_element1.click()
 
# from selenium.webdriver.common.action_chains import ActionChains
# input_element1 = driver.find_element(By.CLASS_NAME, "submit")
# driver.implicitly_wait(1000)
# ActionChains(driver).move_to_element(input_element1).click(input_element1)
 
# input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
# input_element.send_keys('Electronics and Communication Engineering' + Keys.ENTER)
 
