import pandas as pd 
import matplotlib.pyplot as plt
from utilities import *

#First task is to modify the files in the 'names' folder
convert_text_to_csv()

#Determine the trending names in the within a given year range

def get_data(year):
	''' Takes the year as argument and returns a dataframe with the data stored in file, yobyear.csv
	
	get_data(2017) -> returns the following:

	           Name Sex  Count
0          Emma   F  19738
1        Olivia   F  18632
2           Ava   F  15902s
3      Isabella   F  15100
4        Sophia   F  14831
...         ...  ..    ...
32464     Zykai   M      5
32465    Zykeem   M      5
32466     Zylin   M      5
32467     Zylis   M      5
32468     Zyrie   M      5

	''' 
	try:
		path = get_folder_path();
		data = pd.read_csv(str(path)+'/yob'+str(year)+'.csv')
		return data
	#checking file exists 
	except FileNotFoundError as err:
		print('File not found. Make sure you enter a year between 1880 and 2017')
	

def get_male_names(year):
	data = get_data(year)
	male = data[data.Sex == 'M']
	return male 

def get_female_names(year):
	data = get_data(year)
	female = data[data.Sex == 'F']
	return female 

def get_top_names_for_year(year):
	''' Takes the year as argument and returns a dictionary of dictionaries with the top 5 male and female names and their occurrences
	get_top_names_for_year(2017) -> {'male': {'Liam': 18728, 'Noah': 18326, 'William': 14904, 'James': 14232, 'Logan': 13974}, 
	'female': {'Emma': 19738, 'Olivia': 18632, 'Ava': 15902, 'Isabella': 15100, 'Sophia': 14831}}
	'''
	top_names = dict()
	male = get_male_names(year)
	female = get_female_names(year)
	male_dict = dict()
	female_dict = dict()
	for i in range(5):
		male_dict[male.Name.values[i]] = male.Count.values[i]
		female_dict[female.Name.values[i]] = female.Count.values[i]
		top_names['male'] = male_dict
		top_names['female'] = female_dict
	return top_names
	

def get_plot_trending_male_names(year):
	fig = plt.figure()
	ax = fig.add_axes([0.1, 0.1, 0.75, 0.75])
	male = get_male_names(year)
	female = get_female_names(year)
	ax.plot(male.Name[0:5], male.Count[0:5],'go-', linestyle='dashed', label='2017')
	ax.legend(('rene'),loc = 'lower left')
	ax.set_xlabel('Name')
	ax.set_ylabel('Number of name occurrences')
	ax.set_title('Top male baby names for year 2017')
	ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

	plt.show()
	return plt
	
