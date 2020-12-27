import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
import numpy as np

scale = StandardScaler()

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

print(X.head())

scaledX = scale.fit_transform(X)

print(type(scaledX))

# print(scaledX)
scaledX_df = pandas.DataFrame(scaledX[np.arange(len(scaledX))],columns={'Weight', 'Volume'})
print(scaledX[0])
print(scaledX_df.head(10))

regr = linear_model.LinearRegression()
# regr.fit(X, y)
regr.fit(scaledX, y)

print('coefficients are {} '.format(regr.coef_))

# predictedCO2 = regr.predict([[3300, 1500]])

scaled = scale.transform([[2300, 1300]])

predictedCO2 = regr.predict([scaled[0]])

print('Predicted value is {} '.format(predictedCO2))
