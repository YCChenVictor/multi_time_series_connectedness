import pickle
import argparse
from multi_time_series_connectedness.functions.data_processor import load_files
from multi_time_series_connectedness.functions.volatilities import price_data_to_volatility

# python3 volatilities.py --path docs/market_prices --start_at 2024-09-06T00:00:00+01:00 --end_at 2024-09-06T22:27:00+01:00
def main(start_at, end_at, directory, save_path=None):
    datasets = load_files(directory, start_at, end_at)
    volatilities = price_data_to_volatility(datasets)

    if save_path:
        with open(save_path, 'wb') as f:
            pickle.dump(volatilities, f)
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some timeseries data with open, close, high, low.")
    parser.add_argument('--path', type=str, help='Path to the data')
    parser.add_argument('--start_at', type=str, help='Start Time')
    parser.add_argument('--end_at', type=str, help='End Time')

    args = parser.parse_args()
    main(args.start_at, args.end_at, args.path)
