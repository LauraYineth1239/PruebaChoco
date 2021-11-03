from selenium import webdriver
from selenium.webdriver.common import keys
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

#--------------------------------------------------------------------------------------------------------------------

#BotonDresses
btdres = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/a')
btdres.click()
time.sleep(2)

#SeleccionDressSummer
sdres = driver.find_element_by_xpath('//*[@id="subcategories"]/ul/li[3]/div[1]/a')
sdres.click()
time.sleep(2)

#VerDressSummer
vdres = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]')
vdres.click()
time.sleep(2)

#Filtrarcantidad
ctdres = driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]')
ctdres.click()
ctdres.click()
time.sleep(2)

#Filtrartalla
tldres = driver.find_element_by_xpath('//*[@id="group_1"]/option[3]')
tldres.click()
time.sleep(2)

#Filtrarcolor
codres = driver.find_element_by_xpath('//*[@id="color_11"]')
codres.click()
time.sleep(2)

#AgregarFavoritos
# fav = driver.find_element_by_xpath('//*[@id="wishlist_button"]')
# fav.click()
# time.sleep(2)

#Comprar
comp = driver.find_element_by_xpath('//*[@id="add_to_cart"]/button')
comp.click()
time.sleep(3)
compchk = driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')
compchk.click()
time.sleep(2)
comppr = driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]')
comppr.click()
time.sleep(2)
comppr2 = driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button')
comppr2.click()
time.sleep(2)
#AceptarTerminos
acepter = driver.find_element_by_xpath('//*[@id="cgv"]')
acepter.click()
time.sleep(2)
comppr3 = driver.find_element_by_xpath('//*[@id="form"]/p/button')
comppr3.click()
time.sleep(2)