"""
I should reveal the period of connectedness I am calculating, not just number.


"""
# import the required module
import functions.connectedness as f_conn
import functions.coef as coef
import pandas as pd
import datetime


class Rolling_Connectedness:

    def __init__(self, data, max_lag, data_periods, names):
        # to variable to run this module
        self.data = data
        self.names = names
        self.max_lag = max_lag
        self.data_periods = data_periods

        # save the calculated connectedness
        self.data_list = None
        self.rolling_connectedness = None
        self.accuracy_list = None

    def divide_dataframe(self):

        # required variables
        dataframe = self.data
        periods = self.data_periods

        # list to save the data
        data_list = []

        # iteratively divide dataframe
        for i in range(len(dataframe)):

            # get divided data
            data = dataframe.iloc[i: periods+i]
            if len(data) < periods:
                break

            # get the start and end date
            data = data.reset_index(drop=True)

            # add to data_list
            data_list.append(data)

        self.data_list = data_list

    def calculate_rolling(self):

        data_list = self.data_list
        max_lag = self.max_lag
        periods = self.data_periods
        names = self.names

        # create the list of the rolling dataframe
        connectedness_list = []
        date_list = []

        # index
        index = 0

        # start to calculate rolling
        # save_data = []

        for data in data_list:

            # get start and end date
            start_date = data["Date"][0]
            end_date = data["Date"][periods-1]
            period = start_date + " ~ " + end_date

            print("calculate connectedness for next period of %s, period: %s"
                  % (end_date, period))

            # coef and sigma_hat ####
            coef = coef.Coef(data, max_lag)
            coef.f_ols_coef()
            ols_coef = coef.OLS_coef
            ols_sigma = coef.OLS_sigma

            # accuracy
            accuracy = coef.accuracy

            # connectedness
            conn = f_conn.Connectedness(ols_coef, ols_sigma)
            conn.calculate_full_connectedness()
            conn.rename_table(names)
            conn.table_restructure()
            index += 1

            # return accuracy and restrcture_connectedness with period as row
            # name ##### add accuracy into dataframe
            rest = conn.restructure_connectedness
            rest["accuracy"] = accuracy

            # rename row name with the predict connectedness date
            date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            date = date + datetime.timedelta(days=1)
            date_list.append(date)

            # append into connectedness_list
            connectedness_list.append(rest)

            # combine them
            result = pd.concat(connectedness_list, ignore_index=True)

        # add date to the calculated dataframe
        result["Date"] = date_list

        # save rolling connectedness in class
        self.rolling_connectedness = result

    def plot_rolling():
        pass
