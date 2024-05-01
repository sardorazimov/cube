import turtle
from math import sin, cos

win = turtle.Screen()
win.setup(600, 600)
win.tracer(0)
counter = 0


def rotate(x, y, r):
    s, c = sin(r), cos(r)
    return x * c - y * s, x * s + y * c


class Cube:
    VERTEXES = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1), (-1, 1, 1)]
    TRIANGLES = [(0, 1, 2), (2, 3, 0), (0, 4, 5), (5, 1, 0), (0, 4, 3), (4, 7, 3), (5, 4, 7), (7, 6, 5), (7, 6, 3), (6, 2, 3), (5, 1, 2), (2, 6, 5)]

    def __init__(self, pos, counter):
        self.pos = pos
        x, y, z = pos
        self.counter = counter
        self.t = turtle.Turtle()
        self.t.color('blue')

    def draw(self):
        for triangle in self.TRIANGLES:
            points = []
            for vertex in triangle:
                x, y, z = self.VERTEXES[vertex]
                x, z = rotate(x, z, self.counter)
                y, z = rotate(y, z, self.counter)
                x, y = rotate(x, y, self.counter)
                z += 5
                if z != 0:
                    f = 400 / z
                    sx, sy = x * f, y * f
                    points.append((sx, sy))

            self.t.up()
            self.t.goto(points[0][0], points[0][1])
            self.t.down()
            self.t.goto(points[1][0], points[1][1])
            self.t.goto(points[2][0], points[2][1])
            self.t.goto(points[0][0], points[0][1])
            self.t.up()


cube = Cube((0, 0, 0), counter)
while True:
    cube.t.clear()
    cube.draw()
    win.update()
    cube.counter += 0.025
