import pandas as pd

# Define the file paths for the two CSV files you want to merge
file1_path = 'filtered_file1.csv'
file2_path = 'filtered_file2.csv'

# Read the CSV files into pandas DataFrames
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Merge the two DataFrames
merged_df = pd.concat([df1, df2], ignore_index=True)

# Remove duplicates based on all columns
merged_df = merged_df.drop_duplicates()

# Specify the path for the merged CSV file without duplicates
merged_file_path = 'merged_file_without_duplicates.csv'

# Save the merged DataFrame without duplicates to a new CSV file
merged_df.to_csv(merged_file_path, index=False)

print(f"Merged data without duplicates saved to {merged_file_path}")