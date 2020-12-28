from . import create_random_array
import typer
from VisualizeIt.visualizer import SortVisualizer
from VisualizeIt_implementations.BubbleSort import BubbleSort
from random import choice
app = typer.Typer()


def str_to_arr(inp_str: str):
    return list(map(int, inp_str.strip().split(' ')))


@app.command()
def visualize_sort(array: str = "", speed: str = 'mid', array_size: int = 10):
    """
    Sorting Visualizer
    """
    if len(array) == 0:
        array = create_random_array(array_size)
    else:
        array = str_to_arr(array)
    algorithm = BubbleSort(list(array))
    printer = SortVisualizer(algorithm)
    printer.run(speed=speed)


@app.command()
def visualize_search(array: str = "", element: int = 0,
                     speed: str = 'mid', array_size: int = 10):
    """
    Search Visualizer
    """
    if len(array) == 0:
        print('no array provided, making a random array \
                and choosing a random element from it to search (or not?)')
        array = create_random_array(10)
        element = choice(array)
    print("array", array)
    print("element", element)


if __name__ == "__main__":
    app()
