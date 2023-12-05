import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os

def read_vector_from_csv(file_path):
    df = pd.read_csv(file_path)
    if "vector_entry" not in df.columns:
        raise ValueError("CSV file must contain 'vector_entry' column")
    return df["vector_entry"].tolist()

def read_images_from_csv(file_path):
    df = pd.read_csv(file_path)
    if "image_path" not in df.columns:
        raise ValueError("CSV file must contain 'image_path' column")
    return df["image_path"].tolist()

def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    return sum(x * y for x, y in zip(vector1, vector2))

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.patches import Rectangle
import os

def add_image(fig, ax, img_path, x, y, width, height):
    if img_path and os.path.isfile(img_path):
        try:
            img = plt.imread(img_path)
            ax_image = fig.add_axes([x, y, width, height], zorder=1)
            ax_image.imshow(img)
            ax_image.axis('off')
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")
    elif img_path:
        print(f"Image path {img_path} does not exist")

def visualize_dot_product(vector1, vector2, images):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    num_elements = len(vector1)
    
    box_height = 0.6
    box_width = 0.6
    image_size = box_height  # Making image size the same as box height
    padding = 0.1
    image_y_offset = 1 + box_height / 2 + padding
    
    # Draw vectors as text with boxes
    for i, (v1, v2, img) in enumerate(zip(vector1, vector2, images), start=1):
        # Images
        add_image(fig, ax, img, i - image_size / 2, image_y_offset, image_size, image_size)
        
        # Vector 1
        rect = Rectangle((i - box_width / 2, 1 - box_height / 2), box_width, box_height, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)
        ax.text(i, 1, str(v1), ha='center', va='center', fontsize=12)
        
        # Vector 2
        rect = Rectangle((i - box_width / 2, 0 - box_height / 2), box_width, box_height, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)
        ax.text(i, 0, str(v2), ha='center', va='center', fontsize=12)
    
    # Draw lines connecting elements to be multiplied
    for i in range(1, num_elements + 1):
        ax.plot([i, i], [1 - box_height / 2, 0 + box_height / 2], 'k-', linewidth=1)
        ax.text(i, 0.5, '×', ha='center', va='center', fontsize=15, color='black')
    
    # Calculate dot product
    dot_product_result = dot_product(vector1, vector2)
    
    # Show multiplication and addition steps
    for i, (v1, v2) in enumerate(zip(vector1, vector2), start=1):
        product = v1 * v2
        ax.text(i, -0.8, str(product), ha='center', va='center', fontsize=12, color='black')
        if i != len(vector1):
            ax.text(i + 0.5, -0.8, '+', ha='center', va='center', fontsize=12, color='black')
    
    # Show result
    ax.text(len(vector1) + 1, -0.8, '=', ha='center', va='center', fontsize=12, color='black')
    ax.text(len(vector1) + 2, -0.8, str(dot_product_result), ha='center', va='center', fontsize=12, color='black')
    
    ax.set_xlim(0, len(vector1) + 2)
    ax.set_ylim(-5, 2 + image_y_offset)
    ax.axis('off')
    
    plt.title('Dot Product Visualization')
    plt.show()


# Main function and execution remain the same


def main():
    vector1 = read_vector_from_csv("vector1.csv")
    vector2 = read_vector_from_csv("vector2.csv")
    images = read_images_from_csv("images.csv")
    
    if len(vector1) != len(vector2) or len(vector1) != len(images):
        print("Error: Vectors and images list must be of the same length")
        return
    
    result = dot_product(vector1, vector2)
    print("Dot product of the two vectors:", result)
    
    visualize_dot_product(vector1, vector2, images)

if __name__ == "__main__":
    main()
