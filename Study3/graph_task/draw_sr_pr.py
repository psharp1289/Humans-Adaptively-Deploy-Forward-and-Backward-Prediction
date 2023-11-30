import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
import numpy
import matplotlib.patches as mpatches
import matplotlib
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


plt.rcParams["font.size"] = 14  # Replace 12 with the desired font size


# Define the icons as variables
trident = plt.imread("trident.png")
planet = plt.imread("planet.png")
bell = plt.imread("bell.png")
tree = plt.imread("tree.png")
fox = plt.imread("fox.png")
unicorn = plt.imread("unicorn.png")

watch = plt.imread("watch.png")
train = plt.imread("train.png")
houses = plt.imread("houses.png")
compass = plt.imread("compass.png")
thermometer = plt.imread("thermometer.png")
microphone = plt.imread("microphone.png")
north = plt.imread("north.png")
snorkel = plt.imread("snorkel.png")
tophat = plt.imread("tophat.png")
hammer = plt.imread("hammer.png")
apple = plt.imread("apple.png")
window = plt.imread("window.png")

# Define the transition probabilities based on the relative frequency list and dictionary
probabilities = {}
transitions=[ #choice 1
              ['train'],
    
             # transition stage 1
             ['tree']*20,
              ['tree']*20,
              ['bell']*20,
              ['bell']*20,
              ['watch']*20,
              ['watch']*20,
              ['fox']*20,
              ['fox']*20,
              ['unicorn']*20,
             
             #transition stage 2
             ['trident']*4+['planet']*6,
             ['trident']*4+['planet']*6,
             ['trident']*6+['planet']*4,
             ['trident']*20,
             ['planet']*20]


    
state_transitions_dictionary={

'trident':'end','planet':'end',
    
'bell':10,'tree':11,'watch':12,'fox':13,'unicorn':14,
    
'train':3,'tophat':4,'north':1,'snorkel':2,'houses':5,'compass':6,'hammer':7,'apple':8,'window':9,
 
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
            probabilities['{}_transitions'.format(key)].append([key_i,round((val_i/sum_counts),2)])





# Define the position and size of each icon
icon_positions = {
    'trident': (0.75, 0.3, 0.1, 0.1),
    'planet': (1.05, 0.3, 0.1, 0.1),
    'bell': (0.70, 0.5, 0.1, 0.1),
    'tree': (0.40, 0.5, 0.1, 0.1),
    'watch': (0.90, 0.5, 0.1, 0.1),
    'fox': (1.10, 0.5, 0.1, 0.1),
    'unicorn': (1.40, 0.5, 0.1, 0.1),
    
    
    'north': (0.15, 0.8, 0.1, 0.1),
    'snorkel': (0.35, 0.8, 0.1, 0.1),
    'train': (0.55, 0.8, 0.1, 0.1),
    'tophat': (0.75, 0.8, 0.1, 0.1),
    'houses': (0.90, 0.8, 0.1, 0.1),
    'compass': (1.05, 0.8, 0.1, 0.1),
    'hammer': (1.25, 0.8, 0.1, 0.1),
    'apple': (1.45, 0.8, 0.1, 0.1),
    'window': (1.65, 0.8, 0.1, 0.1)
}




# Updated function to highlight connections for a key state
def highlight_key_state_connections(ax, key_state, color, icon_positions, probabilities,type_plot,offset):

    
    PR_dictionary={'planet_unicorn':0.13,
    'planet_bell':0.25,
    'planet_tree':0.25,
    'planet_watch':0.37,
    'planet_compass':0.18,
    'planet_houses':0.18,
    'planet_window':0.13,
    'planet_train':0.12,
    'planet_north':0.12,
    'planet_snorkel':0.12,
    'planet_tophat':0.12,
    }

    SR_dictionary={
    'train_planet':0.60,
    'train_bell':1.0,
    'train_trident':0.40,
    'compass_watch':1.0,
    'compass_planet':0.40,
    'compass_trident':0.60}

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
                    [start_icon_position[1]-0.08+offset, end_icon_position[1]+0.08+offset],
                    color = blue_cmap(PR_dictionary['{}_{}'.format(key_state,state)]), linewidth=6.0, zorder=1)

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
                                [start_icon_position[1]-0.08+offset, end_icon_position[1]+0.08+offset],
                                color = blue_cmap(PR_dictionary['{}_{}'.format(key_state,potential_predecessor[:-12])]), linestyle='-', linewidth=6.0, zorder=1)  # Use dashed line for indirect connections

    if type_plot=='SR':
        # Draw lines for all outgoing connections
        for state in outgoing_states:
            start_icon_position = icon_positions[key_state]
            end_icon_position = icon_positions[state]
            ax.plot([start_icon_position[0]+offset, end_icon_position[0]+offset],
                    [start_icon_position[1]+offset-0.08, end_icon_position[1]+offset+0.08],
                    color = salmon_cmap(SR_dictionary['{}_{}'.format(key_state,state)]), linewidth=6.0, zorder=1)


        # Additionally, find and color all indirect connections related to the key state
        for state in incoming_states.union(outgoing_states):
            if state != key_state:  # Avoid self-loop
                for transition, _ in probabilities.get(f"{state}_transitions", []):
                    if transition != key_state and transition in icon_positions:  # Check if transition is a valid state
                        start_icon_position = icon_positions[key_state]
                        end_icon_position = icon_positions[transition]
                        ax.plot([start_icon_position[0]+offset, end_icon_position[0]+offset],
                                [start_icon_position[1]+offset-0.08, end_icon_position[1]+offset+0.08],
                                color = salmon_cmap(SR_dictionary['{}_{}'.format(key_state,transition)]), linestyle='-', linewidth=6.0)  # Dashed line for indirect connections

num_s_states=[12,12,3]
s_colors=['red','red','blue',]
successor_states=['train','compass','planet']
type_strategy=['SR','SR','PR']
rewarded_states={'planet':100}

offsets=[0,0,0,0,0,0]
index=0
font_size=22

legend_handles=[]
labels=[]
for s_state in successor_states:
    # Create a new figure
    fig, ax = plt.subplots(figsize=(12, 6))

    # Set the limits of the x and y axes
    ax.set_xlim([0, 1.8])
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
            if transition in rewarded_states.keys():
                if type_strategy[index]=='SR':
                    print('here')
                    ax.text(target_x-0.062, target_y-0.17, "{}".format(rewarded_states[transition]),fontsize=font_size,zorder=6)
                else:
                    if transition==s_state:
                        ax.text(target_x-0.062, target_y-0.17, "{}".format(rewarded_states[transition]),fontsize=font_size,zorder=6)
                       



            
        icon_image = eval(icon_name)
        ax.imshow(icon_image, extent=[x - width / 2, x + width / 2, y - height / 2, y + height / 2], zorder=2)

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
        if index>-1:
            sm = plt.cm.ScalarMappable(cmap=salmon_cmap)
            cbar = plt.colorbar(sm, ax=ax, fraction=0.036, pad=0.01, orientation='horizontal')
            cbar.set_label('p(s\'|s)', fontdict={'size': font_size})
            cbar.set_ticks([0, 1])
            cbar.ax.set_xticklabels(['0', '1'], fontsize=font_size)

    if type_strategy[index] == 'PR':
        if index==2:
            print('colormap phase {}: {}\n'.format(s_state,type_strategy[i]))
            sm = plt.cm.ScalarMappable(cmap=blue_cmap)
            cbar = plt.colorbar(sm, ax=ax, fraction=0.036, pad=0.01, orientation='horizontal')
            cbar.set_label('p(s|s\')', fontdict={'size': font_size})
            cbar.set_ticks([0, 1])
            cbar.ax.set_xticklabels(['0', '1'], fontsize=font_size)

    # # Adjust the layout
    # plt.tight_layout()

    # Save and show the plot
    plt.savefig('{}_{}_Fig3.png'.format(s_state,type_strategy[i]), dpi=300, bbox_inches='tight')
    index+=1

