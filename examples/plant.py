def pop(t):
    t.penup()
    state = stack.pop()
    t.goto(state['pos'])
    t.seth(state['heading'])
    t.pendown()


def push(t):
    state = {'pos': t.pos(), 'heading': t.heading()}
    stack.append(state)


stack = []

axiom = 'X'
n = 6
subs = {
    'F': 'FF',
    'X': 'F+[[X]-X]-F[-FX]+X'
}

graphics = {
    'F': lambda t: t.forward(2),
    '+': lambda t: t.right(25),
    '-': lambda t: t.left(25),
    '[': lambda t: push(t),
    ']': lambda t: pop(t)
}
