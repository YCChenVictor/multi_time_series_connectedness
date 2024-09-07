# import required modules
import numpy as np
import datetime
import pandas as pd
import os
from functions.load_data import get_file_names
# =================================


def yang_zhang_volatility(data, name, n=2):
    """
    :param data: a list with Open, High, Low, Close price
    :param n: the periods to obtain the average volatilitys
    :param clean: If clean, then delete the NA values
    :return: A list of volatility data
    """
    # define required variables
    o_c = (data['Open'] / data['Close'].shift(1)).apply(np.log)
    c_o = (data['Close'] / data['Open']).apply(np.log)
    h_o = (data['High'] / data['Open']).apply(np.log)
    l_o = (data['Low'] / data['Open']).apply(np.log)

    # overnight volatility
    vo = o_c.rolling(window=n).apply(np.var, raw=True)

    # today(open to close) volatility
    vt = c_o.rolling(window=n).apply(np.var, raw=True)

    # rogers-satchell volatility
    rs_fomula = h_o * (h_o - c_o) + l_o * (l_o - c_o)
    rs = rs_fomula.rolling(window=n, center=False).sum() * (1.0 / n)

    # super parameter
    k = 0.34 / (1 + (n + 1) / (n - 1))

    # yang-zhang
    result = (vo + k * vt + (1 - k) * rs).apply(np.sqrt)

    result_df = result.to_frame(name=name)

    return pd.concat([data['time'], result_df], axis=1)

def date_format(date):
    list_date = date.split("-")
    year, month, day = list_date[0], list_date[1], list_date[2]
    return datetime.date(int(year), int(month), int(day))


class volatility:
    def __init__(self, path, start_at, end_at):
        # the path filled with timeseries data going to calculate volatility
        self.path = path
        # the start date of the volatility data
        self.start_at = start_at
        # the end date of the volatility data
        self.end_at = end_at
        # Variable generated in periods_of_volatility
        self.volatilities = None

    # read the price data, set up dictionary and then calculate the volatility
    def price_data_to_volatility(self):
        files = get_file_names(self.path)

        volatilities = None
        for i in range(len(files)):
            timeseries_data = pd.read_csv(self.path + "/" + files[i])
            timeseries_data = timeseries_data.loc[
                    (timeseries_data["time"] >= self.start_at) & (timeseries_data["time"] <= self.end_at)]
            timeseries_data = timeseries_data.interpolate()
            volatility = yang_zhang_volatility(timeseries_data, files[i])
            if volatilities is None:
                volatilities = volatility
            else:
                volatilities = volatilities.merge(volatility, on='time', how='outer')

        print(volatilities)
        self.volatilities = volatilities
