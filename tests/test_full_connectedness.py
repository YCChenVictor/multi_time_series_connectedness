import unittest
import pandas as pd
from full_connectedness import calculate_connectedness

class TestConn(unittest.TestCase):

    def test_calculate_connectedness(self):
        print("testing!")
        volatility_dataframe, ols_coef, accuracy = calculate_connectedness(
            self.names, self.csv_files, self.path, self.start_dt, self.end_dt
        )
        self.assertIsInstance(volatility_dataframe, pd.DataFrame)
        self.assertIn('sample1', volatility_dataframe.columns)
        self.assertIn('sample2', volatility_dataframe.columns)
        self.assertIsNotNone(ols_coef)
        self.assertIsNotNone(accuracy)

if __name__ == '__main__':
    unittest.main(verbosity=2)
