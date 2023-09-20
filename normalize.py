import pandas as pd

# Define the file path for the CSV file
csv_file_path = 'merged_file.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)
columns_to_normalize = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence']

# Normalize each row so that the sum is equal to 1
#col_sum = df[columns_to_normalize].div(df[columns_to_normalize].sum(axis=0))
#normalized_data = df[columns_to_normalize]/ col_sum
#df[columns_to_normalize] = df[columns_to_normalize].div(df[columns_to_normalize].sum(axis=0), axis=1)

# Normalize each column so that the sum is equal to 1
#df[columns_to_normalize] = df[columns_to_normalize].div(df[columns_to_normalize].sum(axis=1), axis=0)

# Normalize each row so that the sum is equal to 1
row_sums = df[columns_to_normalize].sum(axis=1)
df[columns_to_normalize] = df[columns_to_normalize].div(row_sums, axis=0)


column_sums = df[columns_to_normalize].sum()
df[columns_to_normalize] = df[columns_to_normalize].div(column_sums, axis=1)

# Specify the path for the CSV file with normalized values
normalized_file_path = 'normalized_data2.csv'

# Save the DataFrame with normalized values to a new CSV file
df.to_csv(normalized_file_path, index=False)

print(f"Normalized data saved to {normalized_file_path}")

