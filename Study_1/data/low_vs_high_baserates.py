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


dict_response2={'1':['predecessorRepresentation',9],
'3':['predecessorRepresentation',9],
'4':['predecessorRepresentation',9],
'5':['predecessorRepresentation',9],
'2':['predecessorRepresentation',1],
'11':['predecessorRepresentation',1],
'13':['predecessorRepresentation',1], # predecessorRepresentation = backward-predictive representation
'15':['predecessorRepresentation',1],
'17':['bias_finalstate',1], # DS = distal bias
'18':['bias_finalstate',1],
'21':['bias_finalstate',9],
'22':['bias_finalstate',9],
'25':['bias_finalstate',1],
'26':['bias_finalstate',1],
'29':['bias_finalstate',9],
'30':['bias_finalstate',9]
}


mb_response={'1':['predictive_representation_test',1],
			 '2':['predictive_representation_test',1],
			 '3':['predictive_representation_test',9],
			 '4':['predictive_representation_test',9],
			 '5':['predictive_representation_test',1],
			 '6':['predictive_representation_test',1],
			 '7':['predictive_representation_test',9],
			 '8':['predictive_representation_test',9]}


dict_index={1.0:0,9.0:1}
response='key_resp_25.keys'
mb_key='key_resp_31.keys'
trident='trident.png'
planet='planet.png'
sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]
sub_csvs=[sub for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]

sub_names=[sub for sub in os.listdir(os.curdir) if sub.endswith('csv') and 'planning' not in sub]
subs_csv=[['sub','PR Evidence','bias_lowbaserate','bias_finalstate','pre_map_change','post_map_change','high_br','low_br']]


sub_num=0
for df in sub_dfs: #iterate over subjects
	df=df.reset_index(drop=True)
	sub_name=df.participant[0]
	counter_planning=0


	evidence_predecessorRepresentation=0
	bias_low_baserateediate=0
	distal_bias_score=0
	pre_map_change_score=0
	post_map_change_score=0
	high_br=0
	low_br=0
	for row in range(len(df[response])):

		if np.isfinite(df[response][row]):
			counter_planning+=1
			if counter_planning<17:
				q_type=dict_response[str(int(df[im2][row]))][0]


				q_type2=dict_response2[str(int(df[im2][row]))][0]
			

				if int(df[response][row])==dict_response[str(int(df[im2][row]))][1]: #

					if q_type=='predecessorRepresentation':
						evidence_predecessorRepresentation+=1

					if q_type=='baseratebias':
						bias_low_baserateediate+=1

				if int(df[response][row])==dict_response2[str(int(df[im2][row]))][1]:
					if q_type2=='bias_finalstate':
						distal_bias_score+=1


			#post-map change queries
			elif counter_planning>20 and counter_planning<25:
				if int(df[response][row])!=mb_response[str(int(df[im2][row]))][1]:
					post_map_change_score+=1
					

		#pre-map change queries
		elif np.isfinite(df[mb_key][row]):
			counter_planning+=1
			if counter_planning>16 and counter_planning<21:
				q_type=mb_response[str(int(df[im2][row]))][0]
				if int(df[mb_key][row])==mb_response[str(int(df[im2][row]))][1]:
					if q_type=='predictive_representation_test':
						pre_map_change_score+=1
					if mb_response[str(int(df[im2][row]))][1]==1:
						high_br+=1
					else:
						low_br+=1
			

	current_row=[sub_name,evidence_predecessorRepresentation/8.0,bias_low_baserateediate/8.0,distal_bias_score/8.0,pre_map_change_score/4.0,post_map_change_score/4.0,high_br/2.0,low_br/2.0]
	subs_csv.append(current_row)
	sub_num+=1



with open('all_planning_questions_baseratebias_lowvshighbaserates.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)