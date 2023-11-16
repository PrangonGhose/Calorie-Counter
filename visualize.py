import matplotlib.pyplot as plt
import pandas as pd
from load_data import load_data

def plot_sell():
  data = load_data('data/all_orders.json')
  print('Enter the no of option from below:\n1. Plot Sell by month\n2. Plot Sell by day')
  choice = int(input())

  df = pd.DataFrame(data)

  df['date'] = pd.to_datetime(df['date'])

  if choice == 1:
    last_year_df = df[df['date'] >= df['date'].max() - pd.DateOffset(years=1)]
    monthly_prices = last_year_df.groupby(last_year_df['date'].dt.to_period("M"))['price'].sum()

    plt.figure(figsize=(5, 5))
    monthly_prices.plot(kind='bar', color='skyblue')
    plt.title('Total Prices per Month (Last 12 months)')
    plt.xlabel('Month')
    plt.ylabel('Total Price')
    plt.show()
  elif choice == 2:
    last_30_days_df = df[df['date'] >= df['date'].max() - pd.DateOffset(days=30)]
    daily_prices = last_30_days_df.groupby(last_30_days_df['date'].dt.to_period("D"))['price'].sum()

    plt.figure(figsize=(5, 5))
    daily_prices.plot(kind='bar', color='salmon')
    plt.title('Total Prices per Day (Last 30 days)')
    plt.xlabel('Day')
    plt.ylabel('Total Price')
    plt.show()
  else:
    print('Invalid choice')
    exit()

plot_sell()