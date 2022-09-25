from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randrange
from fake_useragent import UserAgent

options = webdriver.ChromeOptions()

ua = UserAgent()
user_agent = ua.random

options = webdriver.ChromeOptions()
    
# options.add_argument(f"user-agent={user_agent}")
options.add_argument("--start-maximized")
# options.add_argument("--disable-javascript")
options.add_argument('--disable-notifications')
driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options= options)

driver.get("https://www.google.com")
driver.get("https://www.knolix.com/")

usr_name = driver.find_element(By().NAME, 'user')
usr_name.send_keys('mohammadJavadtabari1024@outlook.com')
#usr_name.send_keys('mim.moltafet@gmail.com')

usr_pass = driver.find_element(By().NAME, 'pass')
usr_pass.send_keys('QAZqaz!@#123')

login_btn = driver.find_element(By.NAME, 'submit_login')
login_btn.click()
# sleep(6)
# tree_btn = driver.find_element(By.CLASS_NAME, 'bitcoin')
# tree_btn.click()
sleep(10)
tree_area = driver.find_element(By.ID, 'btctree')
action = ActionChains(driver)

action.double_click(tree_area)

action.perform()

sleep(10)
driver.refresh()
sleep(10)
tree_area = driver.find_element(By.ID, 'btctree')
action = ActionChains(driver)

action.double_click(tree_area)

action.perform()

sleep(10)
driver.quit()

    