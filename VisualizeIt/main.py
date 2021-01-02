from VisualizeIt.helpers import create_random_array, str_to_arr
import typer
from random import choice

# App Initialization
app = typer.Typer()


@app.command()
def sort(array: str = "", speed: str = 'mid', array_size: int = 10):
    """
    Sorting Visualizer
    """
    if len(array) == 0:
        array_to_sort = create_random_array(int(array_size))
    else:
        array_to_sort = str_to_arr(array)

    from VisualizeIt_implementations.BubbleSort import BubbleSort
    algorithm = BubbleSort(list(array_to_sort))
    from VisualizeIt.visualizer import SortVisualizer
    printer = SortVisualizer(algorithm)
    printer.run(speed=speed)


@app.command()
def search(array: str = "", element: int = 0,
           speed: str = 'mid', array_size: int = 10):
    """Visualizer For Searching Algorithms
    currently supports *Binary Search*

    :array: a string of space separated integers which will be converted to a List.
    :element: Integer to search for in the array
    :speed: speed of Visualization, can be slow, mid, fast, ultra, godspeed or flash
    :array_size: the size of array to generate if it is not specified explicitly
    :returns: None

    """
    if len(array) == 0:
        print('no array provided, making a random array \
                and choosing a random element from it to search (or not?)')
        array_to_search = create_random_array(10)
        element = int(choice(array))
    print("array", array_to_search)
    print("element", element)

    pass


if __name__ == "__main__":
    app()
