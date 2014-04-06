# Guess the week number

import random
import math
import simplegui

# initialize global variables used in your code
secret_number = 0
restriction = 0
active_game = ''
# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number
    global restriction
    global active_game
    active_game = 1
    secret_number = random.randrange(0, 101)
    restriction = 7
    print " "
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is ", restriction

def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_number
    global restriction
    global active_game
    active_game = 0
    secret_number = random.randrange(0, 1001)
    restriction = 10
    print " "
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is ", restriction

def get_input(guess):
    # main game logic goes here	
    global secret_number
    global restriction
    global active_game
    guess = int(guess)
    restriction -= 1
    print " "
    print "Guess was ", guess
    print "Number of remaining guesses is ", restriction
    if secret_number > guess:
        print "Higher!"
    elif secret_number < guess:
        print "Lower!"
    else:
        print "Correct!"
        if active_game:
            range100()
        else:
            range1000()
    if restriction <= 0:
        print "You have lost."
        if active_game:
            range100()
        else:
            range1000()
    
        
# create frame
f = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

# init game
range100()

# start frame
f.start()