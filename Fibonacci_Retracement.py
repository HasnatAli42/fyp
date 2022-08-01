Top = 1
firstRetracement = 0.236
secondRetracement = 0.382
thirdRetracement = 0.501
golden_pocket_start = 0.651
golden_pocket_end = 0.618
lastRetracement = 0.786
Bottom = 0
firstTarget = 0.272
secondTarget = 0.618


class FibonacciRetracement:

    def __init__(self):
        self.start_price = 0
        self.end_price = 0
        self.fib_price_range = 0
        self.isLong = False
        self.isShort = False
        self.isLongTrend = False
        self.isShortTrend = False
        self.f_r_p = 0
        self.s_r_p = 0
        self.t_r_p = 0
        self.g_p_s = 0
        self.g_p_e = 0
        self.l_r_p = 0
        self.f_t_p = 0
        self.s_t_p = 0

    def calculate(self, start_price, end_price):
        self.start_price = start_price
        self.end_price = end_price
        if start_price > end_price:
            self.fib_price_range = self.start_price - self.end_price
            self.isShort = True
        else:
            self.fib_price_range = self.end_price - self.start_price
            self.isLong = True
        if self.isLong:
            self.f_r_p = self.end_price - (self.fib_price_range * firstRetracement)
            self.s_r_p = self.end_price - (self.fib_price_range * secondRetracement)
            self.t_r_p = self.end_price - (self.fib_price_range * thirdRetracement)
            self.g_p_s = self.end_price - (self.fib_price_range * golden_pocket_start)
            self.g_p_e = self.end_price - (self.fib_price_range * golden_pocket_end)
            self.l_r_p = self.end_price - (self.fib_price_range * lastRetracement)
            self.f_t_p = self.end_price + (self.fib_price_range * firstTarget)
            self.s_t_p = self.end_price + (self.fib_price_range * secondTarget)
        elif self.isShort:
            self.f_r_p = self.end_price + (self.fib_price_range * firstRetracement)
            self.s_r_p = self.end_price + (self.fib_price_range * secondRetracement)
            self.t_r_p = self.end_price + (self.fib_price_range * thirdRetracement)
            self.g_p_s = self.end_price + (self.fib_price_range * golden_pocket_start)
            self.g_p_e = self.end_price + (self.fib_price_range * golden_pocket_end)
            self.l_r_p = self.end_price + (self.fib_price_range * lastRetracement)
            self.f_t_p = self.end_price - (self.fib_price_range * firstTarget)
            self.s_t_p = self.end_price - (self.fib_price_range * secondTarget)
        else:
            print("Error")

    def print_fib(self):
        if self.isLong:
            print("*********************** Fib Retracement For Long Order *********************")
            print("Second Target Price        (", secondTarget, ") = ", self.s_t_p)
            print("First Target Price         (", firstTarget, ") = ", self.f_t_p)
            print("End Price                  ( 0.000 ) = ", self.end_price)
            print("First Retracement Price    (", firstRetracement, ") = ", self.f_r_p)
            print("Second Retracement Price   (", secondRetracement, ") = ", self.s_r_p)
            print("Third Retracement Price    (", thirdRetracement, ") = ", self.t_r_p)
            print("Golden Pocket Start Price  (", golden_pocket_start, ") = ", self.g_p_s)
            print("Golden Pocket End Price    (", golden_pocket_end, ") = ", self.g_p_e)
            print("Last Retracement Price     (", lastRetracement, ") = ", self.l_r_p)
            print("Start Price                ( 1.000 ) = ", self.start_price)
        elif self.isShort:
            print("*********************** Fib Retracement For Short Order *********************")
            print("Start Price                ( 1.000 ) = ", self.start_price)
            print("Last Retracement Price     (", lastRetracement, ") = ", self.l_r_p)
            print("Golden Pocket End Price    (", golden_pocket_end, ") = ", self.g_p_e)
            print("Golden Pocket Start Price  (", golden_pocket_start, ") = ", self.g_p_s)
            print("Third Retracement Price    (", thirdRetracement, ") = ", self.t_r_p)
            print("Second Retracement Price   (", secondRetracement, ") = ", self.s_r_p)
            print("First Retracement Price    (", firstRetracement, ") = ", self.f_r_p)
            print("End Price                  ( 0.000 ) = ", self.end_price)
            print("First Target Price         (", firstTarget, ") = ", self.f_t_p)
            print("Second Target Price        (", secondTarget, ") = ", self.s_t_p)

    def search_trend(self, ema20, ema50):
        if ema20 > ema50:
            self.isLongTrend = True
        elif ema20 < ema50:
            self.isShortTrend = True


fib = FibonacciRetracement()
fib.calculate(start_price=1700, end_price=1600)
fib.print_fib()
