import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Load the CSV file
file_path = 'AmesHousing.csv'  
data = pd.read_csv(file_path)

# Apply filters:
lower_limit = data['Lot Area'].quantile(0.20)  #removes houses with lot lower than the lower 20%
upper_limit = data['Lot Area'].quantile(0.80)  #removes houses with lot higher than the upper 20%
pool_area = data['Pool Area'] < 1   #removes houses with pools
bldg_type = data['Bldg Type'] == '1Fam' #filters only 1Fam houses
full_bath = data['Full Bath'] < 3   #filter houses with only less than 3 full baths
filtered_data = data


# Group by 'Yr Sold' and calculate the average SalePrice for each year
yearly_avg = filtered_data.groupby('Yr Sold')['SalePrice'].mean()

# Reshape the data for PolynomialFeatures
x = yearly_avg.index.values.reshape(-1, 1)
y = yearly_avg.values

# Apply Polynomial Features transformation (degree 2 for quadratic)
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

# Fit a linear regression model to the polynomial features
model = LinearRegression()
model.fit(x_poly, y)

# Generate predictions using the polynomial model
y_poly_pred = model.predict(x_poly)

# Plot the original data and the polynomial regression line
plt.figure(figsize=(10, 6))
plt.plot(yearly_avg.index, yearly_avg.values, marker='o', color='blue', label='Average SalePrice')
plt.plot(yearly_avg.index, y_poly_pred, color='red', label='Polynomial Regression Line (Degree 2)')

# Customize the plot
plt.title('Average SalePrice vs Year Sold (With Polynomial Regression)')
plt.xlabel('Year Sold')
plt.ylabel('Average Sale Price')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
