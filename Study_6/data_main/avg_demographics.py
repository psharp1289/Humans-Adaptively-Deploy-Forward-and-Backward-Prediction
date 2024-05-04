import pandas as pd
import glob
import numpy as np

# Step 1: Collect subject files in the current directory
subject_files = glob.glob('[56]*.csv')

all_ages = []
all_gender = []


# Step 4: Find the subject's row in "study6_demographics.csv"
demographics = pd.read_csv('study4_demographics.csv')
demographics['Sex'] = demographics['Sex'].replace({'Male': 0, 'Female': 1})
# Calculate average and standard deviation for age and gender
demographics['Age'] = pd.to_numeric(demographics['Age'], errors='coerce')
demographics['Sex'] = pd.to_numeric(demographics['Sex'], errors='coerce')

average_age = demographics['Age'].mean()
sd_age = demographics['Age'].std()
average_gender = demographics['Sex'].mean()
sd_gender = demographics['Sex'].std()

# Create a DataFrame for the summary statistics
summary_data = pd.DataFrame({
    'average_age': [average_age],
    'SD_age': [sd_age],
    'average_gender': [average_gender],
    'SD_gender': [sd_gender]
})

# Step 6: Save the DataFrame to a new CSV file
summary_data.to_csv('subjects_included_demographics.csv', index=False)

print("Summary CSV file has been created successfully.")
