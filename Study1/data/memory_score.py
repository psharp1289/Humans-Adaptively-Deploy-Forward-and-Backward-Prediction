import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os
import csv

learning_reward_goal_list=[
'compass.png', 
'snorkel.png',
'train.png',
'north.png',
'houses.png',
'tophat.png',
'compass.png',
'microphone.png',
'houses.png',
'snorkel.png',
'thermometer.png',
'tophat.png',
'train.png',
'north.png',
'thermometer.png',
'microphone.png']

im1='s1_image'
im3='s3_image'
dict_response={1.0:'trident',9.0:'planet'}
dict_index={1.0:0,9.0:1}
response='resp4.keys'
trident='trident.png'
planet='planet.png'
sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6')]
sub_names=[sub for sub in os.listdir(os.curdir) if sub.endswith('csv') and 'planning' not in sub]
corrects=[9,1,9,9,1,1,9,1]
subs_csv=[['sub','totals']]

sub_num=0
for df in sub_dfs:
	dict_image_history={'thermometer.png':0,'compass.png':0,'tophat.png':0, 'north.png':0,'train.png':0,'houses.png':0,'snorkel.png':0,'microphone.png':0}
	sub_name=sub_names[sub_num]
	print(sub_name)
	p=0
	t=0
	index_im=0
	ans_counter=0
	img_counter=0
	totals=0
	for row in range(len(df[response])):

		if np.isfinite(df[response][row]):
			dict_image_history[learning_reward_goal_list[img_counter]]+=1
			img_counter+=1
		

			resp=dict_response[df[response][row]]
			if dict_image_history[learning_reward_goal_list[img_counter-1]]>1:

				if int(df[response][row])==corrects[ans_counter]:
					print(ans_counter)
					ans_counter+=1
					totals+=1
	

			index_im+=1
			if index_im==16:
				index_im=0
			
	print('totals={}'.format(totals))
	current_row=[sub_name,(totals)/8.0]
	subs_csv.append(current_row)
	sub_num+=1


with open('planning_memory_quiz_performance_memory_totals.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)