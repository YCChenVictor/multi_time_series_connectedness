import argparse
import functions.f_volatility as f_vol
import functions.coef as f_coef
import functions.f_connectedness as f_conn

def calculate_connectedness(start_at, end_at, files_path):
    # calculate volatility dataframe
    volatility = f_vol.volatility(files_path, start_at, end_at)
    volatility.price_data_to_volatility()
    volatilities = volatility.volatilities
    
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
    conn.f_full_connectedness()
    conn.rename_table(names)
    table = conn.full_connectedness
    print(table) # This is the result of connectedness!
    conn.table_restructure()

def main(start_at, end_at, files_path):
    connectedness_results = calculate_connectedness(start_at, end_at, files_path)
    print("Connectedness Results:", connectedness_results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some financial data.")
    parser.add_argument('--path', type=str, help='Path to the data')
    parser.add_argument('--start_at', type=str, help='Start Time')
    parser.add_argument('--end_at', type=str, help='End Time')

    args = parser.parse_args()
    main(args.start_at, args.end_at, args.path)