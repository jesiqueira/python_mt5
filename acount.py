import MetaTrader5 as mt5
import pandas as pd

# exibimos dados sobre o pacote MetaTrader5
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# estabelecemos a conexão ao MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# conectamo-nos à conta de negociação sem especificar senha e servidor
account_info=mt5.account_info()
if account_info!=None:
    # exibimos os dados sobre a conta de negociação como estão
    print(account_info)
    # exibimos os dados da conta de negociação como um dicionário
    print("Show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("  {}={}".format(prop, account_info_dict[prop]))
    print()

    # convertemos o dicionário num DataFrame e imprimimos
    df=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])
    print("account_info() as dataframe:")
    print(df)
mt5.shutdown()


