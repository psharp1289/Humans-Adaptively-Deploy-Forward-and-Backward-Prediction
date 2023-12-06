import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os
import csv



learning_reward_goal_list=['planet.png','planet.png','planet.png','trident.png','trident.png',
'planet.png','planet.png','trident.png','planet.png','trident.png','trident.png',
'trident.png','planet.png','planet.png','trident.png','planet.png','planet.png','trident.png']

learning_reward_startingstate_list=[['train.png','hammer.png',2,7],
['compass.png','apple.png',5,6],
['snorkel.png','compass.png',1,5],
['apple.png','snorkel.png',6,1],
['compass.png','snorkel.png',5,1],
['train.png','compass.png',2,5],
['compass.png','train.png',5,2],
['apple.png','compass.png',6,5],
['train.png','hammer.png',2,7],
['snorkel.png','compass.png',1,5],
['train.png','compass.png',2,5],
['snorkel.png','hammer.png',1,7],
['north.png','hammer.png',3,7],
['apple.png','tophat.png',6,4],
['north.png','apple.png',3,6],
['train.png','apple.png',2,6],
['tophat.png','hammer.png',4,7],
['train.png','hammer.png',2,7]]

acceptable=['compass.png','houses.png','hammer.png','apple.png','window.png']
im1='s1_image'
im3='s3_image'

response='resp4.keys'
trident='trident.png'
planet='planet.png'
sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]
sub_names=[sub for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]

corrects=[2,'na','na','na','na','na','na','na',2,
'na','na','nq',3,'na','na',2,4,'na']


import math

dict_question={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,
9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0}

# subs_csv=[['sub','image','t_count','p_count','answer','correct','correct_by_history','percent_not_repeat']]
corrects_dict={}

for i in range(1,19):
	corrects_dict[i]=0
subs_csv=[['sub','totals']]

sub_num=0
for df in sub_dfs:
	print(df['participant'][10])
	try:
		if math.isnan(df['participant'][10]):
			sub_name=sub_names[sub_num]
	except:
		sub_name=sub_names[sub_num]
		
	# print('\n\nsub: {}'.format(sub_name))
	index_im=0
	ans_counter=0
	totals=0
	encounter_counter=0
	for row in range(len(df[response])):
		
		if np.isfinite(df[response][row]):
			encounter_counter+=1


			if encounter_counter>0:
				if int(df[response][row])==corrects[ans_counter]:
					corrects_dict[encounter_counter]+=1
					if encounter_counter>0:
						totals+=1
				else:
					if encounter_counter in dict_question.keys():
						dict_question[encounter_counter]+=1
				
				ans_counter+=1
				

	current_row=[sub_name,totals/5.0]
	subs_csv.append(current_row)
	sub_num+=1

dict_question=[key/32.0 for key in dict_question.values()]

print('Incorrects: {}'.format(dict_question))
				
with open('memory_score.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)