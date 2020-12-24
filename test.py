from VisualizeIt.visualizer import SortVisualizer
from VisualizeIt_implementations.BubbleSort import BubbleSort
# Binary Search
#algorithm = BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#printer = SearchVisualizer(algorithm)

# printer.run(element=100)

algorithm = BubbleSort([6, 8, 5, 1, 4, 18, 26, 2, 0])
printer = SortVisualizer(algorithm)
printer.run(speed='godspeed')
