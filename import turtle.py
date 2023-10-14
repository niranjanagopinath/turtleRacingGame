import turtle
import time
import random


WIDTH,HEIGHT=500,500
COLOURS=['orange','pink','blue','red','green','brown','black','maroon','purple','cyan']

 
def get_the_number_of_turtles():
    racers=0
    while True:
        racers=input("enter the number of racers(2-10)")
        if racers.isdigit():
            racers=int(racers)
        else:
            print("please enter a number")
            continue
        if 2<=racers<=10:
            return racers
            break
        else:
             print("enter value between 2 and 10")

             
             
def creating_turtle_screen():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("the turtle game")

    

def create_turtles(shuffled_colours):
    turtles=[]
    spacingg=WIDTH//(len(shuffled_colours)+1) #cuz we need the turtles to be equidistant from the edge of the screen and the from each other
    for i,colour in enumerate(shuffled_colours): # what enumerate basically does it that it makes a list in the form of [(the index value, the element of the iterable)]
        turt=turtle.Turtle()
        turt.color(colour)
        turt.shape("turtle")
        turt.left(90)
        turt.penup()
        turt.setpos(-WIDTH//2 + spacingg*(i+1),-HEIGHT//2+20)
        turt.pendown()
        turtles.append(turt)
    return turtles
     
     
        
def race(shuffled_colours):
    turtles=create_turtles(shuffled_colours)
    while True:
        for  turt in turtles:
            distance=random.randrange(1,20)
            turt.forward(distance)
            
            x,y= turt.pos()
            if y>=HEIGHT//2-5:
                return shuffled_colours[turtles.index(turt)]
            
    



    
racers=get_the_number_of_turtles()
creating_turtle_screen()


random.shuffle(COLOURS)
shuffled_colours=COLOURS[:racers] #this gives same number of shuffled colours as the racers
WINNER=race(shuffled_colours)
print("the winner is",WINNER)


