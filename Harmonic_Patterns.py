from datetime import datetime
import os
import time
import numpy as np
import threading
from numpy.core.defchararray import strip
from Counters import Counters
from DB import DB
from FIle_For_Abdullah import symbols
from Fibonacci_Retracement import Fibonacci_Retracement
from Indicator import Indicator
from Symbols import Symbols
from TradingBot import TradingBot
from Settings import above_or_below_wick, TIME_PERIOD, TIME_SLEEP, max_take_profit_limit
from string_dictionary import bullish_bat, bearish_bat, alt_bull_bat, alt_bear_bat, bullish_gartley, bearish_gartley, \
    bullish_cypher, bullish_shark, bearish_shark, bearish_cypher, bullish_butterfly, bullish_crab, bearish_crab, \
    bullish_deep, bearish_deep

upper_Sharpness = 1.003
lower_sharpness = 0.997


def bullish_bat_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement, fib_A_to_B: Fibonacci_Retracement,
                              fib_A_to_D: Fibonacci_Retracement, symbol):
    print(
        "***************************Searching for " + bullish_bat + " For " + symbol + " *************************** " + str(
            datetime.now()))
    if fib_X_to_A.s_r_p_382 > xabcd.B > fib_X_to_A.g_p_e_618:
        print("B is Valid")
        if fib_A_to_B.s_r_p_382 < xabcd.C < fib_A_to_B.f_r_p_886:
            print("C is Valid")
            if (fib_X_to_A.f_r_p_886 * lower_sharpness) <= xabcd.D <= (fib_X_to_A.f_r_p_886 * upper_Sharpness):
                print_sharpness(upper=fib_X_to_A.f_r_p_886 * upper_Sharpness, middle=xabcd.D,
                                lower=fib_X_to_A.f_r_p_886 * lower_sharpness)
                print("D is Valid")
                print(bullish_bat + " Verified")
                return "D"
            else:
                if xabcd.C > xabcd.D > fib_X_to_A.f_r_p_886:
                    return "C"
    return "InValid " + bullish_bat


def bearish_bat_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement, fib_A_to_B: Fibonacci_Retracement,
                              fib_A_to_D: Fibonacci_Retracement, symbol):
    print(
        "***************************Searching for " + bearish_bat + " For " + symbol + " *************************** " + str(
            datetime.now()))
    if fib_X_to_A.s_r_p_382 < xabcd.B < fib_X_to_A.g_p_e_618:
        print("B is Valid")
        if fib_A_to_B.s_r_p_382 > xabcd.C > fib_A_to_B.f_r_p_886:
            print("C is Valid")
            if (fib_X_to_A.f_r_p_886 * lower_sharpness) <= xabcd.D <= (fib_X_to_A.f_r_p_886 * upper_Sharpness):
                print_sharpness(upper=fib_X_to_A.f_r_p_886 * upper_Sharpness, middle=xabcd.D,
                                lower=fib_X_to_A.f_r_p_886 * lower_sharpness)
                print("D is Valid")
                print(bearish_bat + " Verified")
                return "D"
            else:
                if xabcd.C < xabcd.D < fib_X_to_A.f_r_p_886:
                    return "C"
    return "InValid " + bearish_bat


def alternate_bullish_bat_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement,
                                        fib_A_to_B: Fibonacci_Retracement,
                                        fib_A_to_D: Fibonacci_Retracement, symbol):
    print(
        "***************************Searching for " + alt_bull_bat + " For " + symbol + " *************************** " + str(
            datetime.now()))
    if (fib_X_to_A.s_r_p_382 * lower_sharpness) <= xabcd.B <= (fib_X_to_A.s_r_p_382 * upper_Sharpness):
        print("B is Valid")
        if fib_A_to_B.s_r_p_382 < xabcd.C < fib_A_to_B.f_r_p_886:
            print("C is Valid")
            if (fib_X_to_A.s_l_p_1_130 * lower_sharpness) <= xabcd.D <= (fib_X_to_A.s_l_p_1_130 * upper_Sharpness):
                print_sharpness(upper=fib_X_to_A.s_l_p_1_130 * upper_Sharpness, middle=xabcd.D,
                                lower=fib_X_to_A.s_l_p_1_130 * lower_sharpness)
                print("D is Valid")
                print(alt_bull_bat + " Verified")
                return "D"
            else:
                if xabcd.C > xabcd.D > fib_X_to_A.s_l_p_1_130:
                    return "C"
    return "InValid  " + alt_bull_bat


def alternate_bearish_bat_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement,
                                        fib_A_to_B: Fibonacci_Retracement,
                                        fib_A_to_D: Fibonacci_Retracement, symbol):
    print(
        "***************************Searching for " + alt_bear_bat + " For " + symbol + " *************************** " + str(
            datetime.now()))
    if (fib_X_to_A.s_r_p_382 * lower_sharpness) <= xabcd.B <= (fib_X_to_A.s_r_p_382 * upper_Sharpness):
        print("B is Valid")
        if fib_A_to_B.s_r_p_382 > xabcd.C > fib_A_to_B.f_r_p_886:
            print("C is Valid")
            if (fib_X_to_A.s_l_p_1_130 * lower_sharpness) <= xabcd.D <= (fib_X_to_A.s_l_p_1_130 * upper_Sharpness):
                print_sharpness(upper=fib_X_to_A.s_l_p_1_130 * upper_Sharpness, middle=xabcd.D,
                                lower=fib_X_to_A.s_l_p_1_130 * lower_sharpness)
                print("D is Valid")
                print(alt_bear_bat + " Verified")
                return "D"
            else:
                if xabcd.C < xabcd.D < fib_X_to_A.s_l_p_1_130:
                    return "C"
    return "InValid  " + alt_bear_bat


def bullish_gartley_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement,
                                  fib_A_to_B: Fibonacci_Retracement,
                                  fib_A_to_D: Fibonacci_Retracement, symbol):
    print_search(string=bullish_gartley, sym=symbol)
    if fib_X_to_A.g_p_e_618 > xabcd.B > fib_X_to_A.l_r_p_786:
        print("B is Valid")
        if fib_A_to_B.s_r_p_382 < xabcd.C < fib_A_to_B.f_r_p_886:
            print("C is Valid")
            if (fib_X_to_A.l_r_p_786 * lower_sharpness) <= xabcd.D <= (fib_X_to_A.l_r_p_786 * upper_Sharpness):
                print_sharpness(upper=fib_X_to_A.l_r_p_786 * upper_Sharpness, middle=xabcd.D,
                                lower=fib_X_to_A.l_r_p_786 * lower_sharpness)
                print("D is Valid")
                print(bullish_gartley + " Verified")
                return "D"
            else:
                if xabcd.C > xabcd.D > fib_X_to_A.l_r_p_786:
                    return "C"
    return "InValid  " + bullish_gartley


def bearish_gartley_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement,
                                  fib_A_to_B: Fibonacci_Retracement,
                                  fib_A_to_D: Fibonacci_Retracement, symbol):
    print_search(string=bearish_gartley, sym=symbol)
    if fib_X_to_A.g_p_e_618 < xabcd.B < fib_X_to_A.l_r_p_786:
        print("B is Valid")
        if fib_A_to_B.s_r_p_382 > xabcd.C > fib_A_to_B.f_r_p_886:
            print("C is Valid")
            if (fib_X_to_A.l_r_p_786 * lower_sharpness) <= xabcd.D <= (fib_X_to_A.l_r_p_786 * upper_Sharpness):
                print_sharpness(upper=fib_X_to_A.l_r_p_786 * upper_Sharpness, middle=xabcd.D,
                                lower=fib_X_to_A.l_r_p_786 * lower_sharpness)
                print("D is Valid")
                print(bullish_gartley + " Verified")
                return "D"
            else:
                if xabcd.C < xabcd.D < fib_X_to_A.l_r_p_786 :
                    return "C"
    return "InValid  " + bullish_gartley


def bullish_cypher_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement,
                                  fib_ext_X_to_A_back_to_X: Fibonacci_Retracement,fib_X_to_C: Fibonacci_Retracement,
                                  fib_C_to_D: Fibonacci_Retracement, symbol):
    print_search(string=bullish_cypher, sym=symbol)
    if fib_X_to_A.s_r_p_382 > xabcd.B > fib_X_to_A.g_p_e_618:
        print("B is Valid")
        if fib_ext_X_to_A_back_to_X.f_ext_l_1_272 < xabcd.C < fib_ext_X_to_A_back_to_X.f_ext_l_1_414:
            print("C is Valid")
            if (fib_X_to_C.l_r_p_786 * lower_sharpness) <= xabcd.D <= (fib_X_to_C.l_r_p_786 * upper_Sharpness):
                print("D is Valid")
                print(bullish_cypher + " Verified")
                return "D"
            else:
                if xabcd.C > xabcd.D > fib_X_to_C.l_r_p_786:
                    return "C"
    return "InValid  " + bullish_cypher


def bearish_cypher_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement,
                                  fib_ext_X_to_A_back_to_X: Fibonacci_Retracement,fib_X_to_C: Fibonacci_Retracement,
                                  fib_C_to_D: Fibonacci_Retracement, symbol):
    print_search(string=bearish_cypher, sym=symbol)
    if fib_X_to_A.s_r_p_382 < xabcd.B < fib_X_to_A.g_p_e_618:
        print("B is Valid")
        if fib_ext_X_to_A_back_to_X.f_ext_l_1_272 > xabcd.C > fib_ext_X_to_A_back_to_X.f_ext_l_1_414:
            print("C is Valid")
            if (fib_X_to_C.l_r_p_786 * lower_sharpness) <= xabcd.D <= (fib_X_to_C.l_r_p_786 * upper_Sharpness):
                print("D is Valid")
                print(bearish_cypher + " Verified")
                return "D"
            else:
                if xabcd.C < xabcd.D < fib_X_to_C.l_r_p_786:
                    return "C"
    return "InValid  " + bearish_cypher


def bullish_shark_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement,
                                  fib_A_to_B: Fibonacci_Retracement,fib_X_to_C: Fibonacci_Retracement,
                                  fib_C_to_D: Fibonacci_Retracement, symbol):
    print_search(string=bullish_shark, sym=symbol)
    if fib_X_to_A.s_r_p_382 > xabcd.B > fib_X_to_A.g_p_e_618:
        print("B is Valid")
        if fib_A_to_B.s_l_p_1_130 < xabcd.C < fib_A_to_B.f_l_1_618:
            print("C is Valid")
            if fib_X_to_C.s_l_p_1_130 < xabcd.D < fib_X_to_C.f_r_p_886:
                print("D is Valid")
                print(bullish_shark + " Verified")
                return "D"
            else:
                if xabcd.C > xabcd.D > fib_X_to_C.f_r_p_886:
                    return "C"
    return "InValid  " + bullish_shark


def bearish_shark_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement,
                                  fib_A_to_B: Fibonacci_Retracement,fib_X_to_C: Fibonacci_Retracement,
                                  fib_C_to_D: Fibonacci_Retracement, symbol):
    print_search(string=bearish_shark, sym=symbol)
    if fib_X_to_A.s_r_p_382 < xabcd.B < fib_X_to_A.g_p_e_618:
        print("B is Valid")
        if fib_A_to_B.s_l_p_1_130 > xabcd.C > fib_A_to_B.f_l_1_618:
            print("C is Valid")
            if fib_X_to_C.s_l_p_1_130 > xabcd.D > fib_X_to_C.f_r_p_886:
                print("D is Valid")
                print(bearish_shark + " Verified")
                return "D"
            else:
                if xabcd.C < xabcd.D < fib_X_to_C.f_r_p_886:
                    return "C"
    return "InValid  " + bearish_shark


def bullish_crab_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement,
                                  fib_A_to_B: Fibonacci_Retracement, fib_A_to_D: Fibonacci_Retracement, symbol):
    print_search(string=bullish_crab, sym=symbol)
    if fib_X_to_A.s_r_p_382 > xabcd.B > fib_X_to_A.g_p_e_618:
        print("B is Valid")
        if fib_A_to_B.s_r_p_382 < xabcd.C < fib_A_to_B.f_r_p_886:
            print("C is Valid")
            if (fib_X_to_A.f_l_1_618 * lower_sharpness) <= xabcd.D <= (fib_X_to_A.f_l_1_618 * upper_Sharpness):
                print("D is Valid")
                print(bullish_crab + " Verified")
                return "D"
            else:
                if xabcd.C > xabcd.D > fib_X_to_A.f_l_1_618:
                    return "C"
    return "InValid  " + bullish_crab


def bearish_crab_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement,
                                  fib_A_to_B: Fibonacci_Retracement, fib_A_to_D: Fibonacci_Retracement, symbol):
    print_search(string=bearish_crab, sym=symbol)
    if fib_X_to_A.s_r_p_382 < xabcd.B < fib_X_to_A.g_p_e_618:
        print("B is Valid")
        if fib_A_to_B.s_r_p_382 > xabcd.C > fib_A_to_B.f_r_p_886:
            print("C is Valid")
            if (fib_X_to_A.f_l_1_618 * lower_sharpness) <= xabcd.D <= (fib_X_to_A.f_l_1_618 * upper_Sharpness):
                print("D is Valid")
                print(bearish_crab + " Verified")
                return "D"
            else:
                if xabcd.C < xabcd.D < fib_X_to_A.f_l_1_618:
                    return "C"
    return "InValid  " + bearish_crab


def deep_bullish_crab_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement,
                                  fib_A_to_B: Fibonacci_Retracement, fib_A_to_D: Fibonacci_Retracement, symbol):
    print_search(string=bullish_deep, sym=symbol)
    if (fib_X_to_A.f_r_p_886 * lower_sharpness) <= xabcd.B <= (fib_X_to_A.f_r_p_886 * upper_Sharpness):
        print("B is Valid")
        if fib_A_to_B.s_r_p_382 < xabcd.C < fib_A_to_B.f_r_p_886:
            print("C is Valid")
            if (fib_X_to_A.f_l_1_618 * lower_sharpness) <= xabcd.D <= (fib_X_to_A.f_l_1_618 * upper_Sharpness):
                print("D is Valid")
                print(bullish_deep + " Verified")
                return "D"
            else:
                if xabcd.C > xabcd.D > fib_X_to_A.f_l_1_618:
                    return "C"
    return "InValid  " + bullish_deep


def deep_bearish_crab_chart_pattern(xabcd: Indicator, fib_X_to_A: Fibonacci_Retracement,
                                  fib_A_to_B: Fibonacci_Retracement, fib_A_to_D: Fibonacci_Retracement, symbol):
    print_search(string=bearish_deep, sym=symbol)
    if (fib_X_to_A.f_r_p_886 * lower_sharpness) <= xabcd.B <= (fib_X_to_A.f_r_p_886 * upper_Sharpness):
        print("B is Valid")
        if fib_A_to_B.s_r_p_382 > xabcd.C > fib_A_to_B.f_r_p_886:
            print("C is Valid")
            if (fib_X_to_A.f_l_1_618 * lower_sharpness) <= xabcd.D <= (fib_X_to_A.f_l_1_618 * upper_Sharpness):
                print("D is Valid")
                print(bearish_deep + " Verified")
                return "D"
            else:
                if xabcd.C < xabcd.D < fib_X_to_A.f_l_1_618:
                    return "C"
    return "InValid  " + bearish_deep

def print_harmonic_result(trigger, pattern, timeframe, Symbol, db: DB, indicate: Indicator):
    if trigger == "D":
        data = pattern + " Verified Completely on " + timeframe + " For Symbol " + Symbol + " with X = " + str(
            indicate.X) + " A = " + str(indicate.A) + " B = " + str(indicate.B) + " C = " + str(
            indicate.C) + " D = " + str(indicate.D)
        db.insert_harmonic_pattern(String=data)
    elif trigger == "C":
        data = pattern + " Verified Partially on " + timeframe + " For Symbol " + Symbol + " with X = " + str(
            indicate.X) + " A = " + str(indicate.A) + " B = " + str(indicate.B) + " C = " + str(
            indicate.C) + " D = " + str(indicate.D)
        db.insert_harmonic_pattern(String=data)


def print_search(string, sym):
    print("***************************Searching for " + string + " For " + sym + " *************************** " + str(
        datetime.now()))


def print_sharpness(upper, middle, lower):
    print("Upper = " + str(upper) + " Middle = " + str(middle) + " Lower = " + str(lower))


def main(trade_bot_obj: TradingBot, counter_obj: Counters, indicator_obj: Indicator, symb_obj: Symbols, db_obj: DB):
    db_obj.initialize_db(symb_obj.current_symbol)
    while True:
        open_price, high, low, close = symb_obj.get_data(timeframe=symb_obj.current_timeframe)
        indicator_obj.analyze_trend(close=close)
        indicator_obj.find_x_a_b_c_d(open_price=open_price, high=high, low=low, close=close, find_range=15)
        if indicator_obj.isBullishTrend:

            # Bullish Bat Chat Pattern
            trigger = bullish_bat_chart_pattern(xabcd=indicator_obj,
                                                fib_X_to_A=Fibonacci_Retracement(indicator_obj.X, indicator_obj.A),
                                                fib_A_to_B=Fibonacci_Retracement(indicator_obj.A, indicator_obj.B),
                                                fib_A_to_D=Fibonacci_Retracement(indicator_obj.A, indicator_obj.D),
                                                symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=bullish_bat, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

            # Alternate Bullish Bat Chat Pattern
            trigger = alternate_bullish_bat_chart_pattern(xabcd=indicator_obj,
                                                          fib_X_to_A=Fibonacci_Retracement(indicator_obj.X,
                                                                                           indicator_obj.A),
                                                          fib_A_to_B=Fibonacci_Retracement(indicator_obj.A,
                                                                                           indicator_obj.B),
                                                          fib_A_to_D=Fibonacci_Retracement(indicator_obj.A,
                                                                                           indicator_obj.D),
                                                          symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=alt_bull_bat, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

            # Bullish Gartley Chat Pattern
            trigger = bullish_gartley_chart_pattern(xabcd=indicator_obj,
                                                    fib_X_to_A=Fibonacci_Retracement(indicator_obj.X, indicator_obj.A),
                                                    fib_A_to_B=Fibonacci_Retracement(indicator_obj.A, indicator_obj.B),
                                                    fib_A_to_D=Fibonacci_Retracement(indicator_obj.A, indicator_obj.D),
                                                    symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=bullish_gartley, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

            # Bullish Cypher Chat Pattern
            trigger = bullish_cypher_chart_pattern(xabcd=indicator_obj,
                                                   fib_X_to_A=Fibonacci_Retracement(indicator_obj.X, indicator_obj.A),
                                                   fib_ext_X_to_A_back_to_X=Fibonacci_Retracement(indicator_obj.A, indicator_obj.X),
                                                   fib_X_to_C=Fibonacci_Retracement(indicator_obj.X, indicator_obj.C),
                                                   fib_C_to_D=Fibonacci_Retracement(indicator_obj.C, indicator_obj.D),
                                                   symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=bullish_cypher, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

            # Bullish Shark Chat Pattern
            trigger = bullish_shark_chart_pattern(xabcd=indicator_obj,
                                                  fib_X_to_A=Fibonacci_Retracement(indicator_obj.X, indicator_obj.A),
                                                  fib_A_to_B=Fibonacci_Retracement(indicator_obj.A, indicator_obj.B),
                                                  fib_X_to_C=Fibonacci_Retracement(indicator_obj.X, indicator_obj.C),
                                                  fib_C_to_D=Fibonacci_Retracement(indicator_obj.C, indicator_obj.D),
                                                  symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=bullish_shark, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

            # Bullish Crab Chat Pattern
            trigger = bullish_crab_chart_pattern(xabcd=indicator_obj,
                                                 fib_X_to_A=Fibonacci_Retracement(indicator_obj.X, indicator_obj.A),
                                                 fib_A_to_B=Fibonacci_Retracement(indicator_obj.A, indicator_obj.B),
                                                 fib_A_to_D=Fibonacci_Retracement(indicator_obj.A, indicator_obj.D),
                                                 symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=bullish_crab, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

            # Deep Bullish Crab Chat Pattern
            trigger = deep_bullish_crab_chart_pattern(xabcd=indicator_obj,
                                                      fib_X_to_A=Fibonacci_Retracement(indicator_obj.X, indicator_obj.A),
                                                      fib_A_to_B=Fibonacci_Retracement(indicator_obj.A, indicator_obj.B),
                                                      fib_A_to_D=Fibonacci_Retracement(indicator_obj.A, indicator_obj.D),
                                                      symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=bullish_deep, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

        elif indicator_obj.isBearishTrend:

            # Bearish Bat Chat Pattern
            trigger = bearish_bat_chart_pattern(xabcd=indicator_obj,
                                                fib_X_to_A=Fibonacci_Retracement(indicator_obj.X, indicator_obj.A),
                                                fib_A_to_B=Fibonacci_Retracement(indicator_obj.A, indicator_obj.B),
                                                fib_A_to_D=Fibonacci_Retracement(indicator_obj.A, indicator_obj.D),
                                                symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=bearish_bat, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

            # Alternate Bearish Bat Chat Pattern
            trigger = alternate_bearish_bat_chart_pattern(xabcd=indicator_obj,
                                                          fib_X_to_A=Fibonacci_Retracement(indicator_obj.X,
                                                                                           indicator_obj.A),
                                                          fib_A_to_B=Fibonacci_Retracement(indicator_obj.A,
                                                                                           indicator_obj.B),
                                                          fib_A_to_D=Fibonacci_Retracement(indicator_obj.A,
                                                                                           indicator_obj.D),
                                                          symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=alt_bear_bat, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

            # Bearish Gartley Chat Pattern
            trigger = bearish_gartley_chart_pattern(xabcd=indicator_obj,
                                                    fib_X_to_A=Fibonacci_Retracement(indicator_obj.X, indicator_obj.A),
                                                    fib_A_to_B=Fibonacci_Retracement(indicator_obj.A, indicator_obj.B),
                                                    fib_A_to_D=Fibonacci_Retracement(indicator_obj.A, indicator_obj.D),
                                                    symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=bearish_gartley, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

            # Bearish Cypher Chat Pattern
            trigger = bearish_cypher_chart_pattern(xabcd=indicator_obj,
                                                   fib_X_to_A=Fibonacci_Retracement(indicator_obj.X, indicator_obj.A),
                                                   fib_ext_X_to_A_back_to_X=Fibonacci_Retracement(indicator_obj.A, indicator_obj.X),
                                                   fib_X_to_C=Fibonacci_Retracement(indicator_obj.X, indicator_obj.C),
                                                   fib_C_to_D=Fibonacci_Retracement(indicator_obj.C, indicator_obj.D),
                                                   symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=bearish_cypher, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

            # Bearish Shark Chat Pattern
            trigger = bearish_shark_chart_pattern(xabcd=indicator_obj,
                                                  fib_X_to_A=Fibonacci_Retracement(indicator_obj.X, indicator_obj.A),
                                                  fib_A_to_B=Fibonacci_Retracement(indicator_obj.A, indicator_obj.B),
                                                  fib_X_to_C=Fibonacci_Retracement(indicator_obj.X, indicator_obj.C),
                                                  fib_C_to_D=Fibonacci_Retracement(indicator_obj.C, indicator_obj.D),
                                                  symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=bearish_shark, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

            # Bearish Crab Chat Pattern
            trigger = bearish_crab_chart_pattern(xabcd=indicator_obj,
                                                 fib_X_to_A=Fibonacci_Retracement(indicator_obj.X, indicator_obj.A),
                                                 fib_A_to_B=Fibonacci_Retracement(indicator_obj.A, indicator_obj.B),
                                                 fib_A_to_D=Fibonacci_Retracement(indicator_obj.A, indicator_obj.D),
                                                 symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=bearish_crab, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)

            # Deep Bearish Crab Chat Pattern
            trigger = deep_bearish_crab_chart_pattern(xabcd=indicator_obj,
                                                      fib_X_to_A=Fibonacci_Retracement(indicator_obj.X, indicator_obj.A),
                                                      fib_A_to_B=Fibonacci_Retracement(indicator_obj.A, indicator_obj.B),
                                                      fib_A_to_D=Fibonacci_Retracement(indicator_obj.A, indicator_obj.D),
                                                      symbol=symb_obj.current_symbol)
            print(trigger)
            print_harmonic_result(trigger=trigger, pattern=bearish_deep, timeframe=symb_obj.current_timeframe,
                                  Symbol=symb_obj.current_symbol, db=db_obj, indicate=indicator_obj)
        symb_obj.increment_harmonics()
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
