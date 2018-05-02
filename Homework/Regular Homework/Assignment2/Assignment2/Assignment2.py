#Python program to create a face graphic
#Created by Dana Lockwood (10/12/17)

#import the graphics library
from graphics import *

def main():
    win=GraphWin("Drawings", width=650, height=500) #Set window dimensions
    center = Point(220,220)
    face = Circle(center, 50) #define the dimensions of the face
    lefteye = Point(240,210)
    righteye = Point(210,210)
    face.draw(win) #draw the face
    lefteye.draw(win) #draw left eye
    righteye.draw(win) #draw right eye
    
    #the mouth
    mp1 = Point(200,240)#mouth point 1
    mp2 = mp1.draw(win) #draw mouth point 1
    mp3 = Point(240,240)#mouth point 2
    mp4 = mp3.draw(win) #draw mouth point 2
    line = Line(mp1,mp3)
    line.draw(win) #draw the mouth

main()
    
