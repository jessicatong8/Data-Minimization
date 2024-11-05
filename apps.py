import json
import os


def load_json(filename):
     # load json file to dictionary
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def dump_json(data, filename):
     with open(filename, "w") as file:
        json.dump(data, file)


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
        data = json.load(jsonfile)
        # add to list 
        data_list.append(data)

    # write list of dictionaries to a new json file
    dump_json(data_list, out_filename)

    return data_list


def categories(json_file, out_filename):
    """
    counts apps by category
    :param json_file: (string): Name of json file containing app data.
    :param out_filename: (string): Name of the output json file.
    :return: (dict): Dictionary where keys are categories and values are the number of apps in that category.
    """
    # load json file to dictionary
    data = load_json(json_file)

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
    dump_json(category_dict, out_filename)
    
    return category_dict

def top_categories(categories, num):
    """
    :param categories: (dict): Sorted dictionary of categories and their counts.
    :param num: (int): Number of top categories to return.
    :return: (list): List of top 'num' categories.
    """

    list_categories = []
    for i in range(num):
        list_categories.append(list(categories.keys())[i])
    return list_categories


def group_by_category(json_file, category, out_filename):
    # load json file to dictionary
    app_list = load_json(json_file)

    category_sorted = []

    for app in app_list:
        if app["app_info"]["App Category"] == category:
            category_sorted.append(app)
    
    # write list of dictionaries to a new json file
    dump_json(category_sorted, out_filename)
        
    return category_sorted


    
def main():
    # #place ios json files into list of files
    # files_list = get_files("json_files_ios")
    # #check the length is accurate and every file has been added
    # print(len(files_list))
    # #place dictionaries into list of dictionaries
    # data_list = parse_files(files_list, "ios_apps.json") 
    # #check the length is accurate and every dictionary has been added
    # print(len(data_list))

    # #place google json files into list of files
    # files_list = get_files("json_files_android")
    # #check the length is accurate and every file has been added
    # print(len(files_list))
    # #place dictionaries into list of dictionaries
    # data_list = parse_files(files_list, "android_apps.json") 
    # #check the length is accurate and every dictionary has been added
    # print(len(data_list))

    """
    Android files that don't work
    json_files_android/com.fireletter.text.photo.alphabet.alphabet.fireletter.json
    json_files_android/com.molatra.trainchinese.json
    json_files_android/com.jaffajam.santasslamdunk.json

    """
    
    ios_categories = categories("ios_apps.json", "ios_categories.json")
    #android_categories = categories("android_apps.json", "android_categories.json")
    #check the 5 top categories are printed for ios apps
    top_ios_categories = top_categories(ios_categories, 5)
    print(top_ios_categories)

    grouped = None
    #check the app info is grouped together for all ios game apps
    grouped = group_by_category("ios_apps.json", "Games", "ios_games.json")
    print(len(grouped))

    #check the app info is grouped together for all ios lifestyle apps
    grouped = group_by_category("ios_apps.json", "Lifestyle", "ios_lifestyle.json")
    print(len(grouped))

    #check the app info is grouped together for all ios shopping apps
    grouped = group_by_category("ios_apps.json", "Shopping", "ios_shopping.json")
    print(len(grouped))

    #check the app info is grouped together for all ios travel apps
    grouped = group_by_category("ios_apps.json", "Travel", "ios_travel.json")
    print(len(grouped))

    #check the app info is grouped together for all ios health & fitness apps
    grouped = group_by_category("ios_apps.json", "Health & Fitness", "ios_health.json")
    print(len(grouped))
    

if __name__ == "__main__":
    main()