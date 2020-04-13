from vpython import *

"""constants"""
M = 0.06
eq = vector(0,-6,0)
k = pi**2
t = 0
dt = 0.00001
"""background setting"""
scene1 = canvas(center=vector(0,-4,0),background = color.white)
"""first spring with air drag"""
myb = box(pos = vector(0,0.1,0), axis = vector(0,0,1) ,size = vector(1.5,0.1,1.5), color = color.green)
mass = box(pos = vector(0,-8,0),axis = vector(0,0,1),velocity = vector(0,0,0),size = vector(0.8,0.8,0.8),color = color.blue)
spring = helix(pos = vector(0,0,0) , axis = mass.pos   , radius = 0.4, coils = 20 , color = color.blue )
"""ruler"""
rul = box(pos = vector(2,-5,0), axis = vector(1,0,0), size = vector(1.3,8.1,0.1),color = color.yellow)
da = box(pos = vector(1.7,-1.02,0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = color.black)
L = label(pos = vector(1.1,-1.02,0), text = '0',box = False, height = 10)
n = 1
while (n <= 80):
    if n % 10 == 0:
        da = box(pos = vector(1.7,-1.02-n*0.1,0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = color.black)
        d = n*0.1
        d = str(d)
        L = label(pos = vector(1.1,-1.02-n*0.1,0), text = d , box = False , height = 10)
    elif n % 5 ==0:
        da = box(pos = vector(1.6,-1.02-n*0.1,0),axis = vector(1,0,0), size = vector(0.5,-0.04,0.1),color = color.black)
    else:
        da  = box(pos = vector(1.5,-1.02-0.1*n,0),axis = vector(1,0,0), size = vector(0.3,-0.04,0.1),color = color.black)
    n = n + 1
"""motion of spring"""
while(t < 15000000):

    rate(23000)
    mass.pos = mass.velocity*dt + mass.pos
    mass.velocity = (k/M)*(eq - mass.pos) * dt + mass.velocity
    spring.axis = -spring.pos + mass.pos
    t = t + dt
