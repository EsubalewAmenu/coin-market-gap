import requests
import json

# get exchange, price, Confidence & last updated were paired with USDT


def scrap_token(slug):
    base_url = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug={slug}'
    start = 1
    quoteCurrencyId = 825
    limit = 100
    others = 'category=spot&centerType=all&sort=price&direction=desc&spotUntracked=true'

    url = f'{base_url}&start={start}&quoteCurrencyId={quoteCurrencyId}&limit={limit}&{others}'
    response = requests.get(url)

    if response.status_code == 200:
        return response
    else:
        raise Exception(f'Something went wrong: {response.status_code}')


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