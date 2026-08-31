import numpy as np

array = np.linspace(0, 9, 10, dtype=int)
print(array)

new_array = np.where(array % 2 == 1, -1, array)
print(new_array)

two_d_array = array.reshape(2, 5)
print(two_d_array)

even_sum = 0

for number in array:
    if number % 2 == 0:
        even_sum += number

print(even_sum)