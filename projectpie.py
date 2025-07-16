# import matplotlib.pyplot as plt

# # Data
# subjects = ['Math', 'Science', 'Urdu']
# marks = [80, 90, 70]

# plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90)

# # Add title
# plt.title("Marks Distribution in Subjects")

# # Show the chart
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

temperatures = np.array([34,23,36,23,24,33,44,38,25,19,18,45,42,41,40,30,31,29,35,28,37,26,25,24,22,32,44,22,43,42])

mean_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
std_temp = np.std(temperatures)

print(f"Average temperature is:{mean_temp}")
print(f"Maximum temperature is:{max_temp}")
print(f"Minimum temperature is:{min_temp}")
print(f"Standard temperature is:{std_temp}")

plt.bar(range(1,31),temperatures)
plt.title("Bar chart of temperatures")
plt.xlabel("Days")
plt.ylabel("Temperature (celcisus)")
plt.show()

plt.hist(temperatures, bins=6)
plt.title("Histogram of temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (celcisus)")
plt.show()

plt.plot(temperatures, marker='o')
plt.title("Line chart of temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (celcisus)")
plt.show()