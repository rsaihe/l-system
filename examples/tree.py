def pop(t):
    t.penup()
    state = stack.pop()
    t.goto(state['pos'])
    t.seth(state['heading'])
    t.pendown()
    t.right(45)


def push(t):
    state = {'pos': t.pos(), 'heading': t.heading()}
    stack.append(state)
    t.left(45)


stack = []

axiom = '0'
n = 7
subs = {
    '0': '1[0]0',
    '1': '11'
}

graphics = {
    '0': lambda t: t.forward(3),
    '1': lambda t: t.forward(3),
    '[': lambda t: push(t),
    ']': lambda t: pop(t)
}
