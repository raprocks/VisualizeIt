from typing import Union


class BinarySearch:
    def __init__(self, arr: Union[list, tuple]):
        self.arr = arr

    def step_search(self, element: int):
        start, end = 0, len(self.arr)-1
        mid = (start + end) // 2
        while start <= end:
            if self.arr[mid] < element:
                start = mid+1
            elif self.arr[mid] > element:
                end = mid - 1
            elif self.arr[mid] == element:
                return mid
        if start > end:
            return -1

    def binarySearch(self, arr, first, last, key):
        mid = (first + last) / 2
        while first <= last:
            if arr[mid] < key:
                first = mid + 1
            elif arr[mid] == key:
                print("Element is found at index: " + mid)
                break
            else:
                last = mid - 1

            mid = (first + last) / 2

        if first > last:
            print("Element is not found!")
