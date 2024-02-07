# Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
# Lab 3
# 02/04/2024

#imported packages for task 10 
from scipy.fft import fft, fftfreq 

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
signal1 = 0.5 * np.sin(2 * np.pi * frequency1 * time)
signal2 = 0.5 * np.sin(2 * np.pi * frequency2 * time)

# scale down signal2
downSignal2 = signal2 * 0.3

#create mixed_signal
mixed_signal = signal1 + downSignal2

#scale up mixed signal by 400

#using this mixed signal for task 10 
upMixed_signal = mixed_signal * 400


fftMixedSignal = fft(upMixed_signal)

#calculate corresponding frequencies
lengthOfFrequency = len(upMixed_signal)
frequencies = fftfreq(lengthOfFrequency, 1/SAMPLE_RATE)


#show the plot
plt.figure()
plt.plot(frequencies[:lengthOfFrequency//2], np.abs(fftMixedSignal[:lengthOfFrequency//2]))



plt.title("Task 10 / Fourier Transform")

plt.legend()
plt.show()

