#Rene Figueroa

import os
from pathlib import Path
#first need to add the label row to the files downloaded in the names folder
# label row: Name,Sex,Counter
#second need to convert the files from .txt to .csv to manipulate with pandas and matploblib

#directory containing baby names data is names
#Make sure to unzip the names.zip folder
babies_data_path = Path(os.getcwd() + "/names")
print(babies_data_path)

#obtain the text files names from the names directory

baby_text_files = []
for file_name in babies_data_path.iterdir():
	baby_text_files.append(file_name.name)

baby_text_files.sort()
#remove the 'NationalReadMe.pdf file'
del baby_text_files[0]


#TODO:

#only write "Name,Sex,Count" once
#make sure files exits 

for temp in baby_text_files:
	#to access every text file in the names directory
	temp_path = babies_data_path/temp
	with temp_path.open() as input:
		old_data = input.read()
	with open(temp_path, "w+") as output:
			#write label to every text file
		output.write("Name,Sex,Count\n" + old_data)
		#convert to .csv 
	new_file_name = temp_path.with_suffix('.csv')
	print(new_file_name)
	os.rename(temp_path, new_file_name)

#Utilities should only run once



