"""
After the estimated coefficient calculated, lets build the rolling connectedness
which is use the coefficient to iteratively calculate connectedness through time.

I got the recalculate the estimated sigma all over the time.
"""
# import the required module
from functions.f_connectedness import Connectedness
from functions.f_coef import Coef


class Rolling_Connectedness(Coef, Connectedness):

    def __init__(self, data, max_lag, data_periods):
        super(Coef, self).__init__(data, max_lag)
        self.data_periods = data_periods
        self.data_list = None

    def divide_dataframe(self, dataframe, periods):
        # list to save the data
        data_list = []

        # iteratively divide dataframe
        for i in range(len(dataframe)):
            print(i)
            data = dataframe.iloc[i: periods+i]
            data_list.append(data)

        self.data_list = data_list

    def obtain_coefficient(self, lag):
        self.lag = lag  # calculated from full_connectedness

    def calculate_rolling(self):
        # data_periods = self.data_periods
        lag = self.lag
        data = self.data

        # create the list of the rolling dataframe
        for i in range(1, lag):
            print(data)

    def get_specific_rolling_connectedness():
        pass

    def plot_rolling():
        pass
