import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of players
n_players = 500

# Player IDs from 1 to 500
oyuncu_ids = np.arange(1, n_players + 1)

# Fatigue Index generation (Normal Distribution: Bell Curve)
# Mean 50, Standard Deviation 15
yorgunluk_endeksi = np.random.normal(loc=50, scale=15, size=n_players)
# Clip values to be between 0 and 100
yorgunluk_endeksi = np.clip(yorgunluk_endeksi, 0, 100)

# Success Rate (Field Goal Percentage) generation
# We created a negative correlation scenario where higher fatigue lowers success
# We add a normally distributed noise to give it a bell curve shape
noise = np.random.normal(loc=0, scale=6, size=n_players)
basari_orani = 75 - (yorgunluk_endeksi * 0.6) + noise

# Clip values between 0% and 100%
basari_orani = np.clip(basari_orani, 0, 100)

# Convert to DataFrame
df = pd.DataFrame({
    'Oyuncu_ID': oyuncu_ids,
    'Yorgunluk_Endeksi': np.round(yorgunluk_endeksi, 2),
    'Basari_Orani': np.round(basari_orani, 2)
})

# Save to data.csv
df.to_csv('data.csv', index=False)
print("Data generation complete! 'data.csv' has been successfully created.")
