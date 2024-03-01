from pycoingecko import CoinGeckoAPI
import pandas as pd

if __name__ == "__main__":
    cg = CoinGeckoAPI()
    bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
    print(bitcoin_data)
    bitcoin_data_price = bitcoin_data['prices']
    data = pd.DataFrame(bitcoin_data_price, columns=['TimeStamp', 'Price'])
    data["Date"] = pd.to_datetime(data['TimeStamp'], unit='ms')
    print(data)
    candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})
    print(candlestick_data)
