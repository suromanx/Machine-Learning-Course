import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu

res, res1 = [], []

for i in range(int(64)):
    # генерация двух массивов для нормального распределения
    sample_1 = np.random.normal(0.3, 3, size=int(1e3))
    sample_2 = np.random.normal(0, 3, size=int(1e3))
    # тест на гипотезу: а равны ли мат.ожидания? (0.3 против 0)
    stat, p = ttest_ind(sample_1, sample_2)
    # stat, p = mannwhitneyu(sample_1, sample_2)
    res.append(stat)
    res1.append(p)
    # рисуем графики на p-value (в модуле статистики узнаете, что это такое)
_ = plt.hist(res1, bins=100)


import matplotlib.pyplot as plt
# рисуем получающуюся статистику
_ = plt.hist(res, bins=100)