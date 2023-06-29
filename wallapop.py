from discordwebhook import Discord
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time, os, datetime

from selenium.webdriver.support.wait import WebDriverWait


def addProductSM(email, password, title, price, currency, category, subcategory, specify, productState, description, hashtags, photoFolderPath, shipping, weight,webhook):
    discord = Discord(url=webhook)
    shippingWeight = int(weight)
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--log-level=3")
    #  En este caso, se está excluyendo el interruptor 'enable-logging', que generalmente está habilitado para registrar mensajes de registro en la consola del navegador.
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # Chrome no se cerrará automáticamente cuando el script de Selenium termine de ejecutarse.
    #chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options)

    driver.get("https://es.wallapop.com/login")
    time.sleep(1)

    print('\033[96m Login...')
    loggingButtonBool = False
    while loggingButtonBool == False:
        try:
            driver.find_element(By.CLASS_NAME, 'Welcome__btn-go-login-form').click()
            print('\033[92m Got Form!')
            break
        except:
            print('\033[91m Form Failed!')

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

    driver.switch_to.frame(0)

    #Normal captcha 1 click
    driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]').click()

    captchaBool = False
    while captchaBool == False:
        time.sleep(1.5)
        try:
            elemento = driver.find_element(By.ID, 'recaptcha-anchor')
            valor_aria_checked = elemento.get_attribute('aria-checked')
            if valor_aria_checked == 'true':
                print('\033[96m Captcha Resolved!')
                break
            else:
                print('\033[93m Waiting Captcha Resolve...')
        except:
            print('\033[93m Waiting Captcha Resolve...')

    time.sleep(1)

    driver.switch_to.default_content()
    driver.find_element(By.XPATH, '//*[@id="sign-in-wallapop"]').click()

    mainMenu = False
    while mainMenu == False:
        if driver.current_url == 'https://es.wallapop.com/wall': mainMenu = True

    print('\033[96m Logged in!')

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

    hora_inicio = datetime.datetime.now()
    print('\033[93m Uploading Product...[1/15]')
    titleBool = False
    while titleBool == False:
        try:
            #Title
            driver.find_element(By.ID, 'headline').send_keys(title)
            print('\033[92m Success![1/15]')
            break
        except:
            print('\033[91m Error! Trying again...[1/15]')

    time.sleep(2)

    print('\033[93m Uploading Product...[2/15]')
    categoryBool = False
    while categoryBool == False:
        try:
            # Click Category
            driver.find_element(By.XPATH, '//*[@id="category"]/div').click()
            print('\033[92m Success![2/15]')
            break
        except:
            print('\033[91m Error! Trying again...[2/15]')

    #time.sleep(1)

    print('\033[93m Uploading Product...[3/15]')
    categorySelectedBool = False
    while categorySelectedBool == False:
        try:
            # Select Category
            driver.find_element(By.XPATH, category).click()
            print('\033[92m Success![3/15]')
            break
        except:
            print('\033[91m Error! Trying again...[3/15]')

    #time.sleep(1)

    print('\033[93m Uploading Product...[4/15]')
    subcategoryBool = False
    while subcategoryBool == False:
        try:
            # Click Subcategory
            driver.find_element(By.XPATH, '//*[@id="objectType"]/div').click()
            print('\033[92m Success![4/15]')
            break
        except:
            print('\033[91m Error! Trying again...[4/15]')

    #time.sleep(1)

    subcategorySelectBool = False
    while subcategorySelectBool == False:
        print('\033[93m Uploading Product...[5/15]')
        try:
            # Select SubCategory
            if subcategory is not None: driver.find_element(By.XPATH, subcategory).click()
            print('\033[92m Success![5/15]')
            break
        except:
            print('\033[91m Error! Trying again...[5/15]')

    #time.sleep(1)

    print('\033[93m Uploading Product...[6/15]')
    specifyBool = False
    while specifyBool == False:
        try:
            if specify is not None:
                # Click Specify
                driver.find_element(By.XPATH, '//*[@id="objectType2"]/div/div/div/div[1]').click()
                specifyBool = True
                print('\033[92m Success![6/15]')
                break
            else:
                print('\033[92m Success![6/15]')
                break
        except:
            print('\033[91m Error! Trying again...[6/15]')

    #time.sleep(1)

    print('\033[93m Uploading Product...[7/15]')
    specifySelectBool = False
    while specifySelectBool == False:
        try:
            # Select Specify
            if specifyBool == True:
                driver.find_element(By.XPATH, specify).click()
                print('\033[92m Success![7/15]')
                break
            else:
                print('\033[92m Success![7/15]')
                break
        except:
            print('\033[91m Error! Trying again...[7/15]')

    time.sleep(1)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    print('\033[93m Uploading Product...[8/15]')
    priceBool = False
    while priceBool == False:
        try:
            # Price
            driver.find_element(By.ID, 'price').send_keys(price)
            print('\033[92m Success![8/15]')
            break
        except:
            print('\033[91m Error! Trying again...[8/15]')

    time.sleep(1)

    print('\033[93m Uploading Product...[9/15]')
    conditionBool = False
    while conditionBool == False:
        try:
            # Click Condition
            driver.find_element(By.XPATH, '//*[@id="conditions"]/div/div/div/div[2]').click()
            print('\033[92m Success![9/15]')
            break
        except:
            print('\033[91m Error! Trying again...[9/15]')

    time.sleep(1)

    print('\033[93m Uploading Product...[10/15]')
    conditionSelectBool = False
    while conditionSelectBool == False:
        try:
            # Select Condition
            driver.find_element(By.XPATH, productState).click()
            print('\033[92m Success![10/15]')
            break
        except:
            print('\033[91m Error! Trying again...[10/15]')

    #time.sleep(2)

    print('\033[93m Uploading Product...[11/15]')
    descriptionBool = False
    while descriptionBool == False:
        try:
            # Description
            driver.find_element(By.XPATH, '//*[@id="tellUs"]').send_keys(description)
            print('\033[92m Success![11/15]')
            break
        except:
            print('\033[91m Error! Trying again...[11/15]')

    #time.sleep(2)
    photoFolder = photoFolderPath
    contenido = os.listdir(photoFolder)
    images = 1
    print('\033[93m Uploading Product...[12/15]')
    try:
        for file in contenido:
            if os.path.isfile(os.path.join(photoFolder, file)) and file.endswith('.jpg'):
                print(f'\033[93m Uploading Photo {images}')
                driver.find_element(By.XPATH,
                                    f'/html/body/tsl-root/tsl-private/div/div/div/tsl-upload/div/div/tsl-upload-product/form/div[2]/tsl-drop-area/div/div[2]/div/div[{str(images)}]/label/input').send_keys(
                    photoFolderPath + file)
                print(f'\033[92m Success![12/15] - {images}')
                images += 1
            else:
                print(f'\033[91m Error! [12/15] - {images}')

    except:
        print('\033[91m Error! Trying again...[12/15]')

    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, '/html/body/tsl-root/tsl-private/div/div/div/tsl-upload/div/div/tsl-upload-product/form/div[3]/div/div[2]/div[1]'))

    print('\033[93m Uploading Product...[13/15]')
    shippingBool = False
    while shippingBool == False:
        try:
            # Condition to click on shipping button
            if shipping == False: driver.find_element(By.XPATH, '//*[@id="b7f8ad8f-33a6-4d13-9c6b-ce70a26fd322"]').click()
            print('\033[92m Success![13/15]')
            break
        except:
            print('\033[91m Error! Trying again...[13/15]')

    time.sleep(1)

    print('\033[93m Uploading Product...[14/15]')
    weightBool = False
    while weightBool == False:
        try:
            # Condition to select the package weight
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
            print('\033[92m Success![14/15]')
            break
        except:
            print('\033[91m Error! Trying again...[14/15]')

    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH,'//*[@id="prueba"]'))
    time.sleep(1)

    #Publish product button
    print('\033[93m Uploading Product...[15/15]')
    publishBool = False
    while publishBool == False:
        try:
            segundos_transcurridos = (datetime.datetime.now() - hora_inicio).total_seconds()
            segundos_transcurridos = str(round(segundos_transcurridos, 2))
            driver.find_element(By.XPATH, '//*[@id="prueba"]/div[1]/walla-button').click()
            print('\033[96m Product Uploaded Successfully! [15/15]')
            break
        except:
            print('\033[91m Product Upload Failed!')

    publishUrlBool = False
    while publishUrlBool == False:
        if driver.current_url.__contains__('/app/catalog/published;created=true;'):
            publishUrlBool = True
            discord.post(
                username="SnapSell",
                avatar_url="https://cdn.discordapp.com/attachments/718875492744298569/1119595752738521259/LogoSnapSell.png",
                embeds=[
                    {
                        "title": f"Product: {title} Uploaded!",
                        "fields": [
                            {"name": "Module", "value": "Wallapop", "inline": True},
                            {"name": "Mode", "value": "Save Mode", "inline": True},
                            {"name": "Upload Time", "value": f"{segundos_transcurridos}", "inline": True},
                        ],
                        "footer": {
                            "text": f"SnapSell | Wallapop Module · {datetime.datetime.now()} ",
                            "icon_url": "https://cdn.discordapp.com/attachments/718875492744298569/1119595752738521259/LogoSnapSell.png",
                        },
                    }
                ],
            )

    print(f'\033[95m Upload time: {segundos_transcurridos}')

    return driver

def addProductFM(email, password, title, price, currency, category, subcategory, specify, productState, description, hashtags, photoFolderPath, shipping, weight,webhook):
    discord = Discord(url=webhook)
    shippingWeight = int(weight)
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--log-level=3")
    #  En este caso, se está excluyendo el interruptor 'enable-logging', que generalmente está habilitado para registrar mensajes de registro en la consola del navegador.
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # Chrome no se cerrará automáticamente cuando el script de Selenium termine de ejecutarse.
    #chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options)

    driver.get("https://es.wallapop.com/login")
    time.sleep(1)

    print('\033[96m Login...')
    loggingButtonBool = False
    while loggingButtonBool == False:
        try:
            driver.find_element(By.CLASS_NAME, 'Welcome__btn-go-login-form').click()
            print('\033[92m Got Form!')
            break
        except:
            print('\033[91m Form Failed!')

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

    driver.switch_to.frame(0)

    #Normal captcha 1 click
    driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]').click()

    captchaBool = False
    while captchaBool == False:
        time.sleep(1.5)
        try:
            elemento = driver.find_element(By.ID, 'recaptcha-anchor')
            valor_aria_checked = elemento.get_attribute('aria-checked')
            if valor_aria_checked == 'true':
                print('\033[96m Captcha Resolved!')
                break
            else:
                print('\033[93m Waiting Captcha Resolve...')
        except:
            print('\033[93m Waiting Captcha Resolve...')

    time.sleep(1)

    driver.switch_to.default_content()
    driver.find_element(By.XPATH, '//*[@id="sign-in-wallapop"]').click()

    mainMenu = False
    while mainMenu == False:
        if driver.current_url == 'https://es.wallapop.com/wall': mainMenu = True

    print('\033[96m Logged in!')

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

    hora_inicio = datetime.datetime.now()
    print('\033[93m Uploading Product...[1/15]')
    titleBool = False
    while titleBool == False:
        try:
            #Title
            driver.find_element(By.ID, 'headline').send_keys(title)
            print('\033[92m Success![1/15]')
            break
        except:
            print('\033[91m Error! Trying again...[1/15]')

    time.sleep(2)

    print('\033[93m Uploading Product...[2/15]')
    categoryBool = False
    while categoryBool == False:
        try:
            # Click Category
            driver.find_element(By.XPATH, '//*[@id="category"]/div').click()
            print('\033[92m Success![2/15]')
            break
        except:
            print('\033[91m Error! Trying again...[2/15]')

    #time.sleep(1)

    print('\033[93m Uploading Product...[3/15]')
    categorySelectedBool = False
    while categorySelectedBool == False:
        try:
            # Select Category
            driver.find_element(By.XPATH, category).click()
            print('\033[92m Success![3/15]')
            break
        except:
            print('\033[91m Error! Trying again...[3/15]')

    #time.sleep(1)

    print('\033[93m Uploading Product...[4/15]')
    subcategoryBool = False
    while subcategoryBool == False:
        try:
            # Click Subcategory
            driver.find_element(By.XPATH, '//*[@id="objectType"]/div').click()
            print('\033[92m Success![4/15]')
            break
        except:
            print('\033[91m Error! Trying again...[4/15]')

    #time.sleep(1)

    subcategorySelectBool = False
    while subcategorySelectBool == False:
        print('\033[93m Uploading Product...[5/15]')
        try:
            # Select SubCategory
            if subcategory is not None: driver.find_element(By.XPATH, subcategory).click()
            print('\033[92m Success![5/15]')
            break
        except:
            print('\033[91m Error! Trying again...[5/15]')

    #time.sleep(1)

    print('\033[93m Uploading Product...[6/15]')
    specifyBool = False
    while specifyBool == False:
        try:
            if specify is not None:
                # Click Specify
                driver.find_element(By.XPATH, '//*[@id="objectType2"]/div/div/div/div[1]').click()
                specifyBool = True
                print('\033[92m Success![6/15]')
                break
            else:
                print('\033[92m Success![6/15]')
                break
        except:
            print('\033[91m Error! Trying again...[6/15]')

    #time.sleep(1)

    print('\033[93m Uploading Product...[7/15]')
    specifySelectBool = False
    while specifySelectBool == False:
        try:
            # Select Specify
            if specifyBool == True:
                driver.find_element(By.XPATH, specify).click()
                print('\033[92m Success![7/15]')
                break
            else:
                print('\033[92m Success![7/15]')
                break
        except:
            print('\033[91m Error! Trying again...[7/15]')

    time.sleep(1)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    print('\033[93m Uploading Product...[8/15]')
    priceBool = False
    while priceBool == False:
        try:
            # Price
            driver.find_element(By.ID, 'price').send_keys(price)
            print('\033[92m Success![8/15]')
            break
        except:
            print('\033[91m Error! Trying again...[8/15]')

    time.sleep(1)

    print('\033[93m Uploading Product...[9/15]')
    conditionBool = False
    while conditionBool == False:
        try:
            # Click Condition
            driver.find_element(By.XPATH, '//*[@id="conditions"]/div/div/div/div[2]').click()
            print('\033[92m Success![9/15]')
            break
        except:
            print('\033[91m Error! Trying again...[9/15]')

    time.sleep(1)

    print('\033[93m Uploading Product...[10/15]')
    conditionSelectBool = False
    while conditionSelectBool == False:
        try:
            # Select Condition
            driver.find_element(By.XPATH, productState).click()
            print('\033[92m Success![10/15]')
            break
        except:
            print('\033[91m Error! Trying again...[10/15]')

    #time.sleep(2)

    print('\033[93m Uploading Product...[11/15]')
    descriptionBool = False
    while descriptionBool == False:
        try:
            # Description
            driver.find_element(By.XPATH, '//*[@id="tellUs"]').send_keys(description)
            print('\033[92m Success![11/15]')
            break
        except:
            print('\033[91m Error! Trying again...[11/15]')

    #time.sleep(2)
    photoFolder = photoFolderPath
    contenido = os.listdir(photoFolder)
    images = 1
    print('\033[93m Uploading Product...[12/15]')
    try:
        for file in contenido:
            if os.path.isfile(os.path.join(photoFolder, file)) and file.endswith('.jpg'):
                print(f'\033[93m Uploading Photo {images}')
                driver.find_element(By.XPATH,
                                    f'/html/body/tsl-root/tsl-private/div/div/div/tsl-upload/div/div/tsl-upload-product/form/div[2]/tsl-drop-area/div/div[2]/div/div[{str(images)}]/label/input').send_keys(
                    photoFolderPath + file)
                print(f'\033[92m Success![12/15] - {images}')
                images += 1
            else:
                print(f'\033[91m Error! [12/15] - {images}')

    except:
        print('\033[91m Error! Trying again...[12/15]')

    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, '/html/body/tsl-root/tsl-private/div/div/div/tsl-upload/div/div/tsl-upload-product/form/div[3]/div/div[2]/div[1]'))

    print('\033[93m Uploading Product...[13/15]')
    shippingBool = False
    while shippingBool == False:
        try:
            # Condition to click on shipping button
            if shipping == False: driver.find_element(By.XPATH, '//*[@id="b7f8ad8f-33a6-4d13-9c6b-ce70a26fd322"]').click()
            print('\033[92m Success![13/15]')
            break
        except:
            print('\033[91m Error! Trying again...[13/15]')

    time.sleep(1)

    print('\033[93m Uploading Product...[14/15]')
    weightBool = False
    while weightBool == False:
        try:
            # Condition to select the package weight
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
            print('\033[92m Success![14/15]')
            break
        except:
            print('\033[91m Error! Trying again...[14/15]')

    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH,'//*[@id="prueba"]'))
    time.sleep(1)

    #Publish product button
    print('\033[93m Uploading Product...[15/15]')
    publishBool = False
    while publishBool == False:
        try:
            segundos_transcurridos = (datetime.datetime.now() - hora_inicio).total_seconds()
            segundos_transcurridos = str(round(segundos_transcurridos, 2))
            driver.find_element(By.XPATH, '//*[@id="prueba"]/div[1]/walla-button').click()
            print('\033[96m Product Uploaded Successfully! [15/15]')
            break
        except:
            print('\033[91m Product Upload Failed!')

    publishUrlBool = False
    while publishUrlBool == False:
        if driver.current_url.__contains__('/app/catalog/published;created=true;'):
            publishUrlBool = True
            discord.post(
                username="SnapSell",
                avatar_url="https://cdn.discordapp.com/attachments/718875492744298569/1119595752738521259/LogoSnapSell.png",
                embeds=[
                    {
                        "title": f"Product: {title} Uploaded!",
                        "fields": [
                            {"name": "Module", "value": "Wallapop", "inline": True},
                            {"name": "Mode", "value": "Save Mode", "inline": True},
                            {"name": "Upload Time", "value": f"{segundos_transcurridos}", "inline": True},
                        ],
                        "footer": {
                            "text": f"SnapSell | Wallapop Module · {datetime.datetime.now()} ",
                            "icon_url": "https://cdn.discordapp.com/attachments/718875492744298569/1119595752738521259/LogoSnapSell.png",
                        },
                    }
                ],
            )

    print(f'\033[95m Upload time: {segundos_transcurridos}')

    return driver