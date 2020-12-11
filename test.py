from VisualizeIt.visualizer import SearchVisualizer
from VisualizeIt_implementations.BinarySearch import BinarySearch
algorithm = BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

printer = SearchVisualizer(algorithm)

printer.run(element=7)
