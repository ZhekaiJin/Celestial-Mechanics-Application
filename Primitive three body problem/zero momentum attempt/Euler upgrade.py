#author:scott
GlowScript 2.1 VPython
# this program is runnable in trinket glowscript which is based on vpython 
G=6.67e-11   #gravitational constant

#setting up the drag and click function
drag=False
R=vector(0,0,0)
scene.bind("mousedown", def():
           global drag
           drag=True
           
           scene.bind("mouseup", def():
                      global drag
                      drag=False
                      )
           )

#transformation and scaling factor
cs=5 #for sun
ce=20 #for earth

#setting up the sun coefficient
sun=sphere(pos=vec(-1e11,0,0), radius=cs*6.96e8, color=color.yellow)
sun.m=2e30
sun.p=vec(0,0,0)

#setting up the earth coefficient
earth=sphere(pos=sun.pos+vec(1.5e11,0,0), radius=ce*7e7, color=color.cyan,make_trail=True)
earth.m=6.4e24
#the initial velocity of the Earth
earth.v=vec(0,30e3,0)
earth.p=earth.m*earth.v

#spaceship which is added into the frame
ship=sphere(pos=earth.pos, radius=earth.radius/2, color=color.white,make_trail=True)
ship.v=earth.v
ship.m=100
ship.p=ship.m*ship.v

# seting the scale and the arrow
ascale=10*earth.radius
arr=arrow(pos=ship.pos, axis=vector(0,ascale,0), color=color.yellow)  # arrow define the intial condition of the speed
vscale=mag(earth.v)

vesc=sqrt(2*G*sun.m/mag(sun.pos-ship.pos))  # escape velocity for alert

t=0
dt=200
start=false
escape=false
vship=vector(0,0,0)

while t<dt*2e5:
    rate(10000)
    #checks to see if the mouse is dragging
    if drag:
        #R is just a temp value at the location of the mouse
        R=scene.mouse.pos
        #set the axis of the temp arrow
        arr.axis=R-ship.pos
        #use the axis of temp arrow to set velocity
        ship.v=arr.axis*vscale/ascale+earth.v
        ship.p=ship.v*ship.m
        start=true
        vship=ship.v
    #start and use the calculation step defined in the general three body problem
    if start and !drag:
        arr.visible=false   #cancel the arrow
        
        r=earth.pos-sun.pos  # distance from sun to earth
        r2=ship.pos-sun.pos
        Fp=-G*earth.m*sun.m*norm(r)/mag2(r)  #calculation of gravitaional force
        Fs=-G*ship.m*sun.m*norm(r2)/mag2(r2)
        
        earth.p=earth.p+Fp*dt  #update momentum
        ship.p=ship.p+Fs*dt
        
        earth.pos=earth.pos+earth.p*dt/earth.m  #update position
        ship.pos=ship.pos+ship.p*dt/ship.m
        
        t=t+dt    #update time
E=mag(earth.p)**2/(2*earth.m) - G*earth.m*sun.m/mag(r)  #check if energy is still constant
#print(E)
if mag(vship)>vesc:    #alert as out of range
    print("You are leaving the solar system.")
