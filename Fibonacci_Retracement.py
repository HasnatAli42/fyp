Top = 1
firstRetracement = 0.236
secondRetracement = 0.382
thirdRetracement = 0.501
golden_pocket_start = 0.651
golden_pocket_end = 0.618
lastRetracement = 0.786
finalRetracement = 0.886
Bottom = 0
firstTarget = 0.272
secondTarget = 0.618
stopLoss = 1.13


class Fibonacci_Retracement:

    def __init__(self, start_price, end_price):
        self.start_price = 0
        self.end_price = 0
        self.fib_price_range = 0
        self.isLong = False
        self.isShort = False
        self.isLongTrend = False
        self.isShortTrend = False
        self.f_r_p_236 = 0
        self.s_r_p_382 = 0
        self.t_r_p_501 = 0
        self.g_p_s_651 = 0
        self.g_p_e_618 = 0
        self.l_r_p_786 = 0
        self.f_r_p_886 = 0
        self.f_t_p_272 = 0
        self.s_t_p_618 = 0
        self.s_l_p_1_130 = 0
        self.calculate(start_price=start_price,end_price=end_price)

    def calculate(self, start_price, end_price):
        self.start_price = start_price
        self.end_price = end_price
        if start_price > end_price:
            self.fib_price_range = self.start_price - self.end_price
            self.isShort = True
            self.isLong = False
        else:
            self.fib_price_range = self.end_price - self.start_price
            self.isLong = True
            self.isShort = False
        if self.isLong:
            self.f_r_p_236 = self.end_price - (self.fib_price_range * firstRetracement)
            self.s_r_p_382 = self.end_price - (self.fib_price_range * secondRetracement)
            self.t_r_p_501 = self.end_price - (self.fib_price_range * thirdRetracement)
            self.g_p_s_651 = self.end_price - (self.fib_price_range * golden_pocket_start)
            self.g_p_e_618 = self.end_price - (self.fib_price_range * golden_pocket_end)
            self.l_r_p_786 = self.end_price - (self.fib_price_range * lastRetracement)
            self.f_r_p_886 = self.end_price - (self.fib_price_range * finalRetracement)
            self.f_t_p_272 = self.end_price + (self.fib_price_range * firstTarget)
            self.s_t_p_618 = self.end_price + (self.fib_price_range * secondTarget)
            self.s_l_p_1_130 = self.end_price - (self.fib_price_range * stopLoss)
        elif self.isShort:
            self.f_r_p_236 = self.end_price + (self.fib_price_range * firstRetracement)
            self.s_r_p_382 = self.end_price + (self.fib_price_range * secondRetracement)
            self.t_r_p_501 = self.end_price + (self.fib_price_range * thirdRetracement)
            self.g_p_s_651 = self.end_price + (self.fib_price_range * golden_pocket_start)
            self.g_p_e_618 = self.end_price + (self.fib_price_range * golden_pocket_end)
            self.l_r_p_786 = self.end_price + (self.fib_price_range * lastRetracement)
            self.f_r_p_886 = self.end_price + (self.fib_price_range * finalRetracement)
            self.f_t_p_272 = self.end_price - (self.fib_price_range * firstTarget)
            self.s_t_p_618 = self.end_price - (self.fib_price_range * secondTarget)
            self.s_l_p_1_130 = self.end_price + (self.fib_price_range * stopLoss)
        else:
            print("Error")

    def print_fib(self, heading):
        if self.isLong:
            print("*********************** Fib Retracement For L", heading, " *********************")
            print("Second Target Price        (", secondTarget, ") = ", self.s_t_p_618)
            print("First Target Price         (", firstTarget, ") = ", self.f_t_p_272)
            print("End Price                  ( 0.000 ) = ", self.end_price)
            print("First Retracement Price    (", firstRetracement, ") = ", self.f_r_p_236)
            print("Second Retracement Price   (", secondRetracement, ") = ", self.s_r_p_382)
            print("Third Retracement Price    (", thirdRetracement, ") = ", self.t_r_p_501)
            print("Golden Pocket Start Price  (", golden_pocket_start, ") = ", self.g_p_s_651)
            print("Golden Pocket End Price    (", golden_pocket_end, ") = ", self.g_p_e_618)
            print("Last Retracement Price     (", lastRetracement, ") = ", self.l_r_p_786)
            print("Final Retracement Price    (", finalRetracement, ") = ", self.f_r_p_886)
            print("Start Price                ( 1.000 ) = ", self.start_price)
            print("Stop Loss Price            (", stopLoss, ") = ", self.s_l_p_1_130)

        elif self.isShort:
            print("*********************** Fib Retracement For S ", heading, " *********************")
            print("Stop Loss Price            (", stopLoss, ") = ", self.s_l_p_1_130)
            print("Start Price                ( 1.000 ) = ", self.start_price)
            print("Final Retracement Price    (", finalRetracement, ") = ", self.f_r_p_886)
            print("Last Retracement Price     (", lastRetracement, ") = ", self.l_r_p_786)
            print("Golden Pocket End Price    (", golden_pocket_end, ") = ", self.g_p_e_618)
            print("Golden Pocket Start Price  (", golden_pocket_start, ") = ", self.g_p_s_651)
            print("Third Retracement Price    (", thirdRetracement, ") = ", self.t_r_p_501)
            print("Second Retracement Price   (", secondRetracement, ") = ", self.s_r_p_382)
            print("First Retracement Price    (", firstRetracement, ") = ", self.f_r_p_236)
            print("End Price                  ( 0.000 ) = ", self.end_price)
            print("First Target Price         (", firstTarget, ") = ", self.f_t_p_272)
            print("Second Target Price        (", secondTarget, ") = ", self.s_t_p_618)

    def search_trend(self, ema20, ema50):
        if ema20 > ema50:
            self.isLongTrend = True
        elif ema20 < ema50:
            self.isShortTrend = True


