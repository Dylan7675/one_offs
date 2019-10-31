import pandas as pd
from pandas.errors import EmptyDataError
import csv
import os
import sys
import glob

def main():

    df = []
    dupe_list = []

    print("please setup the CSV file with the first column as the dataset "
          "you want to find values missing from the data set in the second column\n")

    while not df:
        try:

            file = input(f"What CSV file would you like to open: {glob.glob('*.csv')}")
            df = pd.read_csv(file)
            break

        except FileNotFoundError and EmptyDataError and ValueError:
            print(f"File {file} is incompatible or spelled incorrect, Please load a valid csv\n")

    dupe_df = df[df.duplicated(['Device SN'],False)]

    print(dupe_df)
    dupe_df.to_csv(f"{os.getcwd()}/dupe_assets.csv", index=None)

main()
