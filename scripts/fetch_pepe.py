import requests
import pandas as pd

def fetch_pepe_price():
    url = 'https://api.coingecko.com/api/v3/coins/pepe/market_chart'
    params = {
        'vs_currency': 'usd',
        'days': '30',
        'interval': 'daily'
    }

    response = requests.get(url, params=params)
    data = response.json()

    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    
    df.to_csv('data/pepe_price.csv', index=False)
    print("Saved to data/pepe_price.csv")

if __name__ == "__main__":
    fetch_pepe_price()

