import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
file_path = 'AmesHousing.csv'  # Replace this with the actual path to your CSV file
data = pd.read_csv(file_path)

# Apply filters:
# 1. Filter Lot Area between 20th and 80th percentile
lower_limit = data['Lot Area'].quantile(0.20)
upper_limit = data['Lot Area'].quantile(0.80)
pool_area = data['Pool Area'] < 1
bldg_type = data['Bldg Type'] == '1Fam'
full_bath = data['Full Bath'] < 3  
filtered_data = data[(data['Lot Area'] >= lower_limit) & 
                     (data['Lot Area'] <= upper_limit) & 
                     pool_area & 
                     bldg_type & 
                     full_bath] 

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['Yr Sold'], filtered_data['SalePrice'], alpha=0.5)

# Add the regression line
x = filtered_data['Yr Sold']
y = filtered_data['SalePrice']
slope, intercept = np.polyfit(x, y, 1)  # Linear fit (degree=1)
plt.plot(x, slope*x + intercept, color='red', label='Regression Line')

# Customize the plot
plt.title('Scatter Plot of SalePrice vs Year Sold (With Regression Line)')
plt.xlabel('Year Sold')
plt.ylabel('Sale Price')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
