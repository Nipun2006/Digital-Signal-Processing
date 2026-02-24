import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
t = np.linspace(-10,10,2000)
f = 1/(2*np.pi)
duty = 0.5
x = signal.square(2*np.pi*f*t,duty)
y = 0
for i in range (10):
    y += np.sin((2*i+1)*t)/(2*i+1)
y*= 4/np.pi
peak1 = np.max(y)
z = 0
for i in range(50):
    z += np.sin((2*i+1)*t)/(2*i+1)
z*= 4/np.pi
peak2 = np.max(z)
plt.subplot(3,1,1)
plt.plot(t,x),plt.xlabel("Time(t)"),plt.ylabel("Amplitude")
plt.ylim(-2,2),plt.title('Square wave (duty = {})'.format(duty))
plt.subplot(3,1,2)
plt.plot(t,y),plt.xlabel("Time(t)"),plt.ylabel("Amplitude")
plt.ylim(-2,2),plt.title('FFT wave visualized N=10')
plt.subplot(3,1,3)
plt.plot(t,z),plt.xlabel("Time(t)"),plt.ylabel("Amplitude")
plt.ylim(-2,2),plt.title('FFT wave visualized N=50')
plt.figtext(0.5, 0.01, f"Gibbs Factor: N=10 is {peak1:.4f} | N=50 is {peak2:.4f}", ha="center", fontsize=10, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
plt.tight_layout()
plt.show()