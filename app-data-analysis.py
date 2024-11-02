import pandas as pd
import json
import os


# read in json files
# convert to dictionaries, store in a list
# analyze with pandas

""" 
Questions
1. Top categories of apps (4)
2. Top types of purposes (overall, by category) (4)
3. Type of data (overall, by category) (4-10)
"""


def getFiles(directory):
    # assign directory

    files_list = []
    
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(file):
            files_list.append(file)

    return files_list

def parseFiles(files_list):
    data_list = []

    for jsonfile in files_list:
        with open(jsonfile, 'r') as file:
            data = json.load(file)
            data_list.append(data)

    return data_list
    

def main():
    files_list = getFiles("json_files_ios")
    print(len(files_list))
    data_list = parseFiles(files_list)
    print(len(data_list))


if __name__ == "__main__":
    main()