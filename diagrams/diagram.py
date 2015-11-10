import turtle
import random


def get_dict(string):

    arr = {}
    for i in set(string.split()):
        arr[i] = string.split().count(i)

    return arr


def drow(string, type='sectors'):

    arr = get_dict(string)

    if type == 'sectors':
        drow_sectors(arr)
    elif type == 'rays':
        drow_rays(arr)
    else:
        print 'Error, pls choice type: sectors or rays'

def random_color():

    arr = []
    for i in range(3):
        arr.append(random.randint(0, 200))

    return arr


def drow_sectors(arr):

    turtle.reset()
    turtle.colormode(255)
    sum = reduce(lambda a, b: a + b, arr.values())
    x = float(360.0 / sum)
    radius = 100
    new_arr = []

    for z, i in arr.iteritems():
        color = random_color()

        turtle.begin_fill()
        turtle.color(color)
        turtle.pencolor('#000')
        turtle.circle(radius, i * x)
        turtle.goto(0, radius)
        turtle.end_fill()
        turtle.left(90)
        turtle.backward(radius)
        turtle.right(90)

        new_arr.append([z, i, color])

    n = 0
    for k in new_arr:
        print k[2]
        turtle.up()
        turtle.goto(180, 200 - n)
        n += 30
        turtle.down()
        turtle.begin_fill()
        turtle.color(k[2])
        turtle.pencolor('#000')
        turtle.circle(5)
        turtle.end_fill()
        s = '{} - {} time(s)'.format(k[0], k[1])
        turtle.up()
        turtle.forward(15)
        turtle.down()
        turtle.write(s)

    turtle.mainloop()


def drow_rays(arr):

    turtle.reset()
    turtle.colormode(255)
    angle = 360 / len(arr)
    for i, j in arr.iteritems():
        color = random_color()
        turtle.pencolor(color)
        turtle.down()
        for k in xrange(j / min(arr.values())):
            turtle.forward(100)
            turtle.circle(3)

        turtle.up()
        turtle.forward(50)
        turtle.down()
        turtle.write(i)
        turtle.up()

        turtle.backward(j / min(arr.values()) * 100 + 50)
        turtle.left(angle)

    turtle.mainloop()


drow('php javascript hello world script hello world script hello worldscript hello world', 'rays')



