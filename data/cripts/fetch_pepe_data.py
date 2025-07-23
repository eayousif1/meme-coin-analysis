import csv
from datetime import datetime
from pycoingecko import CoinGeckoAPI

def fetch_and_save(days=30):
    cg = CoinGeckoAPI()
    # Fetch market data for PEPE over the last `days`
    data = cg.get_coin_market_chart_by_id(id='pepe', vs_currency='usd', days=days)
    
    # Extract timestamp, price, and volume
    rows = [
        (
            datetime.fromtimestamp(ts/1000).strftime('%Y-%m-%d'),
            price,
            vol
        )
        for ts, price, vol in zip(
            [item[0] for item in data['prices']],
            [item[1] for item in data['prices']],
            [item[1] for item in data['total_volumes']]
        )
    ]

    # Write to CSV
    with open('../data/pepe_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'price_usd', 'volume_usd'])
        writer.writerows(rows)
    print(f"Saved {len(rows)} rows to data/pepe_data.csv")

if __name__ == '__main__':
    fetch_and_save(days=30)

Add script to fetch PEPE data
