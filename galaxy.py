from math import sqrt

#konstanter
G = 6.67408E-11
dt = 60*60*24 # Tid = 1 dag
sun = {}
earth = {}
moon = {}
mercury = {}
venus = {}
mars = {}
jupiter = {}
saturn = {}
uranus = {}
neptune = {}


himlakroppar = [earth, venus, mercury, mars, jupiter,moon, saturn, uranus, neptune]

def setup():
    global sun, earth, moon, venus, mercury, mars, jupiter, saturn, uranus, neptune
    size(600,600) # Sets the size of the window
    
    sun  = {}
    sun["m"] = 1.989E30
    sun["x"] = 0
    sun["y"] = 0
    sun["vx"] = 0
    sun["vy"] = 0

    earth["m"] = 7.989E24 #5.972E24
    earth["x"] = 2E11
    earth["y"] = 0
    earth["vx"] = 0 
    earth["vy"] = 2.5E4
    earth["ax"] = 0 
    earth["ay"] = 0 
    
    moon['m'] = 7E20
    moon['x'] = 2.2E11
    moon['y'] = 0
    moon['vx'] = 0 
    moon['vy'] = 3.3E4
    moon['ax'] = 0 
    moon['ay'] = 0 
    
    mercury['m'] = 3.285E23
    mercury['x'] = 66.02E9
    mercury['y'] = 0
    mercury['vx'] = 0
    mercury['vy'] = 5E4
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
    
    jupiter['m'] = 1.899E27
    jupiter['x'] = 4E11
    jupiter['y'] = 0
    jupiter['vx'] = 0 
    jupiter['vy'] = 1.3E4
    jupiter['ax'] = 0 
    jupiter['ay'] = 0 
    
    saturn['m'] = 5.6E26
    saturn['x'] = 5E11
    saturn['y'] = 0
    saturn['vx'] = 0 
    saturn['vy'] = 9.6E3
    saturn['ax'] = 0 
    saturn['ay'] = 0 
    
    uranus['m'] = 8.7E25
    uranus['x'] = 7E11
    uranus['y'] = 0
    uranus['vx'] = 0 
    uranus['vy'] = 6.8E3
    uranus['ax'] = 0 
    uranus['ay'] = 0 
    
    neptune['m'] = 1E26
    neptune['x'] = 9E11
    neptune['y'] = 0
    neptune['vx'] = 0 
    neptune['vy'] = 5.4E3
    neptune['ax'] = 0 
    neptune['ay'] = 0 

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
    elif typ == 'jupiter':
        fill(255,127,36)
        ellipse(x_pixel, y_pixel, 20, 20)
    elif typ == 'saturn':
        fill(255,211,155)
        ellipse(x_pixel, y_pixel, 20, 20)
    elif typ == 'neptune':
        fill(0,206,209)
        ellipse(x_pixel, y_pixel, 17, 17)
    elif typ == 'uranus':
        fill(191,62,255)
        ellipse(x_pixel, y_pixel, 15, 15)
    
    
def update_positions():
    global sun, earth, mercury, venus, mars
    
    for himlakropp in himlakroppar:
        # 
        dx = sun["x"] - himlakropp["x"]
        dy = sun["y"] - himlakropp["y"]
        l = (dx**2 + dy**2)**0.5
    
    # krafter
        Fg = G*sun["m"]*himlakropp["m"]/l**2
    # kraftkomposanterna
        Fgx = Fg * dx/l
        Fgy = Fg * dy/l

        himlakropp["ax"] += Fgx/himlakropp["m"]
        himlakropp["ay"] += Fgy/himlakropp["m"]
        # beräkning hastighet och acceleration utifrån krafter
        himlakropp["vx"] += himlakropp["ax"]*dt
        himlakropp["vy"] += himlakropp["ay"]*dt
        himlakropp["x"] += himlakropp["vx"]*dt
        himlakropp["y"] += himlakropp["vy"]*dt
        # reset acc efter uppdatering
        himlakropp["ax"] = 0
        himlakropp["ay"] = 0
    
def update_position_moon():
    
    dx = earth["x"] - moon["x"]
    dy = earth["y"] - moon["y"]
    l = (dx**2 + dy**2)**0.5
    
    # gravitational force 
    Fg = G*earth["m"]*moon["m"]/l**2
    # gravitational force komposants
    Fgx = Fg * dx/l
    Fgy = Fg * dy/l
    
    moon["ax"] += Fgx/moon["m"]
    moon["ay"] += Fgy/moon["m"]
        # Updating the position
    moon["vx"] += moon["ax"]*dt
    moon["vy"] += moon["ay"]*dt
    moon["x"] += moon["vx"]*dt
    moon["y"] += moon["vy"]*dt
        # reset acc after update
    moon["ax"] = 0
    moon["ay"] = 0

    

def draw():
    global sun, earth, mercury, moon, venus, mars
    background(3);  # svart bakgrund
    
    update_positions()
    update_position_moon()
    
    show(sun, 'sun')
    show(earth, 'earth')
    show(moon, 'moon')
    show(mercury, 'mercury')
    show(venus, 'venus')
    show(mars, 'mars')
    show(jupiter, 'jupiter')
    show(saturn, 'saturn')
    show(uranus, 'uranus')
    show(neptune, 'neptune')
      
