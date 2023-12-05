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
'1':['predecessorRepresentation',9],
'3':['predecessorRepresentation',9],
'4':['predecessorRepresentation',9],
'5':['predecessorRepresentation',9],
'2':['predecessorRepresentation',1],
'11':['predecessorRepresentation',1],
'13':['predecessorRepresentation',1],
'15':['predecessorRepresentation',1],
'17':['baseratebias',1],
'18':['baseratebias',1],
'21':['baseratebias',1],
'22':['baseratebias',1],
'25':['baseratebias',1],
'26':['baseratebias',1],
'29':['baseratebias',1], # D = bias for left side, which was high base-rate state
'30':['baseratebias',1]
}

rr_dict={'1':['predictive_representation_test',1],
			 '2':['predictive_representation_test',1],
			 '3':['predictive_representation_test',9],
			 '4':['predictive_representation_test',9],
			 '5':['predictive_representation_test',1],
			 '6':['predictive_representation_test',1],
			 '7':['predictive_representation_test',9],
			 '8':['predictive_representation_test',9]}

tr_dict={
'11':['predictive_representation_test_postmap',9],
'12':['predictive_representation_test_postmap',9],
'13':['predictive_representation_test_postmap',1],
'14':['predictive_representation_test_postmap',1]

}

response_mb='key_resp_31.keys'
mb_responses=['7','8','9','10']


dict_index={1.0:0,9.0:1}
response='key_resp_25.keys'
mb_key='key_resp_31.keys'
trident='trident.png'
planet='planet.png'
rt_planning='key_resp_25.rt'
planning_q='PR_vs_SR.thisIndex'
RT_all='click_action.rt'


sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]
sub_names=[sub for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]

subs_csv=[['sub','PR Evidence','bias_highbaserate','pre_map_change','post_map_change','rt_planning_pr','median_RT_actionselection','trial_num','planning_q','PR_individual_answers','experiment']]

sub_num=0
for df in sub_dfs:
	sub_name=sub_names[sub_num]
	print(sub_name)
	avg_RTs=[]
	evidence_predecessorRepresentation=0
	counter_planning=0
	rr_score=0
	tr_score=0
	pr_one=0
	base_rate_high=0
	rts_planning=[]
	planning_qs=[]
	trial_counter=[]
	pr_individual_answers=[]
	transition_revaluation=0
	for row in range(len(df[response])):
		if np.isfinite(df[RT_all][row]):
			avg_RTs.append(float(df[RT_all][row]))
		if np.isfinite(df[response][row]):
			counter_planning+=1
			
			if counter_planning<17:
				

				# planning_qs.append(float(df[planning_q2][row]))

				query_num=str(int(df[im2][row]))
				q_type=dict_response[str(int(df[im2][row]))][0]
				if q_type=='predecessorRepresentation':
					rts_planning.append(float(df[rt_planning][row]))
					trial_counter.append(counter_planning)
				if str(int(df[im2][row])) in mb_responses:
					if int(df[response][row])==rr_dict[str(int(df[im2][row]))][1]:
						rr_score+=1



				if int(df[response][row])==dict_response[str(int(df[im2][row]))][1]: #

					if q_type=='predecessorRepresentation':
						evidence_predecessorRepresentation+=1
						pr_individual_answers.append(1)


						

					if q_type=='baseratebias':
						base_rate_high+=1
				else:
					if q_type=='predecessorRepresentation':
						pr_individual_answers.append(0)




					
		
			
					
	for i in range(len(rts_planning)):
		current_row=[sub_name,evidence_predecessorRepresentation/8.0,base_rate_high/8.0,'','',rts_planning[i],'',trial_counter[i],np.median(avg_RTs),pr_individual_answers[i],5]
		subs_csv.append(current_row)

	# current_row=[sub_name,evidence_predecessorRepresentation/6.0,base_rate_high/4.0,rr_score/4.0,tr_score/4.0,np.median(rts_planning)]
	# subs_csv.append(current_row)
	sub_num+=1


with open('rts_planning.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)

