from multi_time_series_connectedness import Volatility, RollingConnectedness
import pandas as pd

if __name__ == "__main__":
    max_lag = 20
    periods_per_volatility = 80
    volatility = Volatility(n=2)
    volatility.calculate("docs/market_prices", "docs/volatilities.pickle")
    volatilities = pd.read_pickle("docs/volatilities.pickle")
    roll_conn = RollingConnectedness(
        volatilities.dropna(), max_lag, periods_per_volatility
    )
    roll_conn.calculate()
    roll_conn.store("docs/roll_conn.pickle")
