"""
I should reveal the period of connectedness I am calculating, not just number.


"""
# import the required module
import functions.f_connectedness as f_conn
import functions.f_coef as f_coef
import pickle
import os
import functions.about_path as f_about_path


class Rolling_Connectedness:

    def __init__(self, data, max_lag, data_periods):
        # to variable to run this module
        self.data = data
        self.name = list(data)
        self.max_lag = max_lag
        self.data_periods = data_periods

        # save the calculated connectedness
        self.data_list = None
        self.connectedness_list = None

    def divide_dataframe(self):

        # required variables
        dataframe = self.data
        periods = self.data_periods

        # list to save the data
        data_list = []

        # iteratively divide dataframe
        for i in range(len(dataframe)):
            data = dataframe.iloc[i: periods+i]
            data = data.reset_index(drop=True)
            if len(data) < periods:
                break
            data_list.append(data)

        self.data_list = data_list

    def calculate_rolling(self):

        data_list = self.data_list
        max_lag = self.max_lag

        # create the list of the rolling dataframe
        connectedness_list = []
        accuracy_list = []

        # index
        index = 0

        # start to calculate rolling
        for data in data_list:

            print("calculating rolling, period: %s" % index)
            # coef and sigma_hat ####
            coef = f_coef.Coef(data, max_lag)
            coef.f_ols_coef()
            ols_coef = coef.OLS_coef
            ols_sigma = coef.OLS_sigma

            # accuracy
            accuracy = coef.accuracy
            accuracy_list.append(accuracy)

            # connectedness
            conn = f_conn.Connectedness(ols_coef, ols_sigma)
            conn.f_full_connectedness()
            connectedness_list.append(conn.full_connectedness)
            index += 1

        # save rolling connectedness in class
        self.connectedness_list = connectedness_list

        # save rolling connectedness in pickle
        current_path = os.path.dirname(os.path.realpath(__file__))
        file_path = f_about_path.parent_path(current_path, 1)
        save_path = file_path + '/docs/' + 'roll_conn.pickle'
        with open(save_path, 'wb') as f:
            pickle.dump(connectedness_list, f)

    def rolling_to_panel(self):

        # read connectedness in pickle if there is nothing in roll_conn
        current_path = os.path.dirname(os.path.realpath(__file__))
        file_path = f_about_path.parent_path(current_path, 2)
        save_path = file_path + '/docs/' + 'roll_conn.pickle'
        with open(save_path, 'rb') as f:
            result = pickle.load(f)

        # restructure it
        return result

    def plot_rolling():
        pass
