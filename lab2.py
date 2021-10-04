import pandas as pd
import numpy as np
from pandas import DataFrame

pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 2000)

maxSpeed = 'max speed'
weight = 'weight'
acceleration = 'accelerationTime to up 100 km/h'
numberSeats = 'numberSeats'

table = pd.read_csv('carsInfo.csv')


def getNormalizeArray(array):
    startIndex = int(len(array) * 0.2)
    endIndex = int(len(array) * 0.8)
    newArray = []
    for element in array:
        if not np.isnan((float(element))):
            newArray.append((float(element)))
    newArray.sort()
    result = newArray[startIndex:endIndex]
    return result


maxSpeed_table = table[maxSpeed]
weight_table = table[weight]
acceleration_table = table[acceleration]
numberSeats_table = table[numberSeats]

maxSpeed_normalize = getNormalizeArray(maxSpeed_table)
weight_normalize = getNormalizeArray(weight_table)
acceleration_normalize = getNormalizeArray(acceleration_table)
numberSeats_normalize = getNormalizeArray(numberSeats_table)

table_normalize = DataFrame({maxSpeed: maxSpeed_normalize,
                             weight: weight_normalize,
                             acceleration: acceleration_normalize,
                             numberSeats: numberSeats_normalize})

table_normalize.to_csv('newCarInfo.csv', index=False)

# минимальный вес автомобиля
# самый быстрый разгон до 100км/ч
# средняя макс скорость
print('Минимальный вес автомобиля:', table_normalize[weight].min())
print('Самый быстрый разгон до 100км/ч:', table_normalize[acceleration].min())
print('Средняя макс скорость:', table_normalize[maxSpeed].mean())
