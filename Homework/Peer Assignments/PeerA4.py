#Peer assignment by Dana & Beverely (10/5)

#import graphics
from graphics import *

def main():
    win=GraphWin("Drawings", width=650, height=500)
    center = Point (80,80)
    center = Point (50,150)
    center2 = Point (100,150)
    circ1 = Circle (center, 30)
    circ2 = Circle (center2, 50)
    circ1.draw(win) #draw circle 1
    circ2.draw(win) #draw circle 2

main()
