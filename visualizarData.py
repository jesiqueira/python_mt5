import pandas as pd
df = pd.read_csv('data/EURUSD_M5.csv')
print(df.sort_values(by='data', ascending=False))
