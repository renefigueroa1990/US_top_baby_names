#Rene Figueroa

import os
from pathlib import Path
#first need to add the label row to the files downloaded in the names folder
# label row: Name,Sex,Counter
#second need to convert the files from .txt to .csv to manipulate with pandas and matploblib

#directory containing baby names data is names
#Make sure to unzip the names.zip folder


def get_folder_path():
	''' This function returns the path where the 'names' folder is located in your system'''
	babies_data_path = Path(os.getcwd() + "/names")
	return babies_data_path

def get_text_file_names():
	''' This function returns a list with the contents of the 'names' folder'''
	path = get_folder_path()

	#list to hold baby text files
	baby_text_files = list()
	#obtain the text files names from the names directory
	for file_name in path.iterdir():
		baby_text_files.append(file_name.name)

	baby_text_files.sort()
	# #remove the 'NationalReadMe.pdf file'
	del baby_text_files[0]
	return baby_text_files


def convert_text_to_csv():
	''' This function converts the text files returned by the 'get_text_file_names' function to CSV files'''
	# TO TO: check if files is alredy CSV 
	data_path = get_folder_path()
	text_files = get_text_file_names()
	for temp in text_files:
		#to access every text file in the names directory
		temp_path = data_path/temp
		if temp.endswith('.txt'):
			with temp_path.open() as input:
				old_data = input.read()
			with open(temp_path, "w+") as output:
					#write label to every text file
				output.write("Name,Sex,Count\n" + old_data)
				#convert to .csv 
			new_file_name = temp_path.with_suffix('.csv')
			os.rename(temp_path, new_file_name)

#Utilities should only run once
convert_text_to_csv()


