import numpy as np
from scipy import stats


example_array = np.array([24, 16, 30, 10, 12, 28, 38, 2, 4, 36])
example_array1 = np.array([24, 16, 12, 10, 12, 28, 38, 12, 28, 24])

# cout mean / average 
average_of_example_array1 = example_array.mean()
average_of_example_array2 = np.average(example_array)

# count median
median_of_example_array = np.median(example_array)

# count mode 
mode_of_example_array1 = stats.mode(example_array1)


print(mode_of_example_array1)


# print(median_of_example_array)
# print(average_of_example_array1)
# print(average_of_example_array2)