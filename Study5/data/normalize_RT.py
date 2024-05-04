import pandas as pd
import numpy as np
from scipy.stats import zscore

# Load the data from the CSV file
df = pd.read_csv('rt_analysis.csv')

# Calculate normalized log RT
df['log_rt_planning'] = np.log(df['rt_planning_pr'] / df['median_RT_actionselection'])

# Calculate the z-score of PR Evidence across subjects
df['PR'] = zscore(df['PR Evidence'])

df.to_csv('rt_analysis.csv')
