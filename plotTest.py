import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0, 3, 20)

y = np.linspace(0, 9, 20)

#plt.plot(x,y)
plt.plot(np.tan(np.linspace(0,2*np.pi,1000)))
plt.show()