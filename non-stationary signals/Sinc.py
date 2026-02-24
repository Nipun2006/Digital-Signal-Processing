import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(-10,10,1001)
x = np.sinc(t)
def get_max(t,x):
    time = []
    peaks = []
    for i in range(1,len(x)-1):
        if x[i-1] < x[i] and x[i] > x[i+1]:
                time.append(t[i])
                peaks.append(x[i])
    return np.array(time), np.array(peaks)
plt.plot(t,x),plt.xlabel("Time(t)"),plt.ylabel("Amplitude(V)")
plt.title("SinC function")
t_peak,y_peak = get_max(t,x)
plt.plot(t_peak,y_peak,'k*',label = 'discrete points')
plt.show()