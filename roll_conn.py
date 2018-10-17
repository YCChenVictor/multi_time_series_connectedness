import os
import pickle
import functions.f_load_data as f_load
import functions.f_rolling_connectedness as f_roll

# load volatility_dataframe
file_path = os.path.dirname(os.path.realpath(__file__))
save_path = file_path + '/docs/' + 'volatility.pickle'
with open(save_path, 'rb') as f:
    volatility_dataframe = pickle.load(f)

# obtain the names, csv_files, path, start_dt, end_dt
names = f_load.names
csv_files = f_load.csv_files
path = f_load.path
start_dt = f_load.start_dt
end_dt = f_load.end_dt

# start the rolling connectedness
roll_conn = (f_roll.
             Rolling_Connectedness(volatility_dataframe, 20, 80))
roll_conn.divide_dataframe()
roll_conn.calculate_rolling()
# it will save the calculated dict into roll_conn,pickle
