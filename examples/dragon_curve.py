axiom = 'FX'
n = 12
subs = {
    'X': 'X+YF+',
    'Y': '-FX-Y'
}

graphics = {
    'F': lambda t: t.forward(3),
    '+': lambda t: t.right(90),
    '-': lambda t: t.left(90)
}
