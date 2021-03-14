import numpy as np


class Lib:

    def __init__(self):
        return

    @staticmethod
    def swap(arr: list, i: int, j: int) -> list:
        """
        Swaps elements of an array and returns the reference
        """
        arr[i], arr[j] = arr[j], arr[i]
        return arr

    @staticmethod
    def reversePart(arr: list, i: int, j: int) -> list:
        """
            Reverse elements of an array with a Given Indexes
        """
        return np.concatenate([arr[0:i], arr[j:i - 1:-1], arr[j + 1:]])
