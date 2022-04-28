import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# Graph 1
employment= pd.read_csv("emp.csv", encoding='latin-1', low_memory=False)
columns = list(employment.columns)
new_columns = ["GeoName", "Description"] + columns[-20:]
df = employment[new_columns]
geos = df.query("GeoName == 'United States' and Description == 'Total employment (number of jobs)'")
geos = geos.T
geos = geos.iloc[3:]
geos[0] = pd.to_numeric(geos[0])
geos.reset_index(inplace=True)
geos.rename(columns = {'index':'Year', 0:'Total'}, inplace = True)

ax = geos.plot(
    figsize=(15, 10), 
    kind="line", x="Year", 
    y="Total", 
    ylabel="Total * 10,000,000", 
    title="United State Total Employment From 2001 to 2019",
)
ax.figure.savefig("graph1.png")

# Graph 2
employment_rates = pd.read_excel("employmentrate2017.xlsx")
ax = employment_rates.plot(
    figsize=(20, 10), 
    x="Area", 
    y=["White", "Black/Black British"], 
    kind="bar",
    title="Comparison between white and black across the areas"
)
ax.figure.savefig("graph2.png")



# Graph 3
emp = pd.read_csv("SLR2.csv")

graph = sns.lmplot(x='worker percent', y='fertility rate',data=emp,fit_reg=True, height=7).set(title="Fertility Rate vs Worker Percentage") 


graph.figure.savefig("graph3.png") 