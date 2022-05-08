from math import sqrt

#konstanter:
G = 6.6743 * 10^(-11)
Msol = 5.972 * 10^24 
Mjord = 5.972 * 10^24
l = 1.505 * 10^11 #avstånd mellan sol och jord 
dt = 60 * 60 * 24 #tid under en dag, ändra detta för att ändra tidspann

def setup():
    size(700,700) #sätt storleken av fönstret

    sun = (0,0,0,0) # bestäm position av sol
    jorden = (1.496E11,0,0,3.2E4) #bestäm postiton av jord 
    mercury =  (0,0, )

def show(himlakropp):
    if self.body == 'sol':
        fill(252, 243, 207)
    elif self.body == 'earth':
        fill(29, 131, 72)
    elif self.body == 'mercury':
        fill(128, 139, 150)

def rita():
    background(31, 97,141); #mörkblå bakgrundsfärg 

    #beräkna gravitationskraften från avståndet mellan planet och sol
    dx = solx - jordx
    dy = soly - jordy
    l =  5,20340176 * 10^23

    #gravitationskrafterna: 
    Fg = G * Msol * Mjord / (l**2)
        # gravitational force komposants
        Fgx = Fg * dx/l
        Fgy = Fg * dy/l

def applyForce(self, fx, fy):
    self.ax += fx/self.m
    self.ay += fy/self.m 



    earth.applyForce(Fgx, Fgy)
    earth.position(dt) #jordens positions uppdateras 
    earth.show() #visa planeten på skärmen 

sun.show # visa solen 

t = 0

x = 300
y = 300
vx = 0 
vy = 0


 # F = G((Mm)/(r^2))
    # krafterna:
        # Fx = -Fcosa = (-Fx)/r
        # Fy = -Fsina = (-Fy)/r
    #Således blir accelerationerna: 
        #ax = -G(Mx)/(r^3)
        #ay = -G(My)/(r^3) 
        
    #massa svart hål = 4.3 miljoner solmassor = 4,3 * 10^6 * (8,5527*10^36) kg
    #Radie svart hål = 1,2 * 10^9 meter 


vy += (-G) * Msol * x / (r**3) 
vx += (-G) * Msol * y / (r**3)

x += vx * dt
y += vy * dt