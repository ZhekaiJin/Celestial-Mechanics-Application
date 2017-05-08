
# author : scott
from __future__ import division,print_function
from numpy import linspace,meshgrid,sqrt,array,arange,sin, cos
from pylab import plot, show, xlabel, ylabel, scatter
from math import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches



m1= 5.972e24 
m2= 7.347e22
miu=m2/(m1+m2)
Target=0.000001  ## change target accuray !!!!

#define function for effective potential as seen in literature
def effpot(x,y):
    P1=-miu
    P2=1-miu
    r1=sqrt((x-P1)**2+y**2) 
    r2=sqrt((x-P2)**2+y**2)
    V=-(1-miu)/r1-miu/r2 
    return V-(x**2+y**2)/2

#define partials for effpot using central difference theorem
def partialV(x,y):
    h=0.001
    dV_dx=(effpot(x+0.5*h,y)-effpot(x-0.5*h,y))/h
    dV_dy=(effpot(x,y+0.5*h)-effpot(x,y-0.5*h))/h
    return array([dV_dx,dV_dy], float)

#define partial differential equation
def f(r):
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    xprime= vx
    yprime= vy
    vxprime= -partialV(x,y)[0]+2*vy
    vyprime= -partialV(x,y)[1]-2*vx
    return array([xprime,yprime,vxprime,vyprime], float)
    
    
#define forumula for conserved energy
def E(r):
    return 0.5*(r[2]**2+r[3]**2)+effpot(r[0],r[1])
    
def RK4(r,h):   #define Rk4    
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1)
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    return r+(k1+2*k2+2*k3+k4)/6

def Adaptive(r,h):   #define how to fine the pho with return the first approxmiation
    r1=RK4(r,h)
    R1=RK4(r1,h)
    R2=RK4(r,2*h)
    deltax=(R1[0]-R2[0])/30  #x1=R1[0],x2=R2[0],y1=R1[1],y2=R2[1]
    deltay=(R1[1]-R2[1])/30
    pho=h*Target/sqrt(deltax**2+deltay**2)
    return pho,R1
H=10000    
t,b=0,500   #change b here !!!
N = 100000
h = (b-t)/N
x,y=[],[]
tpoints,Epoints = [],[]  
r=array([0.2,0.7, 0.0, 0.0])   #change the inital condition maybe 
while t<b:                          #iterate with t and keep lower the step if pho>1
    pho,R1=Adaptive(r,h)
    if h<H:
        H=h   #find the smallest interval
    if pho>1:
        tpoints.append(t)
        x.append(R1[0])  # the approxmiation using two steps will be used 
        y.append(R1[1])
        Epoints.append(E(r))
        
        t+=2*h
        r=R1
    h=h*pho**(1/4)    

tc=0 
j=0

fig = plt.figure("Energy and trajectory plot")
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-1, 1), ylim=(-1, 1))
ax.grid()
ax.plot([-miu,1-miu],[0,0],'ro')
red_patch = mpatches.Patch(color='red', label='earth and moon')
red1_patch = mpatches.Patch(color='blue', label='spaceship')
ax.legend(handles=[red_patch,red1_patch])

line, = ax.plot([], [], 'o-', lw=2)
earth_text=ax.text(-miu,0.02,'earth')
moon_text=ax.text(0.9-miu,0.02,'moon')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
energy_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)

def init():
    """initialize animation"""
    line.set_data([],[])
    time_text.set_text('')
    energy_text.set_text('')
    return line, time_text, energy_text

interval=H

def animate(i):
    """perform animation step"""
    
    global tc,j
    if tc>tpoints[j]:
        line.set_data(x[j],y[j])
        j+=1
    tc +=interval
    time_text.set_text('time = %.1f' % tc)
    energy_text.set_text('energy = %.8f J' % Epoints[j])
    return line, time_text,energy_text

ani = animation.FuncAnimation(fig, animate, frames=300,
                              interval=H*10**3, blit=True, init_func=init)

plt.show()
