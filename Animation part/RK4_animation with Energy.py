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
def f(r,t):
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
    
#use RK4 solver and test energy conservation


a=0.0
t=0
b = 500
N = 100000
h = (b-a)/N
xpoints = []
ypoints = []
vxpoints = []
vypoints = []
Epoints = []  

r = array([0.2,0.7, 0.0, 0.0],float)
def Calculation(r):
    if  t < b: 
        xpoints.append(r[0])
        ypoints.append(r[1])
        vxpoints.append(r[2])
        vypoints.append(r[3])
        Epoints.append(E(r))
        ET=E(r)
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1, t+0.5*h)
        k3 = h*f(r+0.5*k2, t+0.5*h)
        k4 = h*f(r+k3, t+h)
        r += (k1+2*k2+2*k3+k4)/6
        return r[0],r[1],ET


fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))

ax.grid()
ax.plot([-miu,1-miu],[0,0],'ro')


ax.plot([-1.0049999999999999,0.83499999999999996,1.1550000000000002,0.83499999999999996,0.83499999999999996],[0,0,0,-0.56499999999999995,0.56499999999999995],'go')

red_patch = mpatches.Patch(color='red', label='earth and moon')
blue_patch = mpatches.Patch(color='blue', label='spaceship')
green_patch = mpatches.Patch(color='green', label='Lagrange point')
ax.legend(handles=[red_patch,blue_patch,green_patch])

line, = ax.plot([], [], 'o-', lw=0.5)
earth_text=ax.text(0,-0.1,'E')
moon_text=ax.text(1,-0.1,'M')
L1_text=ax.text(0.83499999999999996-0.05,0.07,'L1')
L2_text=ax.text(1.1550000000000002+0.05,0.07,'L2')
L3_text=ax.text(-1.0049999999999999+0.05,0.1,'L3')
L4_text=ax.text(0.83499999999999996,0.56499999999999995+0.05,'L4')
L5_text=ax.text(0.83499999999999996,-0.56499999999999995-0.15,'L5')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
energy_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)

def init():
    """initialize animation"""
    line.set_data([],[])
    time_text.set_text('')
    energy_text.set_text('')
    return line, time_text, energy_text


def animate(i):
    """perform animation step"""
    x,y,ET=Calculation(r);
    global t
    t+=h
    line.set_data(x,y)
    time_text.set_text('time = %.1f' % t)
    energy_text.set_text('energy = %.8f J' % ET)
    return line, time_text, energy_text


ani = animation.FuncAnimation(fig, animate, frames=300, interval=1, blit=True, init_func=init)




plt.show()


