import pandas as pd
import glob
import numpy as np

# Step 1: Collect subject files in the current directory
subject_files = glob.glob('[56]*.csv')

all_ages = []
all_gender = []

# Step 2: Loop through each subject file
for subject_file in subject_files:
    # Step 3: Get the exact name from the 'PROLIFIC_ID' column
    try:
        subject_data = pd.read_csv(subject_file)
        prolific_id = subject_data['PROLIFIC_PID'][0]
        
        # Step 4: Find the subject's row in "study6_demographics.csv"
        demographics = pd.read_csv('study3_demographics.csv')
        subject_row = demographics[demographics['Participant id'] == prolific_id]
        
        if not subject_row.empty:
            # Step 5: Get their age and gender
            age = float(subject_row['Age'].values[0])
            sex = subject_row['Sex'].values[0]
            sex = 1 if sex == 'Female' else 0
            
            all_ages.append(age)
            all_gender.append(sex)
    except Exception as e:
        print(f"Error processing file {subject_file}: {e}")

# Calculate average and standard deviation for age and gender
average_age = np.mean(all_ages)
sd_age = np.std(all_ages)
average_gender = np.mean(all_gender)
sd_gender = np.std(all_gender)

# Create a DataFrame for the summary statistics
summary_data = pd.DataFrame({
    'average_age': [average_age],
    'SD_age': [sd_age],
    'average_gender': [average_gender],
    'SD_gender': [sd_gender],
    'num_subjects':[len(all_ages)]
})

# Step 6: Save the DataFrame to a new CSV file
summary_data.to_csv('subjects_included_demographics.csv', index=False)

print("Summary CSV file has been created successfully.")
