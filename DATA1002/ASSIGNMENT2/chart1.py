import pandas as pd
import matplotlib.pyplot as plt

# Open the file and read the dataset
with open('SDG_goal3_clean.csv', 'r') as file:
    sdg_data = pd.read_csv(file)

# Calculate average UHC Service Coverage index by Country
uhc_by_country = sdg_data.groupby('Country')['Universal health coverage (UHC) service coverage index'].mean()

# Sort with highest average Country
uhc_sorted_dict = dict(sorted(uhc_by_country.items(), key=lambda item: item[1], reverse=True))

# Convert the sorted data to a DataFrame
uhc_sorted_df = pd.DataFrame(list(uhc_sorted_dict.items()), columns=['Country', 'Average UHC Service Coverage Index'])

# Export the results to a CSV file
uhc_sorted_df.to_csv('average_uhc_service_coverage_by_country.csv', index=False)
print("The data has been exported to 'average_uhc_service_coverage_by_country.csv'")

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(uhc_sorted_df['Country'], uhc_sorted_df['Average UHC Service Coverage Index'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Average UHC Service Coverage Index')
plt.title('Average UHC Service Coverage Index by Country')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Show the chart
plt.tight_layout()  # Adjust layout to ensure everything fits without overlap
plt.show()