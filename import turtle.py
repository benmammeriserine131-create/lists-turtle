import turtle  
t = turtle.Turtle()
side_length = int(input("Enter the length: "))
t.pensize(3)
t.speed(5)
t.showturtle()
colors = ["red", "blue", "green", "orange", "purple", "black"]
for i in range(6):
    t.color(colors[i])        
    t.forward(side_length)    
    t.right(60)                
turtle.done()
