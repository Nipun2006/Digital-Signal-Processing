import numpy as np
import matplotlib.pyplot as plt
v = np.arange(0,1,0.001) #gives evenly spaced points at a interval of 0.001
vt = 0.026
i_s = 1/1000
n=1 
i = i_s * ((np.exp(v/(n*vt)))-1)
plt.plot(v,i),plt.xlabel("Forward Voltage")
plt.ylabel("Current")
plt.title("Forward characteristic V-I plot of PN Junction Diode")
plt.show()