import matplotlib.pyplot as plt

# Time (minutes)
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Speed (km/h)
speed = [0, 35, 43, 33, 29, 25, 35, 33, 21, 16, 12, 44, 47, 4, 47, 37, 13, 32, 21, 0]

distance_2min = []
plot_time = []

for i in range(len(speed) - 2):
    avg_speed = (speed[i] + speed[i+1]) / 2
    distance = avg_speed * (2 / 60)   # distance in km
    distance_2min.append(distance)
    plot_time.append(time[i+1])       # plotted at mid-point

plt.figure()
plt.plot(plot_time, distance_2min, marker='o')
plt.xlabel("Time (minutes)")
plt.ylabel("Distance covered in 2 minutes (km)")
plt.title("Distance Covered Every 2 Minutes")
plt.xticks(range(0, 22, 2))
plt.grid(True)
plt.show()
