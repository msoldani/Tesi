#API_KEY: 6ed41b93c972fb7ce2677d2e7bfe943f
  #  api_url = 'http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&artist=radiohead&track=paranoid+android&api_key=6ed41b93c972fb7ce2677d2e7bfe943f&format=json'  # Replace with the URL of the API you want to call

import csv
import requests
import pandas as pd


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


with open(csv_file_path, 'r',encoding='latin1') as file:
    csv_reader = csv.DictReader(file)
    
    risultato_tag = []
    for row in csv_reader:
        # Get the value from the specified column for the API call
        api_parameter_name = row[api_column_name]
        api_parameter_artist = row[api_column_artist]
        list(api_parameter_artist)
        # Make the API call using the obtained value
        api_result = make_api_call(api_url, api_parameter_name, api_parameter_artist)
        if "error" in api_result:
            risultato_tag.append("Errore")
        else:     
            tags_list = api_result['toptags']['tag']
            # Extract the 'name' values from each tag dictionary
            tag_names = [tag['name'] for tag in tags_list]
            # 'tag_names' now contains the individual tag names
            if len(tag_names) == 0:
                risultato_tag.append("Errore")
            else:
                risultato_tag.append(tag_names)

print(risultato_tag)

df = pd.read_csv(csv_file_path, encoding='latin1')

new_column_values = risultato_tag
df['tags'] = new_column_values

filtered_df = df[df['tags'] != 'Errore']
filtered_csv_file = 'filtered_file.csv'
filtered_df.to_csv(filtered_csv_file, index=False)


df.to_csv(csv_file_path, index=False)
