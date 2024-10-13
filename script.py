from multi_time_series_connectedness import Volatility, Connectedness, RollingConnectedness
import pandas as pd
import pickle
import os

if __name__ == "__main__":
    max_lag = 20
    periods_per_volatility = 80
    volatility = Volatility(n=2)
    volatility.calculate("docs/market_prices", "2024-10-09T00:00:00+01:00", "2024-10-09T09:59:00+01:00", "docs/volatilities.pickle")
    volatilities = pd.read_pickle("docs/volatilities.pickle")
    # train "2024-10-09T01:21:00+01:00", "2024-10-09T09:48:00+01:00"
    # predict "2024-10-09T09:49:00+01:00", "2024-10-09T09:59:00+01:00"
    roll_conn = RollingConnectedness(volatilities.dropna(), max_lag, periods_per_volatility, "2024-10-09T09:49:00+01:00", "2024-10-09T09:59:00+01:00")
    roll_conn.calculate("docs/roll_conn.pickle")
