import pandas as pd
import matplotlib.pyplot as plt

# Sample Data

data = {
    'Runtime (min)' : [90, 110, 130, 95],
    'Numbers' : [1, 2, 3, 4]
}

df = pd.DataFrame(data)

# Optional: Sort by x-axis => Make Line Smoother
df = df.sort_values(by='Runtime (min)')

# Scatter Plot
plt.scatter(df['Runtime (min)'], df['Numbers'], color='teal', edgecolor='black')

# Scatter Plot line connecting points
plt.plot(df['Runtime (min)'], df['Numbers'], color='black', linestyle='-', marker='o')


# Add Labels and Title
plt.xlabel('Runtime (min)')
plt.ylabel('Numbers')
plt.title('Airvo Runtime')

#Optional : Add Grid and Customize
plt.grid(True)
plt.tight_layout()
plt.show()