"""
I think there is no need for specifying csv file name and path. Needs more
modification. => I am working to make a json file to store these information

I also need to check whether the names match csv_files

I also need to do more research about forceatlas

The next step is to claculate rolling connectedness
"""

# import modules
import json
import functions.f_volatility as f_vol
import functions.f_coef as f_coef
import functions.f_connectedness as f_conn
import functions.f_network as f_net
import os
import glob

# load Prerequisite
file_dir = os.path.dirname(os.path.abspath(__file__))
path = file_dir + '/docs/'
os.chdir(path)
with open('Prerequisite.json') as f:
    data = json.load(f)

# update the Prerequisite
if data["target_folder"] == {}:
    print("please speficify the folder filled with csv files to calculate connectedness")
    data["target_folder"] = input("please input target folder:")


"""
# input variables
input

# input the target folder name in docs
target_folder = 'country_stock_csv'
if target_folder is None:
    target_folder = input("input target folder:")
else:
    pass


# obtain csv files from particular folder
file_dir = os.path.dirname(os.path.abspath(__file__))
path = file_dir + '/docs/' + target_folder
os.chdir(path)
csv_files = glob.glob('**.csv')


# setup the names of the variables
names = input("input the names of the volatility variables:")
names = ["US", "UK", "Singapore", "HK", "Taiwan", "Japan", "china"]
if names is None:
    names = csv_files
else:
    pass

# variables for volatility
start_dt = input("input the start date for volatility dataframe:")
end_dt = input("input the end data for volatility dataframe:")
start_dt = "1998-09-01"
end_dt = "2018-01-01"
"""

"""
# calculate volatility dataframe
volatility = f_vol.volatility(names, csv_files, path, start_dt, end_dt)
volatility.price_data_to_volatility()
volatility.periods_of_volatility()
volatility_dataframe = volatility.dataframe

# save name of the dataframe
names = list(volatility_dataframe.columns.values)
names.remove('Date')

# calculate estimated coefficients
coef = f_coef.Coef(volatility_dataframe, 20)
coef.f_ols_coef()
ols_coef = coef.OLS_coef

# accuracy
accuracy = coef.accuracy

# calculate estimated sigma given coef we want
lag = coef.Lag[0]
sx = coef.x
sy = coef.y
ols_sigma = coef.OLS_sigma

# calculate connectedness
conn = f_conn.Connectedness(ols_coef, ols_sigma)
conn.f_full_connectedness()
table = conn.full_connectedness


# construct network plot
network = f_net.Create_Network(table)
network.change_names(names)
network.create_network()
network.plot()
network.show_draw()
"""