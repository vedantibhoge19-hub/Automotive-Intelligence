import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Load the heartbeat audio
fs, data = wavfile.read("a0003.wav")

# If stereo, take only one channel
if len(data.shape) > 1:
    data = data[:,0]

# Normalize signal
data = data / np.max(np.abs(data))

# Simple peak detection
threshold = 0.3
beats = []

for i in range(1, len(data)-1):
    if data[i] > threshold and data[i] > data[i-1] and data[i] > data[i+1]:
        beats.append(i)

# Remove very close peaks (S1 and S2 separation)
filtered_beats = []
min_distance = int(0.25 * fs)  # 0.25 second gap

for b in beats:
    if len(filtered_beats) == 0 or b - filtered_beats[-1] > min_distance:
        filtered_beats.append(b)

# Count beats
num_beats = len(filtered_beats)
duration = len(data) / fs
bpm = (num_beats / duration) * 60

print("Total Beats Detected:", num_beats)
print("Duration (seconds):", round(duration,2))
print("Estimated Heart Rate (BPM):", round(bpm,2))

# Plot waveform with detected beats
time = np.linspace(0, duration, len(data))

plt.figure(figsize=(12,4))
plt.plot(time, data, label="Heartbeat Signal")
plt.scatter(np.array(filtered_beats)/fs, data[filtered_beats], color='red', s=10, label="Detected Beats")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Heartbeat Detection")
plt.legend()
plt.show()
