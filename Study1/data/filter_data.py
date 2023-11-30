import pandas as pd

# Create a sample DataFrame
data1 = 'all_subs_Study1_actionvaluesrounded_PRvsGuessing.csv'
data2 = 'all_subs_Study1_actionvaluesrounded_restofqueries.csv'
df1 = pd.read_csv(data1)
df2 = pd.read_csv(data2)
df=pd.concat([df1,df2],axis=0)

# List of acceptable column prefixes
acceptable_column_prefixes = ['pr_many____ev_prob', 'sr_many____ev_prob', 'pr_one____prob_prob', 'sr_one____prob_prob',
'pr_many____ev_rwd', 'sr_many____ev_rwd', 'pr_one____prob_rwd', 'sr_one____prob_rwd','sub_num','choices']

# Create a regex pattern to match any of the acceptable prefixes
prefix_pattern = '|'.join(acceptable_column_prefixes)

# Filter the DataFrame based on the column prefixes
filtered_df = df.filter(regex=f'^({prefix_pattern})')


filtered_df.to_csv('filtered_data_study1_modelcomparison.csv')