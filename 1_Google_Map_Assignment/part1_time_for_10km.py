import matplotlib.pyplot as plt

# Time (minutes)
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Speed (km/h)
speed = [0, 35, 43, 33, 29, 25, 35, 33, 21, 16, 12, 44, 47, 4, 47, 37, 13, 32, 21, 0]

time_for_10km = []

for s in speed:
    if s == 0:
        time_for_10km.append(0)   # stop condition
    else:
        time_for_10km.append((10 / s) * 60)

plt.figure()
plt.plot(time, time_for_10km, marker='o')
plt.xlabel("Time (minutes)")
plt.ylabel("Time required to travel 10 km (minutes)")
plt.title("Instantaneous Time to Travel 10 km vs Time")
plt.grid(True)
plt.show()
