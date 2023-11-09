from compare_markets_price import compare_market_price
from token_market_data import scrap_token
from tokens_on_exchange import scrap_tokens_on_exchange


data = scrap_token("singularitynet")
compare_market_price = compare_market_price(data)

cap = 500
low_token = (cap/compare_market_price['Lowest Price'])

low_token = low_token * (1 - 0.001)

res = (low_token*compare_market_price['Highest Price'])
res = res * (1 - 0.001)

print(compare_market_price)
print(res - cap)

# all_tokens_on_the_exchange = scrap_tokens_on_exchange("kucoin")

# # print(all_tokens_on_the_exchange)
# print(len(all_tokens_on_the_exchange))
# print(all_tokens_on_the_exchange[1])