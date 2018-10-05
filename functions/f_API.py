"""
# update the Prerequisite (i don't have time for this)
if data["target_folder"] == {}:
    print("please speficify the folder filled with csv files to calculate connectedness")
    data["target_folder"] = input("please input target folder:")

# input the target folder name in docs
target_folder = 'country_stock_csv'
if target_folder is None:
    target_folder = input("input target folder:")
else:
    pass

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
"""

# varibales from prerequisite
target_folder = prerequisite["target_folder"]
start_dt = prerequisite["start_dt"]
end_dt = prerequisite["end_dt"]
names = prerequisite["names"]

# obtain csv files from particular folder
file_dir = os.path.dirname(os.path.abspath(__file__))
path = file_dir + '/docs/' + target_folder
for root, dirs, files in os.walk(path):
    csv_files = files

# clear the names matching to csv_files
if names != {}:
    answer = input("Do you want to clear all the names of variable? y/N:")
    if answer == "y":
        prerequisite.pop('names', None)
        prerequisite["names"] = {}
    else:
        pass

# specify the names matching to csv_files
if names == {}:
    print("no specifying names of variables")
    answer = input("Do you want to specify names of variable? y/N:")
    if answer == "y":
        for csv_file in csv_files:
            name = input("please input the name of " + csv_file + ":")
            prerequisite["names"][csv_file] = name
    else:
        for csv_file in csv_files:
            prerequisite["names"][csv_file] = csv_file

# write the updaged json file
file_dir = os.path.dirname(os.path.abspath(__file__))
path = file_dir + '/docs/'
with open(path + 'Prerequisite.json', 'w') as f:
    json.dump(prerequisite, f)

print(prerequisite)