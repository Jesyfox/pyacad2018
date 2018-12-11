import turtle

bob = turtle.Turtle()


def scale_filling_curve(turtle, size, step, scale):
    for i in range(100):
        turtle.circle(size, step)
        turtle.forward(size)
        size *= scale


if __name__ == '__main__':
    SIZE = 10
    STEP = 130
    SCALE = 1.04

    bob.speed('fastest')

    scale_filling_curve(bob, SIZE, STEP, SCALE)

    print('turtle is done!')
    turtle.done()
