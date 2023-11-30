import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
import numpy
import numpy as np
import matplotlib.colors as mcolors

import matplotlib.pyplot as plt
import numpy as np
import colorsys


# Function to create a colormap
def create_colormap(hue, saturation, n_colors=256):
    """
    Create a colormap that holds saturation and hue constant but varies luminance.
    Hue is given in degrees and saturation is from 0 to 1.
    """
    hue = hue / 360  # convert hue to [0, 1] for colorsys
    return [colorsys.hsv_to_rgb(hue, lum, saturation) for lum in np.linspace(0, 0.95, n_colors)]

# Specific hue for salmon color in degrees (around 6 degrees in the color wheel)
# and saturation of 1 (full saturation)
salmon_hue = 6  # hue for salmon color in degrees
saturation = 1  # full saturation

# Create colormap
salmon_colormap = create_colormap(salmon_hue, saturation)

# Create a color map object
salmon_cmap = mcolors.ListedColormap(salmon_colormap)

# Specific hue for salmon color in degrees (around 6 degrees in the color wheel)
# and saturation of 1 (full saturation)
blue_hue = 218.54  # hue for salmon color in degrees
saturation = 1  # full saturation

# Create colormap
blue_colormap = create_colormap(blue_hue, saturation)

# Create a color map object
blue_cmap = mcolors.ListedColormap(blue_colormap)


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
    if type_plot=='SR':
        box = plt.Rectangle((icon_positions[key_state][0] - icon_positions[key_state][2] / 2,
                             icon_positions[key_state][1] - icon_positions[key_state][3] / 2),
                             icon_positions[key_state][2], icon_positions[key_state][3],
                             linewidth=3.5, edgecolor=salmon_cmap(1.0), facecolor='white',zorder=3)
    if type_plot=='PR':
        box = plt.Rectangle((icon_positions[key_state][0] - icon_positions[key_state][2] / 2,
                             icon_positions[key_state][1] - icon_positions[key_state][3] / 2),
                             icon_positions[key_state][2], icon_positions[key_state][3],
                             linewidth=3.5, edgecolor=blue_cmap(1.0), facecolor='white',zorder=3)
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
            if PR_dictionary['{}_{}'.format(key_state,state)]<0.15:
                zor=1
            else:
                zor=2
            ax.plot([start_icon_position[0]+offset, end_icon_position[0]+offset],
                    [start_icon_position[1]-0.08+offset, end_icon_position[1]+0.05+offset],
                    color = blue_cmap(PR_dictionary['{}_{}'.format(key_state,state)]), linewidth=6.0, zorder=zor)


        # Identify and plot lines for second-level predecessors leading to the direct predecessors
        second_level_predecessors = set()
        for state in incoming_states:
            for potential_predecessor, transitions in probabilities.items():
                for transition, _ in transitions:
                    if transition == state and potential_predecessor != key_state:
                        second_level_predecessors.add(potential_predecessor)
                        start_icon_position = icon_positions[potential_predecessor[:-12]]
                        end_icon_position = icon_positions[key_state]
                        if PR_dictionary['{}_{}'.format(key_state,potential_predecessor[:-12])]<0.15:
                            zor=1
                        else:
                            zor=2
                        # Draw a line to the direct predecessor
                        ax.plot([start_icon_position[0]+offset, end_icon_position[0]+offset],
                                [start_icon_position[1]-0.08+offset, end_icon_position[1]+0.05+offset],
                                color = blue_cmap(PR_dictionary['{}_{}'.format(key_state,potential_predecessor[:-12])]), linestyle='-', linewidth=6.0, zorder=zor)  # Use dashed line for indirect connections

    if type_plot=='SR':
        # Draw lines for all outgoing connections
        for state in outgoing_states:
            if SR_dictionary['{}_{}'.format(key_state,state)]<0.15:
                zor=1
            else:
                zor=2
            start_icon_position = icon_positions[key_state]
            end_icon_position = icon_positions[state]
            ax.plot([start_icon_position[0]+offset, end_icon_position[0]+offset],
                    [start_icon_position[1]+offset-0.05, end_icon_position[1]+offset+0.08],
                    color = salmon_cmap(SR_dictionary['{}_{}'.format(key_state,state)]), linewidth=6.0, zorder=zor)


        # Additionally, find and color all indirect connections related to the key state
        for state in incoming_states.union(outgoing_states):
            if state != key_state:  # Avoid self-loop
                for transition, _ in probabilities.get(f"{state}_transitions", []):
                    if transition != key_state and transition in icon_positions:  # Check if transition is a valid state
                        start_icon_position = icon_positions[key_state]
                        end_icon_position = icon_positions[transition]
                        if SR_dictionary['{}_{}'.format(key_state,state)]<0.15:
                            zor=1
                        else:
                            zor=2
                        ax.plot([start_icon_position[0]+offset, end_icon_position[0]+offset],
                                [start_icon_position[1]+offset-0.05, end_icon_position[1]+offset+0.08],
                                color = salmon_cmap(SR_dictionary['{}_{}'.format(key_state,transition)]), linestyle='-', linewidth=6.0,zorder=zor)  # Dashed line for indirect connections

num_s_states=[12,12,4,3,2]
s_colors=['red','red','blue','blue','blue']
successor_states=['trident','planet','north','train','fox']
type_strategy=['SR','SR','PR','PR','PR']
rewarded_states={'fox':138,'train':168,'north':215}

offsets=[0,0,0,0,0,0]
index=0

font_size=22
for s_state in successor_states:
    # Create a new figure
    fig, ax = plt.subplots(figsize=(12, 6))

    # Set the limits of the x and y axes
    ax.set_xlim([0, 1.6])
    ax.set_ylim([0.1, 1])
    
    highlight_key_state_connections(ax,  s_state, s_colors[index], icon_positions, probabilities,type_strategy[index],offsets[index])
    legend_text='{} {}'.format(num_s_states[index],s_state)
    legend_handles.append(mpatches.Patch(color=s_colors[index], label=legend_text))
    labels.append(legend_text)


    # highlight_key_state_connections(ax, 'tree', 'blue', icon_positions, probabilities, 'PR')

    # Loop through each icon and add it to the plot
    for icon_name, (x, y, width, height) in icon_positions.items():
        
        # Check if this icon is a terminal state
        if state_transitions_dictionary.get(icon_name, None) == 'end':
            icon_image = eval(icon_name)
            ax.imshow(icon_image, extent=[x - width / 2, x + width / 2, y - height / 2, y + height / 2], zorder=4)
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

            if transition in rewarded_states.keys():
                if type_strategy[index]=='SR':
                    print('here')
                    ax.text(target_x-0.062, target_y-0.17, "{}".format(rewarded_states[transition]),fontsize=font_size,zorder=6)
                else:
                    if transition==s_state:
                        ax.text(target_x-0.062, target_y-0.17, "{}".format(rewarded_states[transition]),fontsize=font_size,zorder=6)
                       




            
        icon_image = eval(icon_name)
        ax.imshow(icon_image, extent=[x - width / 2, x + width / 2, y - height / 2, y + height / 2], zorder=4)

        
    # Remove the axes ticks and labels
    # ax.set_xticks([])
    # ax.set_yticks([])
    # ax.set_xticklabels([])
    # ax.set_yticklabels([])



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
    

    if type_strategy[index] == 'SR':
        sm = plt.cm.ScalarMappable(cmap=salmon_cmap)
        cbar = plt.colorbar(sm, ax=ax, fraction=0.036, orientation='horizontal')
        cbar.ax.get_xaxis().labelpad=-20
        cbar.set_label('p(s\'|s)', fontdict={'size': font_size})
        cbar.set_ticks([0, 1])
        cbar.ax.set_xticklabels(['0', '1'], fontsize=font_size)

    if type_strategy[index] == 'PR':

        print('colormap phase {}: {}\n'.format(s_state,type_strategy[i]))
        sm = plt.cm.ScalarMappable(cmap=blue_cmap)
        cbar = plt.colorbar(sm, ax=ax, fraction=0.036, orientation='horizontal')
        cbar.ax.get_xaxis().labelpad=-20
        cbar.set_label('p(s|s\')', fontdict={'size': font_size})
        cbar.set_ticks([0, 1])
        cbar.ax.set_xticklabels(['0', '1'], fontsize=font_size)

    # # Adjust the layout
    plt.tight_layout()

    # Save and show the plot
    plt.savefig('{}_{}_Fig1.png'.format(s_state,type_strategy[i]), dpi=300, bbox_inches='tight')
    index+=1
