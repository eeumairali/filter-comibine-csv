"""This script will collect all csv
and it will filter specific website records
and will generate a new csv file at the end
"""

import pandas as pd
import os

#write path
#path_input = "/home/umair/Desktop/FilteringCsvFiles/inputCsvFiles/"
path_input = "inputCsvFiles/"

#path_output = "/home/umair/Desktop/FilteringCsvFiles/FilteredOutputFile/"
list_of_all_files = os.listdir(path_input)


# filter csv 
all_input_csvs = []
for filename in list_of_all_files:
    if filename.endswith(".csv"):
        all_input_csvs.append(filename)

final_csv = pd.DataFrame()
keyword = "dermologykit.com"
for filename in all_input_csvs:
    print("working on file",filename)
    current_data = pd.read_csv(path_input+filename, encoding='unicode_escape')
    # applying filtering
    url_column = current_data.LeadURL
    filtered_data = current_data[ url_column.str.contains(keyword) ]    
    final_csv = pd.concat([final_csv, filtered_data],axis=0)

final_csv.to_csv("final.csv")    
    
