from compare_markets_price import compare_market_price
from token_market_data import scrap_token
from tokens_on_exchange import scrap_tokens_on_exchange
from tokens_list import token_list

def check_token_status(token):
    data = scrap_token(token)
    compare_market_result = compare_market_price(data)

    cap = 500
    low_token = (cap/compare_market_result['Lowest'])

    low_token = low_token * (1 - 0.001)

    res = (low_token*compare_market_result['Highest'])
    res = res * (1 - 0.001)

    # print(compare_market_result)
    # print(res - cap)
    compare_market_result['retu'] = round((res - cap), 2)


    # all_tokens_on_the_exchange = scrap_tokens_on_exchange("kucoin")

    # # print(all_tokens_on_the_exchange)
    # print(len(all_tokens_on_the_exchange))
    # print(all_tokens_on_the_exchange[1])

    return compare_market_result

def check_tokens(token_list):
    result =  [check_token_status(token) for token in token_list]

    # Sort the token data by the 'Gap' value
    sorted_token_data = sorted(result, key=lambda x: x['retu'], reverse=True)

    return sorted_token_data

# print(check_tokens(token_list))
for token_result in check_tokens(token_list):
    print(token_result)