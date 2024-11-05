from apps import load_json, dump_json
import pandas as pd



def data_types(json_file, out_filename):
    # load json file to list of apps
    app_list = load_json(json_file)

    #print(type(data))
    data_types_dict = {}

    for app in app_list:
        for data_type in app["data_linked"].values():
        
            if data_type not in data_types_dict:
                data_types_dict[data_type] = 1

            else:
                data_types_dict[data_type] += 1
        
        for data_type in app["data_track"].values():
            if data_type not in data_types_dict:
                data_types_dict[data_type] = 1
            
            else:
                data_types_dict[data_type] += 1

    # sorts dictionary by value (increasing rating)
    # Source: https://realpython.com/sort-python-dictionary/
    data_types_dict = dict(sorted(data_types_dict.items(), key=lambda item: item[1], reverse=True))

    # write sorted dictionary to a new json file
    dump_json(data_types_dict, out_filename)

    df = pd.DataFrame.from_dict(data_types_dict, index=[0])
    print(df)
    return data_types_dict


#get list of purposes for all ios game apps
print(data_types("ios_games.json","ios_games_purposes.json"))
#get list of purposes for all ios heath & fitness apps
print(data_types("ios_health.json","ios_health_purposes.json"))
#get list of purposes for all ios lifestyle apps
print(data_types("ios_lifestyle.json","ios_lifestyle_purposes.json"))
#get list of purposes for all ios shopping apps
print(data_types("ios_shopping.json","ios_shopping_purposes.json"))
#get list of purposes for all ios travel apps
print(data_types("ios_travel.json","ios_travel_purposes.json"))
#get list of purposes for all ios app types
print(data_types("ios_apps.json","ios_purposes.json"))




