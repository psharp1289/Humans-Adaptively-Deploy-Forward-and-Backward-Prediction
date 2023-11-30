import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='white', font='arial',palette='Set2', font_scale=1.5, rc=None)

# Given data
model_names = ['PR', 'SR', 'MB', 'BR']
BICs = [
892.1961
,915.5886
,915.5886
,946.7576]

# Calculate delta BICs
min_BIC = min(BICs)
delta_BICs = [bic - min_BIC for bic in BICs]

# Create a horizontal barplot
plt.figure(figsize=(10, 6))
sns.barplot(x=delta_BICs, y=model_names, color="black")
plt.xlabel(r'$\Delta$BIC')  # Using LaTeX-style for delta symbol
plt.title('Model Comparison')
plt.ylabel('model')  # Using LaTeX-style for delta symbol

plt.tight_layout()

# Save the figure as a PNG with dpi=300
plt.savefig("model_comparison.png", dpi=300)

plt.show()
