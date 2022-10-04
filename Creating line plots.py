import pandas as pd
from matplotlib import pyplot as plt

deshaun = {'day_of_week': ['M', 'Tu', 'W', 'Th', 'F'],
        'hours_worked': [8, 5, 3, 5, 8]}
deshaun = pd.DataFrame(deshaun)

mengfei = {'day_of_week': ['M', 'Tu', 'W', 'Th', 'F'],
        'hours_worked': [0, 0, 5, 9, 5]}
mengfei = pd.DataFrame(mengfei)

aditya = {'day_of_week': ['M', 'Tu', 'W', 'Th', 'F'],
        'hours_worked': [10, 2, 1, 0, 0]}
aditya = pd.DataFrame(aditya)

plt.plot(deshaun.day_of_week, deshaun.hours_worked)
plt.plot(mengfei.day_of_week, mengfei.hours_worked)
plt.plot(aditya.day_of_week, aditya.hours_worked)

plt.show()