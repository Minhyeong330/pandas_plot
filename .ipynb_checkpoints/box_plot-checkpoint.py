import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/cs/OneDrive/Desktop/Battery/Testing/230V-UPS90 Data Set.csv', skiprows=1)
column = 'Runtime (min)'

print(df.head())

# Median and quartiles
median = df['Runtime (min)'].median()
q1 = df['Runtime (min)'].quantile(0.25)
q3 = df['Runtime (min)'].quantile(0.75)

# Outliers and Whiskers
iqr = q3 - q1
lower_whisker = df[column][df[column] >= q1 - 1.5 * iqr].min()
upper_whisker = df[column][df[column] <= q3 + 1.5 * iqr].max()
outliers = df[(df[column] < lower_whisker) | (df[column] > upper_whisker)][column] # Pandas (numpy) doesn't recognize 'or' expression.


# Plot Properties
df.boxplot(column='Runtime (min)')
plt.title('Box Plot of Runtime')
plt.ylabel('Runtime')
plt.text(1.1 , mean, f'Mean: {mean:.2f}', verticalalignment='center')
# plt.axhline(mean, color='red', linestyle='--', label='Mean') -> Optional: Horizontal line
plt.text(1.1 , median, f'Median: {median:.2f}', verticalalignment='center')
plt.text(1.1 , q1, f'Q1: {q1:.2f}', verticalalignment='center')
plt.text(1.1 , q3, f'Q3: {q3:.2f}', verticalalignment='center')
plt.text(0.6, lower_whisker, f'Lower Whisker: {lower_whisker:.2f}', verticalalignment='center', color='purple')
plt.text(0.6, upper_whisker, f'Upper Whisker: {upper_whisker:.2f}', verticalalignment='center', color='purple')
for outlier in outliers:
    plt.text(1.05, outlier, f'Outlier: {outlier:.2f}', verticalalignment='center', color='orange')
plt.show()