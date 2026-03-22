import numpy as np
import matplotlib.pyplot as plt
sampling_rate = 1000
duration = 1.0
freq = 50
t = np.linspace(0, duration, 1000, endpoint=False)

signal = np.sin(2 * np.pi * freq * t) + 0.5 * np.sin(2 * np.pi * 120 * t)
noise = np.random.normal(0,0.5, signal.shape)
combined_signal = signal + noise

fft_val = np.fft.fft(combined_signal)
frequencies = np.fft.fftfreq(len(t), 1 / sampling_rate)

magnitude = np.abs(fft_val)
positive_freqs = frequencies[:len(frequencies)//2]
positive_magnitude = magnitude[:len(magnitude)//2] * (2 / len(t))

plt.figure(figsize=(10, 4))
plt.subplot(3,1,1)
plt.plot(t,signal),plt.xlabel("Time(t)"),plt.ylabel("Signal")
plt.title("FFT Result: Frequency Components")
plt.subplot(3,1,2)
plt.plot(t,combined_signal),plt.xlabel("Time(t)"),plt.ylabel("Noisy_Signal")
plt.subplot(3,1,3)
plt.plot(positive_freqs,positive_magnitude),plt.xlabel("Time(t)"),plt.ylabel("Signal")
plt.xlim(0, 150)
plt.tight_layout()
plt.show()