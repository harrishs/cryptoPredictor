import requests

#Fetch the current price of a list of cryptocurrencies from the CoinGecko API. Input as list and output as dictionary
def fetch_crypto_price(crypto_ids):
    ids = ",".join(crypto_ids)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}