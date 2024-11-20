import requests
from datetime import datetime

#Get the current price of a list of cryptocurrencies from the CoinGecko API. Input as list and output as dictionary
def fetch_crypto_price(crypto_ids):
    ids = ",".join(crypto_ids)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
    
#Get the historical prices of cryptocurrencies from CoinGecko API. All strings, date format: "YYYY-MM-DD"
def fetch_historical_data(crypto_id, from_date, to_date):
    from_timestamp = int(datetime.strptime(from_date, "%Y-%m-%d").timestamp())
    to_timestamp = int(datetime.strptime(to_date, "%Y-%m-%d").timestamp())

    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart/range"
    params = {
        "vs_currency": "usd",
        "from": from_timestamp,
        "to": to_timestamp
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}