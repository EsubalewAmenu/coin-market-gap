import requests
import json

limit = 10
url = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit={limit}&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap"
print('Data Fecthing Started!')
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    crypto_slugs = [crypto['slug'] for crypto in data['data']['cryptoCurrencyList']]

    with open('data.txt', 'w') as file:
        file.write(str(crypto_slugs))

    print(f"Data writtend to 'data.txts' ")
else:
    print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
