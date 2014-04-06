# Pong - Multiplayer game
# One player can use the up and down arrow keys and the other player can use keys W and S for controlling the respective pads

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
pos=[300,200]
ball_pos=pos
x=0
# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel, x# these are vectors stored as lists
    ball_pos=[300,200]
    if right==True:
        ball_vel=[random.randrange(3,8), -random.randrange(3,8)]
    else:
        ball_vel=[-random.randrange(3,8), -random.randrange(3,8)]

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1=score2=0
    paddle1_pos=[0,190]
    paddle2_pos=[592,190]
    paddle1_vel=0
    paddle2_vel=0
    x=random.randrange(0,2)
    if x==0:
        flag=True
    else:
        flag=False
    ball_init(flag)

def draw(c):
    global score1, score2, x, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1]+paddle1_vel>=0 and paddle1_pos[1]+paddle1_vel<=320:
        paddle1_pos[1]+=paddle1_vel
    if paddle2_pos[1]+paddle2_vel>=0 and paddle2_pos[1]+paddle2_vel<=320:
        paddle2_pos[1]+=paddle2_vel
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_polygon([[paddle1_pos[0], paddle1_pos[1]], [paddle1_pos[0]+PAD_WIDTH, paddle1_pos[1]], [paddle1_pos[0]+PAD_WIDTH, paddle1_pos[1]+PAD_HEIGHT], [paddle1_pos[0], paddle1_pos[1]+PAD_HEIGHT]], 1, "White", "White")
    c.draw_polygon([[paddle2_pos[0], paddle2_pos[1]], [paddle2_pos[0]+PAD_WIDTH, paddle2_pos[1]], [paddle2_pos[0]+PAD_WIDTH, paddle2_pos[1]+PAD_HEIGHT], [paddle2_pos[0], paddle2_pos[1]+PAD_HEIGHT]], 1, "White", "White")
    
    
    # update ball
    if ball_pos[1]-BALL_RADIUS<=0:
        ball_vel[1]=4
    elif HEIGHT-(ball_pos[1]+BALL_RADIUS-1)<=0:
        ball_vel[1]=-4
    
    if ball_pos[0]-BALL_RADIUS<=8 and paddle1_pos[1]<=ball_pos[1] and paddle1_pos[1]+80>=ball_pos[1]:
        ball_vel[0]*=-1.4
    
    elif WIDTH-(ball_pos[0]+BALL_RADIUS-1)<=8 and paddle2_pos[1]<=ball_pos[1] and paddle2_pos[1]+80>=ball_pos[1]:
        ball_vel[0]*=-1.4
    
    elif ball_pos[0]-BALL_RADIUS<=8:
        score2+=1
        if score2==10:
            x=1
        else:    
            flag=False
            ball_init(flag)
        
    elif WIDTH-(ball_pos[0]+BALL_RADIUS-1)<=8:
        score1+=1
        if score1==10:
            x=2
        else:
            flag=True
            ball_init(flag)
    
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    # draw ball and scores
    c.draw_circle(pos, 60, 5, "Gray") 
    c.draw_circle(ball_pos, 20, 10, "White","White")     
    c.draw_text(str(score1)+ " : ",[520, 30],25,"Yellow")
    c.draw_text(str(score2),[550, 30],25,"Yellow")
    if x==1:
        c.draw_text("B Wins!",[240,200],35,"Yellow")
        ball_pos=[300,200]
        v=[0,0]
    if x==2:
        c.draw_text("A Wins!",[240,200],35,"Yellow")
        ball_pos=[300,200]
        v=[0,0]
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=-6
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel=6
        
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=-6
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel=6
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel=0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel=0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel=0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
frame.start()
new_game()