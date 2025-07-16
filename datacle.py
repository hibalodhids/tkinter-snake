import pandas as pd
df = pd.read_csv("pandemic_remote.csv")
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df.dropna(subset=['Mental_Health_Status']))
# print(df.shape(3,3))
# print(df.isnull)
# print(df.duplicated().sum())

news_df = df.dropna(subset=['Mental_Health_Status'])
print(news_df)