# python3 -m unittest tests/test_full_connectedness.py

import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from multi_time_series_connectedness.connectedness import Connectedness
from tests.data_utils import get_volatilities_data
import multi_time_series_connectedness.coef as f_coef

class TestFullConnectedness(unittest.TestCase):
    def setUp(self):
        volatilities = get_volatilities_data()
        forecast_period = 1
        max_lag = 2
        self.connectedness = Connectedness(volatilities.dropna(), max_lag, forecast_period)

    def test_calculate_connectedness(self):
        result = self.connectedness.calculate().round(6) # the accuracy is 6 decimal places

        # Define the expected DataFrame
        expected_data = {
            "AUDNZD=X.csv": [0.444193, 0.369727, 0.203802, 0.573529],
            "AUDCAD=X.csv": [0.386958, 0.424414, 0.260054, 0.647012],
            "AUDUSD=X.csv": [0.168849, 0.205860, 0.536144, 0.374709],
            "from_other": [0.555807, 0.575586, 0.463856, 0.531750],
        }
        expected_index = [
            "AUDNZD=X.csv",
            "AUDCAD=X.csv",
            "AUDUSD=X.csv",
            "to_other",
        ]
        expected_df = pd.DataFrame(expected_data, index=expected_index)
        # Compare the result with the expected DataFrame
        assert_frame_equal(result, expected_df)


if __name__ == "__main__":
    unittest.main(verbosity=2)
