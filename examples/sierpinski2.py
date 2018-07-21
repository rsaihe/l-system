axiom = 'A'
n = 8
subs = {
    'A': 'B-A-B',
    'B': 'A+B+A'
}

graphics = {
    'A': lambda t: t.forward(2),
    'B': lambda t: t.forward(2),
    '+': lambda t: t.left(60),
    '-': lambda t: t.right(60)
}
