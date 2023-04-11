import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
import numpy
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
# Loop through each icon and add it to the plot
for icon_name, (x, y, width, height) in icon_positions.items():
    
    # Check if this icon is a terminal state
    if state_transitions_dictionary.get(icon_name, None) == 'end':
        icon_image = eval(icon_name)
        ax.imshow(icon_image, extent=[x - width / 2, x + width / 2, y - height / 2, y + height / 2])
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
        arrow_color = plt.cm.get_cmap('hsv')(strength)

        if probability not in probs:
            legend_text='{}'.format(probability)
            legend_handles.append(mpatches.Patch(color=arrow_color, label=legend_text))
            labels.append(legend_text)
            probs.append(probability)

        # Add the arrow to the plot
        ax.arrow(
            arrow_x, arrow_y, target_x - arrow_x, target_y - arrow_y,
            head_width=0.015, head_length=0.02,linewidth=2.0, fc=arrow_color, ec=arrow_color
        )
    icon_image = eval(icon_name)
    ax.imshow(icon_image, extent=[x - width / 2, x + width / 2, y - height / 2, y + height / 2])

# Remove the axes ticks and labels
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])


order=numpy.argsort(probs)
plt.legend([legend_handles[idx] for idx in order],[labels[idx] for idx in order],loc='upper center',title="transition probabilities",ncol=len(transitions))

# Set the title of the plot
plt.title('State Space Study 1 Before Map Change')
plt.tight_layout()
plt.savefig('State Space 1 Pre Map', dpi=300)
# Show the plot
plt.show()

