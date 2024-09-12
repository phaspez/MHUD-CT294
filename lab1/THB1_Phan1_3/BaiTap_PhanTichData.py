import pandas as pd
import numpy as np

df = pd.read_csv("hacker_news.csv", sep=",")
rows, cols = df.shape
print("DATA =====================")
print(df)
print("\n")
print(f"Number of rows: {rows}")
print(f"Number of columns: {cols}")
print("\n")
print("FIRST 10 ROWS =====================")
print(df.head(10))
print("LAST 10 ROWS ======================")
print(df.tail(10))
print("\n")
print("INFO =====================")
print(df.info())
print("\n")
print(df.loc[:, "id"])
y_data = df.loc[:, "author"]
print(y_data)

labels = np.unique(y_data)
print(labels)

print("\n")
print(df.describe())
print("\n")
print(df.columns.values)
