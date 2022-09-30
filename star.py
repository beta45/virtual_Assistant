import turtle
t= turtle.Turtle()
s= turtle.Screen()
s.bgcolor('Black')
t.speed(10)
col=['white','pink','grey','green']
c=0

for i in range(500):
    t.forward(i*5)
    t.speed(5000)
    # t.right(45)
    t.left(144)
    t.color(col[c])
    if c==3:
        c=0
    else:
        c+=1