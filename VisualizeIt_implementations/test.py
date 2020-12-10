from BinarySearch import BinarySearch
import time

array = [1, 2, 3, 5, 7, 9, 10, 27, 56, 78, 89, 789, 899, 1000]

sorter = BinarySearch(array)

steps = sorter.step_search(899)

while True:
    print(steps.__next__())
    print()
    print()
    time.sleep(1.5)
