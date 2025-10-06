from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import metrics
diabetes = load_diabetes()
feature_names = diabetes.feature_names
x=diabetes.data      
y=diabetes.target 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model=LinearRegression()
model.fit(x_train, y_train)
y_pred=model.predict(x_test)
mse=mean_squared_error(y_test, y_pred)
r2=r2_score(y_test, y_pred)
print("Feature Names:")
for feature in feature_names:
    print(feature)
print("Feature matrix shape:", x.shape)
print("Target vector shape:", y.shape)
print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)
bmi_index=feature_names.index('bmi')
bmi_input=float(input("Enter a standardized BMI value (e.g., between -0.1 and 0.2): "))
new_input=np.zeros((1, x.shape[1]))
new_input[0, bmi_index]=bmi_input
prediction=model.predict(new_input)
print(f"Predicted disease progression for BMI = {bmi_input:.2f}: {prediction[0]:.2f}")

