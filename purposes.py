from apps import *
import pandas as pd


def purposes(json_file, out_filename):
    # load json file to list of apps
    app_list = load_json(json_file)

    #print(type(data))
    purposes_dict = {}

    for app in app_list:
        for purpose in app["data_linked"].keys():
        
            if purpose not in purposes_dict:
                purposes_dict[purpose] = 1

            else:
                purposes_dict[purpose] += 1
        
        if app["data_track"]:
            if "data_track" not in purposes_dict:
                purposes_dict["data_track"] = 1
            
            else:
                purposes_dict["data_track"] += 1

    # sorts dictionary by value (increasing rating)
    # Source: https://realpython.com/sort-python-dictionary/
    purposes_dict = dict(sorted(purposes_dict.items(), key=lambda item: item[1], reverse=True))

    # write sorted dictionary to a new json file
    dump_json(purposes_dict, out_filename)

    df = pd.DataFrame(purposes_dict, index=[0])
    df.insert(0, 'Category', 'Games')
    print(df)
    return purposes_dict

top_categories = top_categories(load_json('ios_categories.json'))

# #get list of purposes for all ios game apps
# print(purposes("ios_games.json","ios_games_purposes.json"))
# #get list of purposes for all ios heath & fitness apps
# print(purposes("ios_health.json","ios_health_purposes.json"))
# #get list of purposes for all ios lifestyle apps
# print(purposes("ios_lifestyle.json","ios_lifestyle_purposes.json"))
# #get list of purposes for all ios shopping apps
# print(purposes("ios_shopping.json","ios_shopping_purposes.json"))
# #get list of purposes for all ios travel apps
# print(purposes("ios_travel.json","ios_travel_purposes.json"))
# #get list of purposes for all ios app types
# print(purposes("ios_apps.json","ios_purposes.json"))

#get list of purposes for all ios game apps
(purposes("ios_games.json","ios_games_purposes.json"))
#get list of purposes for all ios heath & fitness apps
(purposes("ios_health.json","ios_health_purposes.json"))
#get list of purposes for all ios lifestyle apps
(purposes("ios_lifestyle.json","ios_lifestyle_purposes.json"))
#get list of purposes for all ios shopping apps
(purposes("ios_shopping.json","ios_shopping_purposes.json"))
#get list of purposes for all ios travel apps
(purposes("ios_travel.json","ios_travel_purposes.json"))
#get list of purposes for all ios app types
(purposes("ios_apps.json","ios_purposes.json"))

