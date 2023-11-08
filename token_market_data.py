from bs4 import BeautifulSoup
import requests
import time
import certifi

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
    
    market_list = soup.find("div", {"id": "section-coin-markets"})

    for crumb in market_list.find_all("span"):
        print(crumb.text)
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