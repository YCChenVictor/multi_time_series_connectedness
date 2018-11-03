import os
import pickle
import functions.f_rolling_connectedness as f_roll

# load volatility_dataframe
file_path = os.path.dirname(os.path.realpath(__file__))
save_path = file_path + '/docs/' + 'volatility.pickle'
with open(save_path, 'rb') as f:
    volatility_dataframe = pickle.load(f)

# save name of the dataframe
names = list(volatility_dataframe.columns.values)
names.remove('Date')
names.append("all")

# start the rolling connectedness
roll_conn = (f_roll.
             Rolling_Connectedness(volatility_dataframe, 20, 80, names))
roll_conn.divide_dataframe()
roll_conn.calculate_rolling()

# obtain the rolling connectedness dataframe
data = roll_conn.rolling_connectedness

# save the volatility_dataframe into pickle
file_path = os.path.dirname(os.path.realpath(__file__))
save_path = file_path + '/docs/' + 'roll_conn.pickle'
with open(save_path, 'wb') as f:
    pickle.dump(data, f)
