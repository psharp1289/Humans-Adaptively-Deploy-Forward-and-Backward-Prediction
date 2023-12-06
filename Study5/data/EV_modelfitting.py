import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os
import csv

im1='r1'
im2='trial_num'

#original
dict_response={
'2':['predecessorRepresentation',1,2],
'4':['predecessorRepresentation',1,2],
'5':['predecessorRepresentation',1,8],
'6':['predecessorRepresentation',1,8],
'7':['baseratebias',1,2],
'8':['baseratebias',1,8],
'9':['baseratebias',1,2],
'10':['baseratebias',1,8],
}
bad_trials=[1,3]
df_EV=pd.read_csv('EVs.csv')
rr_dict={
'7':['predictive_representation_test_premap',1,2],
'8':['predictive_representation_test_premap',1,8],
'9':['predictive_representation_test_premap',9,2],
'10':['predictive_representation_test_premap',9,8]

}

tr_dict={
'11':['predictive_representation_test_postmap',9,2],
'12':['predictive_representation_test_postmap',9,8],
'13':['predictive_representation_test_postmap',1,2],
'14':['predictive_representation_test_postmap',1,8]

}

response_mb='transition_reval_choice.keys'
response_mb2='transition_reval_choice_2.keys'
mb_responses=['7','8','9','10']


dict_index={1.0:0,9.0:1}
response='key_resp_25.keys'
mb_key='transition_reval_choice.keys'
response2='key_resp_36.keys'

mb_key2='transition_reval_choice_2.keys'
trident='trident.png'
planet='planet.png'
rt_planning='key_resp_25.rt'
sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]
sub_names=[sub for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]

subs_csv=[['sub','choice','PR_EV','SR_EV','MB_EV','BR_EV','PR_EV_TWO','SR_EV_TWO','MB_EV_TWO','BR_EV_TWO']]

sub_num=0
for df in sub_dfs:
	sub_name=sub_names[sub_num]
	print(sub_name)
	
	evidence_predecessorRepresentation=0
	counter_planning=0
	rr_score=0
	tr_score=0
	pr_one=0
	base_rate_high=0
	rts_planning=0
	transition_revaluation=0
	for row in range(len(df[response])):
		
		current_row=[sub_name]
		current_row2=[sub_name]

		if np.isfinite(df[response][row]):

			df_temp=df_EV[df_EV['trial_num']==df[im2][row]]
			df_temp=df_temp.reset_index(drop=True)
			counter_planning+=1
			if int(df[response][row])!=2 and int(df[response][row])!=8:
				if int(df[im2][row])<11:
					if int(df[im2][row]) not in bad_trials:
					
						query_num=str(int(df[im2][row]))
						
						try:

							if str(int(df[im2][row])) in mb_responses:

								if int(df[response][row])==rr_dict[str(int(df[im2][row]))][1]:
									rr_score+=1
									current_row.append(1)
									current_row.append(float(df_temp['PR_EV'][0]))
									current_row.append(float(df_temp['SR_EV'][0]))
									current_row.append(float(df_temp['MB_EV'][0]))
									current_row.append(float(df_temp['BR_EV'][0]))
								else:
									current_row.append(0)
									current_row.append(float(df_temp['PR_EV'][0]))
									current_row.append(float(df_temp['SR_EV'][0]))
									current_row.append(float(df_temp['MB_EV'][0]))
									current_row.append(float(df_temp['BR_EV'][0]))
								if int(df[response2][row])==rr_dict[str(int(df[im2][row]))][2]:
									current_row2.append(1)
									current_row2.append(float(df_temp['PR_EV_TWO'][0]))
									current_row2.append(float(df_temp['SR_EV_TWO'][0]))
									current_row2.append(float(df_temp['MB_EV_TWO'][0]))
									current_row2.append(float(df_temp['BR_EV_TWO'][0]))
								else:
									current_row2.append(0)
									current_row2.append(float(df_temp['PR_EV_TWO'][0]))
									current_row2.append(float(df_temp['SR_EV_TWO'][0]))
									current_row2.append(float(df_temp['MB_EV_TWO'][0]))
									current_row2.append(float(df_temp['BR_EV_TWO'][0]))




							else:
								if int(df[response][row])==dict_response[str(int(df[im2][row]))][1]: #
									current_row.append(1)
									current_row.append(float(df_temp['PR_EV'][0]))
									current_row.append(float(df_temp['SR_EV'][0]))
									current_row.append(float(df_temp['MB_EV'][0]))
									current_row.append(float(df_temp['BR_EV'][0]))
								
								else:
									current_row.append(0)
									current_row.append(float(df_temp['PR_EV'][0]))
									current_row.append(float(df_temp['SR_EV'][0]))
									current_row.append(float(df_temp['MB_EV'][0]))
									current_row.append(float(df_temp['BR_EV'][0]))
								if int(df[response2][row])==rr_dict[str(int(df[im2][row]))][2]:
									current_row2.append(1)
									current_row2.append(float(df_temp['PR_EV_TWO'][0]))
									current_row2.append(float(df_temp['SR_EV_TWO'][0]))
									current_row2.append(float(df_temp['MB_EV_TWO'][0]))
									current_row2.append(float(df_temp['BR_EV_TWO'][0]))
								else:
									current_row2.append(0)
									current_row2.append(float(df_temp['PR_EV_TWO'][0]))
									current_row2.append(float(df_temp['SR_EV_TWO'][0]))
									current_row2.append(float(df_temp['MB_EV_TWO'][0]))
									current_row2.append(float(df_temp['BR_EV_TWO'][0]))
						except:
							j='not here'
						
				elif int(df[im2][row])>10:
					if int(df[response][row])==tr_dict[str(int(df[im2][row]))][1]:

						tr_score+=1
				
		try:
			if np.isfinite(df[response_mb][row]):

				df_temp=df_EV[df_EV['trial_num']==df[im2][row]]
				df_temp=df_temp.reset_index(drop=True)
				print('h')
				if int(df[response_mb][row])!=2 and int(df[response_mb][row])!=8:
					if int(df[mb_key][row])==tr_dict[str(int(df[im2][row]))][1]:
						tr_score+=1
						current_row.append(1)
						current_row.append(float(df_temp['PR_EV'][0]))
						current_row.append(float(df_temp['SR_EV'][0]))
						current_row.append(float(df_temp['MB_EV'][0]))
						current_row.append(float(df_temp['BR_EV'][0]))
					else:
						current_row.append(0)
						current_row.append(float(df_temp['PR_EV'][0]))
						current_row.append(float(df_temp['SR_EV'][0]))
						current_row.append(float(df_temp['MB_EV'][0]))
						current_row.append(float(df_temp['BR_EV'][0]))
				# if int(df[mb_key2][row])==tr_dict[str(int(df[im2][row]))][2]:
				# 	current_row2.append(1)
				# 	current_row2.append(float(df_temp['PR_EV_TWO'][0]))
				# 	current_row2.append(float(df_temp['SR_EV_TWO'][0]))
				# 	current_row2.append(float(df_temp['MB_EV_TWO'][0]))
				# 	current_row2.append(float(df_temp['BR_EV_TWO'][0]))
				# else:
				# 	current_row2.append(0)
				# 	current_row2.append(float(df_temp['PR_EV_TWO'][0]))
				# 	current_row2.append(float(df_temp['SR_EV_TWO'][0]))
				# 	current_row2.append(float(df_temp['MB_EV_TWO'][0]))
				# 	current_row2.append(float(df_temp['BR_EV_TWO'][0]))

		except:
			j='not here'

		if len(current_row)>2:
			subs_csv.append(current_row)
		if len(current_row2)>2:
			subs_csv.append(current_row2)

	sub_num+=1


with open('model_fitting_EV_allsubs.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)

