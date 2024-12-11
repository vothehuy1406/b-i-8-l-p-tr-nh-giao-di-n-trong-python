print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
import turtle
import random


screen = turtle.Screen()
screen.bgcolor("white")  
painter = turtle.Turtle() 
painter.pensize(3)  


colors = ["red", "blue", "green", "orange", "purple"]


for i in range(12):
    color = random.choice(colors)  
    painter.pencolor(color) 
    painter.circle(100)  
    painter.right(30)  
    painter.setposition(0, 0) 

painter.hideturtle() 
screen.mainloop()  
