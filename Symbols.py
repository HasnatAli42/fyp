import time

import pandas as pd
import requests

from BinanceFuturesPy.futurespy import Client
from Settings import TIME_PERIOD, LIMIT, Dollars, Leverage


class Symbols:

    def __init__(self, current_index):
        self.symbols = ["BTCBUSD", "ETHBUSD", "BNBBUSD", "ADABUSD", "XRPBUSD", "DOGEBUSD", "SOLBUSD", "FTTBUSD",
                        "AVAXBUSD", "NEARBUSD", "GMTBUSD", "APEBUSD", "GALBUSD", "FTMBUSD", "DODOBUSD", "ANCBUSD",
                        "GALABUSD", "TRXBUSD", "1000LUNCBUSD", "LUNA2BUSD", "DOTBUSD", "TLMBUSD", "ICPBUSD",
                        "WAVESBUSD", "LINKBUSD", "SANDBUSD", "LTCBUSD", "MATICBUSD", "CVXBUSD", "FILBUSD",
                        "1000SHIBBUSD", "LEVERBUSD", "ETCBUSD", "LDOBUSD"]
        self.decimal_point_qty = [3, 3, 2, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 2, 0, 1,
                                  1, 0, 0, 1, 1]
        self.decimal_point_price = [1, 2, 2, 4, 4, 5, 2, 2, 3, 3, 4, 3, 3, 4, 4, 4, 6, 6, 4, 4, 3, 5, 3, 3, 3, 3, 2, 4,
                                    3, 3, 6, 6, 3, 3]
        self.current_index = current_index
        self.current_symbol = self.symbols[self.current_index]
        self.current_decimal_point_qty = self.decimal_point_qty[self.current_index]
        self.current_decimal_point_price = self.decimal_point_price[self.current_index]
        self.current_QNTY = self.dollars_to_cryto_quantiy(Dollars)
        self.api_key = "FBenBPte1P8oxxul5WmL5oxluUd3GGH83RnmGU1v40wxqw1dPh8qAREvKG7nWzad"
        self.secret_key = "M2xd43ai6fLTgwxmEtGT6PAmnMw6wcG61qq7ft1xLlCclvTafZHU63t1dePlvzIE"
        self.current_symbol_price = self.get_price()

    def verify_data(self):
        if len(self.symbols) == len(self.symbols) == len(self.symbols):
            print("Verified with Length = ", len(self.symbols))
        else:
            print("UnVerified")

    def increment(self):
        if self.current_index == len(self.symbols)-1:
            self.current_index = 3
        else:
            self.current_index += 1
        self.current_symbol = self.symbols[self.current_index]
        self.current_decimal_point_qty = self.decimal_point_qty[self.current_index]
        self.current_decimal_point_price = self.decimal_point_price[self.current_index]
        self.current_QNTY = self.dollars_to_cryto_quantiy(Dollars)

    def client(self):
        client = Client(api_key=self.api_key, sec_key=self.secret_key, testnet=False, symbol=self.current_symbol,
                      recv_window=30000)
        client.change_leverage(Leverage)
        return client

    def get_price(self):
        try:
            url = f"https://fapi.binance.com/fapi/v1/ticker/price?symbol={self.current_symbol}"
        except Exception as e:
            time.sleep(180)
            url = f"https://fapi.binance.com/fapi/v1/ticker/price?symbol={self.current_symbol}"
        res = requests.get(url)
        self.current_symbol_price = float(res.json()['price'])
        return self.current_symbol_price

    def dollars_to_cryto_quantiy(self, quantity):
        try:
            url = f"https://fapi.binance.com/fapi/v1/ticker/price?symbol={self.current_symbol}"
        except Exception as e:
            url = f"https://fapi.binance.com/fapi/v1/ticker/price?symbol={self.current_symbol}"
        res = requests.get(url)
        return round((quantity / float(res.json()['price'])), self.current_decimal_point_qty)

    def get_data(self):
        url = "https://fapi.binance.com/fapi/v1/klines?symbol={}&interval={}&limit={}".format(self.current_symbol, TIME_PERIOD,
                                                                                              LIMIT)
        res = requests.get(url)
        closed_data = []
        for each in res.json():
            closed_data.append(each)
        data = pd.DataFrame(data=closed_data).iloc[:, 1: 5]
        data.columns = ["open", "high", "low", "close"]
        data["open"] = pd.to_numeric(data["open"])
        data["high"] = pd.to_numeric(data["high"])
        data["low"] = pd.to_numeric(data["low"])
        data["close"] = pd.to_numeric(data["close"])
        return data["open"], data["high"], data["low"], data["close"]

    def print(self):
        print(self.current_index, ".", self.current_symbol, " : ", self.current_symbol_price)

