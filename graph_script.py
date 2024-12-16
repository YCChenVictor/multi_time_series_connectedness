import pandas as pd

from multi_time_series_connectedness import Volatility, Connectedness

if __name__ == "__main__":
    volatility = Volatility(n=2)
    volatility.calculate("docs/market_prices", "docs/volatilities.pickle")
    volatilities = pd.read_pickle("docs/volatilities.pickle")
    conn = Connectedness(volatilities.dropna(), 20, 1)
    conn.calculate()
    conn.store_graph_data()
    conn.flatten_connectedness()
