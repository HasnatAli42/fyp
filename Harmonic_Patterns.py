from datetime import datetime
import os
import time
import numpy as np
import threading
from numpy.core.defchararray import strip
from Counters import Counters
from DB import DB
from Fibonacci_Retracement import Fibonacci_Retracement
from Indicator import Indicator
from Symbols import Symbols
from TradingBot import TradingBot
from Settings import above_or_below_wick, TIME_PERIOD, TIME_SLEEP, max_take_profit_limit


def bullish_bat_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement, fib_A_to_B: Fibonacci_Retracement,
                              fib_X_to_D: Fibonacci_Retracement):
    if fib_X_to_A.s_r_p_382 > xabcd.B > fib_X_to_A.g_p_e_618:
        print("B is Valid")
        if fib_A_to_B.s_r_p_382 < xabcd.C < fib_A_to_B.f_r_p_886:
            print("C is Valid")
            if (fib_X_to_A.f_r_p_886 * 0.95) < xabcd.D < (fib_X_to_A.f_r_p_886 * 1.05):
                print("D is Valid")
                print("Bullish Bat Chart Pattern Verified")
            else:
                print("InValid Bat Pattern")
        else:
            print("InValid Bat Pattern")
    else:
        print("InValid Bat Pattern")

def main(trade_bot_obj: TradingBot, counter_obj: Counters, indicator_obj: Indicator, symb_obj: Symbols, db_obj: DB):
    while True:
        print("***************************Searching for Bullish Bat Chart Pattern For",symb_obj.current_symbol,"***************************",datetime.now())
        open_price, high, low, close = symb_obj.get_data()
        indicator_obj.analyze_trend(close=close)
        indicator_obj.find_x_a_b_c_d(open_price=open_price, high=high, low=low, close=close, find_range=8)
        if indicator_obj.isBullishTrend:
            bullish_bat_chart_pattern(xabcd=indicator_obj,fib_X_to_A=Fibonacci_Retracement(indicator_obj.X,indicator_obj.A),fib_A_to_B=Fibonacci_Retracement(indicator_obj.A,indicator_obj.B),fib_X_to_D=Fibonacci_Retracement(indicator_obj.X,indicator_obj.D))
        symb_obj.increment()
        time.sleep(TIME_SLEEP)


if __name__ == "__main__":
    counters_obj = Counters()
    indicators_obj = Indicator()
    trading_bot_obj = TradingBot()
    symbol_obj = Symbols(0)
    db = DB()
    while True:
        try:
            if os.path.exists(f'is_order_in_progress_for_harmonic_pattern.txt'):
                file = open(f'is_order_in_progress.txt', 'r')
                x = file.readlines()
                file.close()
                x = strip(x)
                main(trading_bot_obj, counters_obj, indicators_obj, symbol_obj, db)
            else:
                main(trading_bot_obj, counters_obj, indicators_obj, symbol_obj, db)
        except Exception as e:
            print(e)
            try:
                time.sleep(20)
            except Exception as e:
                print(e)
                time.sleep(10)



