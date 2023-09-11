#API_KEY: 6ed41b93c972fb7ce2677d2e7bfe943f
  #  api_url = 'http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&artist=radiohead&track=paranoid+android&api_key=6ed41b93c972fb7ce2677d2e7bfe943f&format=json'  # Replace with the URL of the API you want to call

import csv
import requests
import json
import pandas as pd

# Function to make an API call
def make_api_call(api_url, parameter_name, parameter_artist):
    parameter_artist = parameter_artist[2:-2]
    parameter_name = parameter_name.replace(" ", "+")
    parameter_artist = parameter_artist.replace(" ", "+")

    api_url = f"http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&autocorrect=1&api_key=6ed41b93c972fb7ce2677d2e7bfe943f&format=json&track={parameter_name}&artist={parameter_artist}"
    
    response = requests.get(api_url)
    #print(parameter_name, parameter_artist, concatenated_string)
    try:
        response = requests.get(api_url)

        content = response.text
        
        if response.status_code == 200:
            if "error" in content:
                return ""
            else:
                return response.json()  # Assuming the API response is in JSON format
        else:
            return None
    except Exception as e:
        print(f'Error making API request: {e}')
        return None


# Input CSV file path
csv_file_path = 'sample_tracks.csv'  # Replace with your input CSV file path

# URL of the API you want to call
api_url = 'http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&api_key=6ed41b93c972fb7ce2677d2e7bfe943f&format=json'  # Replace with the URL of the API you want to call
#&artist=radiohead&track=paranoid+android

# Name of the CSV column to use for API calls
api_column_name = 'name'  # Replace with the actual column name
api_column_artist = 'artists'

# Read the CSV file and make API calls for each row
with open(csv_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        # Get the value from the specified column for the API call
        api_parameter_name = row[api_column_name]
        api_parameter_artist = row[api_column_artist]
        list(api_parameter_artist)
        # Make the API call using the obtained value
        api_result = make_api_call(api_url, api_parameter_name, api_parameter_artist)
        if "error" not in api_result:
            print("Ciao")
        #print(api_result['error'])



        #if api_result is not None:
            # Process or print the API result as needed
        #   print(f'API result for row with {api_column_name}={api_parameter_value}: {api_result}')
        #else:
        #    print(f'API call failed for row with {api_column_name}={api_parameter_value}')

