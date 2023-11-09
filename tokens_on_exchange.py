import requests
import json

def scrap_tokens_on_exchange(exchange_slug):

    start = 1
    limit = 1000
    all_pages = []

    while True:
        loaded_tokens = load_more(exchange_slug, start, limit)

        if not loaded_tokens:
            break  # Exit the loop if there's an issue with the request or no more data
        
        all_pages.extend(loaded_tokens)  # Append the page to the list
        start += limit
    return all_pages

def load_more(exchange_slug, start, limit):


    url = f"https://api.coinmarketcap.com/data-api/v3/exchange/market-pairs/latest?slug={exchange_slug}&category=spot&start={start}&limit={limit}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['data']['marketPairs']
    else:
        raise Exception(f'Something went wrong: {response.status_code}')
