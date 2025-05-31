import random
import pytest


def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr

class BucketSort:
    def __init__(self):
        self.array_1 = []
        self.array_2 = [0, 1, 3, 2]
        for x in range(0, random.randint(1, 20)):
            self.array_1.append(random.randint(0, 100))

    def bucketsort(self, array):
        counts = [0] * (max(array) + 1)
        for x in array:
            counts[x] += 1

        sorted_arr = []
        for i in range(len(counts)):
            sorted_arr.extend([i] * counts[i])
        return sorted_arr

    def sort_and_check(self, arr, printable=False):
        if printable is True:
            print(f'Array: {arr}')
        arr = self.bucketsort(arr)
        if printable is True:
            print(f'Sorted array: {arr}')
        for _ in range(0, len(arr) - 1):
            if arr[_] > arr[_ + 1]:
                return False

        return True

    def test(self):
        assert self.sort_and_check(self.array_1) is True
        assert self.sort_and_check(self.array_2) is True
        with pytest.raises(TypeError):
            self.sort_and_check(-1)
        with pytest.raises(ValueError):
            self.sort_and_check([])

bs = BucketSort()
bs.test()
