from matplotlib import pyplot as plt
import pandas as pd

six_months = {'month':['Jan', 'Feb', 'Mar', 'Apr', 'Jun'],
              'hours_worked': [160, 185, 182, 195, 50]}

six_months = pd.DataFrame(six_months)

plt.plot(six_months.month, six_months.hours_worked)
plt.text(2.5, 80, 'Missing June data')
plt.show()
