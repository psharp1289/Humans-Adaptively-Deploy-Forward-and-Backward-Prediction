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
'1':['ASpredecessorRepresentation',1],
'2':['predecessorRepresentation',1],
'3':['ASpredecessorRepresentation',1],
'4':['predecessorRepresentation',1],
'5':['predecessorRepresentation',1],
'6':['predecessorRepresentation',1],
'7':['baseratebias',1],
'8':['baseratebias',1],
'9':['ASbaseratebias',1],
'10':['ASbaseratebias',1],
}

rr_dict={
'7':['predictive_representation_test_premap',1],
'8':['predictive_representation_test_premap',1],
'9':['predictive_representation_test_premap',9],
'10':['predictive_representation_test_premap',9]

}

rr_dict_action2={
'7':['predictive_representation_test_premap',2],
'8':['predictive_representation_test_premap',8],
'9':['predictive_representation_test_premap',2],
'10':['predictive_representation_test_premap',8]

}

tr_dict={
'11':['predictive_representation_test_postmap',9],
'12':['predictive_representation_test_postmap',9],
'13':['predictive_representation_test_postmap',1],
'14':['predictive_representation_test_postmap',1]

}

response_mb='transition_reval_choice.keys'
mb_responses=['7','8','9','10']


dict_index={1.0:0,9.0:1}
response='key_resp_25.keys'
mb_key='key_resp_31.keys'
response2='key_resp_36.keys'
trident='trident.png'
planet='planet.png'
sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]
subs=[x for x in os.listdir(os.curdir) if x.startswith('5') or x.startswith('6')]
sub_names=[x for x in os.listdir(os.curdir) if x.startswith('5') or x.startswith('6')]

subs_csv=[['sub','PR Evidence','bias_highbaserate','pre_map_change','post_map_change','two_step_planning']]

sub_num=0
for df in sub_dfs:
	sub_name=sub_names[sub_num]
	print(sub_name)
	
	evidence_predecessorRepresentation=0
	counter_planning=0
	rr_score=0
	twostep_planning_score=0
	tr_score=0
	pr_one=0
	base_rate_high=0

	transition_revaluation=0
	for row in range(len(df[response])):

		if np.isfinite(df[response][row]):
			counter_planning+=1
			if counter_planning<11:
				query_num=str(int(df[im2][row]))
				q_type=dict_response[str(int(df[im2][row]))][0]

				if str(int(df[im2][row])) in mb_responses:
					if int(df[response][row])==rr_dict[str(int(df[im2][row]))][1]:
						rr_score+=1
						if int(df[response2][row])==rr_dict_action2[str(int(df[im2][row]))][1]:
							twostep_planning_score+=1




				if int(df[response][row])==dict_response[str(int(df[im2][row]))][1]: #

					if q_type=='predecessorRepresentation':
						evidence_predecessorRepresentation+=1

					if q_type=='baseratebias':
						base_rate_high+=1
		
			
			elif counter_planning>10:
				if int(df[response][row])==tr_dict[str(int(df[im2][row]))][1]:
						tr_score+=1
		try:
			if np.isfinite(df[response_mb][row]):
				if int(df[response_mb][row])==tr_dict[str(int(df[im2][row]))][1]:
						tr_score+=1
		except:
			j='not here'

					

	current_row=[sub_name,evidence_predecessorRepresentation/4.0,base_rate_high/2.0,rr_score/4.0,tr_score/4.0,twostep_planning_score/4.0]
	subs_csv.append(current_row)
	sub_num+=1


with open('all_planning_questions_baseratebias2.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)

print('done')
