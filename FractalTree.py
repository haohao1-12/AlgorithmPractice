#基本结束条件：树枝过短
#关键点：回退到原来的位置

import turtle

def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15) # 下一步没有回退是因为循环的尾部已经回退到了起点
        t.left(40)
        tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)

t = turtle.Turtle()
t.left(90)
t. penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(75)
t.hideturtle()
turtle.done()