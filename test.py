from VisualizeIt.visualizer import Visualizer
from VisualizeIt_implementations.BinarySearch import BinarySearch

algorithm = BinarySearch([1, 2, 4, 3, 5, 7, 6])

printer = Visualizer(algorithm)

print(printer.label)
