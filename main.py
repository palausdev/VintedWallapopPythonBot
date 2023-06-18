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
import time, os, datetime, requests
from wallapop import addProduct

client_id = "1119565049208508456"
RPC = Presence(client_id)

RPC.connect()

RPC.update(
    state="Uploading products! | Check our recent news on Twitter!",
    large_image="snapsell",
    buttons=[{"label": "Check It Out!", "url": "https://twitter.com/sutypalaus"}]
)

def authKey(key):
    url = f"https://api.whop.com/api/v2/memberships/{key}/validate_license"

    payload = {"metadata": {"Products": "SnapSell Software"}}
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer mUpBWqoRkfjFR0XiZfbAU2aOh28fYKWYWuGmbl8LYck",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    # print(response.text)
    # print(response.status_code)

    return response


if authKey("S-F36D75-438A7DDA-7DDC4BW").status_code == 201:
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
                   wallapopData(rowcount)[12], wallapopData(rowcount)[13])
    # addProduct(email, password, title, price, currency, category, subcategory, specify, productState, description, hashtags, photoFolderPath, shipping, weight)
elif authKey("").status_code == 401:
    print('\033[91m Reset your key in Dashboard')
elif authKey("").status_code == 400:
    print('\033[91m Key not inserted!')
elif authKey("").status_code == 404:
    print('\033[91m Key inserted Incorrectly!')








