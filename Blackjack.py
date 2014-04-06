# Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
flag=0
flag2=1
flag3=0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.list1=[]

    def __str__(self):
        # return a string representation of a hand
        y=""
        for x in self.list1:
            y=y+x.suit+x.rank
        return y
        
    def add_card(self, card):
        self.list1.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        tot=0
        for x in self.list1:
            if x.rank=='A':
                if tot+11<=21:
                    tot+=11
                else:
                    tot+=1
            else:
                tot+=VALUES[x.rank]  
        return tot
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        self.pos=pos
        for x in self.list1:
            x.draw(canvas, self.pos)
            self.pos[0]+=100
        
        
# define deck class 
class Deck:
    def __init__(self):
        self.d=[]
        for x in SUITS:
            for y in RANKS:
                self.d.append([x,y])

    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.d)

    def deal_card(self):
        global test_hand1, test_hand2, flag
        x=Card(self.d[0][0],self.d[0][1])
        test_hand1.add_card(x)
        x=Card(self.d[1][0],self.d[1][1])
        test_hand1.add_card(x)
        x=Card(self.d[2][0],self.d[2][1])
        test_hand2.add_card(x)
        x=Card(self.d[3][0],self.d[3][1])
        test_hand2.add_card(x)
        print test_hand1
        print test_hand2
        flag=1
        # deal a card object from the deck
    
    def __str__(self):
        # return a string representing the deck
        return str(self.d)


#define event handlers for buttons
def deal():
    global outcome, in_play,flag,flag2,flag3,test_deck, test_hand1, test_hand2
    
    # your code goes here
    in_play = True
    flag=0
    flag2=1
    flag3=0
    test_hand1.list1=[]
    test_hand2.list1=[]
    test_deck=Deck()
    test_deck.shuffle()
    test_deck.deal_card()
    
    
def hit():
    global flag, test_hand1, flag3, msg,score
    # if the hand is in play, hit the player
    if test_hand1.get_value() <= 21:
        x=Card(SUITS[random.randrange(0,4)],RANKS[random.randrange(0,13)])
        test_hand1.add_card(x)

    if test_hand1.get_value()>21:  # if busted, assign a message to outcome, update in_play and score
        msg="You are busted"
        flag3=1
        score-=1
        
        
def stand():
    global test_hand1, test_hand2,score, msg, flag3, flag2	# replace with your code below
   
    flag2=0
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while test_hand2.get_value()<17:
        x=Card(SUITS[random.randrange(0,4)],RANKS[random.randrange(0,13)])
        test_hand2.add_card(x)
        
    # assign a message to outcome, update in_play and score
    if test_hand2.get_value()>=test_hand1.get_value() and test_hand2.get_value()<=21:
        flag3=1
        msg="You Lose"
        score-=1
    elif test_hand2.get_value()>21:
        flag3=1
        msg="You Win"
        score+=1
    elif test_hand1.get_value()>test_hand2.get_value():
        flag3=1
        msg="You Win"
        score+=1
        
# draw handler    
def draw(canvas):
    global flag
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BLACKJACK",[200, 60],40,"White","monospace")
    if flag==1:
        test_hand1.draw(canvas, [100, 400])
        test_hand2.draw(canvas, [100, 200])
        canvas.draw_text("Dealer",[100, 150],25,"Black")
        canvas.draw_text("Player",[100, 350],25,"Black")
        canvas.draw_text("Score : "+str(score),[400, 150],25,"Black")
        if flag2==1:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        canvas.draw_text("BLACKJACK",[200, 60],40,"White","monospace")    
        if flag3==1:
            canvas.draw_text(msg,[250, 350],35,"Black")  
        else:
            canvas.draw_text("Hit or Stand?",[250, 350],25,"Black") 
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

test_hand1=Hand()
test_hand2=Hand()
