import pandas as pd
from matplotlib import pyplot as plt

data = {'officer': ['Deshaun', 'Mengfei', 'Aditya'],
        'avg_hours_worked': [45, 33, 42],
        'std_hours_worked': [3, 9, 5]}

data = pd.DataFrame(data)

plt.bar(data.officer, data.avg_hours_worked, yerr= data.std_hours_worked)
plt.show()