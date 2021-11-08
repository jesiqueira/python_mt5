import talib
from datetime import datetime, tzinfo
from datetime import date
import yfinance as yf
import pandas as pd
import MetaTrader5 as mt5
import pytz
# ^BVSP
# data = yf.download("SPY", start="2020-09-01", end="2021-11-02")

# real = talib.CDLMORNINGSTAR(
#     data['Open'], data['High'], data['Low'], data['Close'])
# print(real[real != 0])

if not mt5.initialize():
    print("Inicialize faleid")
    mt5.shutdown()

print(f"MT5 version: {mt5.__version__}")
print(f"Empresa: {mt5.__author__}")

# solicitamos 1 000 ticks de EURAUD
# euraud_ticks = mt5.copy_ticks_from("EURUSD", datetime(2021,8,28,13), 1000, mt5.COPY_TICKS_ALL)

# Obter timezone da corretora activtrade
# timezone = pytz.timezone("Europe/Luxembourg")

fusoHorario = pytz.timezone("Europe/Luxembourg")
data_atual = datetime.now()
data_hora_luxembourg = data_atual.astimezone(fusoHorario)
data_lux_tx = data_hora_luxembourg.strftime('%d/%m/%Y %H:%M')
ano= int(date.strftime(data_hora_luxembourg, '%Y'))
mes= int(date.strftime(data_hora_luxembourg, '%m'))
dia= int(date.strftime(data_hora_luxembourg, '%d'))
print(f"HOra luxemburgo: {data_lux_tx}")

# criamos o objeto datetime no fuso horário UTC para que não seja aplicado o deslocamento do fuso horário local
print(f"TimeZone Luxemburgo: {data_lux_tx}")
# dataAtual = date.today()
# mes = int(gmt.strftime('%m'))
# ano = int(gmt.strftime('%Y'))
# dia = int(gmt.strftime('%d'))
# gmtL = datetime.now(gmt)
# dl = datetime.strftime(gmt, '%Y-%d-%m %H:%M')
# print(f"DAta Luxembourg: {dl}")

# utc_from = datetime(ano, mes, dia)
# gmt_from = datetime(ano, mes, dia, tzinfo=fusoHorario)

# solicitamos 20 barras de EURUSD M5 do dia atual
rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M5, 0, 200)
mt5.shutdown()
rates_frame = pd.DataFrame(rates)
rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
print(rates_frame['close'])
rates_frame['MA20'] = talib.SMA(rates_frame['close'], timeperiod=20)
print(rates_frame)
rates_frame.to_csv('data/frames_csv.csv')