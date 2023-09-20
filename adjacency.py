import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load your data from the CSV file
data = pd.read_csv('normalized_data2.csv')

# Step 2: Select the columns of interest
columns_of_interest = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence']
data_subset = data[columns_of_interest]

# Step 3: Compute cosine similarity
cosine_sim_matrix = cosine_similarity(data_subset)

# Step 4: Save the cosine similarity matrix to a CSV file
cosine_sim_df = pd.DataFrame(cosine_sim_matrix, columns=data.index, index=data.index)
cosine_sim_df.to_csv('cosine_similarity_matrix.csv', index=False)
