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
    while i <= len(market_pairs):
        if market_pairs[i]["marketReputation"] >= MODERATED_COIN_THRESHOLD:
            highest_price = market_pairs[i]
            break
        i += 1
    
    i = len(market_pairs) - 1
    while i >= 0:
        if market_pairs[i]["marketReputation"] >= MODERATED_COIN_THRESHOLD:
            lowest_price = market_pairs[i]
            break
        i -= 1
  
    if highest_price and lowest_price:
        gap = highest_price["price"] - lowest_price["price"]

    result = {"Gap": gap, "Highest Price": highest_price["price"], "high at":highest_price["exchangeName"],"low at":lowest_price["exchangeName"], "Lowest Price": lowest_price["price"], }
    # print(result)

    return result