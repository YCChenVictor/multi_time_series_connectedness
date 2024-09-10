import pandas as pd
import datetime


def daterange(date1, date2):
    """
    :param date1: start date
    :param date2: end date
    :return: a list of date
    """
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + datetime.timedelta(n)


def date_format(date):
    list_date = date.split("-")
    year, month, day = list_date[0], list_date[1], list_date[2]
    return datetime.date(int(year), int(month), int(day))


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

    def __init__(self, csv_files, names, path, start_dt, end_dt):

        # the required variables
        self.csv_files = csv_files
        self.names = names
        self.path = path
        self.start_dt = date_format(start_dt)
        self.end_dt = date_format(end_dt)

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

    # obtain specify periods of volatility
    def periods_of_volatility(self):

        list_date = []

        for dt in daterange(self.start_dt, self.end_dt):
            list_date.append(dt.strftime("%Y-%m-%d"))

        # specify date here, create specified Date data
        dataframe = pd.DataFrame({'Date': list_date})

        dict_data = self.dict_data
        names = self.names

        for i in range(len(dict_data)):
            movement = dict_data[names[i]].iloc[:, [0, -1]]
            dataframe = dataframe.merge(movement, on='Date')

        self.dataframe = dataframe
