from apps import *
import pandas as pd


def purposes(in_files, categories, out_file):
    """
    :param in_files: (list) list of filenames (strings) for json files with app info
    :param categories: (list) list of category names (strings) corresponding to files
    :return: (df) dataframe containing number of apps collecting data for each purpose by category
    """
    # list to store dataframes for each category
    dataframes = []

    # iterate over all categories
    for i in range(len(in_files)):
        # load json file to list of apps
        app_list = load_json(in_files[i])

        # dictionary to store number of apps collecting data for each purpose
        purposes_dict = {}

        # iterate over all apps in the current category and count the number of apps collecting data for each purpose
        for app in app_list:
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

        # sorts dictionary by value (increasing rating)
        # Source: https://realpython.com/sort-python-dictionary/
        purposes_dict = dict(sorted(purposes_dict.items(), key=lambda item: item[1], reverse=True))

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

in_files = ["ios_apps.json", "ios_games.json", "ios_lifestyle.json", "ios_shopping.json", "ios_travel.json", "ios_health.json"]
top_categories = ["All Apps", 'Games', 'Lifestyle', 'Shopping', 'Travel', 'Health & Fitness']
print(purposes(in_files, top_categories, "ios_purposes.csv"))

