from apps import *
import pandas as pd
import csv


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

def datatype_table(in_file, out_file):
     # load json file to list of apps
    app_list = load_json(in_file)

    # dictionary {purpose: {datatype: count}}
    rows = {}

    # iterate over all apps in the current category and count the number of apps collecting data for each purpose
    for app in app_list:
        #print("app")
        for purpose in app["data_linked"]:
            if purpose not in rows:
                rows[purpose] = []
            for broad_data_type in app["data_linked"][purpose]:
                for specific_data_type in app["data_linked"][purpose][broad_data_type]:
                    if specific_data_type not in rows[purpose]:
                        rows[purpose].append(specific_data_type)
    print(rows)
    for purpose in rows.keys():
        rows[purpose].sort()
    print(rows)
    df = pd.DataFrame(rows)
    # saving the dataframe
    df.to_csv(out_file)
    print(df)

# in_file = "ios_apps.json"
# out_file = "ios_data.json"
# print(data_types(in_file, out_file))

datatype_table("ios_apps.json", "ios_data.csv")