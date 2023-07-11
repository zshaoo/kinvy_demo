import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# 创建浏览器实例
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 打开哔哩哔哩抽奖页面
url = 'https://www.bilibili.com/'  # 替换为哔哩哔哩抽奖页面的URL
driver.get(url)

# 等待登录
login_button_xpath = '//*[@class="login-btn"]'
wait = WebDriverWait(driver, 10)
login_button = wait.until(EC.presence_of_element_located((By.XPATH, login_button_xpath)))
login_button.click()

# 动态输入账号密码
# username=input("请输入用户名：")
# password=input("请输入密码：")

time.sleep(1)
# 找到用户名输入框并输入用户名
username_xpath = '/html/body/div[6]/div/div[4]/div[2]/form/div[1]/input'
username_input = driver.find_element(By.XPATH, username_xpath)
username_input.send_keys("15091523701")

# 找到密码输入框并输入密码
password_xpath = '//*[@class="密码-btn"]'
password_input = driver.find_element(By.XPATH, password_xpath)
password_input.send_keys("523701")

# 等待抽奖元素加载完成
lottery_button_xpath = '//*[@class="lottery-btn"]'
lottery_button = wait.until(EC.presence_of_element_located((By.XPATH, lottery_button_xpath)))

# 循环进行抽奖转发操作
while True:
    # 点击抽奖按钮
    lottery_button.click()
    
    # 跳转到转发页面
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    
    # 进行转发操作（根据实际情况填写对应的转发按钮、输入框等元素的XPath）
    forward_button_xpath = '//*[@class="forward-btn"]'
    forward_button = wait.until(EC.presence_of_element_located((By.XPATH, forward_button_xpath)))
    forward_button.click()
    
    input_xpath = '//*[@class="input-box"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, input_xpath)))
    input_box.send_keys("转发内容")
    
    submit_button_xpath = '//*[@class="submit-btn"]'
    submit_button = wait.until(EC.presence_of_element_located((By.XPATH, submit_button_xpath)))
    submit_button.click()
    
    # 关闭当前转发窗口
    driver.close()
    
    # 切换回抽奖页面
    driver.switch_to.window(handles[0])
    
    # 暂停一段时间，模拟间隔
    time.sleep(5)
