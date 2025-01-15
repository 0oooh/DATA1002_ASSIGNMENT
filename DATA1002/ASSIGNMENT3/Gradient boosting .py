import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Load the data (specify the file path)
data = pd.read_csv("SDG_goal3_clean.csv")

# Set independent and dependent variables (exclude unnecessary columns)
X = data.drop(columns=[
    'Universal health coverage (UHC) service coverage index',
    'Country', 'Region', 'Year',
    'Proportion of births attended by skilled health personnel (%)',
    'Mortality rate attributed to cardiovascular disease, cancer, diabetes or chronic respiratory disease (probability):::BOTHSEX',
    'Mortality rate attributed to cardiovascular disease, cancer, diabetes or chronic respiratory disease (probability):::MALE',
    'Mortality rate attributed to cardiovascular disease, cancer, diabetes or chronic respiratory disease (probability):::FEMALE',
    'Fraction of deaths due to diabetes, among deaths due to cardiovascular disease, cancer, diabetes or chronic respiratory disease',
    'Fraction of deaths due to cancer, among deaths due to cardiovascular disease, cancer, diabetes or chronic respiratory disease',
    'Suicide mortality rate, by sex (deaths per 100,000 population):::BOTHSEX',
    'Suicide mortality rate, by sex (deaths per 100,000 population):::MALE',
    'Suicide mortality rate, by sex (deaths per 100,000 population):::FEMALE',
    'Health worker density, by type of occupation (per 10,000 population)::PHYSICIAN',
    'Health worker density, by type of occupation (per 10,000 population)::NURSEMIDWIFE',
    'Health worker density, by type of occupation (per 10,000 population)::PHARMACIST'
])

# Apply one-hot encoding to categorical columns
X = pd.get_dummies(X, drop_first=True)

# Handle missing values
X = X.fillna(X.mean())

# Set the dependent variable
y = data["Universal health coverage (UHC) service coverage index"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=48)

# Set parameters for gradient boosting
param_grid = {
    'n_estimators': [50, 100, 200],
    'learning_rate': [0.1, 0.3, 0.5],
    'max_depth': [3, 5, 7]
}

# Use GridSearchCV to find the best parameters
grid_search = GridSearchCV(estimator=GradientBoostingRegressor(random_state=47),
                           param_grid=param_grid, scoring='r2', cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

# Extract the best model
best_model = grid_search.best_estimator_
print("Best parameters found: ", grid_search.best_params_)

# Print feature importances
importances = best_model.feature_importances_
feature_importance = pd.Series(importances, index=X.columns).sort_values(ascending=False)
print("Feature Importances:\n", feature_importance)

# Make predictions and evaluate on the test data
y_pred = best_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Output results
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared (R²):", r2)