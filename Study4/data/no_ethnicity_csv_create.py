import pandas as pd
import re

# Load the CSV file
file_path = 'actual_data_realworld_PR.csv'
data = pd.read_csv(file_path)

# Define a list of column suffixes to remove
suffixes_to_remove = ['1', '2', '3', '5', '8', '12']

# Filter out columns with suffixes in the list
filtered_columns = [col for col in data.columns if not re.search(r'\D(' + '|'.join(suffixes_to_remove) + r')$', col)]

filtered_data = data[filtered_columns]

# Save the filtered data to a new CSV file
output_file_path = 'actual_data_realworld_PR_noethnicityqs.csv'
filtered_data.to_csv(output_file_path, index=False)

print(f"Filtered data saved to {output_file_path}")
