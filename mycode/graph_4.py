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
fig.suptitle("Brecha salarial por experiencia", fontsize=16)

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
        medianprops=dict(color="black"),
        capprops=dict(color="black"),
        flierprops=dict(marker="o", markersize=8, 
                        markerfacecolor=gender_colors[gender], 
                        alpha=0.2, markeredgecolor="black")
    )

    # Estética
    ax.set_title("Hombre" if gender == "Man" else "Mujer", fontsize=14)
    ax.set_xlabel("Salario anual", fontsize=12)
  

    # Eje X (ticks cada 25K, en formato $999K)
    max_salary = data['annual_salary_usd'].max()
    max_x = int(np.ceil(max_salary / 25000.0)) * 25000
    xticks_vals = range(0, max_x + 1, 25000)
    xticks_labels = [f"${t//1000}K" for t in xticks_vals]
    ax.set_xticks(xticks_vals)
    ax.set_xticklabels(xticks_labels, fontsize=12)
    ax.set_ylabel("Experiencia (años)", fontsize=12)


plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
