# degree 有限的情况下，degree = n 的三角形，
# 是由3个degree = n-1的三角形按照品字形平叠而成的。
# 同时这三个 degree = n - 1的三角形的边长均为degree = n的三角形的一半。
# 当degree = 0，则就是一个等边三角形，这是递归基本结束条件

import turtle

def sierpinski(degree,points): # points are stored in tuple form (x,y)
    colormap = ['blue','red','green','white','yellow','orange']
    drawTriangle(points, colormap[degree])
    if degree > 0:
        sierpinski(degree - 1,
        {'left':points['left'],
        'top':getMid(points['left'],points['top']),
        'right':getMid(points['left'],points['right'])})

        sierpinski(degree - 1,
        {'left':getMid(points['left'],points['top']),
        'top':points['top'],
        'right':getMid(points['top'],points['right'])})

        sierpinski(degree - 1,
        {'left':getMid(points['left'],points['right']),
        'top':getMid(points['right'],points['top']),
        'right':points['right']})

def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 )

def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

t = turtle.Turtle()

points = {'left': (-200, -100), 'top':(0, 200), 'right':(200, -100)}

sierpinski(5,points)

turtle.done()


