import talib
from datetime import datetime
import yfinance as yf
import pandas as pd
import MetaTrader5 as mt5
#^BVSP
# data = yf.download("SPY", start="2020-09-01", end="2021-10-26")

# real = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])
# print(real[real != 0])

if not mt5.initialize():
    print("Inicialize faleid")
    mt5.shutdown()

# print(mt5.version())
# solicitamos 1 000 ticks de EURAUD
# euraud_ticks = mt5.copy_ticks_from("EURUSD", datetime(2021,8,28,13), 1000, mt5.COPY_TICKS_ALL)
# rates_frame = pd.DataFrame(euraud_ticks)
# print(rates_frame)