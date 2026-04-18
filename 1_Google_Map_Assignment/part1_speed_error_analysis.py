import numpy as np

# Speed from Google Maps (km/h)
speed_measured = np.array([
    0, 35, 43, 33, 29, 25, 35, 33, 21, 16, 12, 44, 47, 4, 47, 37, 13, 32, 21, 0
])

# Distance covered each minute (km)
distance_each_min = speed_measured * (1 / 60)

# Speed calculated back from distance
speed_calculated = distance_each_min * 60

# Error calculations
absolute_error = np.abs(speed_measured - speed_calculated)
mean_error = np.mean(absolute_error)
rmse = np.sqrt(np.mean(absolute_error ** 2))

print("Absolute Error (km/h):", absolute_error)
print("Mean Error (km/h):", round(mean_error, 2))
print("RMSE (km/h):", round(rmse, 2))
