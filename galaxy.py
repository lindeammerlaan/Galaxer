from math import sqrt

#konstanter:
G = 6.6743 * 10^(-11) m^3 kg^(-1) s^(-2)
Msol = 5.972 * 10^24 kg
r = 5,20340176 * 10^23
dt = 60 * 60 * 24 #tid under en dag, ändra detta för att ändra tidspann

def setup():
    size(700,700) #sätt storleken av fönstret

    sun = (0,0,0,0) # bestäm position av sol
    planet = () #bestäm postiton av planet 
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
    
def acceleration: 
    x =
    y = 