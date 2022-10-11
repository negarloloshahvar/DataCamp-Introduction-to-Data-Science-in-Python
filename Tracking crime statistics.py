import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

data = {'Year': [2010, 2011, 2012, 2013, 2014],
        'Phoenix Police Dept': [1.08, 1.27, 1.21, 1.11, 0.94],
        'LA Police Dept': [0.46, 0.45, 0.43, 0.41, 0.39],
        'NY Police Dept': [0.21, 0.22, 0.22, 0.20, 0.19],
        'Philadelphia Police Dept': [0.71, 0.79, 0.78, 0.67, 0.62]}
data = pd.DataFrame(data)

plt.plot(data['Year'], data['Phoenix Police Dept'], label= 'Phoenix', color= "DarkCyan")
plt.plot(data['Year'], data['LA Police Dept'], label= 'Phoenix', linestyle= ':')
plt.plot(data['Year'], data['Philadelphia Police Dept'], label= 'Phoenix', marker= 's')
plt.legend()
plt.show()

