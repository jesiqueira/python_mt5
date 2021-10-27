import talib
import yfinance as yf
#^BVSP
data = yf.download("SPY", start="2020-09-01", end="2021-10-26")

real = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])
print(real[real != 0])