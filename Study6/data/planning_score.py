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
'1':['successorRepresentation',2],
'2':['successorRepresentation',1],
'3':['successorRepresentation',3],
'4':['successorRepresentation',4],
'7':['baseratebias',1],
'8':['baseratebias',1],
'9':['baseratebias',2],
'10':['baseratebias',2],
}

rr_dict={
'7':['predictive_representation_test_premap',1],
'8':['ASpredictive_representation_test_premap',6],
'9':['ASpredictive_representation_test_premap',7],
'10':['predictive_representation_test_premap',2]

}

rr_dict_action2={
'7':['predictive_representation_test_premap','a'],
'8':['predictive_representation_test_premap','k'],
'9':['predictive_representation_test_premap','k'],
'10':['predictive_representation_test_premap','a']

}

tr_dict={
'11':['predictive_representation_test_postmap',7],
'12':['predictive_representation_test_postmap',1],
'13':['predictive_representation_test_postmap',2],
'14':['predictive_representation_test_postmap',6]

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
response2='key_resp_34.keys'
response='key_resp_25.keys'
mb_key='key_resp_31.keys'
trident='trident.png'
planet='planet.png'
sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]

sub_names=[sub for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]

subs_csv=[['sub','SR Evidence','bias_highbaserate','pre_map_change','post_map_change','twostep_planning','num_correct_sr','num_correct_br']]

sub_num=0
for df in sub_dfs:
	sub_name=sub_names[sub_num]	

	evidence_successorRepresentation=0
	base_rate_high=0
	counter_planning=0
	tr_score=0
	rr_score=0
	total_correct=8
	num_correct_br=4
	num_correct_sr=4
	twostep_planning_score=0
	

	for row in range(len(df[response])):

		if np.isfinite(df[response][row]):
			counter_planning+=1
			if counter_planning<11:
				query_num=str(int(df[im2][row]))
				q_type=dict_response[str(int(df[im2][row]))][0]
				if str(int(df[im2][row])) in mb_responses:
					if int(df[response][row])==rr_dict[str(int(df[im2][row]))][1]:
						rr_score+=1
						if str(df[response2][row])==rr_dict_action2[str(int(df[im2][row]))][1]:
							twostep_planning_score+=1

				if int(df[response][row])=='a':
					if q_type=='successorRepresentation':
						# evidence_predecessorRepresentation+=1
						num_correct_sr-=1
						total_correct-=1
					if q_type=='baseratebias':
						# base_rate_high+=1
						num_correct_br-=1
						total_correct-=1
				elif int(df[response][row])=='k':
					if q_type=='successorRepresentation':
						# evidence_predecessorRepresentation+=1
						num_correct_sr-=1
						total_correct-=1
					if q_type=='baseratebias':
						# base_rate_high+=1
						num_correct_br-=1
						total_correct-=1




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

	

	current_row=[sub_names[sub_num],evidence_successorRepresentation/num_correct_sr,base_rate_high/num_correct_br,rr_score/4.0,tr_score/4.0,twostep_planning_score/4.0,num_correct_sr,num_correct_br]
	if total_correct>5:
		subs_csv.append(current_row)
		sub_num+=1
	else:
		print('\nBAD SUB: {}\n'.format(sub_name))



with open('all_planning_questions_baseratebias.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)