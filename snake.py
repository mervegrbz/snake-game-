from turtle import*

import random
import time

delay=0.07
screen=Screen()
screen.setup(500, 500)
screen.tracer(0)
width=500
height=500
screen.bgcolor('green')
snake=Turtle()
snake.shape("square")
snake.shapesize(1.3,1)
snake.penup()
dx =20
dy =0
snake.speed()
face="no"
snakesize=1
start=True
snake.color("black")



headx=snake.xcor()
heady=snake.ycor()
def control():
    global start
    start=True



food=Turtle()
food.penup()
food.goto(-30,-30)
food.shape("circle")
food.color("red")
food.shapesize(1)
food.speed(20)
food.showturtle()
tails=[]
def Up():
    global face
    global dx,dy
    if(face!="Down"):
        snake.setheading(90)
        dy=20
        dx=0        
        face="Up"
def Down():
    global face
    global dx,dy
    if(face!="Up"):
        snake.setheading(-90)
        dy=-20
        dx=0
        face="Down"
def Right():
    global face
    global dx,dy
    if(face!="Left"):
        dy=0
        dx=20
        snake.setheading(0)
        
        face="Right"
def Left():
    global face
    global dx,dy
    if(face!="Right"):
        dy=0
        dx=-20
        snake.setheading(180)
        face="Right"

screen.listen()
screen.onkey(Up,"Up")

screen.onkey(Down,"Down")

screen.onkey(Left,"Left")

screen.onkey(Right,"Right")

screen.onkey(control,"Return")
Score=0



kalem=Turtle()
kalem.hideturtle()
def skor():
    kalem.penup()
    kalem.goto(-30,200)
    kalem.clear()
    text="Score "+str(Score)
    kalem.write(text,align="center",font=["Comic Sans MS",20,])
def gameover():
    
    
    kalem.clear()
    kalem.penup()
    kalem.goto(0,0)
    kalem.write("Game Over "+str(Score),align="center",font=["Comic Sans MS",30,])
    for tail in tails:

        tail.hideturtle()
    tails.clear()
   

while True:
    screen.update()
    if (not start):
        continue
    skor()
    screen.tracer(False)

    if snake.distance(food)<20:
        food.setx(random.randint(-200,200))
        food.sety(random.randint(-200,200))
        Score+=1
        skor()
        newtail=Turtle()
        newtail.shape("square")
        newtail.shapesize(1,1)
        newtail.penup()
        newtail.speed(0)
        newtail.color("black")
        tails.append(newtail)
        delay-=0.001
    for index in range(len(tails)-1,0,-1 ):
    
        
        x=tails[index-1].xcor()
        y=tails[index-1].ycor()
        
        tails[index].goto(x, y)
        
    if len(tails)>0:
        
        x=snake.xcor()
        y=snake.ycor()
        tails[0].goto(x,y)

        
    
    for index in range(1,len(tails)):
        if(snake.distance(tails[index])<20):
            gameover()
            start=False
            Score=0
            time.sleep(1)
            delay=0.08
            snake.goto(0,0)
            break
    
    if (snake.xcor()>width/2) or snake.xcor()<-width/2 or snake.ycor()>height/2 or snake.ycor()<-height/2:
        gameover()
        start=False
        Score=0
      
        delay=0.08
        snake.goto(0,0)


    snake.sety(snake.ycor()+dy)
    snake.setx(snake.xcor()+dx)
    time.sleep(delay+0.02)


        



     
   
