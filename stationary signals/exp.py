import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(-1,1,1000)
a,b = 2,-2
x1 = np.exp(a*t)
x2 = np.exp(b*t)
plt.subplot(2,1,1),plt.plot(t,x1),plt.title("Exp Increasing")
plt.subplot(2,1,2),plt.plot(t,x2),plt.title("Exp Decreasing")
plt.tight_layout()
plt.show()