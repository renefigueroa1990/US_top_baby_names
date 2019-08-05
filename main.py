from trending_names import *

def menu():
	quit = False
	while(quit != True):
		print(25*"*")
		print("Make a choice:")
		print("\n1. Determine top 5 male baby names for a year between 1880 and 2017")
		print("\n2. Determine top 5 female baby names for a year between 1880 and 2017")
		print("\n3. Determine top 5 names for a sequence of years between 1880 and 2017")
		print("\nPress 'q' to quit the program")
		choice = input("Enter your choice: ")

		#do switch statment
		if choice == '1':
			print("You chose option 1\n")
			year = int(input("Enter year between 1880 and 2017: "))
			graph = get_year_plot_trending_male_names(year)
		elif choice == '2':
			print("You chose option 2\n")
			year = int(input("Enter year between 1880 and 2017: "))
			graph = get_year_plot_trending_female_names(year)
		elif choice == '3':
			print("You chose option 3\n")
			valid_list = False
			while(valid_list != True):
				#TO DO: Check user input
				user_data = input("Enter years between 1880 and 2017 (separated by a space i.e: 1990 1995 1998 2005): ")
				if (user_data.find(' ')):
					years = user_data.split(" ")
					valid_list = True
				else:
					print("You need to enter the years separated by a space.")
			[int(year) for year in years]
			graph_m, graph_f = get_plot_trending_name_for_years(years)
		elif choice == 'q' or choice == 'Q':
			print('Bye')
			quit = True
		else:
			print("Invalid option")

def main():
	print("Let's find out the trending names in the United States")
	menu()



if __name__ == "__main__":
	main()