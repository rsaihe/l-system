def iterate(text, subs):
    new_text = []
    for c in list(text):
        if c in subs:
            new_text.append(subs[c])
        else:
            new_text.append(c)

    return ''.join(new_text)


if __name__ == '__main__':
    import argparse
    import importlib
    import turtle

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate fractal images.')
    parser.add_argument('module',
                        help='Python module containing rules for the l-system')
    parser.add_argument('-n', '--num', help='set number of iterations',
                        type=int, default=-1)
    args = parser.parse_args()

    try:
        # Import rule module
        rule = importlib.import_module(args.module)

        # Expand L-system
        num = args.num
        if (num < 0):
            num = rule.n

        text = rule.axiom
        for _ in range(num):
            text = iterate(text, rule.subs)

        # Render using turtle graphics
        turtle.screensize(canvwidth=2000, canvheight=2000)
        turtle.hideturtle()
        turtle.speed(0)
        for c in text:
            if c in rule.graphics:
                rule.graphics[c](turtle)

        turtle.done()
    except ModuleNotFoundError:
        print('Invalid rule module. Make sure not to include file extension.')
    except turtle.Terminator:
        pass
