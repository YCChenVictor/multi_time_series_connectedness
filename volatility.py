# import modules
import functions.f_volatility as f_vol
import functions.f_load_data as f_load
import os
import pickle

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
print(volatility_dataframe)

# save the volatility_dataframe into pickle
file_path = os.path.dirname(os.path.realpath(__file__))
save_path = file_path + '/docs/' + 'volatility.pickle'
with open(save_path, 'wb') as f:
    pickle.dump(volatility_dataframe, f)
