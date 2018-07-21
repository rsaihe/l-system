axiom = 'F'
n = 5
subs = {
    'F': 'F+F-F-F+F'
}

graphics = {
    'F': lambda t: t.forward(2),
    '+': lambda t: t.left(90),
    '-': lambda t: t.right(90)
}
