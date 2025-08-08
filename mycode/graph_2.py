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
plt.yticks(range(0, 200000, 25000), labels=[f"{number:,.0f}" for number in range(0, 200000, 25000)])

plt.show()

#usando plotnine
(
    ggplot(data_ej2, aes(x='fixed_country', y='total_salary_usd')) +
    geom_bar(stat='identity', fill='blue') +
    ggtitle("Salario medio por divisa") +
    xlab("País") +
    ylab("Salario medio ($)") +
    scale_y_continuous(labels=lambda l: [f'{v:,.0f}' for v in l]) 
    
)


