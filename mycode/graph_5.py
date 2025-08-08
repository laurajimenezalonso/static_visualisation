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