import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
csv_file = 'easier_probability_trials2.csv'
df = pd.read_csv(csv_file)

# Create a mask for rows with 'trident.png' in s3_image column
trident_mask = df['s3_image'] == 'trident.png'

# Create a list to store rearranged rows
rearranged_rows = []

i = 0
while i < len(df):
    row = df.loc[i]
    rearranged_rows.append(row)

    if trident_mask[i]:
        j = i + 1
        while j < len(df) and not (df.loc[j, 's1_image'].endswith('.png') and
                                    df.loc[j, 's1_image'] in ['snorkel.png', 'train.png', 'north.png', 'tophat.png']):
            rearranged_rows.append(df.loc[j])
            j += 1

        for _ in range(2):
            if j < len(df) and df.loc[j, 's1_image'].endswith('.png'):
                new_row = df.loc[j].copy()
                new_row['s3_image'] = 'planet.png'
                rearranged_rows.append(new_row)
                j += 1

    i += 1

# Create a new DataFrame with the rearranged rows
new_df = pd.DataFrame(rearranged_rows)

# Save the updated DataFrame to a new CSV file
output_csv = 'updated_file.csv'
new_df.to_csv(output_csv, index=False)
