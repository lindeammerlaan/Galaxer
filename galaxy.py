from math import sqrt

#konstanter:
G = 6.6743E-11
sun = {}
jord = {}
moon = {}
dt = 60 * 60 * 24 #anger tidspann, en dag 

def setup():
    global sun, jord, moon
    size(600,600) #sätt storleken av fönstret

    sun = {}
    sun['m'] = 1.989E30
    sun['x'] = 0
    sun['y'] = 0
    sun['vx'] = 0
    sun['vy'] = 0

    jord['m'] = 5.972E24
    jord['x'] = 2.5102E11
    jord['y'] = 0
    jord['vx'] = 0 
    jord['vy'] = 2.5E4
    jord['ax'] = 0 
    jord['ay'] = 0 

    moon['m'] = 0.07346E24
    moon['x'] = 2.5102E11 + 300000*1000 #1.50635E11
    moon['y'] = 0
    moon['vx'] = 0 
    moon['vy'] = 2.5E4
    moon['ax'] = 0 
    moon['ay'] = 0 

def show(himlakropp, typ):
    a = 1.496E11
    x_pixel = himlakropp['x']*300/5.0/1.496E11 + 300 #(self.x/a+0.5)*300
    y_pixel = himlakropp['y']*300/5.0/1.496E11 + 300 #(self.y/a+0.5)*300

    if typ == 'sol':
        fill(252, 243, 207)
        ellipse(x_pixel, y_pixel, 40, 40)
    elif typ == 'jord':
        fill(29, 131, 72)
        ellipse(x_pixel, y_pixel, 20, 20)
    elif typ == 'moon':
        fill(128, 139, 150)
        ellipse(x_pixel, y_pixel, 10, 10)

def location():
    global sun, jord, moon
    #här sker beräkningen av gravitationella kraften beroende på distansen mellan sol och himlakropp

    dxe = sun['x'] - jord['x']
    dye = sun['y'] - jord['y']
    le = (dxe**2 + dye**2)**0.5

    Fge = G*sun['m']*jord['m']/le**2
    # gravitational force komposants
    Fgxe = Fge * dxe/le
    Fgye = Fge * dye/le

    #här sker beräkningen av gravitationella kraften beroende på distansen mellan jord och måne
    dxm = jord['x'] - moon['x']
    dym = jord['y'] - moon['y']
    lm = (dxm**2 + dym**2)**0.5

    Fgm = G*jord['m']*moon['m']/lm**2
    # gravitational force komposants
    Fgxm = Fgm * dxm/lm
    Fgym = Fgm * dym/lm
    
    #Här sker beräkningen av gravitationella kraften beroende på distansen till solen
    dxs = sun['x'] - moon['x']
    dys = sun['y'] - moon['y']
    ls = (dxs**2 + dys**2)**0.5

    Fgs = G*sun['m']*moon['m']/ls**2
    # gravitational force komposants
    Fgxs = Fgs * dxs/ls
    Fgys = Fgs * dys/ls


    jord['ax'] += Fgxe/jord['m']
    jord['ay'] += Fgye/jord['m']
    # Updatera positionen
    jord['vx'] += jord['ax']*dt
    jord['vy'] += jord['ay']*dt
    jord['x'] += jord['vx']*dt
    jord['y'] += jord['vy']*dt
    # nollställ acceleration efter reset
    jord['ax'] = 0
    jord['ay'] = 0

    moon['ax'] += (Fgxm + Fgxs)/moon['m']
    moon['ay'] += (Fgym + Fgys)/moon['m']
    # Updatera positionen
    moon['vx'] += moon['ax']*dt
    moon['vy'] += moon['ay']*dt
    moon['x'] += moon['vx']*dt
    moon['y'] += moon['vy']*dt
    # nollställ acceleration efter reset
    moon['ax'] = 0
    moon['ay'] = 0
    
def draw():
    global sol, jord, moon
    background(31, 97,141); #mörkblå bakgrundsfärg 

    location()

    show(sun, 'sol')
    show(jord, 'jord')
    show(moon, 'moon')




#beräkna gravitationskraften från avståndet mellan planet och sol
# # #dx = solx - jordx
    #dy = soly - jordy
    #l =  5,20340176 * 10^23

    #gravitationskrafterna: 
    #Fg = G * Msol * Mjord / (l**2)
        # gravitational force komposants
       # Fgx = Fg * dx/l
       # Fgy = Fg * dy/l


 # F = G((Mm)/(r^2))
    # krafterna:
        # Fx = -Fcosa = (-Fx)/r
        # Fy = -Fsina = (-Fy)/r
    #Således blir accelerationerna: 
        #ax = -G(Mx)/(r^3)
        #ay = -G(My)/(r^3) 
        
    #massa svart hål = 4.3 miljoner solmassor = 4,3 * 10^6 * (8,5527*10^36) kg
    #Radie svart hål = 1,2 * 10^9 meter 


#vy += (-G) * Msol * x / (r**3) 
#vx += (-G) * Msol * y / (r**3)

#x += vx * dt
#y += vy * dt