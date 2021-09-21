import numpy as np
import random
import pandas as pd

engineVolume = np.random.normal(5, 1.5, 500)
seatsCount = np.random.randint(1, 8, 500)
acceleration = np.random.uniform(1, 15, 500)
fuelConsumption = np.random.normal(15, 3, 500)

ourDict = dict()

for i in range(len(engineVolume)):
    numberRand = random.randint(0, 100)
    numberCol = random.randint(0, 4)
    if numberRand > 70:
        if numberCol == 0:
            engineVolume[i] = np.nan
        if numberCol == 1:
            seatsCount[i] = np.nan_to_num(np.nan)
        if numberCol == 2:
            acceleration[i] = np.nan
        if numberCol == 3:
            fuelConsumption[i] = np.nan

for i in range(len(engineVolume)):
    numberRand = random.randint(0, 100)
    numberCol = random.randint(0, 4)
    # добавить знак на рандом
    randEngine = np.random.normal(12, 4)
    randSeat = random.randint(40, 60)
    randAcceleration = np.random.normal(0.5, 0.2)
    randConsumption = np.random.normal(40, 10)

    if numberRand > 80:
        if numberCol == 0:
            engineVolume[i] = randEngine
        if numberCol == 1:
            seatsCount[i] = randSeat
        if numberCol == 2:
            acceleration[i] = randAcceleration
        if numberCol == 3:
            fuelConsumption[i] = randConsumption

ourDict = {'Объем двигателя': engineVolume, 'Кол-во сидений': seatsCount, 'ускорение 0/100': acceleration,
           'Расход топлива': fuelConsumption}

df = pd.DataFrame(data=ourDict)
df.to_csv("data.csv", index=False)

# Средний объем двигателя, медиана по кол-ву седений, минимальный расход топлива
