from colorama import Cursor, init, deinit
init()
UP = Cursor.UP()
DOWN = Cursor.DOWN()
RIGHT = Cursor.FORWARD()
LEFT = Cursor.BACK()


def p(x):
    print(x, end='')


p('H'+DOWN+LEFT*3)
p('I'+LEFT+DOWN)
p('I'+LEFT+DOWN)
p(UP*3+RIGHT)
p('B')
p(DOWN+LEFT)
p('Y')
p(DOWN+LEFT)
p('E')
deinit()
