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

    # dictionary {purpose: {datatype: count}}
    dict1 = {}

    # iterate over all apps in the current category and count the number of apps collecting data for each purpose
    for app in app_list:
        #print("app")
        for purpose in app["data_linked"]:
            # dictionary {datatype: count}
            dict2 = {}
            #print("Purpose:", purpose)
            #print(app["data_linked"])
            for broad_data_type in app["data_linked"][purpose]:
                #print("Broad Data Type:", broad_data_type)
                #print(type(broad_data_type.values()))
                for specific_data_type in app["data_linked"][purpose][broad_data_type]:
                    #print("Specific Data Type:", specific_data_type)
                    #print(app["data_linked"][purpose][broad_data_type])
                    if specific_data_type not in dict2:
                        dict2[specific_data_type] = 1
                    else:
                        dict2[specific_data_type] += 1
                #print(dict2)

            #print("Purpose:", purpose, "Data Types: ", dict2)

            # add dict2 into dict1
            # if purpose already in dict1
            if purpose in dict1:
                # for every datatype in dict2
                for datatype in dict2:
                    # if datatype already in purpose of dict1
                    if datatype in dict1[purpose]:
                        # add count to existing count
                        dict1[purpose][datatype] = dict1[purpose][datatype] + dict2[datatype]
                    else:
                        # create new datatype:count item for that purpose
                        dict1[purpose][datatype] = dict2[datatype]
            # if purpose not in dict1, create a new purpose with dict2
            else:
                dict1[purpose] = dict2

            #print(dict2)
            #print(dict1)
            
    # write dictionary to a new json file
    dump_json(dict1, out_file)

    return dict1

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


#df = pd.read_csv('ios_data_types.csv')


in_file = "ios_apps.json"
out_file = "ios_data.json"
print(data_types(in_file, out_file))