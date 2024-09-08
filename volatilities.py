# import modules
import functions.f_volatility as f_vol
import os
import pickle
import argparse

def main(start_at, end_at, files_path):
    # calculate volatility dataframe
    volatility = f_vol.volatility(files_path, start_at, end_at)
    volatility.price_data_to_volatility()
    volatilities = volatility.volatilities

    # save the volatility_dataframe into pickle
    file_path = os.path.dirname(os.path.realpath(__file__))
    save_path = file_path + '/docs/' + 'volatilities.pickle'
    with open(save_path, 'wb') as f:
        pickle.dump(volatilities, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some financial data.")
    parser.add_argument('--path', type=str, help='Path to the data')
    parser.add_argument('--start_at', type=str, help='Start Time')
    parser.add_argument('--end_at', type=str, help='End Time')

    args = parser.parse_args()
    main(args.start_at, args.end_at, args.path)
