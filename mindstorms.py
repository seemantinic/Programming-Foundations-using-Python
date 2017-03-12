import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    #create turtle brad for square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
#    n=0
#    while n<4:
#        brad.forward(100)
#        brad.right(90)
#        n += 1

#def draw_circle():
#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.color("yellow")
#    angie.circle(100)

#def draw_triangle():
#    juno = turtle.Turtle()
#    juno.shape("triangle")
#    juno.color("white")
#    i = 0
#    while i < 2:
#        juno.right(60)
#        juno.forward(60)
#        i += 1
        
##window.exitonclick()

draw_art()
