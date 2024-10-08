import argparse
import pandas as pd
from multi_time_series_connectedness.functions import connectedness as f_conn
import multi_time_series_connectedness.functions.coef as f_coef

def main(path):
    volatilities = pd.read_pickle(path)
    coef = f_coef.Coef(volatilities.dropna(), 20)
    coef.f_ols_coef()
    ols_coef = coef.OLS_coef
    ols_sigma = coef.OLS_sigma
    conn = f_conn.Connectedness(ols_coef, ols_sigma)
    connectedness_results = conn.calculate_connectedness(volatilities)
    print("Connectedness Results:", connectedness_results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some financial data.")
    parser.add_argument('--path', type=str, help='Path to the volatilities pickle file')

    args = parser.parse_args()
    main(args.path)
