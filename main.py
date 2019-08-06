from trending_names import *




def menu():
	lower_bound = 1880
	upper_bound = 2017
	quit = False
	while(quit != True):
		print(35*"*")
		print("Make a choice:")
		print("\n1. Determine top 5 male baby names for a year between 1880 and 2017")
		print("\n2. Determine top 5 female baby names for a year between 1880 and 2017")
		print("\n3. Determine top 5 names for a sequence of years between 1880 and 2017")
		print("\nPress 'q' to quit the program")
		choice = input("Enter your choice: ")

		#do switch statment
		if choice == '1':
			print("You chose option 1\n")
			year = user_input()
			graph = get_year_plot_trending_male_names(year)
		elif choice == '2':
			print("You chose option 2\n")
			year = user_input()
			graph = get_year_plot_trending_female_names(year)
			#get list of years from user
		elif choice == '3':
			print("You chose option 3\n")
			valid = False
			while (valid != True):
				number_of_years = input("Enter the number of years you want to enter: ")
				if number_of_years.isdigit():
					number_of_years = int(number_of_years)
					valid = True
				else:
					print("Please enter an integer representing the number of years")

			#list to hold years
			years = []
			for index in range(0, number_of_years):
				#user input validation
				while True:
					try:
						year = int(input("Enter year between 1880 and 2017: "))
					except ValueError:
						print("Please enter an integer")
						continue
					else:
						if lower_bound <= year <= upper_bound:
							years.append(year)
							break
						else:
							print("Year needs to be within range; try again")
			years.sort()
			graph_m, graph_f = get_plot_trending_name_for_years(years)
		elif choice == 'q' or choice == 'Q':
			print('Thanks for using this program')
			quit = True
		else:
			print("Invalid option")

def main():
	print("Let's find out the trending names in the United States")
	menu()



if __name__ == "__main__":
	main()