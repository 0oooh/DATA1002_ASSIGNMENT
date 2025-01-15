import pandas as pd
from math import sqrt
from sklearn import metrics, neighbors
from sklearn.model_selection import train_test_split

# Load the data
df = pd.read_csv('SDG_goal3_clean.csv')

# Set input variables and target variable
X = df[['Infant mortality rate (deaths per 1,000 live births):::BOTHSEX',
        'Neonatal mortality rate (deaths per 1,000 live births)']]
y = df['Universal health coverage (UHC) service coverage index']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=49)

# Train the KNN model (n_neighbors=11)
neigh = neighbors.KNeighborsRegressor(n_neighbors=11).fit(X_train, y_train)

# Create a sample to predict UHC
sample = pd.DataFrame([[30, 100]], columns=['Infant mortality rate (deaths per 1,000 live births):::BOTHSEX',
        'Neonatal mortality rate (deaths per 1,000 live births)'])
sample_pred = neigh.predict(sample)
print('----- Sample case -----')
print('Infant mortality rate (deaths per 1,000 live births):::BOTHSEX:', sample.iloc[0, 0])  # Modified part
print('Neonatal mortality rate (deaths per 1,000 live births):', sample.iloc[0, 1])  # Modified part
print('Predicted UHC index:', int(sample_pred[0]))  # Modified part
print('-----------------------')

# Perform predictions on the test set
y_pred = neigh.predict(X_test)

# Calculate Root Mean Squared Error
mse = metrics.mean_squared_error(y_test, y_pred)
print('Root Mean Squared Error (RMSE):', sqrt(mse))

# Calculate R-squared Score (the closer to 1, the more accurate the predictions)
print('R-squared score:', metrics.r2_score(y_test, y_pred))