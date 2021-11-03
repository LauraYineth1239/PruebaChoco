from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path= r'D:\Documents\Curso de Selenium Platzi\chromedriver.exe')
driver.get("http://automationpractice.com/index.php")

#BuscarVestidos
bves = driver.find_element_by_xpath('//*[@id="search_query_top"]')
bves.send_keys('dress')
time.sleep(2)
btves = driver.find_element_by_xpath('//*[@id="searchbox"]/button')
btves.click()
time.sleep(2)