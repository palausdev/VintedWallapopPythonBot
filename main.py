# This is a sample Python script.
import array

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from discordwebhook import Discord
from pypresence import Presence
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from config import wallapopData, wallapopCategorySwitch, wallapopSubcategorySwitch, wallapopSpecifySwitch, wallapopConditionSwitch
import time
import os
import datetime

client_id = "1119565049208508456"
RPC = Presence(client_id)

RPC.connect()

RPC.update(
    state="Uploading products! | Check our recent news on Twitter!",
    large_image="snapsell",
    buttons=[{"label": "Check It Out!", "url": "https://twitter.com/sutypalaus"}]
)
print('\033[95m Starting...')
def addProduct(email, password, title, price, currency, category, subcategory, specify, productState, description, hashtags, photoFolderPath, shipping, weight):
    discord = Discord(url="https://discord.com/api/webhooks/1119628512597377024/KCYXUjQ3oR_vuxEt65qJd3_iMPA6_sNGTg-4mCbIvrktwEkUjSl8xGh3xCksOvllUGAs")
    shippingWeight = int(weight)

    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options)

    driver.get("https://es.wallapop.com/login")
    time.sleep(1)

    print('\033[96m Login...')
    driver.find_element(By.CLASS_NAME,'Welcome__btn-go-login-form').click()

    print('\033[93m Inserting Email...')
    emailBool = False
    while emailBool == False:
        try:
            # Email
            driver.find_element(By.ID, 'email').send_keys(email)
            print('\033[92m Email Inserted Correctly!')
            emailBool = True
        except:
            print('\033[91m Email Failed!')

    time.sleep(2)

    print('\033[93m Inserting Password...')
    passwordBool = False
    while passwordBool == False:
        try:
            # Password
            driver.find_element(By.ID, 'password').send_keys(password)
            print('\033[92m Password Inserted Correctly!')
            passwordBool == True
            break
        except:
            print('\033[91m Password Failed!')


    mainMenu = False
    while mainMenu == False:
        if driver.current_url == 'https://es.wallapop.com/wall': mainMenu = True

    print('\033[96m Logged in!')

    hora_inicio = datetime.datetime.now()
    driver.get('https://es.wallapop.com/app/catalog/upload')
    time.sleep(2)
    #Accept private settings button
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

    time.sleep(1)
    productBool = False
    while productBool == False:
        try:
            #Click on option to sell product
            driver.find_element(By.XPATH, '/html/body/tsl-root/tsl-private/div/div/div/tsl-upload/div/div/tsl-category-selector/div/div[3]/div/a[1]').click()
            print('\033[96m Inside list module!')
            break
        except:
            print('\033[93m Trying to access the list...')

    print('\033[93m Inserting Title...')
    try:
        #Title
        driver.find_element(By.ID, 'headline').send_keys(title)
        print('\033[92m Title Inserted Correctly!')
    except:
        print('\033[91m Title Input Failed!')

    time.sleep(2)
    #Click Category
    driver.find_element(By.XPATH, '//*[@id="category"]/div').click()
    #time.sleep(1)
    #Select Category
    driver.find_element(By.XPATH, category).click()
    #time.sleep(1)
    #Click Subcategory
    driver.find_element(By.XPATH, '//*[@id="objectType"]/div').click()
    #time.sleep(1)

    subcategoryBool = False
    while subcategoryBool == False:
        print('\033[93m Selecting Subcategory...')
        try:
            # Select SubCategory
            if subcategory is not None: driver.find_element(By.XPATH, subcategory).click()
            print('\033[92m Subcategory Selected Correctly!')
            break
        except:
            print('\033[91m Select Subcategory Failed!')

    #time.sleep(1)

    #Click Specify
    driver.find_element(By.XPATH, '//*[@id="objectType2"]/div/div/div/div[1]').click()
    #time.sleep(1)

    #Select Specify
    if specify is not None: driver.find_element(By.XPATH, specify).click()


    #time.sleep(1)
    #Price
    driver.find_element(By.ID, 'price').send_keys(price)
    #time.sleep(1)
    #Click Condition
    driver.find_element(By.XPATH, '//*[@id="conditions"]/div/div/div/div[1]').click()
    #time.sleep(1)
    #Select Condition
    driver.find_element(By.XPATH, productState).click()
    #time.sleep(2)
    #Description
    driver.find_element(By.XPATH, '//*[@id="tellUs"]').send_keys(description)
    #time.sleep(2)
    photoFolder = photoFolderPath
    contenido = os.listdir(photoFolder)
    #images = []
    images = 1
    for file in contenido:
        if os.path.isfile(os.path.join(photoFolder, file)) and file.endswith('.jpg'):
            driver.find_element(By.XPATH,
                                f'/html/body/tsl-root/tsl-private/div/div/div/tsl-upload/div/div/tsl-upload-product/form/div[2]/tsl-drop-area/div/div[2]/div/div[{str(images)}]/label/input').send_keys(
                photoFolderPath + '/' + file)
            images += 1

    #Condition to click on shipping button
    if shipping == False: driver.find_element(By.XPATH, '//*[@id="b7f8ad8f-33a6-4d13-9c6b-ce70a26fd322"]').click()

    time.sleep(1)
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
    print('\033[93m Uploading Product...')
    try:
        segundos_transcurridos = (datetime.datetime.now() - hora_inicio).total_seconds()
        segundos_transcurridos = str(round(segundos_transcurridos, 2))
        driver.find_element(By.XPATH, '//*[@id="prueba"]/div[1]/walla-button').click()
        print('\033[96m Product Uploaded Successfully!')
        discord.post(
            username="SnapSell",
            avatar_url="https://cdn.discordapp.com/attachments/718875492744298569/1119595752738521259/LogoSnapSell.png",
            embeds=[
                {
                    "title": f"Product: {title} Uploaded!",
                    "fields": [
                        {"name": "Module", "value": "Wallapop", "inline": True},
                        {"name": "Mode", "value": "Fast Mode", "inline": True},
                        {"name": "Upload Time", "value": f"{segundos_transcurridos}", "inline": True},
                    ],
                    "footer": {
                        "text": f"SnapSell | Wallapop Module · {datetime.datetime.now()} ",
                        "icon_url": "https://cdn.discordapp.com/attachments/718875492744298569/1119595752738521259/LogoSnapSell.png",
                    },
                }
            ],
            #content=f"Product {title} Uploaded Successfully",

        )
    except:
        print('\033[91m Product Upload Failed!')

    #segundos_transcurridos = (datetime.datetime.now() - hora_inicio).total_seconds()

    print(f'\033[95m Upload time: {segundos_transcurridos}')

    return driver


rowcount = 0

for row in open("Sites/wallapop.csv"):
  rowcount += 1
  addProduct(wallapopData(rowcount)[0], wallapopData(rowcount)[1], wallapopData(rowcount)[2], wallapopData(rowcount)[3], wallapopData(rowcount)[4], wallapopCategorySwitch(wallapopData(rowcount)[5]), wallapopSubcategorySwitch(wallapopData(rowcount)[5], wallapopData(rowcount)[6]), wallapopSpecifySwitch(wallapopData(rowcount)[5], wallapopData(rowcount)[6], wallapopData(rowcount)[7]), wallapopConditionSwitch(wallapopData(rowcount)[8]), wallapopData(rowcount)[9], wallapopData(rowcount)[10], wallapopData(rowcount)[11], wallapopData(rowcount)[12], wallapopData(rowcount)[13])
# addProduct(email, password, title, price, currency, category, subcategory, specify, productState, description, hashtags, photoFolderPath, shipping, weight)






