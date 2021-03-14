# for more documentation check the notebooks
# notebooks/lexical_orderings

import numpy as np
from util.Lib import Lib

val = np.array([0, 1, 2])
arrayLength = val.size

# Step 1
largestI = -1

for i in range(arrayLength - 1):
    if val[i] < val[i + 1]:
        largestI = i

# Step 2
largestJ = -1

for j in range(arrayLength):
    if val[largestI] < val[j]:
        largestJ = j


# Step 3
Lib.swap(val, largestI, largestJ)

# Step 4 reverse from largestI + 1 to the end
reversed_list = Lib.reversePart(val, largestI + 1, arrayLength)

print(reversed_list)
