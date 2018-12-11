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

    return tuple(triangle_cordinates)


def make_triangle(turtle, triangle_cordinates):
    turtle.penup()
    # go to stating point
    turtle.goto(triangle_cordinates[-1])
    for x, y in triangle_cordinates:
        turtle.pendown()
        turtle.goto(x, y)


def crop_triangle(cuting_cordinates):
    triangles = []
    for main_cordinate in cuting_cordinates:
        new_triangle = []

        # make a copy of cordinates
        another_cordinates = list(cuting_cordinates[:])

        # delete itering cordinate and add first point of triangle
        new_triangle.append(another_cordinates.pop(another_cordinates.index(main_cordinate)))

        # get centred point of side and other triangle points
        for dx, dy in another_cordinates:
            x, y = main_cordinate
            new_x = round((x + dx)/2, 3)
            new_y = round((y + dy)/2, 3)
            new_triangle.append((new_x, new_y))

        triangles.append(new_triangle)
    return triangles


def serpinskiy_triangle(turtle, triangles, depth_scale):
    if depth_scale <= 0:
        return 0
    smaller_triangles = []
    for triangle in triangles:
        make_triangle(turtle, triangle)
        smaller_triangles = [*smaller_triangles, *crop_triangle(triangle)]
    depth_scale -= 1
    serpinskiy_triangle(turtle, smaller_triangles, depth_scale)



def main():
    main_triangle = [generate_triangle_cordinates(bob, size=250), ]  # pack to list for iteration
    serpinskiy_triangle(bob, main_triangle, depth_scale=6)

    bob.penup()
    bob.home()

    print('turtle is done!')
    turtle.done()


if __name__ == '__main__':
    main()
