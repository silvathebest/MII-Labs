import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option("display.precision", 2)

maxSpeed = 'max speed'
weight = 'weight'
acceleration = 'accelerationTime to up 100 km/h'
numberSeats = 'numberSeats'

table = pd.read_csv('newCarInfo.csv')

x = np.array(table[weight]).reshape((-1, 1))
y = np.array(table[acceleration])

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

print('coefficient of determination: ', r_sq)
