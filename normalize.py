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
row_sums = df[columns_to_normalize].sum(axis=1)
print(row_sums)

for column in columns_to_normalize:
    
    #x_min = df[column].min()
    #x_max = df[column].max()
    #df[column] = (df[column] - x_min) / (x_max - x_min)

    column_sums = df[column].sum()
    df[column] = df[column].div(column_sums)
    column_sums = df[column].sum()




#min = df['energy'].min()
#max = df['energy'].max()
#df['energy'] = (df['energy'] - min) / (max - min)
#print(df)
#print(min,max)
#

# Specify the path for the CSV file with normalized values
normalized_file_path = 'normalized_data3.csv'

# Save the DataFrame with normalized values to a new CSV file
df.to_csv(normalized_file_path, index=False, float_format='%.6f')
df_read = pd.read_csv(normalized_file_path)
print(df_read[columns_to_normalize])

print(f"Normalized data saved to {normalized_file_path}")

