axiom = 'F-G-G'
n = 6
subs = {
    'F': 'F-G+F+G-F',
    'G': 'GG'
}

graphics = {
    'F': lambda t: t.forward(3),
    'G': lambda t: t.forward(3),
    '+': lambda t: t.left(120),
    '-': lambda t: t.right(120)
}
