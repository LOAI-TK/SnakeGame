# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 08:51:06 2023

@author: LOAI
"""

import turtle as tr
import time
import random     # random numbers

delay = 0.1

#set up the screen 
wn = tr.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=540,height=540)  #setup the screen
wn.tracer(0)  # turns of the screen updates

# snake head

head = tr.Turtle()
head.speed(0)    #animation speed
                 # 0 is the fastest animation speed 
head.shape("square")
head.color("cyan")
head.penup()    #so that it doesnt draw anything 
head.goto(0,0)  #when the head starts 
                #we want it to be in the center of the screen
head.direction= "stop"

#Snake Food

food = tr.Turtle()
food.speed(0)    
food.shape("circle")
food.color("red")
food.penup() 
food.goto(0,100) 


Segments=[]
#when the player touches the food 
#we need to add a segment to the snake


#Functions 

def go_up():
    head.direction = "up"
    
def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"    


def move():
    if head.direction == "up":
        y=head.ycor() #this is y coordinates
        head.sety(y+20)
        
    if head.direction == "down":
        y=head.ycor() #this is y coordinates
        head.sety(y-20)
        
    if head.direction == "left":
        x=head.xcor() #this is x coordinates
        head.setx(x-20)
        
    if head.direction == "right":
        x=head.xcor() #this is x coordinates
        head.setx(x+20)
        
#keyboard Bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")        
        


#main Game Loop
while True:  # this Loop made for screen updates 
    wn.update() 
    
    #check for a collisoiobn with the border 
    if head.xcor()>260 or head.xcor()<-260 or head.ycor()>260 or head.ycor()<-260:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"  
        # Hide the segments
        for Segment in Segments:
            Segment.goto(1000, 1000)
    #clear the segments list
        Segments.clear()
    
    #check for collision with the food
    if head.distance(food)<20:
        #move the food to random spot
        x = random.randint(-260, 260)  
        y = random.randint(-260, 260)
        food.goto(x,y)
        
        #add a segment
        new_segment = tr.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        Segments.append(new_segment)
        
    #Move the end segment first in reverse order     
    for index in range(len(Segments)-1, 0, -1):
        x=Segments[index-1].xcor()
        y=Segments[index-1].ycor()
        Segments[index].goto(x, y)
    
    #Move segments 0 to where the head is
    if len (Segments)>0:
        x=head.xcor()
        y=head.ycor()
        Segments[0].goto(x,y)
        
    move()
# Check for head collision with the body segments
    for Segment in Segments:
        if Segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"
        
        # Hide the segments
            for Segment in Segments:
                Segment.goto(1000, 1000)

        # Clear the segments list
            Segments.clear()

    
    time.sleep(delay)

wn.mainloop() #screen is on loop
