# python3 -m unittest tests/test_rolling_connectedness.py

import unittest
from unittest.mock import Mock
from multi_time_series_connectedness.rolling_connectedness import RollingConnectedness
from tests.data_utils import get_volatilities_data
import pandas as pd
import numpy as np


class TestRollingConnectedness(unittest.TestCase):
    # def setUp(self):

    def test_divide_timeseries_volatilities(self):
        pass

    def test_calculate_rolling(self):
        mock_volatilities_data = get_volatilities_data()
        roll_conn = RollingConnectedness(
            mock_volatilities_data,
            1,
            29,
        )
        roll_conn.data = get_volatilities_data().dropna()
        roll_conn.calculate()

        # Define the expected DataFrame
        expected_column_names = [
            "AUDNZD=X.csv_to_AUDNZD=X.csv",
            "AUDNZD=X.csv_to_AUDCAD=X.csv",
            "AUDNZD=X.csv_to_AUDUSD=X.csv",
            "AUDNZD=X.csv_to_to_other",
            "AUDCAD=X.csv_to_AUDNZD=X.csv",
            "AUDCAD=X.csv_to_AUDCAD=X.csv",
            "AUDCAD=X.csv_to_AUDUSD=X.csv",
            "AUDCAD=X.csv_to_to_other",
            "AUDUSD=X.csv_to_AUDNZD=X.csv",
            "AUDUSD=X.csv_to_AUDCAD=X.csv",
            "AUDUSD=X.csv_to_AUDUSD=X.csv",
            "AUDUSD=X.csv_to_to_other",
            "from_other_to_AUDNZD=X.csv",
            "from_other_to_AUDCAD=X.csv",
            "from_other_to_AUDUSD=X.csv",
            "from_other_to_to_other",
            "start_at",
            "end_at",
            "forecast_period",
        ]
        expected_values = [
          0.507183, 0.45722, 0.068288, 0.525509, 0.453369, 0.511491, 0.053709, 0.507078, 
          0.039447, 0.031289, 0.878003, 0.070736, 0.492817, 0.488509, 0.121997, 0.367774, 
          1729210980, 1729212660, 1
        ]

        result = roll_conn.rolling_connectedness
        result = result.drop(columns=['forecast_at'])

        assert result.columns.tolist() == expected_column_names
        assert [round(value, 6) for value in result.iloc[0].tolist()] == expected_values

    def test_with_callback(self):
        mock_volatilities_data = get_volatilities_data()
        roll_conn = RollingConnectedness(
            mock_volatilities_data,
            1,
            29,
        )
        roll_conn.data = get_volatilities_data().dropna()

        def callback(restructured_connectedness):
            print("Callback called with:", restructured_connectedness)
        callback_mock = Mock(side_effect=callback)
        roll_conn.calculate(callback_after_one_connectedness=callback_mock)
        self.assertEqual(callback_mock.call_count, 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
