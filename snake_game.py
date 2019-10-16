import turtle
import time
import random

delay = 0.1 # delays the main game loop so that snake can be seen moving
score = 0
high_score = 0
#Set up screen

window = turtle.Screen()
window.title("Snake")
window.bgcolor("green")
window.setup(width =600, height =600)
window.tracer(0)# turns off screen updates
#using turtle module to create a snake game
#create Snake Head
head = turtle.Turtle() 
head.speed(0) #animation speed of turtle 
head.shape("square") # shae of turtle
head.color("black")# color of snake
head.penup() # ensures the snake does not draw any lines
head.goto(0,0) #snake head will start at the center of the screen
head.direction = "stop" #when the game starts the snakke stays dormant

#snake food
food = turtle.Turtle()
food.speed(0)#animation speed of food
food.shape("circle") #shape of food
food.color("red")#color of food
food.penup() # ensures the food does not draw any lines
food.goto(0,100)

#snake body
segments = []

#pen
pen  =turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align = "center", font = ("arial", 24, "normal") )









#functions
def move(): # snake movement

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20) # moves up by 20 pixels  each time

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20) # moves down by 20 each time

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20) # moves left by 20 each time


    if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20) # moves right by 20 each time


def move_up(): #upward movement
    if head.direction != "down":
        head.direction = "up"   # snake can move up once its not moving down

def move_down():#downward movement
    if head.direction != "up":
        head.direction = "down" # snake can move down once its not moving up

def move_left(): #leftward movement
    if head.direction != "right":
        head.direction = "left" # snake can move left once its not moving right


def move_right():#rightward movement
    if head.direction != "left": # snake can move right once its not moving left
        head.direction = "right"

#keyboard bindings
window.listen() #game window listens for keyboard press
#function mapping for key presses
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

#main game mainloop
while True:
    window.update() #updates screen each iteration
    #checkk for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor()>290 or head.ycor() <-290: # if snake out of border range
        delay = 0.1
        pen.clear()
        time.sleep(1)
        for segment in segments: #clear the segments off the screen
            segment.goto(-1000,-1000)

        segments.clear() # empty the  segments list
        head.goto(0,0) #head returns to original postion
        head.direction = "stop" # head pauses and wait for key press

        score = 0 #reset Score
        pen.write("Score: {} High Score {}".format(score,high_score),align = "center", font = ("arial", 24, "normal"))



    #check if snake eat food


    if head.distance(food) < 20: #once the distance between snake and food is less than 20 it means the snake ate the food
        delay -=0.001
        #move food to random location
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #add a segments
        #snake grows when food is eaten
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("purple")
        new_segment.penup()
        segments.append(new_segment)

        #Add score
        score +=10
 
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score {}".format(score,high_score),align = "center", font = ("arial", 24, "normal"))

    # this set of code allows the snake body to grow
    #move the end segments first in reverse order
    for index in range(len(segments) -1, -1, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

        #move segment 0 to where head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

    move()

    #check for head collision with body
    for segment in segments:

        if segment.distance(head) < 20: #if head collides with body
            pen.clear()
            delay = 0.1
            time.sleep(1)
            segment.goto(-1000,-1000)

            segments.clear() #clear the segment list

            head.goto(0,0) # head returns to center of screen
            head.direction = "stop"

            score = 0 #reset score

            pen.write("Score: {} High Score {}".format(score,high_score),align = "center", font = ("arial", 24, "normal")) #write score on screen




    time.sleep(delay) # while loop is delayed in order to see snake movement 


window.mainloop()
