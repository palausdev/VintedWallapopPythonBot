# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv


def obtener_dato_csv(ruta_archivo, fila, columna):
    with open(ruta_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        datos = list(lector_csv)
        dato = datos[fila][columna]
    return dato

email = obtener_dato_csv("Sites/Wallapop.csv", 1, 0)
pwd = obtener_dato_csv("Sites/Wallapop.csv", 1, 1)
titleProduct = obtener_dato_csv("Sites/Wallapop.csv", 1, 3)
price = obtener_dato_csv("Sites/Wallapop.csv", 1, 5)
description = obtener_dato_csv("Sites/Wallapop.csv", 1, 10)
shippingWeight = obtener_dato_csv("Sites/Wallapop.csv", 1, 1)
shipping = obtener_dato_csv("Sites/Wallapop.csv", 1, 1)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get("https://es.wallapop.com/login")
time.sleep(1)

driver.find_element(By.CLASS_NAME,'Welcome__btn-go-login-form').click()

driver.find_element(By.ID, 'email').send_keys(email)
time.sleep(3)
driver.find_element(By.ID, 'password').send_keys(pwd)

mainMenu = False

while mainMenu == False:
    if driver.current_url == 'https://es.wallapop.com/wall': mainMenu = True

driver.get('https://es.wallapop.com/app/catalog/upload')
time.sleep(2)
driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
driver.find_element(By.XPATH, '/html/body/tsl-root/tsl-private/div/div/div/tsl-upload/div/div/tsl-category-selector/div/div[3]/div/a[1]').click()

driver.find_element(By.ID, 'headline').send_keys(titleProduct)
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="objectType"]/div/div/div/div[1]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="objectType2"]/div/div/div/div[1]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div/ul/li[3]').click()
time.sleep(1)
driver.find_element(By.ID, 'price').send_keys(price)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="conditions"]/div/div/div/div[1]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="conditions"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="tellUs"]').send_keys(description)

if shipping == True: driver.find_element(By.XPATH, '//*[@id="b7f8ad8f-33a6-4d13-9c6b-ce70a26fd322"]').click()

if shippingWeight > 20 and shippingWeight < 30:
    driver.find_element(By.XPATH, '//*[@id="4"]').click()
elif shippingWeight > 10 and shippingWeight < 20:
    driver.find_element(By.XPATH, '//*[@id="3"]').click()
elif shippingWeight > 5 and shippingWeight < 10:
    driver.find_element(By.XPATH, '//*[@id="2"]').click()
elif shippingWeight > 2 and shippingWeight < 5:
    driver.find_element(By.XPATH, '//*[@id="1"]').click()
elif shippingWeight > 0 and shippingWeight < 2:
    driver.find_element(By.XPATH, '//*[@id="0"]').click()






