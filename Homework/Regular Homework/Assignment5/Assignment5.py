#Program to create a smily face, and another face
#By Dana Lockwood (11/2/17)

#import from graphics library
from graphics import *


#Function to create smilley face
def smilely():
    win=GraphWin("Drawings", width=650, height=500)
    #size=width=650, height=500
    center = Point(120,120)
    face = Circle(center, 50) #define the dimensions of the face
    lefteye = Point(140,110)
    righteye = Point(110,110)
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
    drawface(center, win)

#Function to create non-smilley face
def drawface(center, win):
    #win=GraphWin("Drawings", width=650, height=500) #Set window dimensions
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

def main():
    smilely()

main()




    

