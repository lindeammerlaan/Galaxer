from math import sqrt

#konstanter
G = 6.67408E-11
dt = 60*60*24 # Time step one day
sun = {}
earth = {}
moon = {}
mercury = {}
venus = {}
mars = {}

himlakroppar = [earth, venus, mercury, mars, moon]

def setup():
    global sun, earth, moon, venus, mercury, mars
    size(600,600) # Sets the size of the window
    
    sun  = {}
    sun["m"] = 1.989E30
    sun["x"] = 0
    sun["y"] = 0
    sun["vx"] = 0
    sun["vy"] = 0

    earth["m"] = 5.972E24
    earth["x"] = 2E11
    earth["y"] = 0
    earth["vx"] = 0 
    earth["vy"] = 2.5E4
    earth["ax"] = 0 
    earth["ay"] = 0 
    
    moon['m'] = 0.07346E24
    moon['x'] = 3.4902E11
    moon['y'] = 0
    moon['vx'] = 0 
    moon['vy'] = 2.3E4
    moon['ax'] = 0 
    moon['ay'] = 0 
    
    mercury['m'] = 3.285E23
    mercury['x'] = 66.02E9
    mercury['y'] = 0
    mercury['vx'] = 0 
    mercury['vy'] = 4.7E4
    mercury['ax'] = 0 
    mercury['ay'] = 0 
    
    venus['m'] = 4.867E24
    venus['x'] = 1.0894E11
    venus['y'] = 0
    venus['vx'] = 0 
    venus['vy'] = 3.5E4
    venus['ax'] = 0 
    venus['ay'] = 0 
    
    mars['m'] = 6.39E23
    mars['x'] = 2.5E11
    mars['y'] = 0
    mars['vx'] = 0 
    mars['vy'] = 2.4130E4
    mars['ax'] = 0 
    mars['ay'] = 0 

def show(himlakropp, typ):
    # Scale system to show 5 earth orbits on screen
    a = 1.496E11
    x_pixel = himlakropp["x"]*300/5.0/1.496E11 + 300 #(self.x/a+0.5)*300
    y_pixel = himlakropp["y"]*300/5.0/1.496E11 + 300 #(self.y/a+0.5)*300
    
    if typ == 'sun':
        fill(255, 212, 59)
        ellipse(x_pixel, y_pixel, 40, 40)
    elif typ == 'earth':
        fill(62, 176, 73)
        ellipse(x_pixel, y_pixel, 20, 20)
    elif typ == 'moon':
        fill(128, 139, 150)
        ellipse(x_pixel, y_pixel, 10, 10)
    elif typ == 'mercury':
        fill(116, 142, 196)
        ellipse(x_pixel, y_pixel, 10, 10)
    elif typ == 'venus':
        fill(248, 156, 14)
        ellipse(x_pixel, y_pixel, 15, 15)
    elif typ == 'mars':
        fill(139,35,35)
        ellipse(x_pixel, y_pixel, 12, 12)
    
    
def update_positions():
    global sun, earth, mercury, venus, mars
    
    for himlakropp in himlakroppar:
        # calculate the gravitational force from distance between planet and sun
        dx = sun["x"] - himlakropp["x"]
        dy = sun["y"] - himlakropp["y"]
        l = (dx**2 + dy**2)**0.5
    
    # gravitational force 
        Fg = G*sun["m"]*himlakropp["m"]/l**2
    # gravitational force komposants
        Fgx = Fg * dx/l
        Fgy = Fg * dy/l

        himlakropp["ax"] += Fgx/himlakropp["m"]
        himlakropp["ay"] += Fgy/himlakropp["m"]
        # Updating the position
        himlakropp["vx"] += himlakropp["ax"]*dt
        himlakropp["vy"] += himlakropp["ay"]*dt
        himlakropp["x"] += himlakropp["vx"]*dt
        himlakropp["y"] += himlakropp["vy"]*dt
        # reset acc after update
        himlakropp["ax"] = 0
        himlakropp["ay"] = 0
    
def update_moonposition():
    global earth, moon, sun 

    dxe = earth['x'] - moon['x']
    dye = earth['y'] - moon['y']
    le = (dxe**2 + dye**2)**0.5
    
    Fge = G*earth['m']*moon['m']/le**2
        # gravitational force komposants
    Fgxe = Fge * dxe/le
    Fgye = Fge * dye/le
    
    dxs = sun['x'] - moon['x']
    dys = sun['y'] - moon['y']
    ls = (dxs**2 + dys**2)**0.5

    Fgs = G*earth['m']*moon['m']/ls**2
    # gravitational force komposants
    Fgxs = Fgs * dxs/ls
    Fgys = Fgs * dys/ls
    
    moon['ax'] += (Fgxe + Fgxs)/moon['m']
    moon['ay'] += (Fgye + Fgys)/moon['m']
    # Updatera positionen
    moon['vx'] += moon['m']*dt
    moon['vy'] += moon['ay']*dt
    moon['x'] += moon['vx']*dt
    moon['y'] += moon['vy']*dt
    # nollställ acceleration efter reset
    moon['ax'] = 0
    moon['ay'] = 0
    

def draw():
    global sun, earth, mercury, moon, venus, mars
    background(3);  # svart bakgrund
    
    update_positions()
    update_moonposition()
    
    show(sun, 'sun')
    show(earth, 'earth')
    show(moon, 'moon')
    show(mercury, 'mercury')
    show(venus, 'venus')
    show(mars, 'mars')
    