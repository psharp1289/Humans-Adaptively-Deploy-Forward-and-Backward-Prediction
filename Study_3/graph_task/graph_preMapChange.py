import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
import numpy as np
import matplotlib
import numpy
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerBase
plt.rcParams["font.size"] = 18  # Replace 12 with the desired font size

font_size=18
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


# Create a new figure
fig, ax = plt.subplots(figsize=(13, 6))

# Set the limits of the x and y axes
ax.set_xlim([0, 1.80])
ax.set_ylim([0.2, 1])

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
        

        
        arrow_color = plt.cm.get_cmap('gray').reversed()(strength)


        if probability not in probs:
            legend_text='{}'.format(probability)
            legend_handles.append(mpatches.Patch(color=arrow_color, label=legend_text))
            labels.append(legend_text)
            probs.append(probability)


        # Add the arrow to the plot
        if strength>0.4:
            ax.annotate("", xy=(target_x, target_y), xytext=(arrow_x,arrow_y), arrowprops=dict(facecolor=arrow_color,edgecolor=arrow_color),zorder=6)
        else:
            ax.annotate("", xy=(target_x, target_y), xytext=(arrow_x,arrow_y), arrowprops=dict(facecolor=arrow_color,edgecolor=arrow_color),zorder=4)

    icon_image = eval(icon_name)
    ax.imshow(icon_image, extent=[x - width / 2, x + width / 2, y - height / 2, y + height / 2])

# Remove the axes ticks and labels
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])


order=numpy.argsort(probs)
# Remove the axes border

def draw_bracket(ax, x1, x2, y, height=0.03, color='black', linewidth=1):
    """
    Draws a horizontal bracket between x1 and x2 at height y.
    """
    # Draw the horizontal line
    ax.plot([x1, x2], [y, y], color=color, linewidth=linewidth)

    # Draw the vertical lines at the ends
    ax.plot([x1, x1], [y, y - height], color=color, linewidth=linewidth)
    ax.plot([x2, x2], [y, y - height], color=color, linewidth=linewidth)

ax.axis('off')
# Adjust the legend position
class LeftAlignedHandler(HandlerBase):
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        # create a proxy artist that is just a blank rectangle
        patch = mpatches.Rectangle(xy=(xdescent, ydescent), width=width, height=height, color='none', transform=trans)
        # create a text object on the left of the rectangle
        text = mtext.Text(xdescent + width - self.handlelength, ydescent + height / 2., orig_handle.get_label(), verticalalignment='center', horizontalalignment='left', fontsize=fontsize, color=orig_handle.get_text_properties()['color'], transform=trans)
        # return the created artists
        return [patch, text]
order = np.argsort(probs)[::-1]
print(order)

first_legend = plt.legend([legend_handles[idx] for idx in order],
                          [labels[idx] for idx in order],
                          handler_map={str: LeftAlignedHandler()},  # use the custom handler for strings
                          loc='center left',
                          bbox_to_anchor=(0.92, 0.5),
                          title="Transition\nProbabilities",
                          ncol=1,
                          fontsize=font_size,
                          frameon=False)
# Add the first legend manually to the plot
plt.gca().add_artist(first_legend)


# Create custom handles for the second part of the legend
base_rate_handles = [mpatches.Patch(color='none', label='       p=0.1                       p = 0.21                   p = 0.06'),
                     ]

# Create the second part of the legend for Base Rates
# Notice that the bbox_to_anchor values will need to be adjusted to position
# this second legend below the first one.
legend = plt.legend(handles=base_rate_handles,
           loc='upper center',
           bbox_to_anchor=(0.52, 1.08),  # Adjust these values as needed
           title="    Base Rates\n",
           ncol=2,
           handlelength=0,  # Hide the patch
           handletextpad=0,  # Remove space between the patch and the text
           borderaxespad=0.4,
           fontsize=font_size,
           frameon=False)  # Remove the border and padding

title_x = legend.get_bbox_to_anchor().xmin
title_y = legend.get_bbox_to_anchor().ymax
for text in legend.get_texts():
    # Get the position of the text in the legend
    text_x = text.get_position()[0]
    text_y = text.get_position()[1]
    print(title_x)
    print(text_x)
    
    # Draw an arrow from the title to each entry
    # ax.plot([0.50, 0.79],[0.92, 0.96],color='black',linewidth=1,linestyle='-',zorder=8)
    # ax.plot([1.35, 1.08],[0.92, 0.96],color='black',linewidth=1,linestyle='-',zorder=8)
    # ax.plot([0.9, 0.9],[0.92, 0.94],color='black',linewidth=1,linestyle='-',zorder=8)
   # Draw an arrow from the title to each entry
    ax.plot([0.55, 0.84],[0.92, 1.01],color='black',linewidth=1,linestyle='-',zorder=8)
    ax.plot([1.45, 1.08],[0.92, 1.01],color='black',linewidth=1,linestyle='-',zorder=8)
    ax.plot([0.965, 0.965],[0.92, 0.98],color='black',linewidth=1,linestyle='-',zorder=8)
    draw_bracket(ax, 0.1, 0.8, 0.86)
    draw_bracket(ax, 1.7, 1.22, 0.86)
    draw_bracket(ax, 0.87, 1.09, 0.86)

# Set the title of the plot
# plt.tight_layout()
plt.savefig('State Space 3 Pre Map', dpi=300)
# Show the plot
plt.show()

