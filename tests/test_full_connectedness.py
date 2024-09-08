import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from full_connectedness import calculate_connectedness


class TestFullConnectedness(unittest.TestCase):
    # To make sure it is correct, please calculate the connectedness by hand for once

    def setUp(self):
        # Data as a dictionary
        volatilities_data = {
            "time": [
                "2024-09-06T00:00:00+01:00",
                "2024-09-06T00:01:00+01:00",
                "2024-09-06T00:02:00+01:00",
                "2024-09-06T00:03:00+01:00",
                "2024-09-06T00:04:00+01:00",
                "2024-09-06T00:05:00+01:00",
                "2024-09-06T00:06:00+01:00",
                "2024-09-06T00:07:00+01:00",
                "2024-09-06T00:08:00+01:00",
                "2024-09-06T00:09:00+01:00",
                "2024-09-06T00:10:00+01:00",
                "2024-09-06T00:11:00+01:00",
                "2024-09-06T00:12:00+01:00",
                "2024-09-06T00:13:00+01:00",
                "2024-09-06T00:14:00+01:00",
                "2024-09-06T00:15:00+01:00",
                "2024-09-06T00:16:00+01:00",
                "2024-09-06T00:17:00+01:00",
                "2024-09-06T00:18:00+01:00",
                "2024-09-06T00:19:00+01:00",
                "2024-09-06T00:20:00+01:00",
                "2024-09-06T00:21:00+01:00",
                "2024-09-06T00:22:00+01:00",
                "2024-09-06T00:23:00+01:00",
                "2024-09-06T00:24:00+01:00",
                "2024-09-06T00:25:00+01:00",
                "2024-09-06T00:26:00+01:00",
                "2024-09-06T00:27:00+01:00",
                "2024-09-06T00:28:00+01:00",
                "2024-09-06T00:29:00+01:00",
                "2024-09-06T00:30:00+01:00",
            ],
            "AUDNZD=X.csv": [
                None,
                None,
                0.000235,
                0.000133,
                0.000267,
                0.000259,
                0.000110,
                0.000206,
                0.000194,
                0.000090,
                0.000257,
                0.000317,
                0.000120,
                0.000238,
                0.000238,
                0.000065,
                0.000250,
                0.000255,
                0.000080,
                0.000229,
                0.000219,
                0.000067,
                0.000266,
                0.000266,
                0.000059,
                0.000230,
                0.000231,
                0.000062,
                0.000265,
                0.000267,
                0.000058,
            ],
            "AUDCAD=X.csv": [
                None,
                None,
                0.000660,
                0.000116,
                0.000630,
                0.000631,
                0.000094,
                0.000625,
                0.000624,
                0.000090,
                0.000497,
                0.000545,
                0.000065,
                0.000656,
                0.000654,
                0.000070,
                0.000635,
                0.000633,
                0.000078,
                0.000633,
                0.000633,
                0.000076,
                0.000653,
                0.000651,
                0.000065,
                0.000646,
                0.000645,
                0.000041,
                0.000701,
                0.000703,
                0.000075,
            ],
            "AUDUSD=X.csv": [
                None,
                None,
                0.000141,
                0.000140,
                0.000130,
                0.000122,
                0.000134,
                0.000157,
                0.000149,
                0.000097,
                0.000074,
                0.000117,
                0.000145,
                0.000119,
                0.000100,
                0.000138,
                0.000123,
                0.000141,
                0.000133,
                0.000096,
                0.000091,
                0.000098,
                0.000137,
                0.000138,
                0.000117,
                0.000111,
                0.000105,
                0.000099,
                0.000149,
                0.000140,
                0.000130,
            ],
            "CADCHF=X.csv": [
                None,
                None,
                0.000699,
                0.000128,
                0.000721,
                0.000717,
                0.000137,
                0.000722,
                0.000719,
                0.000109,
                0.000561,
                0.000613,
                0.000102,
                0.000764,
                0.000760,
                0.000080,
                0.000621,
                0.000588,
                0.000110,
                0.000708,
                0.000711,
                0.000114,
                0.000754,
                0.000752,
                0.000082,
                0.000564,
                0.000565,
                0.000099,
                0.000764,
                0.000762,
                0.000121,
            ],
            "AUDCHF=X.csv": [
                None,
                None,
                0.000827,
                0.000217,
                0.000776,
                0.000775,
                0.000223,
                0.000628,
                0.000692,
                0.000159,
                0.000580,
                0.000615,
                0.000049,
                0.000799,
                0.000799,
                0.000065,
                0.000612,
                0.000625,
                0.000097,
                0.000689,
                0.000707,
                0.000118,
                0.000832,
                0.000831,
                0.000077,
                0.000793,
                0.000793,
                0.000071,
                0.000835,
                0.000835,
                0.000091,
            ],
            "CADJPY=X.csv": [
                None,
                None,
                0.000156,
                0.000080,
                0.000133,
                0.000205,
                0.000180,
                0.000151,
                0.000213,
                0.000190,
                0.000156,
                0.000146,
                0.000101,
                0.000177,
                0.000189,
                0.000110,
                0.000164,
                0.000189,
                0.000184,
                0.000225,
                0.000187,
                0.000092,
                0.000167,
                0.000175,
                0.000098,
                0.000142,
                0.000130,
                0.000061,
                0.000154,
                0.000157,
                0.000127,
            ],
            "AUDJPY=X.csv": [
                None,
                None,
                0.000160,
                0.000139,
                0.000095,
                0.000182,
                0.000211,
                0.000221,
                0.000243,
                0.000197,
                0.000122,
                0.000110,
                0.000115,
                0.000108,
                0.000130,
                0.000137,
                0.000124,
                0.000183,
                0.000208,
                0.000182,
                0.000152,
                0.000133,
                0.000127,
                0.000123,
                0.000116,
                0.000100,
                0.000089,
                0.000086,
                0.000114,
                0.000134,
                0.000120,
            ],
        }

        # Convert the dictionary to a DataFrame
        volatilities = pd.DataFrame(volatilities_data)
        # Load the data
        self.volatilities = volatilities

    def test_calculate_connectedness(self):
        result = calculate_connectedness(self.volatilities).round(6) # the accuracy is 6 decimal places
        
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
