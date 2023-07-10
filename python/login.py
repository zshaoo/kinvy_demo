import time

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 打开网页
driver.get("https://172.18.30.36")

# 高级
sleep(1)
element = driver.find_element(By.XPATH, '/html/body/div/div[2]/button[3]')
element.click()

# 继续前往172.18.30.36（不安全）
sleep(1)
element = driver.find_element(By.XPATH, '/html/body/div/div[3]/p[2]/a')
element.click()

# 登录
sleep(1)
element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/div[7]/button')
element.click()

sleep(10)
# # 关闭浏览器
# driver.quit()