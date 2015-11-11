import turtle

class Serpinsky(object):

    def __init__(self, points, n, turtleName):
        self.points = points
        self.myTurtle = turtleName

        self.serpinsky(self.points, n)

    def getMid(self, point1, point2):
        return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

    def drow_triangle(self, points):
        self.myTurtle.up()
        self.myTurtle.goto(points[0][0], points[0][1])
        self.myTurtle.down()
        self.myTurtle.goto(points[1][0], points[1][1])
        self.myTurtle.goto(points[2][0], points[2][1])
        self.myTurtle.goto(points[0][0], points[0][1])

    def serpinsky(self, points, repeat):
        self.drow_triangle(points)

        if repeat > 0:
            repeat -= 1
            self.serpinsky([points[0], self.getMid(points[0], points[1]), self.getMid(points[0], points[2])], repeat)
            self.serpinsky([points[1], self.getMid(points[0], points[1]), self.getMid(points[1], points[2])], repeat)
            self.serpinsky([points[2], self.getMid(points[2], points[1]), self.getMid(points[0], points[2])], repeat)


points = [[-200, 0],[100, 300],[400, 0]]
newpoints = [[0, 0], [50, 50], [100, 0]]

myTurtle = turtle.Turtle()
newTurtle = turtle.Turtle()

a = Serpinsky(points, 2, myTurtle)
b = Serpinsky(newpoints, 2, newTurtle)

turtle.mainloop()