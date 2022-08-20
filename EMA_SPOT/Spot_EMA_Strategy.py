import os
from datetime import datetime
import time

from numpy.core.defchararray import strip

from EMA_SPOT.Spot_Indicator import SpotIndicator
from EMA_SPOT.Spot_Symbols import SpotSymbols
from Settings import TIME_SLEEP


def main(symbol_obj: SpotSymbols, indicator_obj: SpotIndicator):
    while True:
        open_price, high, low, close = symbol_obj.get_data(timeframe=symb_obj.current_timeframe)



        symbol_obj.increment()
        time.sleep(TIME_SLEEP)


if __name__ == "__main__":
    symb_obj = SpotSymbols(current_index_symbol=0, current_index_time_frame=0)
    ind_obj = SpotIndicator(higher_EMA=50, lower_EMA=20)
    while True:
        try:
            if os.path.exists(f'is_order_in_progress_for_spot_ema.txt'):
                file = open(f'is_order_in_progress_for_spot_ema.txt', 'r')
                x = file.readlines()
                file.close()
                x = strip(x)
                main(symbol_obj=symb_obj , indicator_obj=ind_obj)
            else:
                main(symbol_obj=symb_obj, indicator_obj=ind_obj)
        except Exception as e:
            print(e)
            try:
                time.sleep(20)
            except Exception as e:
                print(e)
                time.sleep(10)
