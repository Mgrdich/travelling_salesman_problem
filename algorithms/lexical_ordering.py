import numpy as np
from util.functions import swap, reversePart


def lexical_ordering(arr):
    """
        Every time it returns next Lexical order

        Example
        v0 = [1, 2, 3]
        v = lexical_ordering(v0) # [1,3,2]
        v1 = lexical_ordering(v) # [2,1,3]
        v2 = lexical_ordering(v1)# [2 3 1]
    """
    array = np.array(arr)

    # Step 1
    largestI = -1

    for i in range(array.size - 1):
        if array[i] < array[i + 1]:
            largestI = i

    # Step 2
    largestJ = -1

    for j in range(array.size):
        if array[largestI] < array[j]:
            largestJ = j

    # Step 3
    swap(array, largestI, largestJ)

    # Step 4 reverse from largestI + 1 to the end
    return reversePart(array, largestI + 1, array.size)
