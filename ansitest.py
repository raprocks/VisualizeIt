
UP = '\u001b[1A'
DOWN = '\u001b[1B'
RIGHT = '\u001b[1C'
LEFT = '\u001b[1D'


def p(x):
    print(x, end='')


p('H'+LEFT+DOWN)
p('I'+LEFT+DOWN)
p('I'+LEFT+DOWN)
p(UP*3+RIGHT)
p('B')
p(DOWN+LEFT)
p('Y')
p(DOWN+LEFT)
p('E')
