# Card game - Memory

import simplegui
import random

list=range(0,8)+range(0,8)
count=0

# helper function to initialize globals
def init():
    global list, exposed, count, state
    random.shuffle(list)
    exposed=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    state=0
    count=0
    label.set_text("Moves:"+str(count))
    pass  

     
# define event handlers
def mouseclick(pos):
    global state, p, q, count	
    # add game state logic here
    x=pos[0]/50
    y=int(x)
    if state==0:
        if exposed[y]==0:
            exposed[y]=1
            state=1
            p=y
    elif state==1:
        if exposed[y]==0:
            exposed[y]=1
            state=2
            q=y
    else:
        if list[p]==list[q] and exposed[y]==0:  
            exposed[y]=1 
            p=y    
            state=1
        else:
            if exposed[y]==0:
                exposed[y]=1
                count+=1
                label.set_text("Moves:"+str(count))
                exposed[p]=0
                exposed[q]=0
                p=y
                state=1
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global list, exposed
    
    
    for i in range(0,16):
        if exposed[i]==0:
            j=(i+1)*50-50
            k=(i+1)*50
            canvas.draw_polygon([[j,0],[j+50,0],[j+50,100],[j,100]], 1, "Green", "Green")
            canvas.draw_line((k,0), (k, 100), 2, "Black")
            
        if exposed[i]==1:
            a=15+(i+1)*50-50
            canvas.draw_text(str(list[i]),[a,65],50,"White")
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = "+str(count))
# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
