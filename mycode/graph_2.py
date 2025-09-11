#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from plotnine import *

#Import data
data = pd.read_csv('../data/cleanSalaries.csv')


data_ej2=(
    data.groupby(['fixed_country','currency'])[['total_salary_usd']]
    .mean()
    .reset_index()
    .sort_values(by='total_salary_usd', ascending=False)
    .head(8)
)



#usando plotnine
(
    ggplot(data_ej2, aes(x='fixed_country', y='total_salary_usd', fill='currency')) +
    geom_bar(stat='identity') +
    ggtitle('Salario medio por divisa') +
    xlab('País') +
    ylab('Salario medio ($)') +
    scale_y_continuous(labels=lambda l: [f'${v//1000:,.0f}K' for v in l]) 
    
)


#usando matplotlib


# Crear un diccionario que asigne un color a cada divisa
currencies = data_ej2['currency'].unique()
len(currencies)
#vemos que hay 5 divisas. Podriamos crear una lista de colores mayor
colors = ['indianred','mediumseagreen','cornflowerblue','gold','violet']  # paleta de colores
color_map = {cur: colors[i % len(colors)] for i, cur in enumerate(currencies)}

# Asignar colores a cada fila según su divisa
bar_colors = data_ej2['currency'].map(color_map)

plt.bar(data_ej2.fixed_country, data_ej2.total_salary_usd, color=bar_colors)
plt.title('Salario medio por divisa')
plt.xlabel('Pais')
plt.xticks(fontsize=8)
plt.ylabel('Salario medio ($)')
plt.yticks(range(0, 200000, 25000), 
           labels=[f"${number//1000:,.0f}K" for number in range(0, 200000, 25000)])

# Leyenda directa desde el diccionario
from matplotlib.patches import Patch
legend_handles = [Patch(color=c, label=k) for k, c in color_map.items()]
plt.legend(handles=legend_handles, 
        title="Divisa",
        loc="upper center",       # punto de referencia en el centro superior
        bbox_to_anchor=(0.5, -0.1), 
        ncol=5,
        frameon=False)

plt.tight_layout()
plt.show()



