from multi_time_series_connectedness import Volatility, Connectedness, RollingConnectedness
import pandas as pd
import pickle
import os

if __name__ == "__main__":
    volatility = Volatility(n=2)
    volatility.calculate("docs/market_prices", "2024-10-09T00:00:00+01:00", "2024-10-09T09:48:00+01:00", "docs/volatilities.pickle")

    volatilities = pd.read_pickle("docs/volatilities.pickle")

    connectedness = Connectedness(volatilities)
    connectedness.calculate()

    roll_conn = RollingConnectedness(volatilities.dropna(), 20, 80)
    roll_conn.divide_timeseries_volatilities()
    roll_conn.calculate("docs/roll_conn.pickle")
