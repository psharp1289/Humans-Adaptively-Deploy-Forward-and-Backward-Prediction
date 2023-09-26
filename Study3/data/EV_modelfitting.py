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
'1':['successorRepresentation',1],
'2':['successorRepresentation',2],
'3':['successorRepresentation',3],
'4':['successorRepresentation',4],
'5':['successorRepresentation',1],
'6':['successorRepresentation',4],
'7':['baseratebias',2],
'8':['baseratebias',3],
'9':['baseratebias',3],
'10':['baseratebias',2],
}

rr_dict={
'7':['predictive_representation_test_premap',2],
'8':['predictive_representation_test_premap',8],
'9':['predictive_representation_test_premap',7],
'10':['predictive_representation_test_premap',2]

}

tr_dict={
'11':['predictive_representation_test_postmap',7],
'12':['predictive_representation_test_postmap',3],
'13':['predictive_representation_test_postmap',3],
'14':['predictive_representation_test_postmap',8]

}

df_EV=pd.read_csv('EVs.csv')

response_mb='transition_reval_choice.keys'
mb_responses=['7','8','9','10']


dict_index={1.0:0,9.0:1}
response='key_resp_25.keys'
mb_key='key_resp_31.keys'
trident='trident.png'
planet='planet.png'
rt_planning='key_resp_25.rt'
sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]
sub_names=[sub for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]

subs_csv=[['sub','choice','PR_EV','SR_EV','MB_EV','BR_EV']]

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
		if np.isfinite(df[response][row]):

			df_temp=df_EV[df_EV['trial_num']==df[im2][row]]
			df_temp=df_temp.reset_index(drop=True)
			counter_planning+=1
			if counter_planning<11:
				
				query_num=str(int(df[im2][row]))
				q_type=dict_response[str(int(df[im2][row]))][0]

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

						





				else:
					if int(df[response][row])==dict_response[str(int(df[im2][row]))][1]: #
						current_row.append(1)
						current_row.append(float(df_temp['PR_EV'][0]))
						current_row.append(float(df_temp['SR_EV'][0]))
						current_row.append(float(df_temp['MB_EV'][0]))
						current_row.append(float(df_temp['BR_EV'][0]))
						if q_type=='succEVecessorRepresentation':
						
							evidence_predecessorRepresentation+=1

							


						if q_type=='baseratebias':
							base_rate_high+=1
							
					else:
						current_row.append(0)
						current_row.append(float(df_temp['PR_EV'][0]))
						current_row.append(float(df_temp['SR_EV'][0]))
						current_row.append(float(df_temp['MB_EV'][0]))
						current_row.append(float(df_temp['BR_EV'][0]))
			
				
			elif counter_planning>10:
				if int(df[response][row])==tr_dict[str(int(df[im2][row]))][1]:

					tr_score+=1
		try:
			if np.isfinite(df[response_mb][row]):
				df_temp=df_EV[df_EV['trial_num']==df[im2][row]]
				df_temp=df_temp.reset_index(drop=True)
				if int(df[response_mb][row])==tr_dict[str(int(df[im2][row]))][1]:
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

		except:
			j='not here'
		if len(current_row)>2:
			subs_csv.append(current_row)

	sub_num+=1


with open('model_fitting_EV_allsubs.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)

