import pandas as pd
import matplotlib.pyplot as plt

# I can use member. 
# Count will be added by ??? - Jokgu Project

data = {
    'Member' : ['Minhyeong', 'Wonjun'],
    'Count': [15, 22]
}

df = pd.DataFrame(data)

# bar plot
plt.bar(df['Name'], df['Count'], color='skyblue', edgecolor='black')
# Add Labels and title
plt.xlabel('Name')
plt.ylabel('The Number of the 1st place')
# Optional: Add numbers on top of bars
for i in range(len(df)):
    plt.text(i, df['Count'][i] + 0.5, df['Count'][i], ha='center', fontsize=9)
    
plt.tight_layout()
plt.show()