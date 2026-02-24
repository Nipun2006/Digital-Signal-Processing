import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0,1,1000)
f = 5
x1 = np.sin(2*np.pi*f*t)
x2 = np.sin(2*np.pi*f* t**2)
plt.subplot(2,1,1),plt.plot(t,x1),plt.xlabel("Amplitute"),plt.ylabel("Time(t)")
plt.title("Stationary Signal")
plt.subplot(2,1,2),plt.plot(t,x2,'r'),plt.xlabel("Amplitude"),plt.ylabel("Time(t)")
plt.title("Non-Stationary Signal")
plt.tight_layout()
plt.show()
