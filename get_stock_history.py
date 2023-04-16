import alpaca_trade_api as tradeapi
import pandas as pd
from keys import base_url, api_key_id, api_secret

# Set up Alpaca API client
api = tradeapi.REST(api_key_id, api_secret, base_url)

# Define the stock symbol and date range
symbol = 'TSLA'
start_date = '2023-04-14T09:30:00-04:00'  # 9:30 AM Eastern Time
end_date = '2023-04-14T16:00:00-04:00'    # 4:00 PM Eastern Time

# Get historical stock price data from Alpaca API
historical_data = api.get_bars(symbol, '5Min', start=start_date, end=end_date)

# Convert the data to a pandas dataframe
df = pd.DataFrame({
    'date': [bar.t for bar in historical_data],
    'open': [bar.o for bar in historical_data],
    'high': [bar.h for bar in historical_data],
    'low': [bar.l for bar in historical_data],
    'close': [bar.c for bar in historical_data],
    'volume': [bar.v for bar in historical_data]
})

# Save the data to a CSV
df.to_csv('historical_data.csv', index=False)
