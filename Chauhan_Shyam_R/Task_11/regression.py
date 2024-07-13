from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
diabetes = load_diabetes()

# Prepare the data
X = diabetes.data
y = diabetes.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(f'Training Score: {train_score:.2f}')
print(f'Testing Score: {test_score:.2f}')

# Plot residuals
train_residuals = y_train - model.predict(X_train)
test_residuals = y_test - model.predict(X_test)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(model.predict(X_train), train_residuals, alpha=0.5, label='Train Residuals')
plt.axhline(y=0, color='r', linestyle='--')
plt.title('Residual Plot (Training)')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(model.predict(X_test), test_residuals, alpha=0.5, label='Test Residuals')
plt.axhline(y=0, color='r', linestyle='--')
plt.title('Residual Plot (Testing)')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.legend()

plt.tight_layout()
plt.show()
