from compare_markets_price import compare_market_price
from token_market_data import scrap_token
from tokens_on_exchange import scrap_tokens_on_exchange


data = scrap_token("singularitynet")
compare_market_price(data)

all_tokens_on_the_exchange = scrap_tokens_on_exchange("kucoin")

# print(all_tokens_on_the_exchange)
print(len(all_tokens_on_the_exchange))