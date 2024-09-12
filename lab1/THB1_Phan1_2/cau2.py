import pandas as pd

arr = list(range(0, 60, 5))
df = pd.DataFrame([arr[0:12:4], arr[1:12:4], arr[2:12:4], arr[3:12:4]])
for col in df.columns:
  print(list(df[col]))