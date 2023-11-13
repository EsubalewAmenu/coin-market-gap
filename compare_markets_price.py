# param :- list of markets with their price 
# return :- cheapest and expensive market with the gap


def compare_market_price(response):
    data = response.json()
    market_pairs = data["data"]["marketPairs"]
    
    MODERATED_COIN_THRESHOLD = 0.7500001
    highest_price = None
    lowest_price = None
    gap = None

    i = 0 
    while i <= len(market_pairs) -1:
        is_passed = check_point(market_pairs[i],["volumeUsd","volumePercent","depthUsdNegativeTwo","depthUsdPositiveTwo"] )
        if market_pairs[i]["marketReputation"] >= MODERATED_COIN_THRESHOLD and is_passed:
            highest_price = market_pairs[i]
            break
        i += 1
    
    i = len(market_pairs) - 1
    while i >= 0:
        is_passed = check_point(market_pairs[i],["volumeUsd","volumePercent","depthUsdNegativeTwo","depthUsdPositiveTwo"] )
        if market_pairs[i]["marketReputation"] >= MODERATED_COIN_THRESHOLD and is_passed:
            lowest_price = market_pairs[i]
            break
        i -= 1
  
    if highest_price and lowest_price:
        gap = highest_price["price"] - lowest_price["price"]

    result = {"token": highest_price['baseSymbol'], "Gap": gap, "Highest": highest_price["price"], "high_at":highest_price["exchangeName"],"low_at":lowest_price["exchangeName"], "Lowest": lowest_price["price"], }
    # print(result)

    return result

def check_point(market_pair,param):
    for i in param:
        # print(f'{market_pair["exchangeName"]} {i} :- {market_pair[i]}')

        if i == "volumeUsd" and market_pair[i] < 1000: # check if the volume in 24hr is less than 1000 
            return False

        if (i == "depthUsdNegativeTwo" and market_pair[i] < 100) or (i == "depthUsdPositiveTwo" and market_pair[i] < 100):
            return False

        if  market_pair[i] <= 0:
            return False

    return True