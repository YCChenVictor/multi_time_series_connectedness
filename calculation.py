"""
I think there is no need for inputting csv file name and path. Needs more
modification.
"""

# import modules
import functions.f_volatility as f_vol


# variables
names = ["US", "UK", "Singapore", "HK", "Taiwan", "Japan", "china"]
csv_files = ["^GSPC.csv", "^FTSE.csv", "^STI.csv", "^HSI.csv", "^TWII.csv",
             "^N225.csv", "000001.SS.csv"]
path = ("/Users/rucachen/projects/MultiTimeSeries_Connectedness/docs/" +
        "country_stock_csv")
start_dt = "1998-09-01"
end_dt = "2018-01-01"


# calculate volatility dataframe
volatility = f_vol.volatility(names, csv_files, path, start_dt, end_dt)
volatility.price_data_to_volatility()
volatility.periods_of_volatility()
volatility_dataframe = volatility.dataframe

# 