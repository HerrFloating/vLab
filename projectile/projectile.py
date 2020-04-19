from vpython import *
from math import *
"""Constants"""
alpha = 0
beta = 0
g = 9.8
t = 0
dt = 0.001
M = 0.5
v_0 = 2
theta = 30
"""background setting"""
scene1 = canvas(center = vector(8,5,0),background = color.white)
"""Object"""
mass = sphere(pos = vector(0,10,0),velocity = vector(v_0*cos(radians(theta)),v_0*sin(radians(theta)),0),radius = 0.5,color = color.blue , make_trail = False)
"""Run button"""
running = False
def Run(b):
    global mass,running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"
button(text = 'Run' , bind = Run)
"""Reset button"""
def Reset(c):
    global  W1,t , mass , spring
    t = 0
    mass.pos = vector(0,10,0)
    mass.velocity = vector(v_0*cos(radians(theta)),v_0*sin(radians(theta)),0)
    mass.clear_trail()
    W1.text = 'Elapsed time : 0'
button(text = 'Reset' , bind = Reset)
scene1.append_to_caption('\n\n')
"""alpha input"""
def T(s):
    pass
alpha_in = winput(bind = T,prompt = 'Enter alpha and beta (\\(\\alpha \\, v^{\\beta}\\)) :',text = "0", number = 0)
"""beta input"""
beta_in = winput(bind = T,text = "0", number = 0)
scene1.append_to_caption('\n\n')
v = winput(bind = T,prompt = 'Enter \\(v_0\\) and \\(\\theta\\) in degrees  :',text = "2", number = 2)
theta1 = winput(bind = T,text = "30", number = 30)
MathJax.Hub.Queue(["Typeset",MathJax.Hub])
scene1.append_to_caption('\n\n')
"""Timer box"""
W1 = wtext(text = 'Elapsed time : 0')
scene1.append_to_caption('\n\n')
W2 = wtext(text = 'x component : ')
W3 = wtext(text = 'y component : ')
"""Drag"""
def down():
    nonlocal drag, mass
    mass.make_trail = False
    mass.pos.x = scene1.mouse.pos.x
    mass.pos.y = scene1.mouse.pos.y
    drag = True

def move():
    nonlocal drag, mass
    if drag: # mouse button is down
        mass.make_trail = False
        mass.pos.x = scene1.mouse.pos.x
        mass.pos.y = scene1.mouse.pos.y
        mass.color = color.red
        mass.make_trail = False

def up():
    nonlocal drag, mass
    mass.color = color.blue
    mass.make_trail = False
    drag = False
while True:
    scene1.bind("mousedown", down)

    scene1.bind("mousemove", move)

    scene1.bind("mouseup", up)
    W2.text = "x Component : ",scene1.mouse.pos.x
    W3.text = "y Component : ",scene1.mouse.pos.y
    if t == 0 :
        alpha_in.disabled = False
        beta_in.disabled = False
        v.disabled = False
        theta1.disabled = False
        v_0 = v.number
        theta = theta1.number
        alpha = alpha_in.number
        beta = beta_in.number
        mass.velocity.x = v_0*cos(radians(theta))
        mass.velocity.y = v_0*sin(radians(theta))
    rate(1000)
    if running and mass.pos.y >= 0:
            alpha_in.disabled = True
            beta_in.disabled = True
            v.disabled = True
            theta1.disabled = True
            phi = atan(mass.velocity.y/mass.velocity.x)
            mass.make_trail = True
            mass.pos = mass.velocity*dt + mass.pos
            mass.velocity =  (-(alpha/M)*((mass.velocity.mag)**2)*vector(cos(phi),sin(phi),0) -g*vector(0,1,0))*dt + mass.velocity
            t = t + dt
            """Timer"""
            t1 = str(t)
            s = t1.find('.')
            t1 = t1[0:s+3]
            W1.text = "Elapsed time :" , t1
    k = keysdown()
    if 'up' in k: scene1.center =scene1.center +  vector(0,0.001,0)
    if 'down' in k: scene1.center =scene1.center + vector(0,-0.001,0)
    if 'left' in k: scene1.center = scene1.center + vector(-0.001,0,0)
    if 'right' in k: scene1.center = scene1.center + vector(0.001,0,0)
