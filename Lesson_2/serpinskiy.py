import turtle
bob = turtle.Turtle()


def generate_triangle_cordinates(turtle, size=70):
    """
    make the shape with adjustable size
    and return its cordinates
    """
    # returning list
    triangle_cordinates = []
    # make centre point
    home_pos = (0, 0)
    turtle.penup()
    # watch up, turtle!
    turtle.left(90)
    # get cordinates
    for i in range(3):
        turtle.forward(size)
        triangle_cordinates.append(turtle.pos())
        turtle.goto(home_pos)
        turtle.left(120)

    return triangle_cordinates


def make_triangle(turtle, triangle_cordinates):
    turtle.penup()
    # go to stating point
    turtle.goto(triangle_cordinates[-1])
    for x, y in triangle_cordinates:
        turtle.pendown()
        turtle.goto(x, y)


def crop_triangle(cordinates):
    triangles = []
    for main_cordinate in cordinates:
        new_triangle = []
        # make a copy of cordinates
        another_cordinates = cordinates[:]
        # delete itering cordinate
        new_triangle.append(another_cordinates.pop(another_cordinates.index(main_cordinate)))
        # get centred point of side
        for dx, dy in another_cordinates:
            x, y = main_cordinate
            new_x = (x + dx)/2
            new_y = (y + dy)/2
            new_triangle.append((new_x, new_y))
        triangles.append(new_triangle)
    return triangles


def serpinskiy_triangle(turtle, cordinates, depth):
    def smaller_triangles(turtle, triangle, deep):
        deep -= 1
        if deep is 0:
            return 0
        # we start go deeper
        for triangle in crop_triangle(triangle):
            make_triangle(turtle, triangle)
            smaller_triangles(turtle, triangle, deep)
    # write main triangle
    make_triangle(turtle, cordinates)
    smaller_triangles(turtle, cordinates, deep=depth)


def main():
    bob.speed('fastest')
    cord = generate_triangle_cordinates(bob, size=200)
    serpinskiy_triangle(bob, cord, depth=6)

    bob.penup()
    bob.home()

    turtle.done()


if __name__ == '__main__':
    main()
