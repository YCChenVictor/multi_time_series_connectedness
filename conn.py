"""
I also need to do more research about forceatlas

Noe doing table restrcturing
"""

# import modules
import functions.f_volatility as f_vol
import functions.f_coef as f_coef
import functions.f_connectedness as f_conn
import functions.f_load_data as f_load

# obtain the names, csv_files, path, start_dt, end_dt
names = f_load.names
csv_files = f_load.csv_files
path = f_load.path
start_dt = f_load.start_dt
end_dt = f_load.end_dt

# calculate volatility dataframe
volatility = f_vol.volatility(names, csv_files, path, start_dt, end_dt)
volatility.price_data_to_volatility()
volatility.periods_of_volatility()
volatility_dataframe = volatility.dataframe

# save name of the dataframe
names = list(volatility_dataframe.columns.values)
names.remove('Date')
names.append("all")

# calculate estimated coefficients
coef = f_coef.Coef(volatility_dataframe, 20)
coef.f_ols_coef()
ols_coef = coef.OLS_coef

# accuracy
accuracy = coef.accuracy

# calculate estimated sigma given coef we want
# lag = coef.Lag[0]
# sx = coef.x
# sy = coef.y
ols_sigma = coef.OLS_sigma


# calculate connectedness
conn = f_conn.Connectedness(ols_coef, ols_sigma)
conn.f_full_connectedness()
conn.rename_table(names)
table = conn.full_connectedness
conn.table_restructure()
