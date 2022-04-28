
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

equipments_df = pd.read_csv("equipments.csv")
personnel_df = pd.read_csv("personnel.csv")

def equipments_graphs():
	columns = equipments_df.columns
	print("\nChoose the equipment you want to view Graph:\n")
	for idx, column in enumerate(columns[2:]):
		print("{}. {}".format(idx+1, column))
	choice = int(input("Choice: "))
	sns.lineplot(equipments_df.day, equipments_df[columns[choice+1]])
	plt.show()
	

def personnel_graphs():
	columns = personnel_df.columns
	print("\nChoose the type you want to view Graph:\n")
	print("1. Dead\n2. Prisoners of War (POW)")
	choice = int(input("Choice: "))
	if choice == 1:
		sns.lineplot(personnel_df.day, personnel_df.personnel)
	elif choice == 2:
		sns.lineplot(personnel_df.day, personnel_df.POW)

	plt.show()
	


def display_personnel():
	print(personnel_df.to_markdown())

def display_equipments():
	
	columns = equipments_df.columns
	print("\nChoose the equipment you want to view:\n")
	for idx, column in enumerate(columns[2:]):
		print("{}. {}".format(idx+1, column))
	choice = int(input("Choice: "))
	print()
	new_df = equipments_df[["date", "day", columns[choice+1]]]
	print(new_df.to_markdown())

def display_menu():
	choice = int(input("Choose what you want:\n1. A table showing russia personnel losses.\n2. A table showing russia equipments losses\n3. Graphical representation of equipment losses per day\n4. Graphical representation of personnel losses per day\nChoice: "))
	return choice

def main():
	print()
	print("*"*100)
	print("\nWELCOME TO UKRAINE WAR: RUSSIA EQUIPMENTS AND PERSONELL LOSS ANALYSIS\n\n")

	choice = display_menu()
	print()
	print("-"*20)
	if choice == 1:
		display_personnel()
	elif choice == 2:
		display_equipments()
	elif choice == 3:
		equipments_graphs()
	elif choice == 4:
		personnel_graphs()

main()