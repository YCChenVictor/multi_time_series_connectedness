## Project title
Multi Time Series Connectedness

## Motivation
This project is motivated by Financial and Macroeconomics Connectedness created by Diebold and Ylimaz. I want to use this algorithm not only in finance and macroeconomics area but other area, so I start to build this project.

## Installation
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Feature & Example Code
* calculate connectedness of all volatility
  ```
  python3 conn.py
  ```
* calculate volatility
  ```
  python3 volatility.py
  ```

### calculate rolling connectedness

```python
import os
import pickle
import src.functions.f_rolling_connectedness as f_roll

# load volatility_dataframe
file_path = os.path.dirname(os.path.realpath(__file__))
save_path = file_path + '/docs/' + 'volatilities.pickle'
with open(save_path, 'rb') as f:
    volatilities = pickle.load(f)

# start the rolling connectedness
roll_conn = f_roll.Rolling_Connectedness(volatilities.dropna(), 20, 80)
roll_conn.divide_timeseries_volatilities()
roll_conn.calculate_rolling()

# obtain the rolling connectedness dataframe
data = roll_conn.rolling_connectedness
print(data)

# save the volatility_dataframe into pickle
file_path = os.path.dirname(os.path.realpath(__file__))
save_path = file_path + '/docs/' + 'roll_conn.pickle'
with open(save_path, 'wb') as f:
    pickle.dump(data, f)
```

## How to use?
* Put a folder with multiple Panel data into docs folder
* Run the commands in feature section

## Credits
http://financialconnectedness.org/

## License
MIT License