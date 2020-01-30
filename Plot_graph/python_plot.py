import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

import japanize_matplotlib

rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'

# 1週目
input_file = 'japan_optimize.csv'
data = np.array(pd.read_csv(input_file, delimiter=','))
d1 = data[:,0]
d2 = data[:,1]

input_file = 'japan_machineLearning.csv'
data = np.array(pd.read_csv(input_file, delimiter=','))
c1 = data[:,0]
c2 = data[:,1]

plt.figure()

plt.plot(d1, d2, label="最適化問題")
plt.plot(c1, c2, label="機械学習")
plt.legend()
# plt.plot(x_range, y, linestyle='dashed')

plt.show()
