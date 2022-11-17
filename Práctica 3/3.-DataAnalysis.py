import pandas as pd
from tabulate import tabulate
from typing import Tuple, List


def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))


def analysis(file_name:str)->pd.DataFrame:
    df = pd.read_csv(file_name)
    df["percent from NA_Sales"] = df["NA_Sales"] * (100/df["Global_Sales"])
    df["percent from EU_Sales"] = df["EU_Sales"] * (100/df["Global_Sales"])
    print(sum(df["Global_Sales"]))
    return df

df = analysis("../csv/vgsales.csv")
print_tabulate(df.head())
print_tabulate(df.describe())
print(df["Global_Sales"].sum())