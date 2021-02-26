from VisualizeIt.helpers import create_random_array, str_to_arr
import typer
from random import choice, randint
from time import sleep

# App Initialization
app = typer.Typer()


@app.command()
def sort(
    algo: str = typer.Option("", help="ALgorithm to visualize, currently \
                supports 'BubbleSort' and 'ImprovedBubbleSort'"),
    array: str = typer.Option("", help="A Space Separated String of intergers which \
                    will be converted to a list of integers using the map \
                        function. Defaults to a randomly generated array."),
    speed: str = typer.Option('mid', help="Speed of the visualization.\
            Defaults to 'mid', can be 'slow', 'mid', 'fast', 'ultra',\
                 'godspeed' or 'flash'."),
    array_size: int = typer.Option(10, help="size of the array to be generated \
if not explicitly provided. Defaults to 10.")
):
    """Visualizer for Sorting Algorithms

    Args:

        algo (str): ALgorithm to visualize,
currently supports "BubbleSort" and "ImprovedBubbleSort".

        array (str, optional): A Space Separated String of intergers which
 will be converted to a list of integers using the map function.
        Defaults to a randomly generated array.

        speed (str, optional): Speed of the visualization. Defaults to 'mid',
 can be 'flash', 'godspeed', 'ultra', 'slow', 'mid','fast'.

        array_size (int, optional): size of the array to be generated
if not explicitly provided. Defaults to 10.
    """
    if len(array) == 0:
        print("No Array Provided, Making a Random Array")
        sleep(1)
        array_to_sort = create_random_array(int(array_size))
    else:
        array_to_sort = str_to_arr(array)

    if algo.lower() == "bubblesort":
        from VisualizeIt_implementations.BubbleSort import BubbleSort
        algorithm = BubbleSort(list(array_to_sort))
        from VisualizeIt.visualizer import SortVisualizer
        printer = SortVisualizer(algorithm)
        printer.run(speed=speed)
    elif algo.lower() == "improvedbubblesort":
        pass
    else:
        print(
            f"""Invalid Algorithm Requested,
            Support for {algo} is not ready yet."""
        )


@app.command()
def search(algo: str, array: str = "", element: int = 0,
           speed: str = 'mid', array_size: int = 10):
    """Visualizer For Searching Algorithms
    currently supports *Binary Search*

    Args:
        algo (str): Algorithm to Visualize, Currently supports "BinarySearh"
you can give array as input with an element or
let the program make an array and choose an element
not compulsorily from the array.

        array (str, optional): A Space Separated String of intergers
which will be converted to a list of integers using the map function.
Defaults to a randomly generated array.

        speed (str, optional): Speed of the visualization.
Defaults to 'mid', can be 'flash', 'godspeed', 'ultra', 'slow', 'mid','fast'.

        array_size (int, optional): size of the array to be generated
if not explicitly provided. Defaults to 10.
    """
    if len(array) == 0:
        print('no array provided, making a random array \
                and choosing a random element from it to search (or not?)')
        array_to_search = create_random_array(10)
        choose = bool(randint(1, 100) > 50)
        if choose:
            element = int(choice(array))
        else:
            element = int(randint(1, max(array_to_search)))

    if algo.lower() == "binarysearch":
        from visualizeit_implementations.BinarySearch import BinarySearch
        algorithm = BinarySearch(array)
        from visualizeit.visualizer import SearchVisualizer
        printer = SearchVisualizer(algorithm)
        printer.run(element=element, speed=speed)
    else:
        print(
            f"""Invalid Algorithm Requested,
            Support for {algo} is not ready yet."""
        )


if __name__ == "__main__":
    app()
