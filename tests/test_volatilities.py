# python3 -m unittest tests/test_volatilities.py

import unittest
import pandas as pd
import numpy as np
from io import StringIO
from multi_time_series_connectedness.volatility import Volatility
from pandas.testing import assert_frame_equal

class TestVolatilities(unittest.TestCase):
    def setUp(self):
        data_audcad = """
        Unnamed: 0,time,symbol,Open,High,Low,Close
        0,2024-09-06T00:00:00+01:00,AUDCAD=X,0.9097800254821777,0.9098600149154663,0.9097399711608887,0.9097599983215332
        1,2024-09-06T00:01:00+01:00,AUDCAD=X,0.9097599983215332,0.909820020198822,0.9088900089263916,0.9097700119018555
        2,2024-09-06T00:02:00+01:00,AUDCAD=X,0.9097200036048889,0.9099000096321106,0.9096599817276001,0.9098899960517883
        3,2024-09-06T00:03:00+01:00,AUDCAD=X,0.909850001335144,0.9099100232124329,0.9097899794578552,0.9098399877548218
        """
        data_audchf = """
        Unnamed: 0,time,symbol,Open,High,Low,Close
        0,2024-09-06T00:00:00+01:00,AUDCHF=X,0.6707800254821777,0.6708600149154663,0.6707399711608887,0.6707599983215332
        1,2024-09-06T00:01:00+01:00,AUDCHF=X,0.6707599983215332,0.670820020198822,0.6698900089263916,0.6707700119018555
        2,2024-09-06T00:02:00+01:00,AUDCHF=X,0.5687999725341797,0.5689399838447571,0.5687400102615356,0.5688999891281128
        3,2024-09-06T00:03:00+01:00,AUDCHF=X,0.568880021572113,0.5690000057220459,0.5688199996948242,0.5688899755477905
        """

        df_audcad = pd.read_csv(StringIO(data_audcad), index_col=0)
        df_audchf = pd.read_csv(StringIO(data_audchf), index_col=0)

        self.timeseries_data = {
            'AUDCAD=X': df_audcad,
            'AUDCHF=X': df_audchf
        }

    def test_calculate_volatility(self):
        calculator = Volatility(n=2)
        result = calculator.price_data_to_volatility(self.timeseries_data)

        data = {
            'time': [
                '2024-09-06T00:00:00+01:00',
                '2024-09-06T00:01:00+01:00',
                '2024-09-06T00:02:00+01:00',
                '2024-09-06T00:03:00+01:00'
            ],
            'AUDCAD=X': [np.nan, np.nan, 0.000660, 0.000116],
            'AUDCHF=X': [np.nan, np.nan, 0.082454, 0.082431]
        }
        expected_df = pd.DataFrame(data)
        assert_frame_equal(result.round(6), expected_df.round(6))

if __name__ == "__main__":
    unittest.main(verbosity=2)
