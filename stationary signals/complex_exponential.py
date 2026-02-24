import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(-1,1,1000)
f = 5
x1 = np.exp(1j*2*np.pi*f*t)
x2 = np.exp(-1j*2*np.pi*f*t)
plt.subplot(3,2,1),plt.plot(t,x1)
plt.xlabel("Time(t)"),plt.ylabel("Amplitude(A)")
plt.subplot(3,2,2),plt.plot(t,x2)
plt.xlabel("Time(t)"),plt.ylabel("Amplitude(A)")
plt.subplot(3,2,3),plt.plot(t,np.abs(x1))
plt.xlabel("Time(t)"),plt.ylabel("Magnitude")
plt.subplot(3,2,4),plt.plot(t,np.abs(x2))
plt.xlabel("Time(t)"),plt.ylabel("Magnitude")
plt.subplot(3,2,5),plt.plot(t,np.angle(x1)*180/(np.pi))
plt.xlabel("Time(t)"),plt.ylabel("Angle(0)")
plt.subplot(3,2,6),plt.plot(t,np.angle(x2)*180/(np.pi))
plt.xlabel("Time(t)"),plt.ylabel("Angle(0)")
plt.show()