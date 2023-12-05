import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os
import csv



learning_reward_goal_list=['planet.png','planet.png','planet.png','trident.png','trident.png',
'planet.png','planet.png','trident.png','planet.png','trident.png','trident.png',
'trident.png','planet.png','planet.png','trident.png','planet.png','planet.png','trident.png']

learning_reward_startingstate_list=[['north.png','hammer.png',3,7],
['window.png','apple.png',9,8],
['snorkel.png','compass.png',4,6],
['apple.png','tophat.png',8,2],
['houses.png','snorkel.png',5,4],
['north.png','compass.png',3,6],
['houses.png','train.png',5,1],
['window.png','compass.png',9,6],
['train.png','hammer.png',1,7],
['snorkel.png','compass.png',4,6],
['tophat.png','compass.png',2,6],
['houses.png','north.png',5,3],
['apple.png','tophat.png',8,2],
['houses.png','train.png',5,1],
['window.png','hammer.png',9,7],
['train.png','apple.png',1,8],
['snorkel.png','apple.png',4,8],
['hammer.png','window.png',7,9]]


acceptable=['compass.png','houses.png','hammer.png','apple.png','window.png']
im1='s1_image'
im3='s3_image'

response='resp4.keys'
trident='trident.png'
planet='planet.png'
sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]
sub_names=[sub for sub in os.listdir(os.curdir) if sub.endswith('csv') and 'planning' not in sub]
corrects=['na','na','na','na','na','na','na','na','na',
'na','na','na',2,'na',7,1,4,7]


import math


# subs_csv=[['sub','image','t_count','p_count','answer','correct','correct_by_history','percent_not_repeat']]
corrects_dict={}

for i in range(1,19):
	corrects_dict[i]=0
subs_csv=[['sub','totals']]

sub_num=0
for df in sub_dfs:
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
				
				ans_counter+=1
				

	current_row=[sub_name,totals/5.0]
	subs_csv.append(current_row)
	sub_num+=1


with open('memory_score.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)