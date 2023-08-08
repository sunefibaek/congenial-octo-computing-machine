import json
import requests
import pandas as pd

def import_joke(api_url):
    """
    import relevant libraries
    fetch json data from api
    flatten the json data returned from the api
    print the data to the console    
    """
    # fetch json data from api
    response = requests.get(api_url)
    # flatten the json data returned from the api
    json_data = json.loads(response.text)
    # print the data to the console
    print(json_data)
    # return the data
    return json_data

def convert_to_pandas(json_data):
    """
    convert json data to pandas dataframe
    print the data to the console
    """
    # convert json data to pandas dataframe
    df = pd.json_normalize(json_data)
    # print the data to the console
    # print(df)
    # return the data
    return df

convert_to_pandas(import_joke("https://v2.jokeapi.dev/joke/Programming?type=twopart"))