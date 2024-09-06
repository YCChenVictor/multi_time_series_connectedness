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

## Feature
* calculate connectedness of all volatility
  ```
  python3 conn.py
  ```
* calculate volatility
  ```
  python3 volatility.py
  ```
* calculate rolling connectedness
  ```
  python3 roll_conn.py
  ```

## How to use?
* Put a folder with multiple Panel data into docs folder
* Run the commands in feature section

## Credits
http://financialconnectedness.org/

## License
MIT License