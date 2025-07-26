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

#We 
data['fixed_country'].unique()

