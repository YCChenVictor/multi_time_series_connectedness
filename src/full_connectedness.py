import argparse
from src.functions import connectedness as f_conn
import pandas as pd

def main(path):
    volatilities = pd.read_pickle(path)
    connectedness_results = f_conn.Connectedness.calculate_connectedness(volatilities)
    print("Connectedness Results:", connectedness_results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some financial data.")
    parser.add_argument('--path', type=str, help='Path to the volatilities pickle file')

    args = parser.parse_args()
    main(args.path)