from typing import Union


class BubbleSort:
    def __init__(self, arr: Union[list, tuple]):
        self.arr = arr

    def bubblesort(self):
        temp = 0
        for i in range(0, len(self.arr)):
            for j in range(1, len(self.arr)-1):
                if self.arr[j-1] > self.arr[j]:
                    # swap elements
                    temp = self.arr[j-1]
                    self.arr[j-1] = self.arr[j]
                    self.arr[j] = temp

        print("The sorted array is = ")
        for i in range(0, len(self.arr)):
            print(self.arr[i])
