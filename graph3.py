import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

emp = pd.read_csv("SLR2.csv")

graph = sns.lmplot(x='worker percent', y='fertility rate',data=emp,fit_reg=True, height=7).set(title="Fertility Rate vs Worker Percentage") 


graph.figure.savefig("graph3.png") 