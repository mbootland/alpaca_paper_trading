import pandas as pd

# Read the CSV file
df = pd.read_csv("historical_data.csv", parse_dates=['date'], index_col='date')

# Calculate the price change over a specified window (e.g., 10 minutes)
window = 5
df['price_change'] = df['close'].rolling(window=window).apply(lambda x: x[-1] - x[0])

# Define a threshold for trend detection (e.g., 0.5% price change)
threshold = 0.003

# Detect positive trends
df['positive_trend'] = df['price_change'] > (df['close'] * threshold)

# Detect negative trends
df['negative_trend'] = df['price_change'] < -(df['close'] * threshold)

# Print the result
print(df)
