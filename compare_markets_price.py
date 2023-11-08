# param :- list of markets with their price 
# return :- cheapest and expensive market with the gap


def compare_market_price(response):
    data = response.json()

    market_pairs = data["data"]["marketPairs"]

    # Initialize variables for the highest and lowest prices
    highest_price = None
    lowest_price = None

    for market_pair in market_pairs:
        price = market_pair["price"]

        # Check if this is the first price encountered or if it's higher/lower than the current highest/lowest
        if highest_price is None or price > highest_price:
            highest_price = price
        if lowest_price is None or price < lowest_price:
            lowest_price = price
    
    gap = highest_price - lowest_price
    result = {"Gap": gap, "Highest Price": highest_price,"Lowest Price": lowest_price}

    print(result)

    return result