import numpy as np
import pandas as pd
from matplotlib import pyplot as plt




battingData = pd.read_csv('teamBatting.csv')
pitchingData = pd.read_csv('teamPitching.csv')

baseballData =pd.concat([battingData, pitchingData], axis=1, join="outer")


baseballData.to_csv('tables.csv')
# sortByRuns = battingData.sort_values(by=['R'],ascending=False).reset_index(drop=True)
x = baseballData.Runs
y = baseballData.W

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x+b)
print('Equation: ', str(m) + 'x ' + str(b))

# print(x)
runsPlot = plt.scatter(x,y)
plt.show()