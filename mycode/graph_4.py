import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

#Import data
data = pd.read_csv('../data/cleanSalaries.csv')


# Orden de experiencia
exp_order = [
    '1 year or less', '2 - 4 years', '5-7 years', '8 - 10 years',
    '11 - 20 years', '21 - 30 years', '31 - 40 years', '41 years or more'
]
exp_labels = ['<1','1-4','5-7','8-10','11-20','21-30','31-40','>=41']

# Definir colores por género
gender_colors = {
    'Man': 'cornflowerblue',
    'Woman': 'indianred'
}

fig, axes = plt.subplots(2, 1, figsize=(10, 12), sharex=True, sharey=True)
fig.suptitle('Brecha salarial por experiencia', fontsize=16)

for ax, gender in zip(axes, ['Man', 'Woman']):
    subset = data[data['gender'] == gender]

    # Valores de salarios por experiencia (lista de arrays)
    values = [subset[subset['field_experience'] == exp]['annual_salary_usd'].dropna()
              for exp in exp_order]

    # Boxplot horizontal
    bp = ax.boxplot(
        values,
        vert=False,
        patch_artist=True,
        tick_labels=exp_labels,
        boxprops=dict(facecolor=gender_colors[gender], alpha=0.6),
        medianprops=dict(color='black'),
        capprops=dict(color='black'),
        flierprops=dict(marker='o', markersize=8, 
                        markerfacecolor=gender_colors[gender], 
                        alpha=0.2, markeredgecolor='black')
    )

    # Estética
    ax.set_title('Hombre' if gender == 'Man' else 'Mujer', fontsize=14)
    ax.set_xlabel('Salario anual', fontsize=12)
  

    # Eje X (ticks cada 25K, en formato $999K)
    max_salary = data['annual_salary_usd'].max()
    max_x = int(np.ceil(max_salary / 25000.0)) * 25000
    xticks_vals = range(0, max_x + 1, 25000)
    xticks_labels = [f'${t//1000}K' for t in xticks_vals]
    ax.set_xticks(xticks_vals)
    ax.set_xticklabels(xticks_labels, fontsize=12)
    ax.set_ylabel('Experiencia (años)', fontsize=12)


plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()



import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))

# Creamos el boxplot
ax = sns.boxplot(
    data=data,
    x='annual_salary_usd',
    y='field_experience',
    hue='gender',
    orient='h',
    palette={'Man': 'cornflowerblue', 'Woman': 'indianred'},
    flierprops=dict(marker='o', markersize=4, alpha=0.3)  # estilo base
)


# Ajuste de ejes
plt.yticks(ticks=range(len(exp_order)), labels=exp_labels)
plt.ylabel('Experiencia (años)')

max_salary = data['annual_salary_usd'].max()
max_x = int(np.ceil(max_salary / 25000.0)) * 25000
xticks_vals = range(0, max_x+1, 25000)
xticks_labels = [f'${t//1000}K' for t in xticks_vals]
plt.xticks(xticks_vals, xticks_labels)
plt.xlabel('Salario anual')

plt.title('Brecha salarial')

# Leyenda personalizada
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles, ['Hombre', 'Mujer'], title='Género')

plt.tight_layout()
plt.show()





from plotnine import (
    ggplot, aes, geom_boxplot, coord_flip,
    scale_y_continuous, scale_x_discrete, scale_fill_manual,
    labs, theme, element_text, position_dodge
)
import numpy as np
import math

# ticks para el eje salario
max_salary = data['annual_salary_usd'].max()
max_x = int(math.ceil(max_salary / 25000.0)) * 25000
xticks = list(range(0, max_x + 1, 25000))

p = (
    ggplot(data, aes(x='field_experience', y='annual_salary_usd', fill='gender'))
    + geom_boxplot(position=position_dodge(width=0.8), width=0.6, outlier_alpha=0.2)
    + coord_flip()  # ahora queda horizontal: salario en X, experiencia en Y visualmente
    + scale_x_discrete(limits=exp_order, labels=exp_labels)   # orden y etiquetas de experiencia
    + scale_y_continuous(breaks=xticks, labels=[f"${t//1000}K" for t in xticks])  # ticks salario
    + scale_fill_manual(values={'Man': 'cornflowerblue', 'Woman': 'indianred'},
                        labels=['Hombre', 'Mujer'])
    + labs(x='Experiencia (años)', y='Salario anual', title='Brecha salarial', fill='Género')
    + theme(figure_size=(10, 6), axis_text_y=element_text(size=9))
)

p
