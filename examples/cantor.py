def forward(t):
    t.penup()
    t.forward(3)


def no_draw_forward(t):
    t.pendown()
    t.forward(3)


axiom = 'A'
n = 5
subs = {
    'A': 'ABA',
    'B': 'BBB'
}

graphics = {
    'A': lambda t: forward(t),
    'B': lambda t: no_draw_forward(t)
}
