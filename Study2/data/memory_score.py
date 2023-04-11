import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os
import csv



#key variables
learning_reward_goal_list=['snorkel.png','tophat.png','houses.png',
'north.png','train.png','hammer.png','apple.png','window.png',
'compass.png','tophat.png','snorkel.png','train.png','north.png',
'hammer.png','apple.png','houses.png','compass.png','window.png']

['snorkel.png','tophat.png','houses.png',
'north.png','train.png','hammer.png','apple.png','window.png',
'compass.png','tophat.png','snorkel.png','train.png','north.png',
'hammer.png','apple.png','houses.png','compass.png','window.png']

acceptable=['compass.png','houses.png','hammer.png','apple.png','window.png']
im1='s1_image'
im3='s3_image'
dict_response={1.0:'trident',9.0:'planet'}
dict_index={1.0:0,9.0:1}
response='resp4.keys'
trident='trident.png'
planet='planet.png'
sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.endswith('csv') and 'planning' not in sub]
sub_names=[sub for sub in os.listdir(os.curdir) if sub.endswith('csv') and 'planning' not in sub]
corrects=[1,1,9,9,9]

# subs_csv=[['sub','image','t_count','p_count','answer','correct','correct_by_history','percent_not_repeat']]
subs_csv=[['sub','totals','correct_on_6040']]

sub_num=0
for df in sub_dfs:
	dict_correct_twice={
	'compass.png':0, 
	'snorkel.png':0,
	'train.png':0,
	'north.png':0,
	'houses.png':0,
	'tophat.png':0,
	'microphone.png':0,
	'thermometer.png':0}
	dict_image_history={'hammer.png':[0,0],'compass.png':[0,0],'tophat.png':[0,0], 'north.png':[0,0],'train.png':[0,0],'houses.png':[0,0],'snorkel.png':[0,0],'apple.png':[0,0],'window.png':[0,0]}
	sub_name=sub_names[sub_num]
	print(sub_name)
	p=0
	t=0
	index_im=0
	ans_counter=0
	totals=0
	total_64=0
	for row in range(len(df[response])):
		if df[im1][row]==trident:
			dict_image_history[df[im3][row]][0]+=1
		elif df[im1][row]==planet:
			dict_image_history[df[im3][row]][1]+=1
		if np.isfinite(df[response][row]): #valid response
			resp=dict_response[df[response][row]]
			if learning_reward_goal_list[index_im] in acceptable: #where fwd and bwd planning agree on policy
				if ans_counter>4:
					if int(df[response][row])==corrects[ans_counter-5]:
							totals+=1
			
				ans_counter+=1

			max_value = max(dict_image_history[learning_reward_goal_list[index_im]])
			max_index = dict_image_history[learning_reward_goal_list[index_im]].index(max_value)
			
			index_im+=1
			if index_im==18:
				index_im=0
			
	print('totals={}'.format(totals))
	

	current_row=[sub_name,totals/5.0]
	subs_csv.append(current_row)
	sub_num+=1


with open('memory_totals.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)