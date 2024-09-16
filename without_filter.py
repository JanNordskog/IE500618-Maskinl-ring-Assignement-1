import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
file_path = 'AmesHousing.csv'  
data = pd.read_csv(file_path)

# Apply filters:

lower_limit = data['Lot Area'].quantile(0.20)  # removes houses with lot lower than the lower 20%
upper_limit = data['Lot Area'].quantile(0.80)  # removes houses with lot higher than the upper 20%
pool_area = data['Pool Area'] < 1   # removes houses with pools
bldg_type = data['Bldg Type'] == '1Fam' # filters only 1Fam houses
full_bath = data['Full Bath'] < 3   # filters houses with only less than 3 full baths
filtered_data = data[(data['Lot Area'] >= lower_limit) & 
                     (data['Lot Area'] <= upper_limit) & 
                     pool_area & 
                     bldg_type & 
                     full_bath] 

# Group by 'Yr Sold' and calculate the average SalePrice for each year
yearly_avg = filtered_data.groupby('Yr Sold')['SalePrice'].mean()

# Create the scatter plot for the yearly average
plt.figure(figsize=(10, 6))
plt.plot(yearly_avg.index, yearly_avg.values, marker='o', color='blue', label='Average SalePrice')

# Add a regression line for the average prices
slope, intercept = np.polyfit(yearly_avg.index, yearly_avg.values, 1)  # Linear fit (degree=1)
plt.plot(yearly_avg.index, slope * yearly_avg.index + intercept, color='red', label='Regression Line')

# Customize the plot
plt.title('Average SalePrice vs Year Sold (With Regression Line)')
plt.xlabel('Year Sold')
plt.ylabel('Average Sale Price')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
