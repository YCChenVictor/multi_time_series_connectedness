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

import os
import json
import functions.about_path as about_path

# load Prerequisite
file_dir = os.path.dirname(os.path.abspath(__file__))
path = about_path.parent_path(file_dir, 1) + '/docs/'
with open(path + 'Prerequisite.json') as f:
    prerequisite = json.load(f)

# varibales from prerequisite
target_folder = prerequisite["target_folder"]
start_dt = prerequisite["start_dt"]
end_dt = prerequisite["end_dt"]
names = prerequisite["names"]

# get all the names of the csv files
file_dir = os.path.dirname(os.path.abspath(__file__))
path = about_path.parent_path(file_dir, 1) + '/docs/' + target_folder
for root, dirs, files in os.walk(path):
    csv_files = files

# specify all the names (this should be solve with json)
if prerequisite["names"] is None:
    answer = input("whether to specify the names? y/N:")
    if answer == "y":
        print("please enter the list of the names matching the following csv" +
              "files")
        print(csv_files)
        names = input("input names:")
    else:
        names = csv_files
