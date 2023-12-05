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



response_mb='transition_reval_choice.keys'
mb_responses=['7','8','9','10']

mb_response={'1':['MB',1],
			 '2':['MB',1],
			 '3':['MB',9],
			 '4':['MB',9],
			 '5':['MB',1],
			 '6':['MB',1],
			 '7':['MB',9],
			 '8':['MB',9]}
mb_response2={'1':['MBL',1],
			 '2':['MBH',1],
			 '3':['MBL2',9],
			 '4':['MBH2',9],
			 '5':['MBL',1],
			 '6':['MBH',1],
			 '7':['MBL2',9],
			 '8':['MBH2',9]}

dict_index={1.0:0,9.0:1}
response='key_resp_25.keys'
mb_key='key_resp_31.keys'
trident='trident.png'
planet='planet.png'

rt_planning=[]
sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]
sub_names=[sub for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]

subs_csv=[['sub','SR Evidence','bias_highbaserate','pre_map_change','post_map_change','high_br','low_br']]

sub_num=0
for df in sub_dfs:
	sub_name=sub_names[sub_num]	

	evidence_successorRepresentation=0
	base_rate_high=0
	counter_planning=0
	tr_score=0
	rr_score=0
	high_br=0
	low_br=0
	

	for row in range(len(df[response])):

		if np.isfinite(df[response][row]):
			counter_planning+=1
			if counter_planning<11:
				query_num=str(int(df[im2][row]))
				q_type=dict_response[str(int(df[im2][row]))][0]
				if str(int(df[im2][row])) in mb_responses:
					if int(df[response][row])==rr_dict[str(int(df[im2][row]))][1]:
						rr_score+=1
						if rr_dict[str(int(df[im2][row]))][1]==2:
							high_br+=1
						else:
							low_br+=1



				if int(df[response][row])==dict_response[str(int(df[im2][row]))][1]: #

					if q_type=='successorRepresentation':
						evidence_successorRepresentation+=1

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

	

	current_row=[sub_names[sub_num],evidence_successorRepresentation/6.0,base_rate_high/4.0,rr_score/4.0,tr_score/4.0,high_br/2.0,low_br/2.0]
	subs_csv.append(current_row)
	sub_num+=1


with open('all_planning_questions_baseratebias_lowvshighbaserates.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)