# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from config import wallapopData, wallapopCategorySwitch, wallapopSubcategorySwitch, wallapopSpecifySwitch, wallapopConditionSwitch
import time

def addProduct(email, password, title, price, currency, category, subcategory, specify, productState, description, hashtags, photoFolderPath, shipping, weight):
    #email = obtener_dato_csv("Sites/Wallapop.csv", 1, 0)
    #pwd = obtener_dato_csv("Sites/wallapop.csv", 1, 1)
    #titleProduct = obtener_dato_csv("Sites/wallapop.csv", 1, 3)
    #price = obtener_dato_csv("Sites/wallapop.csv", 1, 5)
    #description = obtener_dato_csv("Sites/wallapop.csv", 1, 10)
    #shippingWeight = obtener_dato_csv("Sites/wallapop.csv", 1, 14)
    shippingWeight = int(weight)
    #shipping = obtener_dato_csv("Sites/wallapop.csv", 1, 1)

    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options)

    driver.get("https://es.wallapop.com/login")
    time.sleep(1)

    driver.find_element(By.CLASS_NAME,'Welcome__btn-go-login-form').click()
    #Email
    driver.find_element(By.ID, 'email').send_keys(email)
    time.sleep(6)
    #Password
    driver.find_element(By.ID, 'password').send_keys(password)

    mainMenu = False

    while mainMenu == False:
        if driver.current_url == 'https://es.wallapop.com/wall': mainMenu = True

    driver.get('https://es.wallapop.com/app/catalog/upload')
    time.sleep(2)
    #Accept private settings button
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    #Click on option to sell product
    driver.find_element(By.XPATH, '/html/body/tsl-root/tsl-private/div/div/div/tsl-upload/div/div/tsl-category-selector/div/div[3]/div/a[1]').click()

    #Title
    driver.find_element(By.ID, 'headline').send_keys(title)
    time.sleep(3)
    #Click Category
    driver.find_element(By.XPATH, '//*[@id="category"]/div').click()
    time.sleep(1)
    #Select Category
    driver.find_element(By.XPATH, category).click()
    time.sleep(1)
    #Click Subcategory
    driver.find_element(By.XPATH, '//*[@id="objectType"]/div').click()
    time.sleep(1)

    #Select Category
    if subcategory is not None: driver.find_element(By.XPATH, subcategory).click()

    time.sleep(1)

    #Click Specify
    driver.find_element(By.XPATH, '//*[@id="objectType2"]/div/div/div/div[1]').click()
    time.sleep(1)

    #Select Specify
    if specify is not None: driver.find_element(By.XPATH, specify).click()


    time.sleep(1)
    #Price
    driver.find_element(By.ID, 'price').send_keys(price)
    time.sleep(1)
    #Click Condition
    #driver.find_element(By.XPATH, '//*[@id="conditions"]/div/div/div/div[1]').click()
    time.sleep(1)
    #Select Condition
    #driver.find_element(By.XPATH, '//*[@id="conditions"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]').click()
    time.sleep(2)
    #Description
    #driver.find_element(By.XPATH, '//*[@id="tellUs"]').send_keys(description)

    #Adding photo
    #driver.find_element(By.XPATH, '/html/body/tsl-root/tsl-private/div/div/div/tsl-upload/div/div/tsl-upload-product/form/div[2]/tsl-drop-area/div/div[2]/div/div[1]/label/input').send_keys('/Users/paupalacios/Downloads/Logo-TowerDefenseRuine.jpg')

    #Condition to click on shipping button
    if shipping == False: driver.find_element(By.XPATH, '//*[@id="b7f8ad8f-33a6-4d13-9c6b-ce70a26fd322"]').click()

    #Condition to select the package weight
    if shippingWeight > 20 and shippingWeight <= 30:
        driver.find_element(By.XPATH, '//*[@id="4"]').click()
    elif shippingWeight > 10 and shippingWeight <= 20:
        driver.find_element(By.XPATH, '//*[@id="3"]').click()
    elif shippingWeight > 5 and shippingWeight <= 10:
        driver.find_element(By.XPATH, '//*[@id="2"]').click()
    elif shippingWeight > 2 and shippingWeight <= 5:
        driver.find_element(By.XPATH, '//*[@id="1"]').click()
    elif shippingWeight > 0 and shippingWeight <= 2:
        driver.find_element(By.XPATH, '//*[@id="0"]').click()

    #Publish product button
    driver.find_element(By.XPATH, '//*[@id="prueba"]/div[1]/walla-button').click()
    return driver


rowcount = 0

for row in open("Sites/wallapop.csv"):
  rowcount += 1
  addProduct(wallapopData(rowcount)[0], wallapopData(rowcount)[1], wallapopData(rowcount)[2], wallapopData(rowcount)[3], wallapopData(rowcount)[4], wallapopCategorySwitch(wallapopData(rowcount)[5]), wallapopSubcategorySwitch(wallapopData(rowcount)[5], wallapopData(rowcount)[6]), wallapopSpecifySwitch(wallapopData(rowcount)[5], wallapopData(rowcount)[6], wallapopData(rowcount)[7]), wallapopConditionSwitch(wallapopData(rowcount)[8]), wallapopData(rowcount)[9], wallapopData(rowcount)[10], wallapopData(rowcount)[11], wallapopData(rowcount)[12], wallapopData(rowcount)[13])
# addProduct(email, password, title, price, currency, category, subcategory, specify, productState, description, hashtags, photoFolderPath, shipping, weight)






