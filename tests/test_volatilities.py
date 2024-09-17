import unittest
from multi_time_series_connectedness.volatilities import calculate_volatility

class TestVolatilities(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_data'
        os.makedirs(self.test_dir, exist_ok=True)

#         ,time,symbol,Open,High,Low,Close
# 0,2024-09-06T00:00:00+01:00,AUDCAD=X,0.9097800254821777,0.9098600149154663,0.9097399711608887,0.9097599983215332
# 1,2024-09-06T00:01:00+01:00,AUDCAD=X,0.9097599983215332,0.909820020198822,0.9088900089263916,0.9097700119018555

# ,time,symbol,Open,High,Low,Close
# 0,2024-09-06T00:00:00+01:00,AUDCHF=X,0.5687500238418579,0.5688999891281128,0.5687500238418579,0.5688300132751465
# 1,2024-09-06T00:01:00+01:00,AUDCHF=X,0.5688599944114685,0.5688999891281128,0.5681700110435486,0.5688400268554688

        # Create fake CSV files
        data1 = {'column1': [1, 2, 3], 'column2': [4, 5, 6]}
        data2 = {'column1': [7, 8, 9], 'column2': [10, 11, 12]}

        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)

        df1.to_csv(os.path.join(self.test_dir, 'test1.csv'), index=False)
        df2.to_csv(os.path.join(self.test_dir, 'test2.csv'), index=False)

    def test_calculate_volatility(self):
        result = calculate_volatility(self.timeseries_data)

        expected_df = pd.DataFrame(expected_data, index=expected_index)
        # Compare the result with the expected DataFrame
        assert_frame_equal(result, expected_df)

if __name__ == "__main__":
    unittest.main(verbosity=2)
