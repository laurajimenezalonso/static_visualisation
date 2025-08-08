import numpy as np
import pandas as pd

#Import data
data = pd.read_csv('../data/salaries.csv')


#Create a new columns 'fixed_country' where we copy country in lower case 
data = data.assign(
    fixed_country=data.country.str.lower().str.strip()
)

#We check what are the values included in country that we can fix
data['country'].unique()



#We fixe datat related to UK
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("king"), "united kingdom", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.startswith("uk"), "united kingdom", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.replace(" ", "").str.startswith("u.k"), "united kingdom", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.replace(" ", "").str.startswith("u.k"), "united kingdom", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("kindom"), "united kingdom", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("england"), "united kingdom", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("scot"), "united kingdom", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("britain"), "united kingdom", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("wales"), "united kingdom", data.fixed_country)
)


#We fix data related to US
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("state"), "united states", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("america"), "united states", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.startswith("us"), "united states", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.replace(" ", "").str.startswith("u.s"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("isa"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("statws"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("status"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("sates"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("stattes"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("stares"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("status"), "united states", data.fixed_country)
)


data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("statss"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("i.s"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("is"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("the us"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("statues"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("sttes"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.startswith("us"), "united states", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("california"), "united states", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("virginia"), "united states", data.fixed_country)
)

#We fix data related to Canada
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("canad"), "canada", data.fixed_country)
)

data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("canda"), "canada", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("cnada"), "canada", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.startswith("can"), "canada", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.startswith("csnada"), "canada", data.fixed_country)
)
#We fix data related to NL
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("nethe"), "netherland", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("nede"), "netherland", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.startswith("nl"), "netherland", data.fixed_country)
)

#We fix data related to HK
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("konh"), "hong kong", data.fixed_country)
)
#NZ
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("new z"), "new zealand", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("nz"), "new zealand", data.fixed_country)
)

#UAE
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("emirates"), "uae", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.startswith("ua"), "uae", data.fixed_country)
)
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("u.a."), "uae", data.fixed_country)
)
#JAPAN
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("jap"), "japan", data.fixed_country)
)


#ITALY
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.startswith("ital"), "italy", data.fixed_country)
)

#AU
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.startswith("austra"), "australia", data.fixed_country)
)

#Spain
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("catalonia"), "spain", data.fixed_country)
)

#Remote
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("remote"), "remote", data.fixed_country)
)

#Denmark
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("danmark"), "denmark", data.fixed_country)
)

#Romania
data = data.assign(
    fixed_country=np.where(data.fixed_country.str.contains("romania"), "romania", data.fixed_country)
)


#a=data.fixed_country.value_counts().reset_index().head(20)['count'].sum() / data.shape[0]
#print(a)

#We review countries after fixing the data
data['fixed_country'].unique()






######
"""
Ejercicio 1

Queremos formatear los datos correctamente para prepararlos de cara a las visualizaciones solicitadas en los siguientes ejercicios. Para ello, se pide:

- Leer los sets de datos proporcionados
- Aplicar el tipo de cambio a las columnas de salario y bonus para que todo quede representado en USD
- Eliminar datos con poca muestra que introducen ruido:
    o Registros de las edades "under 18" y "65 or over".
    o Registros con salarios anuales (sin bonus) por encima de los 200K dólares.
    o Registros con géneros distintos a "Man" o "Woman".
- Imputar los valores faltantes (si los hay) de salario y bonus a 0.
"""
#we read fx file
fx= pd.read_csv('../data/exchange_rates.csv')
fx.head()

#to convert all salaries and bonuses into USD we will join both datasets

data_usd=pd.merge(
    data,
    fx,
    on='currency',
    how='left'
)

#create 3 new columns : salary in usd, bonus in usd and sum of previous one


data_usd['annual_salary_usd']=data_usd['annual_salary']*data_usd['exchange_rate'] 
data_usd['bonus_salary_usd']=data_usd['bonus_salary']*data_usd['exchange_rate'] 
data_usd['total_salary_usd']=(data_usd['bonus_salary']+data_usd['annual_salary'])*data_usd['exchange_rate']

#To eliminate data, we will filter data we want to keep and asign it 
#to a new dataset


data_usd['age'].unique()
data_usd['gender'].unique()


#We keep
# - age not int 'under 18' and '65 or over'
#  salaries lower that 200K USD
# gender other than 'man' and 'women'


data_filtered = data_usd[
    (~data_usd['age'].isin(['under 18', '65 or over'])) &
    (data_usd['annual_salary_usd'] <= 200000) &
    (data_usd['gender'].isin(['Man', 'Woman']))
]

#we fill missing salaries and bonus with 0

data_filtered.loc[:, 'annual_salary'] = data_filtered['annual_salary'].fillna(0)
data_filtered.loc[:, 'bonus_salary'] = data_filtered['bonus_salary'].fillna(0)
data_filtered.loc[:, 'annual_salary_usd'] = data_filtered['annual_salary_usd'].fillna(0)
data_filtered.loc[:, 'bonus_salary_usd'] = data_filtered['bonus_salary_usd'].fillna(0)
data_filtered.loc[:, 'total_salary_usd'] = data_filtered['total_salary_usd'].fillna(0)


#We export the filtered data, as it will be used in exercise 2 to 5
data_filtered.to_csv('../data/cleanSalaries.csv')