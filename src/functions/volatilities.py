import pandas as pd
import numpy as np

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

def price_data_to_volatility(datasets):
    volatilities = None
    for key, value in datasets.items():
        volatility = yang_zhang_volatility(value, key)
        if volatilities is None:
            volatilities = volatility
        else:
            volatilities = volatilities.merge(volatility, on='time', how='outer')

    return volatilities
