import numpy as np
from util.functions import swap, reversePart

val = np.array([0, 1, 2, 3, 4, 5, 7, 6])
arrayLength = len(val)

# Step 1
largestI = -1

for i in range(arrayLength - 1):
    if val[i] < val[i + 1]:
        largestI = i

# Step 2
largestJ = -1

for j in range(arrayLength):
    if val[j] < val[largestI]:
        largestJ = j

# Step 3
# swap(val, largestI, largestJ)

# Step 4 reverse from largestI + 1 to the end
# reversed_list = reversePart(val, largestI + 1, arrayLength - 1)
