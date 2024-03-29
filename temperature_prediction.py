#Regresion lineal
#Atoany Fierro

import numpy as np
from sklearn.linear_model import LinearRegression

x: month
y: temperature
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape((-1, 1))
y = np.array([26, 29, 31, 33, 32, 29, 28, 27, 27, 27])

model = LinearRegression()

model.fit(x, y)

#Intersections and slope
print('intercept:', model.intercept_)
print('slope:', model.coef_)

#Predictions
x_new = np.array([11]).reshape((-1, 1))
y_pred = model.predict(x_new)
print('Temperatura del mes de noviembre:', y_pred, sep='\n')
