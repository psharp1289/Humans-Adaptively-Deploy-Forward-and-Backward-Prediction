import shutil
import pandas as pd

df_bad=pd.read_csv('bad_subs.csv')

for sub in df_bad.bad_sub_ids.unique():
	try:
		shutil.move(sub,'bad_subs/{}'.format(sub))
	except:
		print('already moved')



# dfb=dfa.groupby('subject', as_index=False).mean()
# for sub in dfb.subject.unique():
# 	if dfb[dfb['subject']==sub].optimal_delayed_score.mean()<0.34:
# 		shutil.copy(sub,'not_delayed/{}'.format(sub))
# 	else:
# 		shutil.copy(sub,'delayed/{}'.format(sub))
	
