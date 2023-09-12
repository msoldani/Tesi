import csv
import random

input_csv_path = 'tracks_features.csv'  # Replace with the path to your input CSV file
output_csv_path = 'sample_tracks.csv'  # Replace with the desired output file path

# Determine the number of rows you want in your sample
sample_size = 300  # Replace with the desired sample size

# Create a list of row indices to sample from
with open(input_csv_path, 'r', encoding="latin1") as input_file:
    csv_reader = csv.reader(input_file)
    header = next(csv_reader)  # Read the header row (optional)
    all_rows = list(csv_reader)

# Ensure the sample size is not greater than the total number of rows
sample_size = min(sample_size, len(all_rows))

# Use random.sample to get a random sample of row indices
sample_indices = random.sample(range(len(all_rows)), sample_size)

# Extract the sampled rows based on the random indices
sampled_rows = [all_rows[i] for i in sample_indices]

# Write the sampled rows to a new CSV file
with open(output_csv_path, 'w', newline='', encoding="latin1") as output_file:
    csv_writer = csv.writer(output_file)
    # Write the header row (if you have one)
    if header:
        csv_writer.writerow(header)
    # Write the sampled rows
    csv_writer.writerows(sampled_rows)

print(f"Randomly sampled {sample_size} rows and saved to {output_csv_path}")
