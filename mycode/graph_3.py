import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
from plotnine import *

#Import data
data = pd.read_csv('../data/cleanSalaries.csv')

data['median_salary_age'] = data.groupby('age')['annual_salary_usd'].transform('median')

age_order = ['18-24', '25-34', '35-44', '45-54', '55-64']
colors = ['indianred','mediumseagreen','cornflowerblue','gold','violet']  # paleta de colores


# Rango máximo del eje X
max_salary = data['annual_salary_usd'].max()
max_x = int(np.ceil(max_salary / 25000.0)) * 25000



plt.figure(figsize=(8, 12))
plt.suptitle('Distribución de salario por edad')

# Recorremos todas las edades 
for i, element in enumerate(age_order):    

    # Subplot
    ax = plt.subplot2grid((len(age_order), 1), (i, 0))

    
    # Pintamos el gráfico 
    ax.hist(
        data[data['age'] == element].loc[:, 'annual_salary_usd'].values,
        color= colors[i],
        bins=20,
        alpha=0.2,
        edgecolor="black")
    
    # Titulo de cada subplot
    ax.set_title(element)
    
    # Línea vertical en la mediana
    ax.axvline(data[data['age'] == element]['median_salary_age'].iloc[0], 
                color=colors[i], 
                linestyle="--", 
                linewidth=1.5)
    
    
    # Configuración del eje X
    xticks_vals = range(0, max_x + 1, 25000)
    xticks_labels = [f"${t//1000}K" for t in xticks_vals]
    ax.set_xticks(xticks_vals)
    ax.set_xticklabels(xticks_labels, rotation=0)
    ax.set_xlabel("Salario anual (sin bonus)")
    
    
    # Configuración del eje Y (sin ticks ni etiquetas)
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_ylabel("Distribución")
   

# Ajustamos los márgenes de cada gráfico después de añadir todos
plt.tight_layout()

plt.show()




import seaborn as sns

# Orden y colores
age_order = ['18-24', '25-34', '35-44', '45-54', '55-64']
colors = ['indianred','mediumseagreen','cornflowerblue','gold','violet']
age_colors = dict(zip(age_order, colors))

# Rango máximo del eje X
max_salary = data['annual_salary_usd'].max()
max_x = int(np.ceil(max_salary / 25000.0)) * 25000
xticks_vals = range(0, max_x + 1, 25000)
xticks_labels = [f'${t//1000}K' for t in xticks_vals]

# Usamos FacetGrid (una columna, faceteado por edad)
g = sns.FacetGrid(
    data, 
    row="age", 
    hue="age", 
    palette=age_colors, 
    row_order=age_order,
    sharex=True, 
    sharey=False, 
    height=2, aspect=4
)

# Densidad por cada edad
g.map(sns.kdeplot, "annual_salary_usd", fill=True, alpha=0.2)

# Líneas verticales de la mediana
for ax, age in zip(g.axes.flatten(), age_order):
    median_val = data.loc[data['age'] == age, 'median_salary_age'].iloc[0]
    ax.axvline(median_val, color=age_colors[age], linestyle="--", linewidth=1.5)

    # Configuración de ticks
    ax.set_xticks(xticks_vals)
    ax.set_xticklabels(xticks_labels, rotation=0)
    ax.set_xlabel("Salario anual (sin bonus)")
    ax.set_yticks([])
    ax.set_ylabel("Distribución")

# Título general
plt.subplots_adjust(top=0.92)
g.fig.suptitle("Distribución de salario por edad")

plt.show()
