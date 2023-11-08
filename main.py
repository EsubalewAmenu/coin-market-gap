from compare_markets_price import compare_market_price
from token_market_data import scrap_token


data = scrap_token()
compare_market_price(data)