import os
import pickle
import src.functions.rolling_connectedness as f_roll

# load volatility_dataframe
file_path = os.path.dirname(os.path.realpath(__file__))
save_path = file_path + '/docs/' + 'volatilities.pickle'
with open(save_path, 'rb') as f:
    volatilities = pickle.load(f)

# start the rolling connectedness
roll_conn = f_roll.Rolling_Connectedness(volatilities.dropna(), 20, 80)
roll_conn.divide_timeseries_volatilities()
roll_conn.calculate_rolling()

# obtain the rolling connectedness dataframe
data = roll_conn.rolling_connectedness
print(data)

# save the volatility_dataframe into pickle
file_path = os.path.dirname(os.path.realpath(__file__))
save_path = file_path + '/docs/' + 'roll_conn.pickle'
with open(save_path, 'wb') as f:
    pickle.dump(data, f)
