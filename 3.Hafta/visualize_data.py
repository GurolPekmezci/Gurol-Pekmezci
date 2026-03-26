import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Read the data
if not os.path.exists('data.csv'):
    print("Error: 'data.csv' not found. Please run generate_data.py first.")
    exit()

df = pd.read_csv('data.csv')

# Set plot theme
sns.set_theme(style="whitegrid")
plt.figure(figsize=(18, 6))

# 1. Fatigue Index Bell Curve (Distribution)
plt.subplot(1, 3, 1)
sns.histplot(df['Yorgunluk_Endeksi'], kde=True, color='red', stat='density', bins=25)
plt.title('Fatigue Index Distribution (Bell Curve)', fontsize=14)
plt.xlabel('Fatigue Index (0-100)', fontsize=12)
plt.ylabel('Density', fontsize=12)

# 2. Success Rate Bell Curve (Distribution)
plt.subplot(1, 3, 2)
sns.histplot(df['Basari_Orani'], kde=True, color='blue', stat='density', bins=25)
plt.title('Field Goal Success Rate Distribution', fontsize=14)
plt.xlabel('Success Rate (%)', fontsize=12)
plt.ylabel('Density', fontsize=12)

# 3. Fatigue vs Success Rate Analysis (Scatter with Regression)
plt.subplot(1, 3, 3)
sns.regplot(
    x='Yorgunluk_Endeksi', 
    y='Basari_Orani', 
    data=df, 
    scatter_kws={'alpha': 0.6, 'color': 'purple', 's': 20}, 
    line_kws={'color': 'black', 'linewidth': 2}
)
plt.title('Fatigue vs Success Rate Analysis', fontsize=14)
plt.xlabel('Fatigue Index', fontsize=12)
plt.ylabel('Success Rate (%)', fontsize=12)

# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig('analysis_plots.png', dpi=300)

print("Visualization complete! 'analysis_plots.png' saved.")
# Display plots
plt.show()
