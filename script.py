from multi_time_series_connectedness import Volatility

if __name__ == "__main__":
    volatility = Volatility(n=2)
    volatility.calculate("2024-09-06T00:00:00+01:00", "2024-09-06T22:27:00+01:00", "docs/market_prices", "docs/volatilities.pickle")

