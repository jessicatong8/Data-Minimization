import json
import os


def load_json(filename):
    """
    :param filename: (string): Name of the json file.
    :return: object containing the data from the json file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def dump_json(data, filename):
     """
     :param data: (object) Data to be saved in json format.
     :param filename: (string): Name of the output json file.
     :return: (None) data is saved in the specified json file.
     """
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
        if jsonfile == "json_files_android/.DS_Store":
            continue
        # load json file to dictionary
        data = load_json(jsonfile)
        # add to list 
        data_list.append(data)

    # write list of dictionaries to a new json file
    dump_json(data_list, out_filename)

    return data_list


def categories(appstore, json_file, out_filename):
    """
    counts apps by category
    :param appstore: (string): "ios" or "android"
    :param json_file: (string): Name of json file containing app data.
    :param out_filename: (string): Name of the output json file.
    :return: (dict): Dictionary where keys are categories and values are the number of apps in that category.
    """
    # load json file to dictionary
    data = load_json(json_file)

    #print(type(data))
    category_dict = {}

    count = 0
    for app in data:
        #print(app["App name"])
        if appstore == "ios":
            category = app["app_info"]["App Category"]
            numReviews = app["app_info"]["No. of Ratings"]
        elif appstore == "android":
            if len(app["App category"]) < 1:
                count += 1
            elif len(app["App category"]) > 1:
                category = "Games"
            else:
                category = app["App category"][0]
            numReviews = app["Total reviews"]
            print(numReviews)
            if numReviews == "No reviews":
                numReviews = 0
            else:
                numReviews = int(numReviews)
            print(numReviews)
    
        if category not in category_dict:
            category_dict[category] = numReviews
        else:
            category_dict[category] += numReviews
            
    print("not counted: ", count)

    # sorts dictionary by value (increasing rating)
    # Source: https://realpython.com/sort-python-dictionary/
    category_dict = dict(sorted(category_dict.items(), key=lambda item: item[1], reverse=True))

    # write sorted dictionary to a new json file
    dump_json(category_dict, out_filename)
    
    return category_dict

def top_apps(appstore, json_file, out_filename):
    # load json file to dictionary
    data = load_json(json_file)

    #print(type(data))
    name_dict = {}

    for app in data:
        if appstore == "ios":
            name = app["app_info"]["App Name"]
            numReviews = app["app_info"]["No. of Ratings"]
        elif appstore == "android":
            name = app["App name"]
            numReviews = app["Total reviews"]
            if numReviews == "No reviews":
                numReviews = 0
            else:
                numReviews = int(numReviews)

        if name not in name_dict:
            name_dict[name] = numReviews
        else:
            name_dict[name] += numReviews

    # sorts dictionary by value (increasing rating)
    # Source: https://realpython.com/sort-python-dictionary/
    name_dict = dict(sorted(name_dict.items(), key=lambda item: item[1], reverse=True))

    # write sorted dictionary to a new json file
    dump_json(name_dict, out_filename)
    
    return name_dict

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
    """
    :param json_file: (string): Name of json file containing app data.
    :param category: (string): Category to group by.
    :param out_filename: (string): Name of the output json file to write to.
    :return: (list): List of dictionaries containing app data from the json files that belong to the specified category.
    """
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
    
    
    #categories("ios", "ios_apps.json", "ios_categories_ratings.json")
    #top_apps("ios_apps.json", "ios_top_apps_ratings.json")
    #categories("android", "android_apps.json", "android_categories_ratings.json")
    top_apps("android", "android_apps.json", "android_top_apps_ratings.json")
    
    # top_categories = ['Games', 'Lifestyle', 'Shopping', 'Travel', 'Health & Fitness']
    # out_files = ["ios_games.json", "ios_lifestyle.json", "ios_shopping.json", "ios_travel.json", "ios_health.json"]

    # # group apps by category into json files
    # for i in range(len(top_categories)):
    #     grouped = group_by_category("ios_apps.json", top_categories[i], out_files[i])
    #     # check appropriate number of apps have been grouped together
    #     print(len(grouped))

if __name__ == "__main__":
    main()