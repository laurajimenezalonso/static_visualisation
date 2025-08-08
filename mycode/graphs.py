#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from plotnine import *

#Import data
data = pd.read_csv('../data/cleanSalaries.csv')


data_ej2=(
    data.groupby(['fixed_country'])[['total_salary_usd']]
    .mean()
    .reset_index()
    .sort_values(by='total_salary_usd', ascending=False)
    .head(8)
)

#usando matplotlib
plt.bar(data_ej2.fixed_country, data_ej2.total_salary_usd)
plt.title("Salario medio por divisa")
plt.xlabel("Pais")
plt.ylabel("Salario medio ($)")
#plt.yticks(range(1200, 1800, 100), labels=[f"{number:,.2f}" for number in range(1200, 1800, 100)])

plt.show()

#usando plotnine
ggplot(data_ej2, aes(x='fixed_country', y='total_salary_usd')) + geom_bar()

p9.ggplot(data_ej2) + p9.geom_bar()
#Calcular el salario medio (sin bonus) por edad y educación.
data_ej5=(
    data.groupby(['age','education'])[['annual_salary_usd']]
    .mean()
    .reset_index()
)