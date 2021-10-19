import pandas as pd
import numpy as np
from pandas import DataFrame

maxSpeed = 'max speed'
weight = 'weight'
acceleration = 'accelerationTime to up 100 km/h'
numberSeats = 'numberSeats'

table = pd.read_csv('carsInfo.csv')

maxSpeed_table = table[maxSpeed]
weight_table = table[weight]
acceleration_table = table[acceleration]
numberSeats_table = table[numberSeats]


def normalized_array(input_array):
    output_array = input_array.copy()
    output_array = [element for element in output_array if not np.isnan(element)]
    output_array.sort()
    lower_quartile_value = np.quantile(output_array, 0.25)
    upper_quartile_value = np.quantile(output_array, 0.75)
    interquartile_range = lower_quartile_value - upper_quartile_value
    lower_inner_fence = lower_quartile_value + 0.1 * interquartile_range
    upper_inner_fence = upper_quartile_value - 0.2 * interquartile_range
    median_value = np.median(output_array)
    return list(map(lambda x: x if lower_inner_fence <= x <= upper_inner_fence else median_value,
                    input_array))


maxSpeed_table = normalized_array(maxSpeed_table)
weight_table = normalized_array(weight_table)
acceleration_table = normalized_array(acceleration_table)
numberSeats_table = normalized_array(numberSeats_table)

output_table = DataFrame({maxSpeed: maxSpeed_table,
                          weight: weight_table,
                          acceleration: acceleration_table,
                          numberSeats: numberSeats_table})

print('минимальный вес автомобиля: ', output_table[weight].min())
print('самый быстрый разгон до 100км/ч: ', output_table[acceleration].min())
print('средняя макс скорость ', output_table[maxSpeed].mean())

output_table.to_csv('newCarInfo.csv', index=False)

# минимальный вес автомобиля
# самый быстрый разгон до 100км/ч
# средняя макс скорость
