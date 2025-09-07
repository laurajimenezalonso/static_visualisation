import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from plotnine import *

#Import data
data = pd.read_csv('../data/cleanSalaries.csv')

#Calcular el salario medio (sin bonus) por edad y educación.
data_ej5=(
    data.groupby(['age','education'])[['annual_salary_usd']]
    .mean()
    .reset_index()
)

education_order = [
    'High School',
    'Some college',
    'College degree',
    "Master's degree",
    'Professional degree (MD, JD, etc.)',
    'PhD'
]

education_labels = [ 
    'High School',
    'Some college',
    'College degree',
    "Maste's degree",
    'Professional degree',
    'PhD'
]

age_order = ['18-24', '25-34', '35-44', '45-54', '55-64']

#Pivotamos los datos para poder pasar la matriz al imshow
pivot_data_ej5 = data_ej5.pivot(
    index='age', 
    columns='education', 
    values='annual_salary_usd'
)
#print(pivot_data_ej5)

# Reordenamos los datos de la manera que queremos que salga en el orden que queremos
pivot_data_ej5 = pivot_data_ej5.reindex(
    index=age_order, 
    columns=education_order
)

#print(pivot_data_ej5)

#usando matplotlib
graph_5=plt.imshow(pivot_data_ej5, cmap='Greens')

plt.title('Salario medio por edad y educación')

# x axis
plt.xlabel('Educación')
plt.xticks(
    ticks=range(len(pivot_data_ej5.columns)), 
    labels=education_labels,
    rotation=90,
    ha='right'
)
# y axis
plt.ylabel('Edad')
plt.yticks(
    ticks=range(len(pivot_data_ej5.index)),
    labels=age_order
)



cbar=plt.colorbar(graph_5)
cbar.set_label("Salario medio (sin bonus)")

ticks = list(range(40000, 120001, 40000))

print(ticks)
cbar.set_ticks(ticks)
cbar.set_ticklabels([f"${t//1000}K" for t in ticks])

plt.show()

