import numpy as np
import matplotlib.pyplot as plt
def get_max(t,x):
    time = []
    peaks = []
    for i in range(1,len(x)-1):
        if x[i-1] < x[i] and x[i] > x[i+1]:
                time.append(t[i])
                peaks.append(x[i])
    return np.array(time), np.array(peaks)
def get_zeroes(t,x):
    time = []
    zeroes = []
    for i in range(1,len(x)-1):
        if x[i-1]*x[i] < 0:
            if abs(x[i]) < abs(x[i-1]):
                time.append(t[i])
                zeroes.append(x[i])
            else:
                time.append(t[i-1])
                zeroes.append(x[i-1])
                 
    return np.array(time),np.array(zeroes)
t = np.linspace(0,1,1000)
A = 5
f = 5
ph = 0
x = A*np.sin(2*np.pi*f*t + ph)
peak_times,peaks = get_max(t,x)
zero_times,zeroes = get_zeroes(t,x)
plt.plot(t,x),plt.xlabel('Time'),plt.ylabel('Amplitude')
plt.plot(peak_times,peaks,'k*',label = 'discrete points')
plt.plot(zero_times,zeroes,'ro',label = 'discrete points')
plt.title("My First Wave!")
print("No of crossings = ",len(zero_times))
plt.show()

