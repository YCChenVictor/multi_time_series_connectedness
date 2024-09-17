import unittest
from unittest.mock import Mock
import multi_time_series_connectedness.functions.f_rolling_connectedness as f_roll
from tests.data_utils import get_volatilities_data
import pandas as pd
import numpy as np


class TestRollingConnectedness(unittest.TestCase):
    # def setUp(self):

    def test_divide_timeseries_volatilities(self):
        pass

    def test_calculate_rolling(self):
        mock_volatilities_data = get_volatilities_data()
        roll_conn = f_roll.Rolling_Connectedness(
            pd.DataFrame(
                columns=[
                    "AUDNZD=X.csv",
                    "AUDCAD=X.csv",
                    "AUDUSD=X.csv",
                    "CADCHF=X.csv",
                    "AUDCHF=X.csv",
                    "CADJPY=X.csv",
                    "AUDJPY=X.csv",
                ]
            ),
            20,
            len(mock_volatilities_data.dropna()),
        )
        roll_conn.data_list = [
            get_volatilities_data().dropna(),
            get_volatilities_data().dropna(),
        ]
        roll_conn.calculate_rolling()

        # Define the expected DataFrame
        expected_column_names = ["AUDNZD=X.csv_->_AUDNZD=X.csv", "AUDNZD=X.csv_->_AUDCAD=X.csv", "AUDNZD=X.csv_->_AUDUSD=X.csv", "AUDNZD=X.csv_->_CADCHF=X.csv", "AUDNZD=X.csv_->_AUDCHF=X.csv", "AUDNZD=X.csv_->_CADJPY=X.csv", "AUDNZD=X.csv_->_AUDJPY=X.csv", "AUDNZD=X.csv_->_all", "AUDCAD=X.csv_->_AUDNZD=X.csv", "AUDCAD=X.csv_->_AUDCAD=X.csv", "AUDCAD=X.csv_->_AUDUSD=X.csv", "AUDCAD=X.csv_->_CADCHF=X.csv", "AUDCAD=X.csv_->_AUDCHF=X.csv", "AUDCAD=X.csv_->_CADJPY=X.csv", "AUDCAD=X.csv_->_AUDJPY=X.csv", "AUDCAD=X.csv_->_all", "AUDUSD=X.csv_->_AUDNZD=X.csv", "AUDUSD=X.csv_->_AUDCAD=X.csv", "AUDUSD=X.csv_->_AUDUSD=X.csv", "AUDUSD=X.csv_->_CADCHF=X.csv", "AUDUSD=X.csv_->_AUDCHF=X.csv", "AUDUSD=X.csv_->_CADJPY=X.csv", "AUDUSD=X.csv_->_AUDJPY=X.csv", "AUDUSD=X.csv_->_all", "CADCHF=X.csv_->_AUDNZD=X.csv", "CADCHF=X.csv_->_AUDCAD=X.csv", "CADCHF=X.csv_->_AUDUSD=X.csv", "CADCHF=X.csv_->_CADCHF=X.csv", "CADCHF=X.csv_->_AUDCHF=X.csv", "CADCHF=X.csv_->_CADJPY=X.csv", "CADCHF=X.csv_->_AUDJPY=X.csv", "CADCHF=X.csv_->_all", "AUDCHF=X.csv_->_AUDNZD=X.csv", "AUDCHF=X.csv_->_AUDCAD=X.csv", "AUDCHF=X.csv_->_AUDUSD=X.csv", "AUDCHF=X.csv_->_CADCHF=X.csv", "AUDCHF=X.csv_->_AUDCHF=X.csv", "AUDCHF=X.csv_->_CADJPY=X.csv", "AUDCHF=X.csv_->_AUDJPY=X.csv", "AUDCHF=X.csv_->_all", "CADJPY=X.csv_->_AUDNZD=X.csv", "CADJPY=X.csv_->_AUDCAD=X.csv", "CADJPY=X.csv_->_AUDUSD=X.csv", "CADJPY=X.csv_->_CADCHF=X.csv", "CADJPY=X.csv_->_AUDCHF=X.csv", "CADJPY=X.csv_->_CADJPY=X.csv", "CADJPY=X.csv_->_AUDJPY=X.csv", "CADJPY=X.csv_->_all", "AUDJPY=X.csv_->_AUDNZD=X.csv", "AUDJPY=X.csv_->_AUDCAD=X.csv", "AUDJPY=X.csv_->_AUDUSD=X.csv", "AUDJPY=X.csv_->_CADCHF=X.csv", "AUDJPY=X.csv_->_AUDCHF=X.csv", "AUDJPY=X.csv_->_CADJPY=X.csv", "AUDJPY=X.csv_->_AUDJPY=X.csv", "AUDJPY=X.csv_->_all", "all_->_AUDNZD=X.csv", "all_->_AUDCAD=X.csv", "all_->_AUDUSD=X.csv", "all_->_CADCHF=X.csv", "all_->_AUDCHF=X.csv", "all_->_CADJPY=X.csv", "all_->_AUDJPY=X.csv", "all_->_all", "accuracy"]
        expected_values = [
          0.514986, 0.129445, 0.001052, 0.174791, 0.036608, 0.010068, 0.03521, 0.387174, 0.163375, 0.408033, 0.073418, 0.274542, 0.001427, 0.006138, 0.086044, 0.604944, 0.001641, 0.09078, 0.329994, 0.051811, 0.231146, 0.161461, 0.244822, 0.781662, 0.206547, 0.257043, 0.039231, 0.43581, 0.012706, 0.0, 0.03713, 0.552658, 0.045964, 0.00142, 0.18597, 0.013501, 0.410156, 0.17796, 0.111078, 0.535893, 0.011966, 0.00578, 0.12297, 0.0, 0.168461, 0.433284, 0.159115, 0.468293, 0.05552, 0.107498, 0.247365, 0.049545, 0.139496, 0.21109, 0.326601, 0.810513, 0.485014, 0.591967, 0.670006, 0.56419, 0.589844, 0.566716, 0.673399, 0.591591, 1.0
        ]

        result = roll_conn.rolling_connectedness
        assert result.shape[0] == 2
        assert result.columns.tolist() == expected_column_names
        assert list(np.round(result.iloc[0].values, 6)) == expected_values

    def test_with_callback(self):
        roll_conn = f_roll.Rolling_Connectedness(
            pd.DataFrame(
                columns=[
                    "AUDNZD=X.csv",
                    "AUDCAD=X.csv",
                    "AUDUSD=X.csv",
                    "CADCHF=X.csv",
                    "AUDCHF=X.csv",
                    "CADJPY=X.csv",
                    "AUDJPY=X.csv",
                ]
            ),
            20,
            2,
        )
        roll_conn.data_list = [
            get_volatilities_data().dropna(),
            get_volatilities_data().dropna(),
        ]

        def callback(restructured_connectedness):
            print("Callback called with:", restructured_connectedness)
        callback_mock = Mock(side_effect=callback)
        roll_conn.calculate_rolling(callback_after_one_connectedness=callback_mock)
        self.assertEqual(callback_mock.call_count, 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
