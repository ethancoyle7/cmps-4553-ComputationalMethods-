import numpy as np
import matplotlib, matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#X is an array of ordered pairs, each order pair are two coefs
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
print ("X is ")
print(X)

# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3
print ("y is ", y)

reg = LinearRegression().fit(X, y)

print("Score: ", reg.score(X, y))
print("Coef: ", reg.coef_)
print("Intercept: ", reg.intercept_)
yp =reg.predict( np.array([[3, 5]]))
print("Prediction: " , yp)
