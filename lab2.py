import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 2000)

maxSpeed = 'max speed'
weight = 'weight'
acceleration = 'accelerationTime to up 100 km/h'
numberSeats = 'numberSeats'

table = pd.read_csv('carsInfo.csv')

default_maxSpeed = 180
default_weight = 1000
default_acceleration = 10.0
default_numberSeats = 4
min_maxSpeed = 50
min_weight = 500
max_acceleration = 2.0
max_numberSeats = 8

maxSpeed_table = table[maxSpeed]
weight_table = table[weight]
acceleration_table = table[acceleration]
numberSeats_table = table[numberSeats]
# Убираем пропуски
maxSpeed_table.update(maxSpeed_table.replace(np.nan, default_maxSpeed))
# Убираем шумы
table.loc[(table[maxSpeed] < min_maxSpeed), maxSpeed] = default_maxSpeed

weight_table.update(weight_table.replace(np.nan, default_weight))
table.loc[(table[weight] < min_weight), weight] = default_weight

acceleration_table.update(acceleration_table.replace(np.nan, default_acceleration))
table.loc[(table[acceleration] < max_acceleration), acceleration] = default_acceleration

numberSeats_table.update(numberSeats_table.replace(np.nan, default_numberSeats))
table.loc[(table[numberSeats] > max_numberSeats), numberSeats] = default_numberSeats

table.to_csv('newCarInfo.csv', index=False)

# минимальный вес автомобиля
# самый быстрый разгон до 100км/ч
# средняя макс скорость
print('Минимальный вес автомобиля:', table[weight].min())
print('Самый быстрый разгон до 100км/ч:', table[acceleration].min())
print('Средняя макс скорость:', table[maxSpeed].mean())
