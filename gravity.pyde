# 2021.08.03 Kiwi
#
# Daniel Shiffman's Nature of Code 2.5
# exploring mutual gravitational attraction using the Mover class
# 
# v0.01 basic attractor and many movers
# v0.02 mutual gravitation

from Mover import *
from Attractor import *
        
        
def setup():
    global movers, attractor
    
    size(1200, 700)
    colorMode(HSB, 360, 100, 100, 100)
    # background(209, 95, 33)
    background(0)
    frameRate(144)
    
    stroke(0, 0, 100)
    strokeWeight(2)
 
    movers = []
    
    for i in range(20):
        movers.append(Mover(random(width), random(height), random(10, 70)))
    attractor = Attractor(width/2, height/2, 100)
    
    smooth()

def draw():
    global movers, attractor
    background(209, 95, 33, 5)
        
    # fade everything that is drawn
    # fill(0, 3)
    # fill(209, 95, 33, 1);
    # rect(0, 0, width, height);
    
    for mover in movers:
        attractor.attract(mover)    
        mover.update()
        mover.show()
        
    attractor.show()
    
