import pandas as pd
import matplotlib.pyplot as plt

# Specify the CSV file path
file_path = 'SDG_goal3_clean.csv'
# Read the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Select the relevant columns to use
columns = ['Country', 'Proportion of births attended by skilled health personnel (%)',
           'Infant mortality rate (deaths per 1,000 live births):::BOTHSEX']

# Filter the DataFrame to keep only the selected columns
filtered_data = data[columns]

# Calculate the average values grouped by country
average_data = filtered_data.groupby('Country').mean().reset_index()

# Save the averaged data to a new CSV file
output_file_path = 'average_births_and_infant_mortality.csv'
average_data.to_csv(output_file_path, index=False)

print(f"CSV has been successfully saved: {output_file_path}")

# Plot the data as a bar chart
plt.figure(figsize=(14, 8))

# Plot the proportion of births attended by skilled health personnel
plt.bar(average_data['Country'], average_data['Proportion of births attended by skilled health personnel (%)'], color='b', label='Skilled Births (%)')

# Plot the infant mortality rate as a red line
plt.plot(average_data['Country'], average_data['Infant mortality rate (deaths per 1,000 live births):::BOTHSEX'], color='r', marker='o', label='Infant Mortality Rate (per 1,000 live births)')

# Rotate the x-axis labels for readability
plt.xticks(rotation=90)

# Add labels and title
plt.xlabel('Country')
plt.ylabel('Value')
plt.title('Proportion of Births Attended by Skilled Personnel vs Infant Mortality Rate')

# Add a legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()