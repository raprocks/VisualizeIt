from colorama import Cursor, init, deinit, Fore, Back, Style
init()
UP = Cursor.UP()
DOWN = Cursor.DOWN()
RIGHT = Cursor.FORWARD()
LEFT = Cursor.BACK()


print(Fore.LIGHTBLUE_EX+"Hello"+Style.RESET_ALL)
print(Fore.BLUE + "Hello"+Style.RESET_ALL)
