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
transitions=[['trident']+['planet'],
            
['bell']*108+['tree']*108+['watch']*3+['fox']*141,
['bell']*72+['tree']*72+['watch']*9+['unicorn']*7,

['train']*4+['tophat']*4,         
['snorkel']*4+['north']*4,
['compass']*4+['houses']*4,            
['hammer']*4+['apple']*4,
['window']*4]

state_transitions_dictionary={

#second stage
'trident':1,'planet':2,
    
'bell':3,'tree':4,'watch':5,'fox':6,'unicorn':7,
    
'houses':'end','compass':'end','train':'end','tophat':'end','north':'end','snorkel':'end','hammer':'end','apple':'end','window':'end'

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


# Create a new figure
fig, ax = plt.subplots(figsize=(12, 6))

# Set the limits of the x and y axes
ax.set_xlim([0, 1.80])
ax.set_ylim([0.2, 1])

# Define the position and size of each icon
icon_positions = {
    'trident': (0.75, 0.8, 0.1, 0.1),
    'planet': (1.05, 0.8, 0.1, 0.1),
    'bell': (0.40, 0.5, 0.1, 0.1),
    'tree': (0.70, 0.5, 0.1, 0.1),
    'watch': (0.90, 0.5, 0.1, 0.1),
    'fox': (1.10, 0.5, 0.1, 0.1),
    'unicorn': (1.40, 0.5, 0.1, 0.1),
    
    'train': (0.15, 0.3, 0.1, 0.1),
    'tophat': (0.35, 0.3, 0.1, 0.1),
    'north': (0.55, 0.3, 0.1, 0.1),
    'snorkel': (0.75, 0.3, 0.1, 0.1),
    'houses': (0.90, 0.3, 0.1, 0.1),
    'compass': (1.05, 0.3, 0.1, 0.1),
    'hammer': (1.25, 0.3, 0.1, 0.1),
    'apple': (1.45, 0.3, 0.1, 0.1),
    'window': (1.65, 0.3, 0.1, 0.1)
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

        if strength==0.04:
            strength+=0.10
        if strength==0.06:
            strength+=0.20
        if strength==0.39:
            strength+=0.10
        if strength==0.45:
            strength+=0.15
        if strength==0.5:
            strength+=0.25
        

        
        arrow_color = plt.cm.get_cmap('hsv')(strength)
        if strength==1.0:
            arrow_color='black'


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
plt.legend([legend_handles[idx] for idx in order],[labels[idx] for idx in order],prop={'size': 12},loc='upper center',title="transition probabilities",ncol=len(transitions))

# Set the title of the plot
plt.title('State Space Study 2 Before Map Change')
plt.tight_layout()
plt.savefig('State Space 2 Pre Map', dpi=300)
# Show the plot
plt.show()

