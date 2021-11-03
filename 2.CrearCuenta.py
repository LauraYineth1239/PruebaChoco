from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path= r'D:\Documents\Curso de Selenium Platzi\chromedriver.exe')
driver.get("http://automationpractice.com/index.php")

#Inicio de Sesion
botonIni = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
botonIni.click()
time.sleep(2)

#Crear cuenta
Cemail = driver.find_element_by_xpath('//*[@id="email_create"]')
Cemail.send_keys('laurayineth1239@gmail.com')
time.sleep(2)
Cemail.send_keys(Keys.TAB)

#Boton de crear cuenta
botoncrcu = driver.find_element_by_xpath('//*[@id="SubmitCreate"]')
botoncrcu.click()
time.sleep(2)

#Formulario de crear cuenta
#Etiqueta de Mr o Mrs
titulo = driver.find_element_by_id('id_gender1')
titulo.click()
time.sleep(2)

#Nombre
cnombre = driver.find_element_by_id('customer_firstname')
cnombre.send_keys('Laura')
time.sleep(2)
cnombre.send_keys(Keys.TAB)

#Apellido
capellido = driver.find_element_by_xpath('//*[@id="customer_lastname"]')
capellido.send_keys('Delgado')
time.sleep(2)
capellido.send_keys(Keys.TAB)

#Contraseña
ccontraseña = driver.find_element_by_xpath('//*[@id="passwd"]')
ccontraseña.send_keys('Laurayineth123')
time.sleep(2)
ccontraseña.send_keys(Keys.TAB)

#FechaCumple
cdia = driver.find_element_by_xpath('//*[@id="days"]/option[3]')
cdia.click()
time.sleep(2)
cmes = driver.find_element_by_xpath('//*[@id="months"]/option[7]')
cmes.click()
time.sleep(2)
caño = driver.find_element_by_xpath('//*[@id="years"]/option[29]')
caño.click()
time.sleep(2)

#Suscripcion
cnewles = driver.find_element_by_xpath('//*[@id="uniform-newsletter"]/span')
cnewles.click()
time.sleep(2)

#Compañia
ccompa = driver.find_element_by_xpath('//*[@id="company"]')
ccompa.send_keys('Pruebas S.A.S')
time.sleep(2)

#Direccion
cdire = driver.find_element_by_xpath('//*[@id="address1"]')
cdire.send_keys('Calle 23 # 3a - 2')
time.sleep(2)

#Pais
cpai = driver.find_element_by_xpath('//*[@id="city"]')
cpai.send_keys('Estados Unidos')
time.sleep(2)

#Ciudad
cciu = driver.find_element_by_xpath('//*[@id="id_state"]/option[34]')
cciu.click()
time.sleep(2)

#CodigoPostal
ccp = driver.find_element_by_xpath('//*[@id="postcode"]')
ccp.send_keys('33101')
time.sleep(2)

#InformacionAdicional
cad = driver.find_element_by_xpath('//*[@id="other"]')
cad.send_keys('300456822')
time.sleep(2)

#Celular
ccel = driver.find_element_by_xpath('//*[@id="phone_mobile"]')
ccel.send_keys('3000948422')
time.sleep(2)

#BotondeRegistrar
botonres = driver.find_element_by_xpath('//*[@id="submitAccount"]')
botonres.click()
time.sleep(2)




