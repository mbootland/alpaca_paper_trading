import pandas as pd
import plotly.graph_objects as go

# Read the CSV file
df = pd.read_csv("historical_data.csv", parse_dates=['date'])

# Create a candlestick chart (go.Candlestick or go.Scatter)
fig = go.Figure(
    go.Candlestick(
        x=df['date'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
    )
)

# Customize the chart layout
fig.update_layout(
    title='Tesla Stock Price',
    yaxis_title='Price',
    xaxis_title='Date',
    xaxis_rangeslider_visible=False
)

# Show the chart
fig.show()
