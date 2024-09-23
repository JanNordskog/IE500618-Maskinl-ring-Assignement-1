## Summary

The features we have selected is to focus on specific property characteristics that can help in refining our model and ensuring that the data we use for predictions is relevant and clean. Notice that we also added a code snippet for removing rows containing more than 20% empty/null data to help prepare our data. Let’s break down why these particular filters could be useful:

### 1. lower_limit = filtered_data['Lot Area'].quantile(0.20) and upper_limit = filtered_data['Lot Area'].quantile(0.80)
- Why it's useful:
    - The Lot Area feature (the size of the property’s land) can be a key determinant of housing prices.
    - Using the 20th and 80th percentiles as limits helps remove outliers—both extremely small and extremely large properties—without discarding too much data.
    - Why discard extreme values?
        - Properties with extremely small or large lot areas can behave differently from typical properties, which could skew the model’s predictions. For example, very large lots may have unique pricing dynamics that aren't representative of the majority of houses in the dataset.
    - Filtering between the 20th and 80th percentiles ensures you’re working with data that captures more typical properties, making the model more likely to generalize well for future predictions.
### 2. pool_area = filtered_data['Pool Area'] < 1
- Why it's useful:
    - The Pool Area feature refers as a boolean of the pool on the property.
    - Filtering for properties with Pool Area less than 1 effectively selects homes without a pool.
    - Why exclude pools?
        - Homes with pools can have a different pricing dynamic due to the added luxury. If most homes in the dataset don’t have pools, those with pools can act as outliers.
        - This filter helps to ensure that the model isn't disproportionately affected by these outliers, making it better suited for predicting prices of more typical homes.
### 3. bldg_type = filtered_data['Bldg Type'] == '1Fam'
- Why it's useful:
    - The Bldg Type (Building Type) feature represents the type of residential building. In this case, '1Fam' refers to single-family homes.
    - Why filter for single-family homes?
        - Single-family homes have a distinct market compared to other building types like townhomes or duplexes, where pricing dynamics differ due to factors like shared walls, amenities, and land ownership.
        - By filtering for single-family homes, you are narrowing down the analysis to properties that have more similar characteristics, leading to better model performance when predicting prices for similar homes.
### 4. full_bath = filtered_data['Full Bath'] < 3
- Why it's useful:
    - The Full Bath feature represents the number of full bathrooms in a property.
    - Filtering for properties with fewer than 3 full bathrooms focuses on more typical family homes.
    - Why filter on bathroom count?
        - Homes with more than 3 full bathrooms can often be luxury properties or larger multi-family units, which can skew the price distribution. The more bathrooms a home has, the more expensive it may be, but this relationship might not be linear or consistent across the dataset.
        - By focusing on homes with fewer than 3 bathrooms, you're likely targeting more common homes in the dataset, improving the model’s ability to predict the prices of average homes.

#### The evaluation of the four models based on the Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) for the provided predictions.

## Model Comparison Overview
- Linear Regression:

    - MAE: $18,849
    - RMSE: $25,171
    - Evaluation: Linear regression performs decently but shows relatively higher MAE and RMSE compared to the other models. This indicates that while the model predicts fairly well, it's still susceptible to errors, particularly on certain data points where larger deviations (as reflected by the RMSE) are observed.

- Polynomial Regression:

    - MAE: $17,824
    - RMSE: $24,164
    - Evaluation: Polynomial regression improves over the linear model, reducing both MAE and RMSE. This suggests that the model captures some non-linear relationships between the features and the target, improving the overall prediction quality. However, the marginal improvement in RMSE indicates that polynomial regression may be slightly better but still not significantly superior for this dataset.

- Gradient Boosting Regressor:

    - MAE: $17,101
    - RMSE: $23,733
    - Evaluation: Gradient Boosting delivers the best performance among all the models, with the lowest MAE and RMSE. This indicates that the model is consistently making more accurate predictions and is less influenced by larger errors (as reflected by the low RMSE). The boost in performance is expected given that Gradient Boosting is known for handling complex patterns and non-linearities in the data well.

- Random Forest Regressor:

    - MAE: $17,804
    - RMSE: $24,841
    - Evaluation: Random Forest performs slightly worse than Gradient Boosting but still does a good job. The MAE and RMSE are slightly higher than Polynomial Regression but comparable to Gradient Boosting. Random Forests are good at capturing complex patterns in the data, but they might struggle slightly with the specific relationships in this dataset, as indicated by a slightly higher RMSE.

## Conclusion and Recommendation
- Best Model: The Gradient Boosting Regressor outperforms the other models in terms of both MAE and RMSE, making it the best choice for this dataset. The lower RMSE suggests it handles larger errors better, and the lower MAE shows that its predictions are more accurate on average.

- Runner-Up: Polynomial Regression also provides good results and is a strong alternative if you're looking for a simpler model that captures non-linearities.

- Linear Regression and Random Forest are both reasonable choices, but they are outperformed by Gradient Boosting and Polynomial Regression in terms of error metrics.

Given the evaluation, you might want to further optimize the Gradient Boosting Regressor, possibly tuning its hyperparameters (e.g., learning rate, number of estimators) to see if you can achieve even better performance.

### Summary of Model Evaluation Metrics

| Model                    | Mean Absolute Error (MAE) | Root Mean Squared Error (RMSE) |
|---------------------------|--------------------------|-------------------------------|
| **Linear Regression**      | \$18,849                 | \$25,171                      |
| **Polynomial Regression**  | \$17,824                 | \$24,164                      |
| **Gradient Boosting**      | \$17,101                 | \$23,733                      |
| **Random Forest**          | \$17,804                 | \$24,841                      |


In conclusion, Gradient Boosting Regressor provides the most accurate predictions in this case. If further refinement is needed, model tuning or feature engineering may further enhance performance.

## Team Collaboration Overview

This project was a collaborative effort between Jan and Rune, where we worked together to predict house prices using the **Ames Housing dataset**.

### Tasks

- **Rune Molander**: 
  - Led the data cleaning and preprocessing phase, ensuring the dataset was ready for analysis.
  - Applied transformations such as handling missing data, filtering extreme outliers, and one-hot encoding categorical variables.
  - Implemented the initial machine learning models, including **Linear Regression**, **Polynomial Regression**, **Gradient Boosting Regressor**, and **Random Forest Regressor**.
  - Performed model evaluation using metrics such as **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**.
  
- **Jan Nordskog**: 
  - Focused on feature engineering, identifying key features such as **Lot Area**, **Full Bath**, and **Building Type** that could significantly influence house prices.
  - Worked on hyperparameter tuning and model optimization, experimenting with different configurations of models like **Random Forest** and **Gradient Boosting** to enhance performance.
  - Assisted in reviewing the results and ensuring that the models' predictions were logical and aligned with real-world housing price expectations.
  - Worked on documenting the evaluation process and the collaboration overview.
  
### Collaboration Process

1. **Initial Planning**: 
   - We began by discussing the overall approach to the problem, identifying the key steps in the data analysis process, including **data cleaning**, **feature selection**, and **modeling**. Together, we explored the dataset, identified outliers, and discussed possible features that could improve model performance.

2. **Data Preprocessing**: 
   - Rune Molander led this phase, ensuring that missing data was handled, and irrelevant features were filtered out. We frequently communicated about how to handle outliers, such as extreme values in the **Lot Area**, and agreed on the percentile filtering technique.

3. **Feature Engineering**:
   - Jan Nordskog proposed ideas for improving feature selection, suggesting important features like the number of bathrooms and the type of building. These features were integrated into the models, and we worked together to refine the selection based on initial results.

4. **Model Implementation**:
   - We divided the task of implementing different models. Rune implemented and evaluated the **Linear Regression** and **Polynomial Regression** models, while Jan focused on advanced models such as **Gradient Boosting** and **Random Forest**.
   - We regularly shared code and insights, comparing model performance through metrics like MAE and RMSE. This allowed us to iterate quickly, fine-tuning hyperparameters and improving results.

5. **Model Evaluation and Final Results**:
   - Once all models were implemented, we came together to evaluate their performance. We analyzed the prediction errors and discussed why certain models, like **Gradient Boosting**, performed better in terms of RMSE and MAE.
   - Rune documented the results in tabular form, and Jan contributed by summarizing the model performance and suggesting next steps for possible further optimization.


### Tools and Technologies Used

- **Python Libraries**: 
  - `pandas`, `numpy` for data manipulation and analysis.
  - `scikit-learn` for machine learning models and preprocessing.
  - `matplotlib` for data visualization and understanding feature distributions.



We believe the lessons learned during this project will be valuable as we continue to work on similar machine learning problems in the future.

