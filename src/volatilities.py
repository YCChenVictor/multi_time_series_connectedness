import os
import pickle
import argparse
import pandas as pd
import numpy as np

def load_files(directory, start_at, end_at):
    all_entries = os.listdir(directory)
    files = [entry for entry in all_entries if os.path.isfile(os.path.join(directory, entry))]
    datasets = {}
    for i in range(len(files)):
        datasets[files[i]] = wash_data(pd.read_csv(directory + '/' + files[i]), start_at, end_at)
    return datasets

def wash_data(dataset, start_at, end_at):
    data_subset = dataset.loc[
            (dataset["time"] >= start_at) & (dataset["time"] <= end_at)]
    washed_data = data_subset.interpolate()
    return washed_data

def yang_zhang_volatility(data, name, n=2):
    """
    :param data: a list with Open, High, Low, Close price
    :param n: the periods to obtain the average volatilitys
    :param clean: If clean, then delete the NA values
    :return: A list of volatility data
    """
    # define required variables
    o_c = (data['Open'] / data['Close'].shift(1)).apply(np.log)
    c_o = (data['Close'] / data['Open']).apply(np.log)
    h_o = (data['High'] / data['Open']).apply(np.log)
    l_o = (data['Low'] / data['Open']).apply(np.log)

    # overnight volatility
    vo = o_c.rolling(window=n).apply(np.var, raw=True)

    # today(open to close) volatility
    vt = c_o.rolling(window=n).apply(np.var, raw=True)

    # rogers-satchell volatility
    rs_fomula = h_o * (h_o - c_o) + l_o * (l_o - c_o)
    rs = rs_fomula.rolling(window=n, center=False).sum() * (1.0 / n)

    # super parameter
    k = 0.34 / (1 + (n + 1) / (n - 1))

    # yang-zhang
    result = (vo + k * vt + (1 - k) * rs).apply(np.sqrt)

    result_df = result.to_frame(name=name)

    return pd.concat([data['time'], result_df], axis=1)

def price_data_to_volatility(datasets):
    volatilities = None
    for key, value in datasets.items():
        volatility = yang_zhang_volatility(value, key)
        if volatilities is None:
            volatilities = volatility
        else:
            volatilities = volatilities.merge(volatility, on='time', how='outer')

    return volatilities

# python3 src/volatilities.py --path docs/market_prices --start_at 2024-09-06T00:00:00+01:00 --end_at 2024-09-06T22:27:00+01:00
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
