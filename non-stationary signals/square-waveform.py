import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
t = np.linspace(0,1,1000)
f = 5
duty = [0.15,0.25,0.5,0.75]
for i in range(len(duty)):
    x = signal.square(2*np.pi*f*t,duty[i])
    plt.subplot(2,2,i+1)
    plt.plot(t,x),plt.xlabel("Time(t)"),plt.ylabel("Amplitude")
    plt.ylim(-2,2),plt.title('square wave (duty = {})'.format(duty[i]))
    plt.tight_layout()
plt.show()