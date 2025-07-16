import pandas as pd 
import numpy as np 


df = pd.read_csv("datacoins.csv")

X = df['sno'].values
y = df['price'].values

m, b = np.polyfit(X, y, 1)

next_day = df['sno'].max() + 1
predicted_price = m * next_day + b

print(f"📈 Predicted Bitcoin price at 7:00 PM (day {next_day}): {predicted_price:.2f} USD")