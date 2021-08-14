# -*- coding: utf-8 -*- // this is required for unicode characters
from Mover import *

class Attractor(Mover):
    def __init__(self, x, y, m):
        super(Attractor, self).__init__(x, y, m)
        
    
    def attract(self, mover):        
        force = PVector.sub(self.pos, mover.pos)  # this is the direction vector as well
        d = force.mag()
        d = constrain(d, 10, 33)
        # something is wrong here : ; it was 1/r² falloff and 1/r² division by zero           
        G = 1  # let the gravitational constant just be one right now
        strength = (G * self.mass * mover.mass) / (d ** 2)
        
        # now that we have the direction and the desired magnitude of the force...
        force.setMag(strength)
        # mover.apply_force(force)
        mover.apply_force(force)
