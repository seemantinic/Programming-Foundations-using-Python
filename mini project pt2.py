import turtle

def draw_circle(some_turtle):
    for i in range(1,44):
        some_turtle.circle(i)
        i += 4
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    #create turtle brad for square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("orange")
    brad.speed(15)
    for i in range(1,9):
        draw_circle(brad)
        brad.right(45)
    brad.right(90)
    brad.forward(180)

draw_art()
