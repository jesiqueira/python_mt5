import talib as ta
from datetime import datetime, date
import pandas as pd
import MetaTrader5 as mt5

if not mt5.initialize():
    print('Inicilização Falhou')
    mt5.shutdown()

print(f"MT5 version: {mt5.__version__}")
print(f"Empresa: {mt5.__author__}")

# copias as 200 barras da atual até a 200 em timeframe_m5
# rates = mt5.copy_rates_from_pos('EURUSD', mt5.TIMEFRAME_M5, 0, 500)
# copias as 500 barras  em timeframe_m1
rates = mt5.copy_rates_from_pos('EURUSD', mt5.TIMEFRAME_M1, 0, 500)

# fechar conexão
mt5.shutdown()

# gerar dataFrame
df = pd.DataFrame(rates)

# converter dateTime para data currente e add no dataFrame
df['data'] = pd.to_datetime(df['time'], unit='s')

# gerar medias moveis M9, M20 e M200
df['M9'] = ta.SMA(df['close'], timeperiod=9)
df['M20'] = ta.SMA(df['close'], timeperiod=20)
df['M200'] = ta.SMA(df['close'], timeperiod=200)
df['ADX'] = ta.ADX(df['high'], df['low'], df['close'], timeperiod=14)

df.to_csv('data/EURUSD_M1.csv')

