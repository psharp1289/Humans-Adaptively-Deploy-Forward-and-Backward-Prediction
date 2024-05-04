import pandas as pd
import numpy as np

df=pd.read_csv('surveydata_study7.csv')

dictionary_survey={'Q1':'that a individual from ILLINOIS will work as a CHIROPRACTOR',
'Q2':'that a individual from NORTH CAROLINA will work as a PHYSICAL THERAPIST',
'Q3':'that a individual from MARYLAND (MD) will work as a MANAGER OF FOOD SERVICES',
'Q4':'that a individual from Massachusetts (MA) individual will work as a PHYSICAL THERAPIST'}

# Initialize an empty list to hold the sum of correct answers for each subject
sum_list = []

# Iterate over each row in the DataFrame
for idx, row in df.iterrows():
    sum_for_row = 0  # Initialize a sum for the current row/subject
    for query in ['Q1', 'Q2', 'Q3', 'Q4']:
        if row[query] == dictionary_survey[query]:
            sum_for_row += 1  # Add 1 to the sum if the answer is correct
    sum_list.append(sum_for_row/4.0)  # Append the sum for the current subject to the list

# Add the list of sums as a new column in the DataFrame
df['Sum'] = sum_list

df.to_csv('survey_with_scores.csv')

print(df)