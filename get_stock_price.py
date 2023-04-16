import alpaca_trade_api as tradeapi
from keys import base_url, api_key_id, api_secret

# Set stock symbol to Tesla 
symbol = "TSLA"

# Create Alpaca API client
api = tradeapi.REST(api_key_id, api_secret, base_url)

# get_latest_trade of Tesla stock
stock = api.get_latest_trade(symbol)
print(stock.price)