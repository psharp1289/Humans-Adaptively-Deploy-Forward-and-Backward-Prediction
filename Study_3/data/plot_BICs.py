import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='white', font='arial',palette='Set2', font_scale=2.8, rc=None)

# Given data
model_names = ['PR', 'SR', 'MB', 'BR']
BICs = [
1134.249
,952.4946
,1101.209
,1113.594]

# Calculate delta BICs
min_BIC = min(BICs)
delta_BICs = [bic - min_BIC for bic in BICs]

# Create a horizontal barplot
plt.figure(figsize=(6, 6))
sns.barplot(x=delta_BICs, y=model_names, color="black")
plt.xlabel(r'$\Delta$BIC')  # Using LaTeX-style for delta symbol
plt.title('Model Comparison')

plt.tight_layout()

# Save the figure as a PNG with dpi=300
plt.savefig("model_comparison.png", dpi=300)

plt.show()
