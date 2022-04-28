import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

employment_rates = pd.read_excel("employmentrate2017.xlsx")
ax = employment_rates.plot(
    figsize=(20, 10), 
    x="Area", 
    y=["White", "Black/Black British"], 
    kind="bar",
    title="Comparison between white and black across the areas"
)
ax.figure.savefig("graph2.png")
