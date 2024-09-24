"""
I should reveal the period of connectedness I am calculating, not just number.


"""
# import the required module
import src.functions.connectedness as f_conn
import src.functions.coef as f_coef
import pandas as pd

class Rolling_Connectedness:

    def __init__(self, data, max_lag, data_periods):
        # to variable to run this module
        self.data = data
        self.max_lag = max_lag
        self.data_periods = data_periods
        self.name = [col for col in data.columns if col != 'time'] + ['all']

        # save the calculated connectedness
        self.data_list = None
        self.rolling_connectedness = None
        self.accuracy_list = None

    def divide_timeseries_volatilities(self):
        dataframe = self.data
        periods = self.data_periods

        data_list = []

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

    def calculate_rolling(self, callback_after_one_connectedness=None):
        connectedness_list = []
        for data in self.data_list:
            start_date = data["time"].iloc[0]
            end_date = data["time"].iloc[self.data_periods-1]
            period = start_date + " ~ " + end_date
            print("calculate connectedness for next period of %s, period: %s"
                  % (end_date, period))

            coef = f_coef.Coef(data, self.max_lag)
            coef.f_ols_coef()
            ols_coef = coef.OLS_coef
            ols_sigma = coef.OLS_sigma

            accuracy = coef.accuracy

            conn = f_conn.Connectedness(ols_coef, ols_sigma)
            conn.calculate_full_connectedness()
            conn.rename_table(self.name)
            conn.flatten_connectedness()

            restructured_connectedness = conn.restructure_connectedness
            restructured_connectedness["accuracy"] = accuracy
            if callback_after_one_connectedness:
                callback_after_one_connectedness(restructured_connectedness)
            connectedness_list.append(restructured_connectedness)

            restructured_connectedness_timeseries = pd.concat(connectedness_list, ignore_index=True)

        self.rolling_connectedness = restructured_connectedness_timeseries

    def plot_rolling():
        pass
