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
    time.sleep(4) # wait for the page to load
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find the specific table that contains the data
    table = soup.find("table", class_="sc-66133f36-3 iBYPqx cmc-table")

    # Find all the rows within the table
    rows = table.find("tbody").find_all("tr")

    data_list = []  # Initialize a list to store the data in JSON format

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 9:
            continue  # Skip header 

        exchange = cols[1].text.strip()
        pair = cols[2].text.strip()
        price = float(cols[3].text.strip().replace("$", "").replace(",", ""))
        depth_posotive_2_percent = cols[4].text.strip()
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
            "depth_posotive_2_percent": depth_posotive_2_percent,
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

    print(json_data)

    # # Find the specific div that contains the data
    # data_div = soup.find("div", class_="sc-d782507f-0 csxNkd")

    # # Find all the elements within the div
    # elements = data_div.find_all(["span", "a"])

    # data_list = []  # Initialize a list to store the data in JSON format
    # current_data = {}  # Initialize a dictionary to store the current data

    # for element in elements:
    #     text = element.get_text(strip=True)
    #     print(text)
    #     if text:
    #         if "Exchange" in text:
    #             if current_data:
    #                 data_list.append(current_data)
    #             current_data = {"exchange": text.split()[-1]}
    #         if "Pair" in text:
    #             current_data["pair"] = text.split()[-1]
    #         if "Price" in text and "$" in text:
    #             current_data["price"] = float(text.split("$")[-1].replace(",", ""))
    #         if "Volume (24h)" in text:
    #             current_data["volume_24h"] = text.split("$")[-1].replace(",", "")

    
    
    # if current_data:
    #     data_list.append(current_data)

    # # Convert the data list to JSON
    # json_data = json.dumps(data_list, indent=4)

    # #print(json_data)



    market_list = soup.find("div", {"id": "section-coin-markets"})

    for crumb in market_list.find_all("span"):
        pass
        # print(crumb.text)
        # category_names.append(crumb.text)
            
    return market_list

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