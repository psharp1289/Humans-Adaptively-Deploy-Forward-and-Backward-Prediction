import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
import numpy
import numpy as np
plt.rcParams["font.size"] = 12  # Replace 12 with the desired font size


# Define the icons as variables
trident = plt.imread("trident.png")
planet = plt.imread("planet.png")
bell = plt.imread("bell.png")
tree = plt.imread("tree.png")
fox = plt.imread("fox.png")
watch = plt.imread("watch.png")
train = plt.imread("train.png")
houses = plt.imread("houses.png")
compass = plt.imread("compass.png")
thermometer = plt.imread("thermometer.png")
microphone = plt.imread("microphone.png")
north = plt.imread("north.png")
snorkel = plt.imread("snorkel.png")
tophat = plt.imread("tophat.png")

# Define the transition probabilities based on the relative frequency list and dictionary
probabilities = {}

transitions=[['trident','planet'],

['bell']*72+['tree']*8+['watch']*72+['fox']*8,
['bell']*8+['tree']*152+['watch']*8+['fox']*152,

['houses']*48+['compass']*12+['train']*20,       
['houses']*24+['compass']*96+['thermometer']*40,
['microphone']*20+['north']*48+['snorkel']*12,            
['tophat']*40+['north']*24+['snorkel']*96]


state_transitions_dictionary={

#second stage
'trident':1,'planet':2,

'bell':3,'tree':4,'watch':5,'fox':6,

'houses':'end','compass':'end','train':'end','thermometer':'end','microphone':'end','tophat':'end','north':'end','snorkel':'end'

}
def list_to_counts_dict(lst):
	counts_dict = {}
	for item in lst:
		if item in counts_dict:
			counts_dict[item] += 1
		else:
			counts_dict[item] = 1
	return counts_dict


# Define the transition probabilities based on the relative frequency list and dictionary
n_states = len(state_transitions_dictionary)
max_transitions = max([len(sublist) for row in transitions for sublist in row])

for key, val in state_transitions_dictionary.items():
	if val != 'end':
		probabilities['{}_transitions'.format(key)]=[]

		transitions_temp=transitions[val]

		counts_dict = list_to_counts_dict(transitions_temp)
		sum_counts=sum(counts_dict.values())

		for key_i, val_i in counts_dict.items():
			probabilities['{}_transitions'.format(key)].append([key_i,val_i/sum_counts])

print(probabilities)
# Create a new figure
fig, ax = plt.subplots(figsize=(12, 6))

# Set the limits of the x and y axes
ax.set_xlim([0, 1.6])
ax.set_ylim([0.1, 1])

# Define the position and size of each icon
icon_positions = {
	'trident': (0.60, 0.8, 0.1, 0.1),
	'planet': (1.00, 0.8, 0.1, 0.1),
	'bell': (0.20, 0.5, 0.1, 0.1),
	'tree': (0.60, 0.5, 0.1, 0.1),
	'watch': (1.00, 0.5, 0.1, 0.1),
	'fox': (1.40, 0.5, 0.1, 0.1),
	'train': (0.10, 0.2, 0.1, 0.1),
	'houses': (0.30, 0.2, 0.1, 0.1),
	'compass': (0.50, 0.2, 0.1, 0.1),
	'thermometer': (0.70, 0.2, 0.1, 0.1),
	'microphone': (0.90, 0.2, 0.1, 0.1),
	'north': (1.10, 0.2, 0.1, 0.1),
	'snorkel': (1.30, 0.2, 0.1, 0.1),
	'tophat': (1.50, 0.2, 0.1, 0.1),
}

probs=[]
legend_handles=[]
labels=[]

# Updated function to highlight connections for a key state
def highlight_key_state_connections(ax, key_state, color, icon_positions, probabilities,type_plot,offset):

	PR_dictionary={'north_planet':0.38,
	'north_trident':0.62,
	'north_fox':0.33,
	'north_watch':0.67,
	'fox_planet':0.95,
	'fox_trident':0.05,
	'train_planet':0.10,
	'train_trident':0.90,
	'train_bell':1.00}

	SR_dictionary={'planet_fox':0.48,
	'planet_bell':0.02,
	'planet_tree':0.48,
	'planet_watch':0.02,
	'planet_compass':0.28,
	'planet_houses':0.09,
	'planet_thermometer':0.12,
	'planet_train':0.01,
	'planet_north':0.09,
	'planet_microphone':0.01,
	'planet_snorkel':0.28,
	'planet_tophat':0.12,
	'trident_fox':0.05,
	'trident_tree':0.05,
	'trident_bell':0.45,
	'trident_watch':0.45,
	'trident_compass':0.09,
	'trident_houses':0.28,
	'trident_thermometer':0.01,
	'trident_train':0.12,
	'trident_north':0.28,
	'trident_snorkel':0.09,
	'trident_microphone':0.12,
	'trident_tophat':0.01,}

	# Draw a colored box around the key state
	box = plt.Rectangle((icon_positions[key_state][0] - icon_positions[key_state][2] / 2,
						 icon_positions[key_state][1] - icon_positions[key_state][3] / 2),
						 icon_positions[key_state][2], icon_positions[key_state][3],
						 linewidth=2, edgecolor='black', facecolor='none',zorder=3)
	ax.add_patch(box)
	
	# Find all states that lead directly to the key state (incoming states)
	incoming_states = set()
	for state, transitions in probabilities.items():
		for transition, _ in transitions:
			if transition == key_state:
				incoming_states.add(state[:-12])

	# Find all states that the key state leads to directly (outgoing states)
	outgoing_states = set()
	if f"{key_state}_transitions" in probabilities:
		for transition, _ in probabilities[f"{key_state}_transitions"]:
			outgoing_states.add(transition)

	
	if type_plot=='PR':

		# Draw lines for all direct incoming connections to the key state
		for state in incoming_states:
			start_icon_position = icon_positions[state]
			end_icon_position = icon_positions[key_state]
			ax.plot([start_icon_position[0]+offset, end_icon_position[0]+offset],
					[start_icon_position[1]-0.05+offset, end_icon_position[1]+0.05+offset],
					color = plt.cm.get_cmap('Blues')(PR_dictionary['{}_{}'.format(key_state,state)]), linewidth=2.0, zorder=1)

		# Identify and plot lines for second-level predecessors leading to the direct predecessors
		second_level_predecessors = set()
		for state in incoming_states:
			for potential_predecessor, transitions in probabilities.items():
				for transition, _ in transitions:
					if transition == state and potential_predecessor != key_state:
						second_level_predecessors.add(potential_predecessor)
						start_icon_position = icon_positions[potential_predecessor[:-12]]
						end_icon_position = icon_positions[key_state]
						
						# Draw a line to the direct predecessor
						ax.plot([start_icon_position[0]+offset, end_icon_position[0]+offset],
								[start_icon_position[1]-0.05+offset, end_icon_position[1]+0.05+offset],
								color = plt.cm.get_cmap('Blues')(PR_dictionary['{}_{}'.format(key_state,state)]), linestyle='-', linewidth=2.0, zorder=1)  # Use dashed line for indirect connections

	if type_plot=='SR':
		# Draw lines for all outgoing connections
		for state in outgoing_states:
			start_icon_position = icon_positions[key_state]
			end_icon_position = icon_positions[state]
			ax.plot([start_icon_position[0]+offset, end_icon_position[0]+offset],
					[start_icon_position[1]+offset-0.05, end_icon_position[1]+offset+0.05],
					color = plt.cm.get_cmap('Reds')(SR_dictionary['{}_{}'.format(key_state,state)]/0.80), linewidth=2.0, zorder=1)


		# Additionally, find and color all indirect connections related to the key state
		for state in incoming_states.union(outgoing_states):
			if state != key_state:  # Avoid self-loop
				for transition, _ in probabilities.get(f"{state}_transitions", []):
					if transition != key_state and transition in icon_positions:  # Check if transition is a valid state
						start_icon_position = icon_positions[key_state]
						end_icon_position = icon_positions[transition]
						ax.plot([start_icon_position[0]+offset, end_icon_position[0]+offset],
								[start_icon_position[1]+offset-0.05, end_icon_position[1]+offset+0.05],
								color = plt.cm.get_cmap('Reds')(SR_dictionary['{}_{}'.format(key_state,transition)]/0.80), linestyle='-', linewidth=2.0)  # Dashed line for indirect connections

num_s_states=[12,12]
s_colors=['blue']
successor_states=['train']

offsets=[0,0]
i=0
for s_state in successor_states:
	highlight_key_state_connections(ax,  s_state, s_colors[i], icon_positions, probabilities, 'PR',offsets[i])
	legend_text='{} {}'.format(num_s_states[i],s_state)
	legend_handles.append(mpatches.Patch(color=s_colors[i], label=legend_text))
	labels.append(legend_text)
	i+=1

# highlight_key_state_connections(ax, 'tree', 'blue', icon_positions, probabilities, 'PR')

# Loop through each icon and add it to the plot
for icon_name, (x, y, width, height) in icon_positions.items():
	
	# Check if this icon is a terminal state
	if state_transitions_dictionary.get(icon_name, None) == 'end':
		icon_image = eval(icon_name)
		ax.imshow(icon_image, extent=[x - width / 2, x + width / 2, y - height / 2, y + height / 2], zorder=2)
		continue

	# Loop through the transitions for this icon and add arrows to the plot
	for i, (transition, probability) in enumerate(probabilities[f"{icon_name}_transitions"]):
		target_icon_position = icon_positions[transition]
		strength = probability
		
		# Define the arrow coordinates
		arrow_x = x
		arrow_y = y-0.05
		target_x = target_icon_position[0]
		target_y = target_icon_position[1]+0.06

		# Define the arrow color based on the strength of the transition
		if strength==0.475:
			strength+=0.10
		if strength==0.6:
			strength+=0.10
		if strength==0.05:
			strength+=0.05
		# arrow_color = plt.cm.get_cmap('gray').reversed()(strength)


		
	icon_image = eval(icon_name)
	ax.imshow(icon_image, extent=[x - width / 2, x + width / 2, y - height / 2, y + height / 2], zorder=2)

# Remove the axes ticks and labels
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])



# Add the arrow to the plot
# ax.arrow(
# arrow_x, arrow_y, target_x - arrow_x, target_y - arrow_y,
# head_width=0.015, head_length=0.02,linewidth=4.0, fc=arrow_color, ec=arrow_color
# )
# Call the new function after the original plot to highlight the 'compass' connections in orange

# Remove the axes border
ax.axis('off')

# Simulating 'probs' as a probability distribution for the purpose of creating the colorbar
# Create a colorbar using the Reds colormap with the simulated probabilities
sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(vmin=0, vmax=1.0))
cbar = plt.colorbar(sm, ax=ax, fraction=0.036, pad=0.04,orientation='horizontal')

# Set the colorbar label
cbar.set_label('p(s|s\')')


# Set the title of the plot and adjust position
plt.title('',pad=-120)  # Adjust the pad value as needed

# Optionally, adjust spacing manually
plt.subplots_adjust(top=0.2)

# # Adjust the layout
plt.tight_layout()


# Save and show the plot
plt.savefig('Train_PR_Fig1.png', dpi=300, bbox_inches='tight')
plt.show()
