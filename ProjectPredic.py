import pandas as pd
import numpy as np

# 1. Sample Bitcoin price data (for 7 days)
prices = [107133, 105613, 108824, 109602, 108041, 108218,109215]
days = pd.date_range(start='2025-07-01', periods=7)


df=pd.DataFrame({
    'Date': days,
    'Price': prices
})

last_3_days = df['Price'][-3:]
average_price = np.mean(last_3_days)

predicted_next_price =average_price

print("Last 3 days' prices:\n", last_3_days.values)
print("Predicted next price:", predicted_next_price)