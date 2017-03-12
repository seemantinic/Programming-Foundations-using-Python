import turtle

def draw_rhombus(some_turtle):
    #for i in range(1,5):
     some_turtle.right(140)
     some_turtle.forward(50)
     some_turtle.right(40)
     some_turtle.forward(50)
     some_turtle.right(140)
     some_turtle.forward(50)
     some_turtle.right(40)
     some_turtle.forward(50)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    #create turtle brad for square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("orange")
    brad.speed(5)
    for i in range(1,37):
        draw_rhombus(brad)
        brad.right(10)
    brad.right(90)
    brad.forward(180)

draw_art()
