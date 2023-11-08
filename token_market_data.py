from bs4 import BeautifulSoup
import requests
import time
import certifi
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# https://coinmarketcap.com/currencies/singularitynet/#Markets

# scrap exchange, price, Confidence & last updated were paired with USDT


def scrap_token():

    url = 'https://coinmarketcap.com/currencies/singularitynet/#Markets'

    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(4) 

    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.find("table", class_="sc-66133f36-3 iBYPqx cmc-table")
    rows = table.find("tbody").find_all("tr")


    data_list = []  

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 9:
            continue  # Skip header

        exchange = cols[1].text.strip()
        pair = cols[2].text.strip()
        price = float(cols[3].text.strip().replace("$", "").replace(",", ""))
        depth_positive_2_percent = cols[4].text.strip()
        depth_negative_2_percent = cols[5].text.strip()
        volume_24h = cols[6].text.strip().replace("$", "").replace(",", "")
        volume = cols[7].text.strip().replace("$", "").replace(",", "")
        confidence = cols[8].text.strip()
        liquidity_score = float(cols[9].text.strip().replace("$", "").replace(",", ""))
        updated = cols[10].text.strip()

        data = {
            "exchange": exchange,
            "pair": pair,
            "price": price,
            "depth_positive_2_percent": depth_positive_2_percent,
            "depth_negative_2_percent": depth_negative_2_percent,
            "volume_24h": volume_24h,
            "volume": volume,
            "confidence": confidence,
            "liquidity_score": liquidity_score,
            "updated": updated
        }
        data_list.append(data)

    # Convert the data list to JSON
    json_data = json.dumps(data_list, indent=4)

            
    return json_data

# [
#     {
#         "exchange": "binance",
#         "price": 0.2353,
#         "pair": "USDT",
#         ....
#     },
#     {
#         "exchange": "cucoin",
#         "price": 0.2367,
#         "pair": "USDT",
#         ....
#     },
#     {
#         "exchange": "HTX",
#         "price": 0.2345,
#         "pair": "USDT",
#         ....
#     },
#     ....
# ]