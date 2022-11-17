#Function declaration


import pandas as pd
from tabulate import tabulate

#Code

#from file
df = pd.read_csv("./csv/vgsales.csv")
print(df)

df_LIMP = pd.DataFrame.from_dict(df.loc[:,['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales', 'EU_Sales', 'JP_Sales',
'Other_Sales', 'Global_Sales']])
print(df_LIMP)