import numpy as np
from util.functions import swap, reversePart


def lexical_ordering(arr):
    """
        Every time it returns next Lexical order
    """
    val = np.array(arr)

    # Step 1
    largestI = -1

    for i in range(val.size - 1):
        if val[i] < val[i + 1]:
            largestI = i

    # Step 2
    largestJ = -1

    for j in range(val.size):
        if val[largestI] < val[j]:
            largestJ = j

    # Step 3
    swap(val, largestI, largestJ)

    # Step 4 reverse from largestI + 1 to the end
    return reversePart(val, largestI + 1, arrayLength)
