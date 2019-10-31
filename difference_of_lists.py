import pandas as pd
from pandas.errors import EmptyDataError
import csv
import os
import sys
import glob

def main():
"""This is a Set difference comparison to find values in list1 not in list2"""
    df = []
    missing_list = []

    print("please setup the CSV file with the first column as the dataset "
          "you want to find values missing from the data set in the second column\n")

    while not df:
        try:

            file = input(f"What CSV file would you like to open: {glob.glob('./*.csv')}")
            df = pd.read_csv(file)
            break

        except FileNotFoundError and EmptyDataError and ValueError:
            print(f"File {file} is incompatible or spelled incorrect, Please load a valid csv\n")

    list2 = df['col_2'].unique()

    for value in df['col_1'].tolist():
        if value not in list2:
            missing_list.append(str(value))

    missing_df = pd.DataFrame(missing_list, columns=['missing_values'])
    missing_df.to_csv(f"{os.getcwd()}/missing_values.csv", index=None)


main()
