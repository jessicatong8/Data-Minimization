from apps import *
import pandas as pd


def data_types(in_files, categories, out_file):
    """
    :param in_files: (list) list of filenames (strings) for json files with app info
    :param categories: (list) list of category names (strings) corresponding to files
    :return: (df) dataframe containing number of apps collecting data for each purpose by category
    """
    # list to store dataframes for each category
    dataframes = []

    # iterate over all categories
    for i in range(len(in_files)):
        #print(i)
        # load json file to list of apps
        app_list = load_json(in_files[i])

        # dictionary to store number of apps collecting data for each purpose
        data_type_dict = {}

        # iterate over all apps in the current category and count the number of apps collecting data for each purpose
        for app in app_list:
            #print(i)
            for purpose in app["data_linked"].keys():
                print("Purpose:", purpose)
                for broad_data_type in app["data_linked"].values():
                    #print("Broad Data Type: ", broad_data_type)
                    #print(type(broad_data_type.values()))
                    for key in broad_data_type.keys():
                        for specific_data_type in broad_data_type[key]:
                            #print(specific_data_type)
                            if specific_data_type not in data_type_dict:
                                data_type_dict[specific_data_type] = 1
                            else:
                                data_type_dict[specific_data_type] += 1
                #print(i)
                print(data_type_dict)
                print(df.loc[0,purpose])
                
                df.loc[0, purpose] = data_type_dict
                print(df)
                break

            break
        
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



in_files = ["ios_apps.json", "ios_games.json", "ios_lifestyle.json", "ios_shopping.json", "ios_travel.json", "ios_health.json"]
top_categories = ["All Apps", 'Games', 'Lifestyle', 'Shopping', 'Travel', 'Health & Fitness']
data_types(in_files, top_categories, "ios_data_types.csv")


# in_files = ["ios_apps.json"]
# top_categories = ["All Apps", 'Games', 'Lifestyle', 'Shopping', 'Travel', 'Health & Fitness']
# data_types(in_files, top_categories, "ios_data_types.csv")