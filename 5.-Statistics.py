import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.read_csv("./csv/vgsales.csv")


df_LIMP = pd.DataFrame.from_dict(df.loc[:,['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales', 'EU_Sales', 'JP_Sales',
'Other_Sales', 'Global_Sales']])
print(df_LIMP)


fig = go.Figure()
fig.add_trace(go.Box(y=df_LIMP.Name.loc[df_LIMP.Global_Sales=='NA_Sales'],name="Ventas"))
fig.add_trace(go.Box(x=df_LIMP.Year,name="Año"))
fig.update_layout(
    title={
        'text': "Ventas por año",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.show()