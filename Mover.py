class Mover(object):
    def __init__(self, x, y, mass):     
        self.pos = PVector(x, y)
        self.vel = PVector.random2D()
        self.vel.mult(5)
        self.acc = PVector(0, 0)   
        self.mass = mass
        self.r = sqrt(self.mass) * 2
        
        
    def show(self):
        fill(0, 0, 100, 20)
        circle(self.pos.x, self.pos.y, self.r*2)
        
        
    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(10)
        self.pos.add(self.vel)
        self.acc.set(0, 0)
        
        
    def apply_force(self, force):  # remember, force is a PVector
        # F=ma, so a=F/m
        # self.acc.add(force.div(self.mass))
        self.acc.add(PVector.div(force, self.mass))
