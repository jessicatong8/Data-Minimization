from apps import *
import pandas as pd


def purposes_countByCategory(in_file, categories, out_file):
    """
    :param in_files: (list) list of filenames (strings) for json files with app info
    :param categories: (list) list of category names (strings) corresponding to files
    :return: (df) dataframe containing number of apps collecting data for each purpose by category
    """
    # list to store dataframes for each category
    dataframes = []

    # load json file to list of apps
    app_list = load_json(in_file)
    
    # iterate over all categories
    for i in range(len(categories)):
        # dictionary to store number of apps collecting data for each purpose
        purposes_dict = {}
        # iterate over all apps in the current category and count the number of apps collecting data for each purpose
        for app in app_list:
            if app["app_info"]["App Category"] == categories[i]:
                for purpose in app["data_linked"].keys():
                    if purpose not in purposes_dict:
                        purposes_dict[purpose] = 1
                    else:
                        purposes_dict[purpose] += 1
                if app["data_track"]:
                    if "Tracking" not in purposes_dict:
                        purposes_dict["Tracking"] = 1
                    else:
                        purposes_dict["Tracking"] += 1

        # create a dataframe from dictionary for each category
        df = pd.DataFrame(purposes_dict, index=[0])
        # add column for category name
        df.insert(0, 'Category', categories[i])
        # add dataframe to list of dataframes for all categories
        dataframes.append(df)
   
    # combine all dataframes
    purposes_by_category = pd.concat(dataframes)

    # save dataframe to csv file
    purposes_by_category.to_csv(out_file, index = False)

    return purposes_by_category


def purposes_percentByCategory(in_file, categories, out_file):
    """
    :param in_files: (list) list of filenames (strings) for json files with app info
    :param categories: (list) list of category names (strings) corresponding to files
    :return: (df) dataframe containing percentage of apps collecting data for each purpose by category
    """
    # list to store dataframes for each category
    dataframes = []

    # load json file to list of apps
    app_list = load_json(in_file)
    
    # iterate over all categories
    for i in range(len(categories)):
        # dictionary to store number of apps collecting data for each purpose
        purposes_dict = {}
        # count number of apps in each category
        num_apps = 0
        # iterate over all apps in the current category and count the number of apps collecting data for each purpose
        for app in app_list:
            if app["app_info"]["App Category"] == categories[i]:
                num_apps += 1
                for purpose in app["data_linked"].keys():
                    if purpose not in purposes_dict:
                        purposes_dict[purpose] = 1
                    else:
                        purposes_dict[purpose] += 1
                if app["data_track"]:
                    if "Tracking" not in purposes_dict:
                        purposes_dict["Tracking"] = 1
                    else:
                        purposes_dict["Tracking"] += 1
        
        # calculate percentage of apps collecting data for each purpose
        for purpose in purposes_dict:
            purposes_dict[purpose] = round((purposes_dict[purpose] / num_apps), 4)

        # create a dataframe from dictionary for each category
        df = pd.DataFrame(purposes_dict, index=[0])
        # add column for category name
        df.insert(0, 'Category', categories[i])
        # add dataframe to list of dataframes for all categories
        dataframes.append(df)
   
    # combine all dataframes
    purposes_by_category = pd.concat(dataframes)

    # save dataframe to csv file
    purposes_by_category.to_csv(out_file, index = False)

    return purposes_by_category


categories = load_json("ios_categories_ratings.json")
categories = list(categories.keys())

#print(purposes_countByCategory("ios_apps.json", categories, "ios_purposes_countByCategory.csv"))
print(purposes_percentByCategory("ios_apps.json", categories, "ios_purposes_percentByCategory.csv"))

