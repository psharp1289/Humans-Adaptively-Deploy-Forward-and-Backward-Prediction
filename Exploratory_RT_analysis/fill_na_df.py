import pandas as pd
import numpy as np

# Read data
df = pd.read_csv('all_rt_data.csv')

# Fill NA values with 0
df_filled = df
# Compute log_rt_planning
df_filled['log_rt_planning'] = np.log(df_filled['rt_planning_pr'])

# Calculate the mean and standard deviation of log_rt_planning
mean_log_rt = df_filled['log_rt_planning'].mean()
std_log_rt = df_filled['log_rt_planning'].std()
df_filled.to_csv('all_rt_data_filled.csv', index=False)

# Define a condition for the extreme values
condition = (df_filled['log_rt_planning'] < (mean_log_rt - 4*std_log_rt)) | (df_filled['log_rt_planning'] > (mean_log_rt + 4*std_log_rt))

# Remove the extreme values
df_no_extreme = df_filled[~condition]

# Save the cleaned DataFrame to a new CSV file
df_no_extreme.to_csv('all_rt_data_filled_no_extreme.csv', index=False)
