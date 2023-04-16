import alpaca_trade_api as tradeapi
from keys import base_url, api_key_id, api_secret

# Define the stock symbol and order quantity
symbol = "TSLA"
qty = 1

# Create API client
api = tradeapi.REST(api_key_id, api_secret, base_url)

# Check if the market is open
clock = api.get_clock()
if not clock.is_open:
    print("Market is currently closed. Order cannot be placed.")
    exit()

# Place the order
try:
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    print(f"Order of {qty} share(s) of {symbol} placed successfully.")
except Exception as e:
    print("Error submitting order: ", e)