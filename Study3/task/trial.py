import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Create a random 5x5 matrix
data = np.random.random((5, 5))

fig, ax = plt.subplots()
cax = ax.matshow(data, cmap='viridis')

# Create borders around each entry
lines = []
for i in range(data.shape[0] + 1):
    lines.extend([[(i-0.5, -0.5), (i-0.5, data.shape[1]-0.5)],
                  [(-0.5, i-0.5), (data.shape[0]-0.5, i-0.5)]])
lc = LineCollection(lines, linewidths=1, colors='white')  # Adjust linewidths and colors as needed
ax.add_collection(lc)

# Show the plot
plt.colorbar(cax)
plt.show()
