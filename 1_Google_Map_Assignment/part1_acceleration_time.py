import matplotlib.pyplot as plt
import numpy as np

# Time (minutes)
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Speed (km/h)
speed = [0, 35, 43, 33, 29, 25, 35, 33, 21, 16, 12, 44, 47, 4, 47, 37, 13, 32, 21, 0]

# Calculate acceleration (km/h per minute)
acceleration = np.diff(speed)  # delta speed
time_acc = time[1:]            # corresponding time values

plt.figure()
plt.plot(time_acc, acceleration, marker='o')
plt.xlabel("Time (minutes)")
plt.ylabel("Acceleration (km/h per minute)")
plt.title("Acceleration vs Time")
plt.grid(True)
plt.show()
