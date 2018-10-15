"""
After the rolling connectedness is claculated, which predicts the connectedness
after five days. I cna use the connectedness to verify the stock movement.
First of all, get the movement. If close > open, movement is 1 and 0 vice
versa.
"""
import os
import json
import functions.f_predict_movement as f_p_move

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

# calculate movement
predict = f_p_move.predict_movement(csv_files, names, path)
predict.get_movements()
print(predict.dict_data)
"""
predict.get_movements()
print(predict.dict_data)
"""
