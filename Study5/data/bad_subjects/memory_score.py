import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import shutil

def move_file(source_path, destination_path):
	import shutil
	try:
		shutil.move(source_path, destination_path)
		print("File moved successfully.")
	except FileNotFoundError:
		print("Source file not found.")
	except PermissionError:
		print("Permission denied. Unable to move the file.")
	except shutil.Error as e:
		print(f"Error occurred while moving the file: {e}")

# Example usage
source_file = "path/to/source/file.txt"
destination_directory = "path/to/destination/directory/"

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
response2='resp4_3.keys'
trial_num2='trials_2.thisIndex'

dict_secondstage={7:2,
1:8,
4:8,
3:2,
5:2,
0:2,
2:2,
8:8,
6:8}

subs=[x for x in os.listdir(os.curdir) if x.startswith('5') or x.startswith('6')]

sub_names=[x for x in os.listdir(os.curdir) if x.startswith('5') or x.startswith('6')]
sub_dfs=[pd.read_csv(sub) for sub in os.listdir(os.curdir) if sub.startswith('5') or sub.startswith('6') and sub.endswith('csv')]

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
		if np.isfinite(df[response2][row]):
			if int(df[trial_num2][row])>4:
				if dict_secondstage[int(df[trial_num2][row])]==int(df[response2][row]):
					totals+=1

			
	print('totals={}'.format(totals))
	

	current_row=[sub_name,totals/9.0]
	subs_csv.append(current_row)
	if (totals/9.0)<0.7:
		move_file(subs[sub_num], 'rb/{}'.format(subs[sub_num]))

	sub_num+=1
	


with open('memory_totals2.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(subs_csv)