import pandas as pd
import matplotlib.pyplot as plt

# Check the file path and file name
df = pd.read_csv('C:/Users/cs/OneDrive/Desktop/Battery/Testing/230V-UPS90 Data Set.csv', skiprows=1)
column = 'Runtime (min)' # Check a column name

print(df.head())

# Median and quartiles
median = df[column].median()
q1 = df[column].quantile(0.25)
q3 = df[column].quantile(0.75)

# Outliers and Whiskers
iqr = q3 - q1
lower_whisker = df[column][df[column] >= q1 - 1.5 * iqr].min()
upper_whisker = df[column][df[column] <= q3 + 1.5 * iqr].max()
outliers = df[(df[column] < lower_whisker) | (df[column] > upper_whisker)][column] # Pandas (numpy) doesn't recognize 'or' expression.
mean = df[column].mean()

# Plot Properties ---> Need to fix label's titels when I change the column
df.boxplot(column)
plt.title('Box Plot of Runtime (min)') # Check title
plt.ylabel('Runtime (min)') # Check y label name
plt.text(0.6 , mean, f'Mean: {mean:.0f}', verticalalignment='center')

# Thickness
df.boxplot(column,
           boxprops=dict(linewidth=2),
           whiskerprops=dict(linewidth=2),
           capprops=dict(linewidth=2),
           medianprops=dict(linewidth=2))

# plt.axhline(mean, color='red', linestyle='--', label='Mean') -> Optional: Horizontal line
plt.text(1.1 , median, f'Median: {median:.0f}', verticalalignment='center')
plt.text(1.1 , q1, f'Q1: {q1:.0f}', verticalalignment='center')
plt.text(1.1 , q3, f'Q3: {q3:.0f}', verticalalignment='center')
plt.text(0.6, lower_whisker, f'Lower Whisker: {lower_whisker:.0f}', verticalalignment='center', color='black')
plt.text(0.6, upper_whisker, f'Upper Whisker: {upper_whisker:.0f}', verticalalignment='center', color='black')
for outlier in outliers:
    plt.text(1.05, outlier, f'Outlier: {outlier:.0f}', verticalalignment='center', color='red')


plt.tight_layout()
plt.show()