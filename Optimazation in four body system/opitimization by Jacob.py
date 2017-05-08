# -*- coding: utf-8 -*-
"""
Created on Fri May  5 20:41:12 2017

@author: maare
"""

from __future__ import division,print_function  
from numpy import linspace,meshgrid,sqrt, array, arange, sin, cos
from pylab import plot, show, xlabel, ylabel
from math import pi
from numpy.linalg import norm

m_earth= 5.972e24 
m_moon= 7.347e22
m_sun= 1.989e30
d_earth_sun=149.9e9
d_earth_moon=384.4e6
omegam=2.66186e-6
omegas = 1.99102e-7

radius_earth=6.371e6
radius_moon=1.737e6

r_escape= float(input("Enter escape orbit radius in earth radius units: "))
r_escape*= radius_earth/d_earth_moon

r_capture= float(input("Enter capture orbit in moon radius units: "))
r_capture*= radius_moon/d_earth_moon

#M2-M3 normalized rotating frame
def miu_m2_m3(mi): #normalization function
    return mi/(m_earth+m_moon) 

def distance(x0,y0,x1,y1): #distance function
    return sqrt((x1-x0)**2+(y1-y0)**2)

def effpot_m2_m3(theta_sun, x, y):
    x_earth=-miu_m2_m3(m_moon)
    y_earth=0
    x_moon=1-miu_m2_m3(m_moon)
    y_moon= 0
    x_sun=-d_earth_sun/d_earth_moon*cos(theta_sun)
    y_sun=-d_earth_sun/d_earth_moon*sin(theta_sun) 
    r_earth=distance(x_earth,y_earth,x,y)
    r_moon=distance(x_moon,y_moon,x,y)
    r_sun=distance(x_sun,y_sun,x,y)
    U = (x**2+y**2)/2+miu_m2_m3(m_earth)/r_earth+miu_m2_m3(m_moon)/r_moon+miu_m2_m3(m_sun)/r_sun
    return U

def partialV_m2_m3(r,theta_sun):#gradient of effective potential using central difference theorem
    x=r[0]
    y=r[1]
    dV_dx= (effpot_m2_m3(theta_sun, x+0.5*h, y)-effpot_m2_m3(theta_sun, x-0.5*h, y))/h
    dV_dy= (effpot_m2_m3(theta_sun, x, y+0.5*h)-effpot_m2_m3(theta_sun, x, y-0.5*h))/h
    return array([dV_dx,dV_dy], float)
    
def r_3b_m2_m3(theta_sun): #position vector ofr m3
    return array([-d_earth_sun/d_earth_moon*cos(theta_sun), -d_earth_sun/d_earth_moon*sin(theta_sun), float])
    
def I_m2_m3(theta_sun):
    r_x=r_3b_m2_m3(theta_sun)[0]
    r_y=r_3b_m2_m3(theta_sun)[1]
    I_x= -miu_m2_m3(m_sun)*r_x/distance(r_x, r_y, 0, 0)**3
    I_y= -miu_m2_m3(m_sun)*r_y/distance(r_x, r_y, 0, 0)**3
    return array([I_x, I_y], float)    #indirect acceleration due to m3 as seen in literature

def f_m2_m3(r, theta_sun):
    x=r[0]
    y=r[1]    
    vx=r[2]
    vy=r[3]
    xprime=vx
    yprime=vy
    vxprime= partialV_m2_m3(r,(omegas/omegam-1)*t)[0]+I_m2_m3((omegas/omegam-1)*t)[0]+2*yprime
    vyprime= partialV_m2_m3(r,(omegas/omegam-1)*t)[1]+I_m2_m3((omegas/omegam-1)*t)[1]-2*xprime
    return array([xprime,yprime,vxprime,vyprime], float)

def RK4_m2_m3(r,t): #returns change in r as calculated by RK4
    k1 = h*f_m2_m3(r,(omegas/omegam-1)*t)
    k2 = h*f_m2_m3(r+0.5*k1,(omegas/omegam-1)*(t+0.5*h))
    k3 = h*f_m2_m3(r+0.5*k2,(omegas/omegam-1)*(t+0.5*h))
    k4 = h*f_m2_m3(r+k3,(omegas/omegam-1)*(t+h))
    r += (k1+2*k2+2*k3+k4)/6
    return r

def E_m2_m3(r, theta_sun):
    x=r[0]
    y=r[1]
    return 0.5*(r[2]**2+r[3]**2)-effpot_m2_m3(theta_sun, x, y)

def orbit_v(m, r): # Calculate orbit velocity at a certain radius about primary
    mass_primary = miu_m2_m3(m)
    return sqrt(mass_primary/r)



L1 = [0.835, 0]
L4 = [0.8349, 0.5650, 0, 0]
h=0.01
tau=[]
delta_Vs = []
Emin = E_m2_m3(L4, 0)


for deg in range (270, 360):   
    rad= float(deg*pi/180)
    delta_V=0.0
    t=0.0
    x_moon = 1-miu_m2_m3(m_moon)
    r = array([x_moon+r_capture*cos(rad), r_capture*sin(rad), (orbit_v(m_moon, r_capture)+delta_V)*sin(rad), -(orbit_v(m_moon, r_capture)+delta_V)*cos(rad)], float)
    mindV=sqrt(2*(Emin-E_m2_m3(r, 0))+orbit_v(m_earth, r_capture)**2)-orbit_v(m_earth, r_capture)
    delta_V=mindV
    #print(mindV)
    while r[0]>L1[0]:
        r = array([x_moon+r_capture*cos(rad), r_capture*sin(rad), (orbit_v(m_moon, r_capture)+delta_V)*sin(rad), -(orbit_v(m_moon, r_capture)+delta_V)*cos(rad)], float)
        while r[2]<=0:
            r = RK4_m2_m3(r,t)
            if r[0]<=L1[0]:
                tau.append(deg)
                delta_Vs.append(delta_V)
                print(deg)
                break
            t -= h
        delta_V+=0.01
        
#print (tau, delta_Vs)

min_index= delta_Vs.index(min(delta_Vs))

deg_min3, delta_V_min3 = tau[min_index], delta_Vs[min_index]
rad_min3 = float(deg_min3*pi/180)

xpoints = []
ypoints = []
vxpoints = []
vypoints = []
Epoints = []
tpoints = []  

r = array([x_moon+r_capture*cos(rad_min3), r_capture*sin(rad_min3), (orbit_v(m_moon, r_capture)+delta_V_min3)*sin(rad_min3), -(orbit_v(m_moon, r_capture)+delta_V_min3)*cos(rad_min3)], float)
t=0.0
#print(RK4(r,0))
while r[0]>L1[0]:
    xpoints.append(r[0])
    ypoints.append(r[1])
    vxpoints.append(r[2])
    vypoints.append(r[3])
    #Epoints.append(E(r, (omegas/omegam-1)*t))    
    r = RK4_m2_m3(r,t)
    t-=h
    
plot(xpoints, ypoints)
show()
    








#M1-M2 normalized rotating frame
def miu_m1_m2(mi): #normalization function
    return mi/(m_earth+m_sun) 

def effpot_m1_m2(theta_moon, x, y):
    x_sun=-miu_m1_m2(m_earth)
    y_sun=0
    x_earth=1-miu_m1_m2(m_earth)
    y_earth= 0
    x_moon=x_earth+d_earth_moon/d_earth_sun*cos(theta_moon)
    y_moon=d_earth_moon/d_earth_sun*sin(theta_moon) 
    r_earth=distance(x_earth,y_earth,x,y)
    r_moon=distance(x_moon,y_moon,x,y)
    r_sun=distance(x_sun,y_sun,x,y)
    U = (x**2+y**2)/2+miu_m1_m2(m_earth)/r_earth+miu_m1_m2(m_moon)/r_moon+miu_m1_m2(m_sun)/r_sun
    return U

def partialV_m1_m2(r,theta_moon):#gradient of effective potential using central difference theorem
    x=r[0]
    y=r[1]
    dV_dx= (effpot_m1_m2(theta_moon, x+0.5*h, y)-effpot_m1_m2(theta_moon, x-0.5*h, y))/h
    dV_dy= (effpot_m1_m2(theta_moon, x, y+0.5*h)-effpot_m1_m2(theta_moon, x, y-0.5*h))/h
    return array([dV_dx,dV_dy], float)
    
def r_3b_m1_m2(theta_moon): #position vector ofr m3
    return array([1-miu_m1_m2(m_earth)+d_earth_moon/d_earth_sun*cos(theta_moon), d_earth_moon/d_earth_sun*sin(theta_moon), float])
    
def I_m1_m2(theta_moon):
    r_x=r_3b_m1_m2(theta_moon)[0]
    r_y=r_3b_m1_m2(theta_moon)[1]
    I_x= -miu_m1_m2(m_moon)*r_x/distance(r_x, r_y, 0, 0)**3
    I_y= -miu_m1_m2(m_moon)*r_y/distance(r_x, r_y, 0, 0)**3
    return array([I_x, I_y], float)    #indirect acceleration due to m3 as seen in literature

def f_m1_m2(r, theta_moon):
    x=r[0]
    y=r[1]    
    vx=r[2]
    vy=r[3]
    xprime=vx
    yprime=vy
    vxprime= partialV_m1_m2(r,(omegam/omegas-1)*t)[0]+I_m1_m2((omegam/omegas-1)*t)[0]+2*yprime
    vyprime= partialV_m1_m2(r,(omegam/omegas-1)*t)[1]+I_m1_m2((omegam/omegas-1)*t)[1]-2*xprime
    return array([xprime,yprime,vxprime,vyprime], float)

def RK4_m1_m2(r,t): #returns change in r as calculated by RK4
    k1 = h1*f_m1_m2(r,(omegam/omegas-1)*t)
    k2 = h1*f_m1_m2(r+0.5*k1,(omegam/omegas-1)*(t+0.5*h1))
    k3 = h1*f_m1_m2(r+0.5*k2,(omegam/omegas-1)*(t+0.5*h1))
    k4 = h1*f_m1_m2(r+k3,(omegam/omegas-1)*(t+h1))
    r += (k1+2*k2+2*k3+k4)/6
    return r

def E_m1_m2(r, theta_moon):
    x=r[0]
    y=r[1]
    return 0.5*(r[2]**2+r[3]**2)-effpot_m1_m2(theta_moon, x, y)

xpoints = []
ypoints = []
vxpoints = []
vypoints = []
Epoints = []
tpoints = []  

t=0.0
#print(RK4(r,0))
r_m1_m2 = array([1-miu_m1_m2(m_earth)+d_earth_moon/d_earth_sun*cos(0.0)+d_earth_moon/d_earth_sun*r_capture*cos(rad_min3), d_earth_moon/d_earth_sun*r_capture*sin(rad_min3), d_earth_moon/d_earth_sun*(orbit_v(m_moon, r_capture)+delta_V_min3)*sin(rad_min3), -d_earth_moon/d_earth_sun*(orbit_v(m_moon, r_capture)+delta_V_min3)*cos(rad_min3)], float)
h1=0.001
#print (1-miu_m1_m2(m_earth))
#print(1-miu_m1_m2(m_earth)+d_earth_moon/d_earth_sun*cos(0.0)+d_earth_moon/d_earth_sun*r_capture*cos(rad_min))
while r_m1_m2[0]>1-miu_m1_m2(m_earth):
    xpoints.append(r_m1_m2[0])
    ypoints.append(r_m1_m2[1])
    vxpoints.append(r_m1_m2[2])
    vypoints.append(r_m1_m2[3])
    tpoints.append(t)
    #Epoints.append(E(r, (omegas/omegam-1)*t))    
    r_m1_m2 = RK4_m1_m2(r_m1_m2,t)
    #print (r_m1_m2)
    t-=h
    
plot(xpoints, ypoints)
show()
capture_trajectory_time= tpoints[len(tpoints)-1]
r_3=[xpoints[len(xpoints)-1], ypoints[len(ypoints)-1], -vxpoints[len(vxpoints)-1], -vypoints[len(vypoints)-1]]
print(r_3)
#print(capture_trajectory_time)




h=0.01
tau2=[]
delta_Vs2 = []
r_L2= array([0.99, 0, 0, 0], float)
Emin2 = E_m1_m2(r_L2, (omegam/omegas-1)*capture_trajectory_time)


"""

#Non-transit orbit search
delta_V2=0.0
x_earth=1-miu_m1_m2(m_earth)
theta2=0.0
rad_2= float(theta2*pi/180)
r_2 = array([x_earth+d_earth_moon/d_earth_sun*r_escape*cos(rad_2), d_earth_moon/d_earth_sun*r_escape*sin(rad_2), -d_earth_moon/d_earth_sun*(orbit_v(m_earth, r_escape)+delta_V2)*sin(rad_2), d_earth_moon/d_earth_sun*(orbit_v(m_earth, r_escape)+delta_V2)*cos(rad_2)], float)
mindV2=sqrt(2*(Emin2-E_m1_m2(r_2, 0))+orbit_v(m_earth, r_escape)**2)-orbit_v(m_earth, r_escape)
delta_V2=mindV2
print (" inital distance for theta = 0 ", distance(r_2[0], r_2[1], r_3[0], r_3[1]))
while distance(r_2[0], r_2[1], r_3[0], r_3[1])>10^-5:
    t_param=-20
    while t_param<capture_trajectory_time:
        t=t_param
        theta2=0.0
        while theta2<=90:
            rad_2= float(theta2*pi/180)
            r_2 = array([x_earth+d_earth_moon/d_earth_sun*r_escape*cos(rad_2), d_earth_moon/d_earth_sun*r_escape*sin(rad_2), -d_earth_moon/d_earth_sun*(orbit_v(m_earth, r_escape)+delta_V2)*sin(rad_2), d_earth_moon/d_earth_sun*(orbit_v(m_earth, r_escape)+delta_V2)*cos(rad_2)], float)
            while t<capture_trajectory_time:
                r_2 = RK4_m1_m2(r_2,t)
                t+=h
            if distance(r_2[0], r_2[1], r_3[0], r_3[1])<10^-6 and r_2[2]>=0:
                delta_V_min_init=delta_V2
                t_param_min=t_param
                theta2_min =theta2
            else:
                print(delta_V2, t_param, theta2, distance(r_2[0], r_2[1], r_3[0], r_3[1]), "no" )
                theta2+=2.0
        t_param+=0.2
    delta_V2+=0.1
    if delta_V2>= 10:
            print("not suitable path found... change error bound")            
                

print ("finished")

"""