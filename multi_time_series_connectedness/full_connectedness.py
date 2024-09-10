import argparse
import functions.f_volatility as f_vol
import functions.coef as f_coef
import functions.connectedness as f_conn
from functions.load_data import get_file_names
import pandas as pd

def calculate_connectedness(volatilities):
    # get the variable names
    names = list(volatilities.columns[1:])
    
    # calculate estimated coefficients
    max_lag = 20
    coef = f_coef.Coef(volatilities.dropna(), max_lag)
    coef.f_ols_coef()
    ols_coef = coef.OLS_coef
    
    # accuracy
    accuracy = coef.accuracy
    print("Accuracy:", accuracy)
    ols_sigma = coef.OLS_sigma

    # calculate connectedness
    conn = f_conn.Connectedness(ols_coef, ols_sigma)
    conn.calculate_full_connectedness()
    conn.rename_table(names + ["all"])
    table = conn.full_connectedness
    return table
    # conn.table_restructure()

def main(path):
    volatilities = pd.read_pickle(path)
    connectedness_results = calculate_connectedness(volatilities)
    print("Connectedness Results:", connectedness_results)

if __name__ == "__main__":
    # specify the path
    parser = argparse.ArgumentParser(description="Process some financial data.")
    parser.add_argument('--path', type=str, help='Path to the data')

    args = parser.parse_args()
    main(args.path)