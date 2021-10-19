import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

maxSpeed = 'max speed'
weight = 'weight'
acceleration = 'accelerationTime to up 100 km/h'
numberSeats = 'numberSeats'

table = pd.read_csv('newCarInfo.csv')

x = np.array(table[weight]).reshape((-1, 1))
y = np.array(table[maxSpeed])

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

y_predict = model.predict(x)
sns.regplot(x=x, y=y)
sns.regplot(x=x, y=y_predict)

plt.xlabel("Вес")
plt.ylabel("Макс скорость")
plt.show()

print('coefficient of determination: ', r_sq)
