import json
import os
import pandas as pd
import numpy as np


def get_files(directory):
    """
    :param directory: (string): name of directory
    :return: (list): List of filenames in the directory.
    """
    
    # list to store all filenames in directory
    files_list = []
    
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(file):
            files_list.append(file)

    return files_list

def parse_files(files_list, out_filename):
    """
    :param files_list: List of filenames
    :param out_filename: (string): Name of the output json file.
    :return: (list): List of dictionaries containing app data from the json files.
    """

    # list to store dictionaries
    data_list = []
    # iterate over files
    for jsonfile in files_list:
        # load json file to dictionary
        with open(jsonfile, 'r') as file:
            """
            json_files_android/com.fireletter.text.photo.alphabet.alphabet.fireletter.json
            json_files_android/com.molatra.trainchinese.json
            json_files_android/com.jaffajam.santasslamdunk.json

            """
            data = json.load(file)
            # add to list 
            #print(jsonfile)
            np.set_printoptions(threshold=np.inf)
            df = pd.DataFrame(data)
            print(data)
            print(df)
            data_list.append(data)
            df.to_csv('test.csv', index=False) 

    
    # write list of dictionaries to a new json file
    with open(out_filename, "w") as file:
        json.dump(data_list, file)

    return data_list
files_list = get_files("json_files_ios")
parse_files(files_list,"test")

def categories(json_file, out_filename):
    """
    counts apps by category
    :param json_file: (string): Name of json file containing app data.
    :param out_filename: (string): Name of the output json file.
    :return: (dict): Dictionary where keys are categories and values are the number of apps in that category.
    """
    # load json file to dictionary
    with open(json_file, 'r') as file:
        data = json.load(file)

    #print(type(data))
    category_dict = {}

    for app in data:
        category = app["app_info"]["App Category"]

        if category not in category_dict:
            category_dict[category] = 1
        else:
            category_dict[category] += 1

    # sorts dictionary by value (increasing rating)
    # Source: https://realpython.com/sort-python-dictionary/
    category_dict = dict(sorted(category_dict.items(), key=lambda item: item[1], reverse=True))

    # write sorted dictionary to a new json file
    with open(out_filename, "w") as file:
        json.dump(category_dict, file)
    
    return category_dict

def main():
    # #place ios json files into list of files
    # files_list = get_files("json_files_ios")
    # #check the length is accurate and every file has been added
    # print(len(files_list))
    # #place dictionaries into list of dictionaries
    # data_list = parse_files(files_list, "ios_apps.json") 
    # #check the length is accurate and every dictionary has been added
    # print(len(data_list))

    #place google json files into list of files
    files_list = get_files("json_files_android")
    #check the length is accurate and every file has been added
    print(len(files_list))
    #place dictionaries into list of dictionaries
    data_list = parse_files(files_list, "android_apps.json") 
    #check the length is accurate and every dictionary has been added
    print(len(data_list))

    print(categories("ios_apps.json", "ios_categories.json"))
    print(categories("android_apps.json", "android_categories.json"))



# if __name__ == "__main__":
#     main()