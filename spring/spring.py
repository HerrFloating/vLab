from vpython import *
from math import *

"""constants"""
M1 = 0.3
eq = vector(0,-8,0)
t = 0
dt = 1e-3
"""background setting"""
scene1 = canvas(center = vector(0,-8,0),background = color.white)
"""Drag"""
drag = False
scene1.bind("mousedown",def():
    global drag
    drag = True

    scene1.bind("mouseup",def():
        global drag
        drag = False
    )

)
"""spring"""
roof = box(pos = vector(0,0.1,0), axis = vector(0,0,1) ,size = vector(1.5,0.1,1.5), color = color.green)
mass = box(pos = vector(0,-10,0),axis = vector(0,0,1),velocity = vector(0,0,0),size = vector(0.8,0.8,0.8),color = color.blue , make_trail = True)
spring = helix(pos = vector(0,0,0) , axis = mass.pos   , radius = 0.4, coils = 20 , color = color.blue )
"""Run button"""
running = False
def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"
button(text = 'Run' , bind = Run)
"""Reset button"""
def Reset(c):
    global  W1,t , mass , spring
    t = 0
    mass.pos = vector(0,-10,0)
    spring.axis = mass.pos
    mass.velocity = vector(0,0,0)
    mass.clear_trail()
    W1.text = 'Elapsed time : 0'
button(text = 'Reset' , bind = Reset)
scene1.append_to_caption('\n\n')
"""input spring constant"""
def T(s):
    pass
W = winput(bind = T,prompt = 'Enter K : (press ENTER)',text = "pi**2", number = pi**2)
k1 = W.number
scene1.append_to_caption('\n\n')
"""gravity acceleraion"""
def T1(s):
    pass
gravity = winput(bind = T1,prompt = 'Enter g : (press ENTER)',text = "0", number = 0)
g = gravity.number
scene1.append_to_caption('\n\n')
"""Timer box"""
W1 = wtext(text = 'Elapsed time : 0')
scene1.append_to_caption('\n\n')
"""Error"""
Error = wtext(text = 'No Error')
"""ruler"""
rul = box(pos = vector(2,-8,0), axis = vector(1,0,0), size = vector(1.3,16.05,0.1),color = color.yellow)
da = box(pos = vector(1.7,-0.02,0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = color.black)
L = label(pos = vector(1.02,-0.02,0), text = '0',box = False, height = 10)
n = 1
while (n <= 160):
    if n % 10 == 0:
        da = box(pos = vector(1.7,-0.02-n*0.1,0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = color.black)
        d = n*0.1
        d = str(d)
        L = label(pos = vector(1.02,-0.02-n*0.1,0), text = d , box = False , height = 10)
    elif n % 5 ==0:
        da = box(pos = vector(1.6,-0.02-n*0.1,0),axis = vector(1,0,0), size = vector(0.5,-0.04,0.1),color = color.black)
    else:
        da  = box(pos = vector(1.5,-0.02-0.1*n,0),axis = vector(1,0,0), size = vector(0.3,-0.04,0.1),color = color.black)
    n = n + 1
while True:
    if drag:
        mass.make_trail = False
        mass.pos.y = scene1.mouse.pos.y
        spring.axis = mass.pos
    if mass.pos.y > 0 or mass.pos.y < -15:
        Error.text = "Error: Mass position has to be between 0 and 15 ."
        mass.pos.y = -10
        spring.axis = mass.pos
    else:
        Error.text = "No Error"
    if t == 0:
        W.disabled = False
        k1 = W.number
        gravity.disabled = False
        g = gravity.number
    else:
        W.disabled = True
        gravity.disabled = True
    rate(1e3)
    if running :
        mass.make_trail = True
        mass.pos = mass.velocity*dt + mass.pos
        mass.velocity = ((k1/M1)*(eq - mass.pos) - g*vector(0,1,0))* dt + mass.velocity
        spring.axis = mass.pos
        t = t + dt
        """Timer"""
        t1 = str(t)
        s = t1.find('.')
        t1 = t1[0:s+3]
        W1.text = "Elapsed time :" , t1
    k = keysdown()
    if 'up' in k: scene1.center =scene1.center +  vector(0,0.001,0)
    if 'down' in k: scene1.center =scene1.center + vector(0,-0.001,0)
