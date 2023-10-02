import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# Step 1: Load your data from the CSV file
data = pd.read_csv('normalized_data3.csv')

# Step 2: Select the columns of interest
columns_of_interest = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence']
data_subset = data[columns_of_interest].astype(np.float32)

# Step 3: Compute cosine similarity
cosine_sim_matrix = cosine_similarity(data_subset)

# Step 4: Save the cosine similarity matrix to a CSV file
cosine_sim_df = pd.DataFrame(cosine_sim_matrix, columns=data.index, index=data.index)
cosine_sim_df.to_csv('cosine_similarity_matrix.csv', index=False)

"""

import numpy as np
from scipy.spatial import distance
from scipy.sparse import lil_matrix, save_npz

# Step 1: Load your data from the CSV file
data = pd.read_csv('normalized_data3.csv')

# Step 2: Select the columns of interest
columns_of_interest = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence']
data_subset = data[columns_of_interest].astype(np.float32)

# Define the batch size
batch_size = 1000  # Adjust this based on your available RAM

# Initialize a sparse matrix to store the cosine similarity
num_samples = len(data_subset)
cosine_sim_sparse = lil_matrix((num_samples, num_samples), dtype=np.float32)

# Step 3: Compute cosine similarity in batches
for i in range(0, num_samples, batch_size):
    print(i)
    batch_data = data_subset.iloc[i:i+batch_size]
    cosine_sim_batch = 1 - distance.cdist(batch_data, data_subset, metric='cosine')
    cosine_sim_sparse[i:i+batch_size, :] = cosine_sim_batch

# Step 4: Save the sparse cosine similarity matrix
save_npz('cosine_similarity_matrix.npz', cosine_sim_sparse)
"""