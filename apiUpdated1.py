#API_KEY: 6ed41b93c972fb7ce2677d2e7bfe943f
  #  api_url = 'http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&artist=radiohead&track=paranoid+android&api_key=6ed41b93c972fb7ce2677d2e7bfe943f&format=json'  # Replace with the URL of the API you want to call

import csv
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor


def make_api_call(api_url, parameter_name, parameter_artist):
    parameter_artist = parameter_artist[2:-2]
    parameter_name = parameter_name.replace(" ", "+")
    parameter_artist = parameter_artist.replace(" ", "+")

    api_url = f"http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&autocorrect=1&api_key=6ed41b93c972fb7ce2677d2e7bfe943f&format=json&track={parameter_name}&artist={parameter_artist}"
    
    response = requests.get(api_url)

    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
                return response.json()  
        else:
            return None
    except Exception as e:
        print(f'Error making API request: {e}')
        return None

csv_file_path = 'sample_tracks.csv'  

api_url = 'http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&api_key=6ed41b93c972fb7ce2677d2e7bfe943f&format=json'  


api_column_name = 'name' 
api_column_artist = 'artists'


max_workers = 2 # Adjust this number based on your preference
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    risultato_tag = []
    futures = []
    
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            api_parameter_name = row[api_column_name]
            api_parameter_artist = row[api_column_artist]
            api_result_future = executor.submit(make_api_call, api_url, api_parameter_name, api_parameter_artist)
            print(api_result_future)
            futures.append(api_result_future)
    
    # Wait for all futures to complete
    for future in futures:
        api_result = future.result()
        print(api_result)
        if api_result is None:
            risultato_tag.append("Errore")
        elif 'error' in api_result:
            risultato_tag.append("Errore")
        else:     
            tags_list = api_result['toptags']['tag']
            tag_names = [tag['name'] for tag in tags_list]
            if len(tag_names) == 0:
                risultato_tag.append("Errore")
            else:
                risultato_tag.append(tag_names)

df = pd.read_csv(csv_file_path, encoding='latin1')

new_column_values = risultato_tag
df['tags'] = new_column_values

filtered_df = df[df['tags'] != 'Errore']
filtered_csv_file = 'filtered_file.csv'
filtered_df.to_csv(filtered_csv_file, index=False)


df.to_csv(csv_file_path, index=False)
