import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load the CSV file
file_path = 'AmesHousing.csv'  
data = pd.read_csv(file_path)

# Apply filters:
# Filter Lot Area between 20th and 80th percentile
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

# Select features (e.g., 'Yr Sold', 'Lot Area', 'Gr Liv Area') and target variable ('SalePrice')
X = filtered_data[['Yr Sold', 'Lot Area', 'Gr Liv Area']]  # Features (you can add more if needed)
y = filtered_data['SalePrice']  # Target variable

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Evaluate the model on the training and testing sets
mse_train = mean_squared_error(y_train, y_train_pred)
mse_test = mean_squared_error(y_test, y_test_pred)
mae_test = mean_absolute_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)

# Display results
print(f"Training MSE: {mse_train:.2f}")
print(f"Test MSE: {mse_test:.2f}")
print(f"Test MAE: {mae_test:.2f}")
print(f"Test R² Score: {r2_test:.2f}")
