import unittest
import pandas as pd
from full_connectedness import calculate_volatility

class TestConn(unittest.TestCase):

    def setUp(self):
        # Sample data
        self.names = ['sample1', 'sample2']
        self.csv_files = ['sample_data/sample1.csv', 'sample_data/sample2.csv']
        self.path = 'sample_data/'
        self.start_dt = '2020-01-01'
        self.end_dt = '2021-01-01'

        # Create sample CSV files
        data1 = {
            'Date': pd.date_range(start='1/1/2020', periods=5),
            'sample1': [1, 2, 3, 4, 5]
        }
        data2 = {
            'Date': pd.date_range(start='1/1/2020', periods=5),
            'sample2': [5, 4, 3, 2, 1]
        }
        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)
        df1.to_csv(self.csv_files[0], index=False)
        df2.to_csv(self.csv_files[1], index=False)

    def test_calculate_volatility(self):
        volatility_dataframe, ols_coef, accuracy = calculate_volatility(
            self.names, self.csv_files, self.path, self.start_dt, self.end_dt
        )

        # Assertions
        self.assertIsInstance(volatility_dataframe, pd.DataFrame)
        self.assertIn('sample1', volatility_dataframe.columns)
        self.assertIn('sample2', volatility_dataframe.columns)
        self.assertIsNotNone(ols_coef)
        self.assertIsNotNone(accuracy)

if __name__ == '__main__':
    unittest.main(verbosity=2)
