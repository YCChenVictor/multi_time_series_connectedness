# from functions import f_rolling_connectedness
import functions.f_volatility as f_vol
import functions.f_rolling_connectedness as f_roll
import os
import json

# get the data #####

# load Prerequisite
file_dir = os.path.dirname(os.path.abspath(__file__))
path = file_dir + '/docs/'
with open(path + 'Prerequisite.json') as f:
    prerequisite = json.load(f)


# varibales from prerequisite
target_folder = prerequisite["target_folder"]
start_dt = prerequisite["start_dt"]
end_dt = prerequisite["end_dt"]


# get all the names of the csv files
file_dir = os.path.dirname(os.path.abspath(__file__))
path = file_dir + '/docs/' + target_folder
for root, dirs, files in os.walk(path):
    csv_files = files


# specify all the names (this should be solve with json)
names = ["HK", "Japan", "Singapore", "China", "US", "UK", "Taiwan"]
if names is None:
    answer = input("whether to specify the names? y/N:")
    if answer == "y":
        print("please enter the list of the names matching the following csv" +
              "files")
        print(csv_files)
        names = input("input names:")
    else:
        names = csv_files


# calculate volatility dataframe
volatility = f_vol.volatility(names, csv_files, path, start_dt, end_dt)
volatility.price_data_to_volatility()
volatility.periods_of_volatility()
volatility_dataframe = volatility.dataframe

# start the rolling connectedness
roll_conn = (f_roll.
             Rolling_Connectedness(volatility_dataframe, 20, 300))
roll_conn.divide_dataframe()
roll_conn.calculate_rolling()
