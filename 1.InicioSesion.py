
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path= r'D:\Documents\Curso de Selenium Platzi\chromedriver.exe')
driver.get("http://automationpractice.com/index.php")

#Login
#Boton de Inicio de Sesion
botsig = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
botsig.click()
time.sleep(2)

#Email
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('laurayineth1239@gmail.com')
time.sleep(2)

#Contraseña
contra = driver.find_element_by_xpath('//*[@id="passwd"]')
contra.send_keys('Laurayineth123')
time.sleep(2)

#BotonInicio
botini = driver.find_element_by_xpath('//*[@id="SubmitLogin"]')
botini.click()
time.sleep(2)