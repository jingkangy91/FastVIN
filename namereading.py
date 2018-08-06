import pandas as pd
import os

def read_name():
    list_name = input(
        "Please input VIN list filename in 'list' dir " +
        "(default 'vin_list.csv'):\n"
    )
    if list_name == '':
        # list_name = 'vin_list.csv'
        list_name = 'vin_list_test.csv'
    df = pd.read_csv(os.path.join('list', list_name))
    df.dropna(inplace=True)

    return df, list_name

if __name__ == "__main__":
    read_name()