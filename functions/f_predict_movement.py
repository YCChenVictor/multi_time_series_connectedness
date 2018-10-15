import pandas as pd


def movement(dataframe):

    # list to save index
    index_list = []
    for index, row in dataframe.iterrows():

        Open = row['Open']
        Close = row['Close']

        if Close > Open:
            index = 1
        else:
            index = 0

        # list to save index
        index_list.append(index)

    # add new column of index to dataframe
    return index_list


class predict_movement():

    def __init__(self, csv_files, names, path):

        # the required variables
        self.csv_files = csv_files
        self.names = names
        self.path = path

        # calculated movement
        self.dict_data = None
        self.movement_dataframe = None

    def get_movements(self):

        csv_files = self.csv_files
        names = self.names

        dict_data = {}  # the dictionary
        for i in range(len(names)):
            dict_data[names[i]] = pd.read_csv(self.path + "/" + csv_files[i])

        # deal with the Non-data problem
        for i in range(len(dict_data)):
            dict_data[names[i]] = dict_data[names[i]].interpolate()

        # start to calculate movement
        for i in range(len(dict_data)):
            move_name = names[i] + '_move'
            dict_data[names[i]][move_name] = movement(dict_data[names[i]])

        self.dict_data = dict_data
