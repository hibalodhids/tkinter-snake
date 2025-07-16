# import numpy as np
# import pandas as pd

# prices = [2405, 2570, 2590, 2508, 2516, 2570, 2539]
# days = pd.date_range(start="2025-07-01",periods=7)

# df = pd.DataFrame({
#     "Date": days,
#     "Price": prices
# })

# last_3_days =df['Price'][-3:]
# average_price = np.mean(last_3_days)

# predicted_next_price = average_price

# print(predicted_next_price)


import numpy as np
import pandas as pd

df = pd.read_csv("input.csv")

df['Close (USD)'] = df['Close (USD)'].astype(str).str.replace(',', '')
df['Close (USD)'] = df['Close (USD)'].astype(float)

df['Date'] = pd.to_datetime(df['Date'])
# Step 4: Sort data by date (oldest to newest)
df = df.sort_values('Date')

# Step 5: Take last 3 prices
last_3_days = df['Close (USD)'].tail(3)

# Step 6: Calculate average of last 3 days
average_price = np.mean(last_3_days)

# Step 7: Predict next price as the average
predicted_next_price = average_price

# Step 8: Print the result
print("Predicted next day price:", predicted_next_price)

import numpy as np
import pandas as pd

# Read and clean CSV
df = pd.read_csv("post.csv")
print(df.head())
print(df.describe())





# import pandas as pd
# import numpy as np

# df = pd.read_csv("datacoins.csv")
# days = pd.date_range(start="2025-07-28",periods=10 )

# df = pd.DataFrame({
#     "Date": days,
#     "Price": df
#  })


# last_4_days =df['Price'][-4:]
# average_price = np.mean(last_4_days)

# predicted_next_price = average_price

# print(predicted_next_price)
# print(df)