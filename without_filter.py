import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

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

# Polynomial regression: degree 2 (quadratic)
x = filtered_data['Yr Sold'].values.reshape(-1, 1)  # Reshape for sklearn
y = filtered_data['SalePrice'].values

# Apply PolynomialFeatures
poly = PolynomialFeatures(degree=2)  # For quadratic regression
x_poly = poly.fit_transform(x)

# Fit the linear regression model
model = LinearRegression()
model.fit(x_poly, y)

# Predict using the polynomial model
y_poly_pred = model.predict(x_poly)

# Plot the polynomial regression line
sorted_idx = np.argsort(x.flatten())  # Sort the indices to plot the line smoothly
plt.plot(x[sorted_idx], y_poly_pred[sorted_idx], color='red', label='Polynomial Regression Line (Degree 2)')

# Customize the plot
plt.title('Scatter Plot of SalePrice vs Year Sold (With Polynomial Regression)')
plt.xlabel('Year Sold')
plt.ylabel('Sale Price')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
