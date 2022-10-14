from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
import requests 
from selenium import webdriver 

driver = webdriver.chrome(ChromeDriverManager().install())

chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage') 
driver.get('https://en.m.wikipedia.org/wiki/Machine_learning')

links = driver.find_elements_by_tag_name('a')
 
for element in links: 
 print(element.get_attribute('href'))