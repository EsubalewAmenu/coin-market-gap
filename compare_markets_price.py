from token_market_data import scrap_token
# param :- list of markets with their price 
# return :- cheapest and expensive market with the gap

data = scrap_token()

highest_price = data[0]["price"]
lowest_price = data[0]["price"]

for entry in data:
    price = entry["price"]

    # Update the highest and lowest prices if necessary
    if price > highest_price:
        highest_price = price
    if price < lowest_price:
        lowest_price = price

print("Highest Price:", highest_price)
print("Lowest Price:", lowest_price) 