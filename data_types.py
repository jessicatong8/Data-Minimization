from apps import *
import pandas as pd


def data_types(in_file, out_file):
    """
    :param in_files: (list) list of filenames (strings) for json files with app info
    :param categories: (list) list of category names (strings) corresponding to files
    :return: (df) dataframe containing number of apps collecting data for each purpose by category
    """

    # load json file to list of apps
    app_list = load_json(in_file)

    # dictionary to store number of apps collecting data for each purpose
    dict1 = {}

    # iterate over all apps in the current category and count the number of apps collecting data for each purpose
    for app in app_list:
        for purpose in app["data_linked"].keys():
            dict2 = {}
            #print("Purpose:", purpose)
            for broad_data_type in app["data_linked"].values():
                #print("Broad Data Type: ", broad_data_type)
                #print(type(broad_data_type.values()))
                for key in broad_data_type.keys():
                    for specific_data_type in broad_data_type[key]:
                        #print(specific_data_type)
                        if specific_data_type not in dict2:
                            dict2[specific_data_type] = 1
                        else:
                            dict2[specific_data_type] += 1
       
            for key in dict2:
                if key in dict1:
                    dict1[key] = dict1[key] + dict2[key]
                else:
                    dict1[key] = dict2[key]
    
    print(dict1)

        #break
        
            # if app["data_track"]:
            #     if "Tracking" not in purposes_dict:
            #         purposes_dict["Tracking"] = 1
                
            #     else:
            #         purposes_dict["Tracking"] += 1

        # sorts dictionary by value (increasing rating)
        # Source: https://realpython.com/sort-python-dictionary/
        #data_type_dict = dict(sorted(purposes_dict.items(), key=lambda item: item[1], reverse=True))

        # # create a dataframe from dictionary for each category
        # df = pd.DataFrame(purposes_dict, index=[0])
        # # add column for category name
        # df.insert(0, 'Category', categories[i])
        # # add dataframe to list of dataframes for all categories
        # dataframes.append(df)
   
    # # combine all dataframes
    # purposes_by_category = pd.concat(dataframes)

    # # save dataframe to csv file
    # purposes_by_category.to_csv(out_file, index = False)

    # return purposes_by_category


df = pd.read_csv('ios_data_types.csv')



# in_files = ["ios_apps.json", "ios_games.json", "ios_lifestyle.json", "ios_shopping.json", "ios_travel.json", "ios_health.json"]
# top_categories = ["All Apps", 'Games', 'Lifestyle', 'Shopping', 'Travel', 'Health & Fitness']
# data_types(in_files, top_categories, "ios_data_types.csv")


in_file = "ios_apps.json"
data_types(in_file, "test.csv")