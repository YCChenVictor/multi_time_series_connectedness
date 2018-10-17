import os
import pickle

# load volatility dataframe and movement dataframe
file_path = os.path.dirname(os.path.realpath(__file__))
save_path = file_path + '/docs/' + 'roll_conn.pickle'

with open(save_path, 'rb') as f:
    result = pickle.load(f)

# turn the multiple connectedness dict into dataframe
