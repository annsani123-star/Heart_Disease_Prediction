import pandas as pd

df = pd.read_csv("processed.cleveland.data", header=None)

print(df.head())
print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing values:")
print(df.isnull().sum())