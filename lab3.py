import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

maxSpeed = 'max speed'
weight = 'weight'
acceleration = 'accelerationTime to up 100 km/h'
numberSeats = 'numberSeats'

table = pd.read_csv('newCarInfo.csv')

x = np.array(table[weight]).reshape((-1, 1))
y = np.array(table[acceleration])

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x=table[maxSpeed], y=table[weight], color="blue", edgecolors="white", linewidths=0.1, alpha=0.7)
plt.xlabel("Максимальная скорость")
plt.ylabel("Вес")
plt.show()

print('coefficient of determination: ', r_sq)
