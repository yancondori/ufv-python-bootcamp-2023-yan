import turtle
import random2

#Setting Up the Turtles 
player_one = turtle.Turtle()
player_one.color("black")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("red")
player_two.penup()
player_two.goto(-200,100)

#Setting Up Turtle's Homes
player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

#Creating the Die as a dice number list
die = [1,2,3,4,5,6]

# The Game, input ask you how many times you roll the dice the shows you the resul (1 to 6) and it'd multiplies by 20
for i in range(20):
    if player_one.pos() >= (300,100): #the goal has the tuple (300,100)
            print("Player One Wins!")
            break
    elif player_two.pos() >= (300,-100):
            print("Player Two Wins!")
            break
    else:
            player_one_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random2.choice(die)
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(20*die_outcome)
            player_one.fd(20*die_outcome)
            player_two_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random2.choice(die)
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(20*die_outcome)
            player_two.fd(20*die_outcome)