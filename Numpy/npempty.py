import numpy as np

empArr = np.empty((3, 4))

empArr[0] = [1, 2, 3, 4]
empArr[1] = [5, 6, 7, 8]
empArr[2] = [9, 10, 11, 12]

for i in range(len(empArr)):
    row = empArr[i]
    for value in row:
        print(int(value))


