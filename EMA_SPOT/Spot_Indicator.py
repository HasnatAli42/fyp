import numpy as np
import talib


class SpotIndicator:
    def __init__(self, higher_EMA, lower_EMA):
        self.higher_EMA = higher_EMA
        self.lower_EMA = lower_EMA
        self.latest_high_EMA = 0
        self.latest_low_EMA = 0
        self.previous_high_EMA = 0
        self.previous_low_EMA = 0

    def calculate(self,close):
        close = np.array(close)
        self.latest_high_EMA = talib.EMA(close, self.higher_EMA)[-1]
        self.latest_low_EMA = talib.EMA(close, self.lower_EMA)[-1]
        self.previous_high_EMA = talib.EMA(close, self.higher_EMA)[-2]
        self.previous_low_EMA = talib.EMA(close, self.lower_EMA)[-2]

    def first_print(self, currency_price, SYMBOL):
        print("\n--------- Currency ---------")
        print(SYMBOL, ":", currency_price)
        print("----------------------------")
        print("\n************** Strategy Result First Run ***********")
        print("Current ", self.higher_EMA, "EMA : ", self.latest_high_EMA)
        print("Previous ", self.higher_EMA, "EMA : ", self.previous_high_EMA)
        print("Current ", self.lower_EMA, "EMA : ", self.latest_low_EMA)
        print("Previous ", self.lower_EMA, "EMA : ", self.previous_low_EMA)


