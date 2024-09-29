# python3 -m unittest tests/test_full_connectedness.py

import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from src.functions.connectedness import Connectedness
from tests.data_utils import get_volatilities_data
import src.functions.coef as f_coef

class TestFullConnectedness(unittest.TestCase):
    # To make sure it is correct, please calculate the connectedness by hand for once

    def setUp(self):
        self.volatilities = get_volatilities_data()
        coef = f_coef.Coef(self.volatilities.dropna(), 20)
        coef.f_ols_coef()
        ols_coef = coef.OLS_coef
        ols_sigma = coef.OLS_sigma
        self.connectedness = Connectedness(ols_coef, ols_sigma)

    def test_calculate_connectedness(self):
        result = self.connectedness.calculate_connectedness(self.volatilities).round(6) # the accuracy is 6 decimal places
        
        # Define the expected DataFrame
        expected_data = {
            "AUDNZD=X.csv": [0.514986, 0.129445, 0.001052, 0.174791, 0.036608, 0.010068, 0.035210, 0.387174],
            "AUDCAD=X.csv": [0.163375, 0.408033, 0.073418, 0.274542, 0.001427, 0.006138, 0.086044, 0.604944],
            "AUDUSD=X.csv": [0.001641, 0.090780, 0.329994, 0.051811, 0.231146, 0.161461, 0.244822, 0.781662],
            "CADCHF=X.csv": [0.206547, 0.257043, 0.039231, 0.435810, 0.012706, 0.000000, 0.037130, 0.552658],
            "AUDCHF=X.csv": [0.045964, 0.001420, 0.185970, 0.013501, 0.410156, 0.177960, 0.111078, 0.535893],
            "CADJPY=X.csv": [0.011966, 0.005780, 0.122970, 0.000000, 0.168461, 0.433284, 0.159115, 0.468293],
            "AUDJPY=X.csv": [0.055520, 0.107498, 0.247365, 0.049545, 0.139496, 0.211090, 0.326601, 0.810513],
            "all": [0.485014, 0.591967, 0.670006, 0.564190, 0.589844, 0.566716, 0.673399, 0.591591],
        }
        expected_index = [
            "AUDNZD=X.csv",
            "AUDCAD=X.csv",
            "AUDUSD=X.csv",
            "CADCHF=X.csv",
            "AUDCHF=X.csv",
            "CADJPY=X.csv",
            "AUDJPY=X.csv",
            "all",
        ]
        expected_df = pd.DataFrame(expected_data, index=expected_index)
        # Compare the result with the expected DataFrame
        assert_frame_equal(result, expected_df)


if __name__ == "__main__":
    unittest.main(verbosity=2)
