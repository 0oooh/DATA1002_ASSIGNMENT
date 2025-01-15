import pandas as pd
import matplotlib.pyplot as plt
# Load the CSV file
file_path = 'SDG_goal3_clean.csv'
data = pd.read_csv(file_path)
# Select relevant attributes
columns = [
   'Country',
   'Proportion of births attended by skilled health personnel (%)',
   'Infant mortality rate (deaths per 1,000 live births):::BOTHSEX',
   'Universal health coverage (UHC) service coverage index'
]
# Filter the data to include only the relevant columns
filtered_data = data[columns]
# Calculate average values by country
average_data = filtered_data.groupby('Country').mean().reset_index()
# Create a bubble plot
plt.figure(figsize=(12, 8))
plt.scatter(
   average_data['Universal health coverage (UHC) service coverage index'],
   average_data['Proportion of births attended by skilled health personnel (%)'],
   s=average_data['Infant mortality rate (deaths per 1,000 live births):::BOTHSEX'] * 10,  # Scale bubble size
   alpha=0.5,
   edgecolors="w",
   linewidth=0.5
)
# Adding labels and titles
plt.title('Bubble Plot: UHC, Skilled Birth Attendance, and Infant Mortality Rates by Country')
plt.xlabel('Universal Health Coverage (UHC) Service Coverage Index')
plt.ylabel('Proportion of Births Attended by Skilled Health Personnel (%)')
# Annotate countries on the plot
for i in range(len(average_data)):
   plt.annotate(
       average_data['Country'][i],
       (average_data['Universal health coverage (UHC) service coverage index'][i],
        average_data['Proportion of births attended by skilled health personnel (%)'][i]),
       fontsize=8,
       ha='right'
  )
plt.grid(True)
plt.show()
