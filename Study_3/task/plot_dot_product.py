import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.collections import LineCollection  # <-- Add this line

def visualize_vector(s1_image_name, df, reward_list):
    # Extract relevant rows from the dataframe
    rows = df[df['s1_image'] == s1_image_name]
    
    # Create a vector from the probabilities
    unique_next_images = rows['Next Image'].unique()
    prob_vector = np.array(rows['Probability'].values)
    
    # Create the reward vector
    reward_dict = dict(reward_list)
    reward_vector = np.array([reward_dict[img] if img in reward_dict else 0 for img in unique_next_images])
    
    # Visualize the vectors
    fig, ax = plt.subplots(2, 1, figsize=(10, 7))
    
    # Displaying images instead of image names
    for i, image in enumerate(unique_next_images):
        img = plt.imread(image)
        imagebox = OffsetImage(img, zoom=0.12)
        ab = AnnotationBbox(imagebox, (i, -0.25), frameon=False, pad=0)
        ax[0].add_artist(ab)
    
    # Visualizing the Probability Vector
    cax1 = ax[0].matshow([prob_vector], cmap='Reds', aspect="auto")
    lines = []
    
    
    ax[0].set_xticks(np.arange(len(unique_next_images)))
    ax[0].set_xticklabels(['' for _ in unique_next_images])
    ax[0].set_yticklabels([])
    ax[0].set_title('SR Vector')
    for i in range(len(prob_vector)):
        ax[0].text(i, 0, round(prob_vector[i], 2), ha='center', va='center', color='k',fontsize=20)
    for i in range(len(unique_next_images)):  # 2 because there's only one row in the matshow plot, and we need to border it above and below
        lines.extend([[(i-0.5, -0.5), (i-0.5, len(prob_vector)-0.5)],
                      [(-0.5, i-0.5), (len(prob_vector)-0.5, i-0.5)]])
    lines.append([(len(unique_next_images)-0.5, -0.5), (len(unique_next_images)-0.5, 0.5)])

    lc1 = LineCollection(lines, linewidths=10, colors='black')
    ax[0].add_collection(lc1)
    # Visualizing the Reward Vector
    cax2 = ax[1].matshow([reward_vector], cmap='Reds', aspect="auto")
    lines = []
    
    
  
    ax[1].set_xticks(np.arange(len(unique_next_images)))
    ax[1].set_xticklabels(['' for _ in unique_next_images])
    ax[1].set_yticklabels([])
    ax[1].set_title('Reward Vector')


    for i in range(len(reward_vector)):
        ax[1].text(i, 0, round(reward_vector[i], 2), ha='center', va='center', color='k',fontsize=20)
    for i in range(len(unique_next_images)):
        lines.extend([[(i-0.5, -0.5), (i-0.5, len(reward_vector)-0.5)],
                      [(-0.5, i-0.5), (len(reward_vector)-0.5, i-0.5)]])
    lines.append([(len(unique_next_images)-0.5, -0.5), (len(unique_next_images)-0.5, 0.5)])

    lc2 = LineCollection(lines, linewidths=10, colors='black')
    ax[1].add_collection(lc2)
    plt.tight_layout()
    # Compute and display dot product
    dot_product = np.dot(prob_vector, reward_vector)
    print("Dot Product Calculation:")
    print(f"{prob_vector} (Prob Vector)")
    print(f"{reward_vector} (Reward Vector)")
    print(f"Dot Product: {dot_product}")

    # New figure to visualize the multiplication process
    fig_mul, ax_mul = plt.subplots(figsize=(15, 10))
    ax_mul.axis('off')
    y_pos = 0.8
    product_results = []
    
    # Drawing the multiplication process
    for i in range(len(prob_vector)):
        sr_val = prob_vector[i]
        reward_val = reward_vector[i]
        product_val = sr_val * reward_val
        product_results.append(product_val)

        # Displaying the values
        ax_mul.text(0.2, y_pos, f"{sr_val:.2f}", fontsize=15)
        ax_mul.text(0.3, y_pos, "x", fontsize=15)
        ax_mul.text(0.4, y_pos, f"{reward_val:.2f}", fontsize=15)
        ax_mul.text(0.5, y_pos, "=", fontsize=15)
        ax_mul.text(0.6, y_pos, f"{product_val:.2f}", fontsize=15)

        y_pos -= 0.1

    # Displaying the summation
    ax_mul.text(0.7, 0.4 + 0.1 * len(prob_vector)/2, "+", fontsize=15, va='center')
    ax_mul.text(0.8, 0.4 + 0.1 * len(prob_vector)/2, f"= {dot_product:.2f}", fontsize=20, va='center')

    plt.show()
    
    
    
    return dot_product

# Load data
data='SR_probabilities.csv'
df = pd.read_csv(data)
df = df[df['Probability'] != 0.0]
print(df)

reward_list = [("unicorn.png", 1), ("fox.png", 2)]

visualize_vector("houses.png", df, reward_list)
