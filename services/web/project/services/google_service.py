import random
import pandas as pd
from project.functions.parse_ads_data import parse_ads_data
from project.functions.check_fileformat import check_fileformat
# google service


def get_google_ads_usage(api_key):
    # TODO:this function should download report through API
    # return nothing
    pass


def get_google_impression_count(api_key):
    # dummy
    return random.randint(0, 2500)


def get_new_data(file_name):
    
    file = pd.read_csv(file_name)
    current_usage = parse_ads_data(file)

    for key, value in current_usage.items():
        is_correct = check_fileformat(value)
        if(is_correct == False):
            print(f'Budget limit of campaign {key} is not an integer')
        else:
            current_usage[key] = int(value)


    return current_usage, file