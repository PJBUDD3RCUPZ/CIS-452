# Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
# Lab 3
# 02/04/2024
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

SAMPLE_RATE = 44000
DURATION = 5

time = np.arange(0,DURATION,1/SAMPLE_RATE)

#base frequencies Hz
frequency1 = 432
frequency2 = 4000

#set signals
signal1 = 0.5 * np.sin(2 * np.pi * frequency1 * DURATION)
signal2 = 0.5 * np.sin(2 * np.pi * frequency2 * DURATION)

# scale down signal2
downSignal2 = signal2 * 0.3

#create mixed_signal
mixed_signal = signal1 + downSignal2

#scale up mixed signal by 400
upMixed_signal = mixed_signal * 400

# Plot the first 1000 data points of mixed_signal
plt.plot(time[:1000],np.arange(1000), label='Mixed Signal')

# Show the plot
plt.title('First 1000 Data Points of Mixed Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Save mixed_signal as a WAV file
#write('output.wav', SAMPLE_RATE, mixed_signal)
