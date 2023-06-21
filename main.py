from pypresence import Presence
from config import wallapopData, wallapopCategorySwitch, wallapopSubcategorySwitch, wallapopSpecifySwitch, wallapopConditionSwitch
import requests,json,sys, os
from wallapop import addProduct
from pyfiglet import figlet_format

print("Validating Key...")

sys.stdout.write("\x1b]2;SnapSell - Menu\x07")

result = figlet_format("SnapSell", font = "big")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()

client_id = "1119565049208508456"
RPC = Presence(client_id)

RPC.connect()

RPC.update(
    state="Uploading products! | Check our recent news on Twitter!",
    large_image="snapsell",
    buttons=[{"label": "Check It Out!", "url": "https://twitter.com/sutypalaus"}]
)

# Ruta del archivo JSON
json_file = 'config.json'

# Abrir el archivo JSON
with open(json_file, 'r') as file:
    # Cargar el contenido del archivo JSON
    data = json.load(file)

# Obtener el valor de la clave "webhook"
webhook_value = data["webhook"]
key_value = data["key"]

def menu():
    print(result)
    print("---------------------------")
    print("Select an option:")
    print("[1] Wallapop")
    print("[2] Vinted")
    print("[3] Config")
    print("[0] Exit")
    print("---------------------------")


def authKey(key):
    url = f"https://api.whop.com/api/v2/memberships/{key}/validate_license"

    payload = {"metadata": {"Products": "SnapSell Software"}}
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer mUpBWqoRkfjFR0XiZfbAU2aOh28fYKWYWuGmbl8LYck",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response


if authKey(key_value).status_code == 201:
    cls()
    menu()
    option = input(">> ")

    while option != '0':
        if option == '1':
            print('\033[95m Starting...')
            rowcount = 0
            for row in open("Sites/wallapop.csv"):
                rowcount += 1
                addProduct(wallapopData(rowcount)[0], wallapopData(rowcount)[1], wallapopData(rowcount)[2],
                           wallapopData(rowcount)[3], wallapopData(rowcount)[4],
                           wallapopCategorySwitch(wallapopData(rowcount)[5]),
                           wallapopSubcategorySwitch(wallapopData(rowcount)[5], wallapopData(rowcount)[6]),
                           wallapopSpecifySwitch(wallapopData(rowcount)[5], wallapopData(rowcount)[6],
                                                 wallapopData(rowcount)[7]), wallapopConditionSwitch(wallapopData(rowcount)[8]),
                           wallapopData(rowcount)[9], wallapopData(rowcount)[10], wallapopData(rowcount)[11],
                           wallapopData(rowcount)[12], wallapopData(rowcount)[13], webhook_value)

    quit()
elif authKey(key_value).status_code == 401:
    print('\033[91m Reset your key in Dashboard')
elif authKey(key_value).status_code == 400:
    print('\033[91m Key not inserted!')
elif authKey(key_value).status_code == 404:
    print('\033[91m Key inserted Incorrectly!')








