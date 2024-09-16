import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'AmesHousing.csv'  # Replace this with the actual path to your CSV file
data = pd.read_csv(file_path)

# Filter Lot Area to remove extreme outliers (keep within 1st and 99th percentiles)
data_filtered = data[(data['Lot Area'] > data['Lot Area'].quantile(0.01)) & 
                     (data['Lot Area'] < data['Lot Area'].quantile(0.99))]

# Filter Mas Vnr Area to remove extreme outliers (keep within 1st and 99th percentiles)
data_filtered = data_filtered[(data_filtered['Mas Vnr Area'] < data_filtered['Mas Vnr Area'].quantile(0.99))]

# Remove properties with very large Pool Areas (since most have none, keep within 99th percentile)
data_filtered = data_filtered[data_filtered['Pool Area'] < data_filtered['Pool Area'].quantile(0.99)]

# Filter Misc Val to remove extreme values (keep within 99th percentile)
data_filtered = data_filtered[data_filtered['Misc Val'] < data_filtered['Misc Val'].quantile(0.99)]

# Filter SalePrice to remove extreme values (keep within 1st and 99th percentiles)
data_filtered = data_filtered[(data_filtered['SalePrice'] > data_filtered['SalePrice'].quantile(0.01)) & 
                              (data_filtered['SalePrice'] < data_filtered['SalePrice'].quantile(0.99))]

# Now, create the scatter plot with the filtered data
plt.figure(figsize=(10, 6))
plt.scatter(data_filtered['Yr Sold'], data_filtered['SalePrice'], alpha=0.5)
plt.title('Scatter Plot of SalePrice vs Year Sold (Filtered Data)')
plt.xlabel('Year Sold')
plt.ylabel('Sale Price')
plt.grid(True)

# Show the plot
plt.show()
