import pandas as pd

df = pd.read_csv("weatherHistory.csv")
print(df.head())
print(df.shape)
print(df.describe())