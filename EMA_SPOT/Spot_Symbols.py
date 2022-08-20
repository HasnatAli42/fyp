import time

import pandas as pd
import requests
from binance.client import Client
from Spot_Settings import TIME_PERIOD, LIMIT, Dollars


class SpotSymbols:

    def __init__(self, current_index_symbol, current_index_time_frame):
        self.symbols = ["BTCBUSD", "ETHBUSD", "SOLBUSD", "BNBBUSD", "ETCBUSD", "FILBUSD", "MATICBUSD", "APEBUSD", "OPBUSD",
           "ADABUSD", "RUNEBUSD", "EURBUSD", "AVAXBUSD", "LUNCBUSD", "DOTBUSD", "SHIBBUSD", "LUNABUSD", "NEARBUSD",
           "XRPBUSD", "GALABUSD", "LINKBUSD", "GMTBUSD", "STPTBUSD", "BTCSTBUSD", "ROSEBUSD", "FTMBUSD", "ALPACABUSD",
           "LDOBUSD", "LOKABUSD", "VETBUSD", "GALBUSD", "WINBUSD", "JASMYBUSD", "PEOPLEBUSD", "SANDBUSD", "HIGHBUSD",
           "WINGBUSD", "NMRBUSD", "CHZBUSD", "CREAMBUSD", "UNIBUSD", "ICPBUSD", "ENSBUSD", "DOGEBUSD", "FORTHBUSD",
           "GLMRBUSD", "GBPBUSD", "LITBUSD", "SNXBUSD", "LTCBUSD", "AXSBUSD", "EGLDBUSD", "WAVESBUSD", "DEGOBUSD",
           "TRXBUSD", "LEVERBUSD", "CRVBUSD", "DYDXBUSD", "ATOMBUSD", "MANABUSD", "IMXBUSD", "UNFIBUSD", "CTXCBUSD",
           "NEXOBUSD", "THETABUSD", "KDABUSD", "RADBUSD", "AAVEBUSD", "BURGERBUSD", "FTTBUSD", "AUDBUSD", "BONDBUSD",
           "PAXGBUSD", "YFIBUSD", "TWTBUSD", "HIVEBUSD", "BAKEBUSD", "ANCBUSD", "ZILBUSD", "ONEBUSD", "BCHBUSD",
           "AUCTIONBUSD", "EOSBUSD", "MOBBUSD", "ALGOBUSD", "LINABUSD", "VOXELBUSD", "DARBUSD", "MBOXBUSD", "XMRBUSD",
           "SLPBUSD", "GRTBUSD", "ALICEBUSD", "NULSBUSD", "QIBUSD", "OGBUSD", "ACHBUSD", "PROMBUSD", "PYRBUSD",
           "DENTBUSD", "TRBBUSD", "PUNDIXBUSD", "SUSHIBUSD", "HBARBUSD", "ARBUSD", "CAKEBUSD", "ENJBUSD", "LRCBUSD",
           "TLMBUSD", "BADGERBUSD", "WAXPBUSD", "DODOBUSD", "MINABUSD", "RNDRBUSD", "XTZBUSD", "RSRBUSD", "VIDTBUSD",
           "LAZIOBUSD", "MBLBUSD", "LAZIOBUSD", "COTIBUSD", "KP3RBUSD", "BICOBUSD", "FLOWBUSD", "FXSBUSD", "SANTOSBUSD",
           "AUDIOBUSD", "PONDBUSD", "HOTBUSD", "BELBUSD", "CVXBUSD", "BNXBUSD", "CELOBUSD", "KLAYBUSD", "QNTBUSD",
           "C98BUSD", "XLMBUSD", "OOKIBUSD", "KSMBUSD", "FRONTBUSD", "NEOBUSD", "FIDABUSD", "BTTCBUSD", "1INCHBUSD",
           "COMPBUSD", "RVNBUSD", "ADXBUSD", "KAVABUSD", "SKLBUSD", "MOVRBUSD", "SYSBUSD", "OGNBUSD", "EPXBUSD",
            "PORTOBUSD", "JUVBUSD", "DATABUSD", "HNTBUSD", "SXPBUSD", "BETABUSD", "ALPHABUSD", "CELRBUSD",
           "RAREBUSD", "YGGBUSD", "ICXBUSD", "LSKBUSD", "WOOBUSD", "ACABUSD", "ANKRBUSD", "TVKBUSD", "ASTRBUSD",
           "KNCBUSD", "TORNBUSD", "BSWBUSD", "ZECBUSD", "UFTBUSD", "FIROBUSD", "MASKBUSD", "CTXCBUSD", "FETBUSD",
           "BARBUSD", "FLUXBUSD", "ATABUSD", "DREPBUSD", "BATBUSD", "SRMBUSD", "API3BUSD", "SPELLBUSD", "MKRBUSD",
           "IDEXBUSD", "DASHBUSD", "IOTABUSD", "SCRTBUSD", "STXBUSD", "CHRBUSD", "XECBUSD", "ANTBUSD", "QUICKBUSD",
           "OCEANBUSD", "GTCBUSD", "REEFBUSD", "CTSIBUSD", "SUPERBUSD", "ASRBUSD", "AERGOBUSD", "TKOBUSD", "ALCXBUSD",
           "FARMBUSD", "POLSBUSD", "UMABUSD", "AUTOBUSD", "IOSTBUSD", "TOMOBUSD", "ARPABUSD", "UMABUSD", "INJBUSD", "ACMBUSD",
           "RAYBUSD", "COSBUSD", "WBTCBUSD", "JOEBUSD", "BTGBUSD", "ALPINEBUSD", "CLVBUSD", "CVPBUSD", "CFXBUSD",
           "KEYBUSD", "REIBUSD", "XECBUSD", "MTLBUSD", "TRIBEBUSD", "STMXBUSD", "ONTBUSD", "DUSKBUSD", "TROYBUSD",
           "AMPBUSD", "ATMBUSD", "BALBUSD", "SFPBUSD", "DEXEBUSD", "DIABUSD", "XVSBUSD", "USDPBUSD", "SUNBUSD",
           "ELFBUSD", "ILVBUSD", "PSGBUSD", "MDXBUSD", "COCOSBUSD", "STRAXBUSD", "ERNBUSD", "LTOBUSD", "MDTBUSD",
           "LPTBUSD", "QTUMBUSD", "IQBUSD", "AGLDBUSD", "ZENBUSD", "MULTIBUSD", "ORNBUSD", "MCBUSD", "DGBBUSD",
           "GTOBUSD", "AKROBUSD", "OMBUSD", "WRXBUSD", "CITYBUSD", "RENBUSD", "PHABUSD", "HARDBUSD", "TFUELBUSD",
           "OMGBUSD", "XVGBUSD", "BIFIBUSD", "BNTBUSD", "BLZBUSD", "UTKBUSD", "DFBUSD", "JSTBUSD", "DNTBUSD", 'TBUSD',
           "GHSTBUSD", "DOCKBUSD", "MLNBUSD", "FORBUSD", "FISBUSD", "CKBBUSD", "POWRBUSD", "NKNBUSD", "SCBUSD",
           "CVCBUSD", "XNOBUSD", "PLABUSD", "OXTBUSD", "STEEMBUSD", "POLYBUSD"]
        self.decimal_point_qty = [3, 3, 2, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 2, 0, 1,
                                  1, 0, 0, 1, 1]
        self.decimal_point_price = [1, 2, 2, 4, 4, 5, 2, 2, 3, 3, 4, 3, 3, 4, 4, 4, 6, 6, 4, 4, 3, 5, 3, 3, 3, 3, 2, 4,
                                    3, 3, 6, 6, 3, 3]
        self.upper_sharpness = [1.002, 1.0025, 1.003, 1.004, 1.005]
        self.lower_sharpness = [0.998, 0.9975, 0.997, 0.996, 0.995]
        self.timeframe = ["1d"]
        self.current_index = current_index_symbol
        self.current_symbol = self.symbols[self.current_index]
        self.current_decimal_point_qty = self.decimal_point_qty[self.current_index]
        self.current_decimal_point_price = self.decimal_point_price[self.current_index]
        self.current_QNTY = self.dollars_to_cryto_quantiy(Dollars)
        self.api_key = "FBenBPte1P8oxxul5WmL5oxluUd3GGH83RnmGU1v40wxqw1dPh8qAREvKG7nWzad"
        self.secret_key = "M2xd43ai6fLTgwxmEtGT6PAmnMw6wcG61qq7ft1xLlCclvTafZHU63t1dePlvzIE"
        self.current_symbol_price = self.get_price_spot()
        # self.timeframe = ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1D"]
        self.current_index_timeframe = current_index_time_frame
        self.current_timeframe = self.timeframe[self.current_index_timeframe]
        self.current_upper_sharpness = self.upper_sharpness[self.current_index_timeframe]
        self.current_lower_sharpness = self.lower_sharpness[self.current_index_timeframe]

    def verify_data(self):
        if len(self.symbols) == len(self.symbols) == len(self.symbols):
            print("Verified with Length = ", len(self.symbols))
        else:
            print("UnVerified")

    def increment(self):
        if self.current_index == len(self.symbols) - 1:
            self.current_index = 0
        else:
            self.current_index += 1
        self.current_symbol = self.symbols[self.current_index]
        self.current_decimal_point_qty = self.decimal_point_qty[self.current_index]
        self.current_decimal_point_price = self.decimal_point_price[self.current_index]
        self.current_QNTY = self.dollars_to_cryto_quantiy(Dollars)

    def client(self):
        client = Client(api_key=self.api_key, api_secret=self.secret_key)
        return client

    def get_price_spot(self):
        try:
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={self.current_symbol}"
        except Exception as e:
            time.sleep(10)
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={self.current_symbol}"
        res = requests.get(url)
        self.current_symbol_price = float(res.json()['price'])
        return self.current_symbol_price

    def dollars_to_cryto_quantiy(self, quantity):
        try:
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={self.current_symbol}"
        except Exception as e:
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={self.current_symbol}"
        res = requests.get(url)
        return round((quantity / float(res.json()['price'])), self.current_decimal_point_qty)

    def get_data(self, timeframe):
        url = "https://api.binance.com/api/v3/klines?symbol={}&interval={}&limit={}".format(self.current_symbol,
                                                                                              timeframe,
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

    def print_current_status(self):
        print("********************* Finding EMA CROSSING For "+self.current_symbol+" at TimeFrame = "+ self.current_timeframe+ " ******************************")
