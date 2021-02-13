import numpy as np


def swap(arr, i, j):
    """
    Swaps elements of an array and returns the reference
    """
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def reversePart(arr, i, j):
    """
        reverse elements of an array with a Given Indexes
    """
    return np.concatenate([arr[0:i], arr[j:i - 1:-1], arr[j + 1:]])