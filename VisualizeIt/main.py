from . import create_random_array
import typer
from VisualizeIt.visualizer import SortVisualizer
from VisualizeIt_implementations.BubbleSort import BubbleSort
from typing import List
app = typer.Typer()


@app.command()
def visualize_sort(array: List[int] = [], speed: str = 'mid'):
    """
    Sorting Visualizer
    """
    if len(array) == 0:
        array = create_random_array(15)
    algorithm = BubbleSort(list(array))
    printer = SortVisualizer(algorithm)
    printer.run(speed=speed)


@app.command()
def visualize_search(array: str, element: int = 0, speed: str = 'mid'):
    """
    Search Visualizer
    """
    print("array is", array.split(' '))


if __name__ == "__main__":
    app()
