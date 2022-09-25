from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from fake_useragent import UserAgent
import clipboard
import requests

for i in range(0, 1000):
    
    user_agent = UserAgent().random

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options= options)

    ref_code = '623336bfea5c6'
    email_site = 'https://tempmailo.com/'
    target_site = 'https://www.knolix.com/'

    driver.get(email_site)

    tmp_email_cp_btn = driver.find_element(By().XPATH, '//*[@id="apptmo"]/div/div[1]/div[1]/div/button/span')
    tmp_email_cp_btn.click()
    tmp_email = clipboard.paste()


    driver.execute_script('''window.open("","_blank");''')
    driver.switch_to.window(driver.window_handles[1])
    driver.get(target_site)

    reg_btn = driver.find_element(By().XPATH, '//*[@id="main"]/div/div/div[1]/div/center/div[3]/center[1]/button')
    reg_btn.click()
    sleep(1)
    req_input = driver.find_element(By().XPATH, '//*[@id="modallogin"]/div/div/form/input')
    req_input.send_keys(ref_code)
    req_submit = driver.find_element(By().XPATH, '//*[@id="modallogin"]/div/div/form/center/input')
    req_submit.click()
    sleep(1)

    reg_btn = driver.find_element(By().XPATH, '//*[@id="main"]/div/div/div[1]/div/center/div[3]/center[1]/button')
    reg_btn.click()
    sleep(1)
    req_input = driver.find_element(By().XPATH, '//*[@id="modallogin"]/div/div/form/input')
    req_input.send_keys(tmp_email)
    req_submit = driver.find_element(By().XPATH, '//*[@id="modallogin"]/div/div/form/center/input')
    req_submit.click()

    sleep(15)
    driver.switch_to.window(driver.window_handles[0])
    auth_email = driver.find_element(By().XPATH, '//*[@id="apptmo"]/div/div[2]/div[1]/ul/li/div[2]/div')
    auth_email.click()
    sleep(1)

    auth_email_content = driver.find_element(By().XPATH, '/html/body')
    auth_email_content.click()

    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys('A').send_keys('C').key_up(Keys.CONTROL).perform()

    email_text = clipboard.paste()
    email_link = email_text.split(' ')[2]

    driver.execute_script('''window.open("","_blank");''')
    driver.switch_to.window(driver.window_handles[2])
    driver.get(email_link)


    acc_pass = driver.find_element(By().XPATH, '//*[@id="main"]/div/div/div[1]/div/center/div[3]/h3[2]/font').text

    with open('emails.txt', 'w') as file:
        file.write(f'{tmp_email}:{acc_pass} \n')

    driver.quit()
