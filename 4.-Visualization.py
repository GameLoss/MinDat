
#4.- Graficacion.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./csv/vgsales.csv")

df_LIMP = pd.DataFrame.from_dict(df.loc[:,['Rank','Name','Platform','Year','NA_Sales','Global_Sales']])
print(df_LIMP)

#df_LIMP = pd.DataFrame.from_dict(df.loc[:,['Team','Date','Home','Opponent','WINorLOSS','TeamPoints','OpponentPoints']])

#Se graficara los puntos del equipo y del oponente
x_values = df['Year'].unique()
y_values = df['NA_Sales'].value_counts().tolist()
ax = plt.subplot() 
ax.set_xticks(x_values)   #Eje x
ax.set_xticklabels(x_values)  #Etiquetas del eje x   
plt.ylabel('Year') #Nombre del eje x
plt.bar(x_values, y_values)
plt.show()
plt.close('all')