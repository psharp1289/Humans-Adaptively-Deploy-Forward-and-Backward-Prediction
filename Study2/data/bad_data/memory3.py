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

acceptable=['hammer.png','apple.png','window.png']
im1='s1_image'
im3='s3_image'
dict_response={1.0:'trident',9.0:'planet'}
dict_index={1.0:0,9.0:1}
response='resp4.keys'
trident='trident.png'
planet='planet.png'
sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.endswith('csv') and 'planning' not in sub]
sub_names=[sub for sub in os.listdir(os.curdir) if sub.endswith('csv') and 'planning' not in sub]
corrects=[1,1,9,1,1,9]

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
		if np.isfinite(df[response][row]):
			resp=dict_response[df[response][row]]
			if learning_reward_goal_list[index_im] in acceptable:

				if int(df[response][row])==corrects[ans_counter]:
					if corrects[ans_counter]==9:
						total_64+=1
					correct_ans=1

					totals+=1
					# dict_correct_twice[learning_reward_goal_list[index_im]]+=1
				else:
					correct_ans=0
				ans_counter+=1
				print(ans_counter)
			max_value = max(dict_image_history[learning_reward_goal_list[index_im]])
			max_index = dict_image_history[learning_reward_goal_list[index_im]].index(max_value)
			if dict_index[df[response][row]]==max_index:
				emp_corr=1
			else:
				emp_corr=0
			# current_row=[sub_name,learning_reward_goal_list[index_im],dict_image_history[learning_reward_goal_list[index_im]][0],dict_image_history[learning_reward_goal_list[index_im]][1],resp,correct_ans,emp_corr]
			# subs_csv.append(current_row)
			index_im+=1
			if index_im==18:
				index_im=0
			
	print('totals={}'.format(totals))
	num_non_repeat=0
	for value in dict_correct_twice.values():
		if value<2:
			num_non_repeat+=1

	current_row=[sub_name,totals/6.0]
	subs_csv.append(current_row)
	sub_num+=1


with open('planning_memory_quiz_performance_memory_totals_r3_2.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)