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

sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6') and not sub.startswith('5acc65f668b65b00018db322')]
sub_names=[sub for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6') and not sub.startswith('5acc65f668b65b00018db322')]

dict_index={1.0:0,9.0:1}
response='key_resp_25.keys'
mb_key='key_resp_31.keys'
rt_planning='key_resp_24.rt'
rt_planning2='key_resp_25.rt'
planning_q='PR_vs_SR.thisIndex'
RT_all='click_action.rt'




subs_csv=[['sub','SR Evidence','bias_highbaserate','pre_map_change','post_map_change','rt_planning_pr','median_RT_actionselection','trial_num','planning_q','PR_individual_answers']]

sub_num=0
for df in sub_dfs:
	sub_name=sub_names[sub_num]
	print(sub_name)
	avg_RTs=[]
	evidence_successorRepresentation=0
	counter_planning=0
	rr_score=0
	tr_score=0
	pr_one=0
	base_rate_high=0
	rts_planning=[]
	planning_qs=[]
	pr_invidiual_qs=[]

	transition_revaluation=0
	for row in range(len(df[response])):
		if np.isfinite(df[RT_all][row]):
			avg_RTs.append(float(df[RT_all][row]))
		if np.isfinite(df[response][row]):
			counter_planning+=1
			if counter_planning<11:
				

				planning_qs.append(float(df[planning_q][row]))

				query_num=str(int(df[im2][row]))
				q_type=dict_response[str(int(df[im2][row]))][0]
				if q_type=='successorRepresentation':
					rts_planning.append(float(df[rt_planning2][row]))

				if str(int(df[im2][row])) in mb_responses:
					if int(df[response][row])==rr_dict[str(int(df[im2][row]))][1]:
						rr_score+=1



				if int(df[response][row])==dict_response[str(int(df[im2][row]))][1]: #

					if q_type=='successorRepresentation':
						evidence_successorRepresentation+=1
						pr_invidiual_qs.append(0)


					if q_type=='baseratebias':
						base_rate_high+=1

				else:
					if q_type=='successorRepresentation':
						pr_invidiual_qs.append(1)

				

			
			elif counter_planning>10:
				if int(df[response][row])==tr_dict[str(int(df[im2][row]))][1]:
						tr_score+=1
		try:
			if np.isfinite(df[response_mb][row]):
				if int(df[response_mb][row])==tr_dict[str(int(df[im2][row]))][1]:
						tr_score+=1
		except:
			j='not here'

					
	for i in range(len(rts_planning)):
		current_row=[sub_name,evidence_successorRepresentation/6.0,base_rate_high/4.0,rr_score/4.0,tr_score/4.0,rts_planning[i],np.median(avg_RTs),i+1,planning_qs[i],pr_invidiual_qs[i]]
		subs_csv.append(current_row)

	# current_row=[sub_name,evidence_predecessorRepresentation/6.0,base_rate_high/4.0,rr_score/4.0,tr_score/4.0,np.median(rts_planning)]
	# subs_csv.append(current_row)
	sub_num+=1


df = pd.DataFrame(subs_csv[1:], columns=subs_csv[0])
df=df.dropna()
df.to_csv('rts_planning.csv')


# with open('rts_planning.csv','w') as f:
# 	writer=csv.writer(f)
# 	writer.writerows(subs_csv)

