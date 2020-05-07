from vpython import *
from math import *

"""constants"""
k1 = pi**2
M1 = 0
m = 0.07
eq = vector(0,-8,0)
t = 0
dt = 1e-3
eq.y = -8-((M1+m/2)*g/k1)

"""background setting"""
scene1 = canvas(center = vector(0,-8,0),background = color.white)
mass = box(pos = eq,axis = vector(1,0,0),size=vector(0.01,0.01,0.01),velocity = vector(0,0,0),visible = False,pickable = False)
"""Masses"""
mass1=cylinder(pos = vector(-5,-19,0),axis=vector(0,-1.5,0),radius = 0.8,color = vector(229/255,137/255,57/255))
t1 = text(pos = mass1.pos + vector(0,-0.75,1),color=color.black,text = '50 g',height = 0.3 , depth=0)
mass1 = compound([mass1,t1])
mass1.pos.z = 0
mass1.mass = 0.05
mass2=cylinder(pos = vector(-7,-19,0),axis=vector(0,-1.3,0),radius = 0.8,color = vector(229/255,123/255,57/255))
t2 = text(pos = mass2.pos + vector(0,-1.3/2,1),color=color.black,text = '40 g',height = 0.3 , depth=0)
mass2 = compound([mass2,t2])
mass2.pos.z=0
mass2.mass = 0.04
mass3=cylinder(pos = vector(-9,-19,0),axis=vector(0,-1.1,0),radius = 0.8,color = vector(229/255,109/255,57/255))
t3 = text(pos = mass3.pos + vector(0,-1.1/2,1),color=color.black,text = '30 g',height = 0.3 , depth=0)
mass3 = compound([mass3,t3])
mass3.pos.z=0
mass3.mass = 0.03
mass4=cylinder(pos = vector(-11,-19,0),axis=vector(0,-0.9,0),radius = 0.8,color = vector(229/255,91/255,57/255))
t4 = text(pos = mass4.pos + vector(0,-0.9/2,1),color=color.black,text = '20 g',height = 0.3 , depth=0)
mass4 = compound([mass4,t4])
mass4.pos.z = 0
mass4.mass = 0.02
mass5=cylinder(pos = vector(-13,-19,0),axis=vector(0,-0.7,0),radius = 0.8,color = vector(229/255,57/255,57/255))
t5 = text(pos = mass5.pos + vector(0,-0.7/2,1),color=color.black,text = '10 g',height = 0.3 , depth=0)
mass5 = compound([mass5,t5])
mass5.pos.z = 0
mass5.mass = 0.01
v = arrow(pos = vector(-4,0,0),axis = vector(3.5,0,0),shaftwidth = 0.1,length = 2,visible = False,color = color.red)
"""paye"""
paye1 = cylinder(pos =vector(9.5,1,0),radius = 0.2,axis = vector(0,-19,0), color=vector(229/255,229/255,229/255),pickable = False)
sh= box(pos=vector(9.5,0,0.2),axis = vector(0,1,0),size = vector(0.6,1,0.1),color = color.black,pickable = False)
s = cylinder(pos = vector(10,0.1,0),axis=vector(0.5,0,0),radius = 0.1,color=vector(229/255,229/255,229/255),pickable = False)
pich1=cylinder(pos=vector(10.5,0.1,0),axis = vector(0.1,0,0),radius=0.2,pickable = False)
roof = cylinder(pos = vector(-0.5,0.1,0), axis = vector(9.5,0,0), radius = 0.1 , color=vector(229/255,229/255,229/255),pickable = False)
sh1= box(pos=vector(9.5,-2,0.2),axis = vector(0,1,0),size = vector(0.6,1,0.1),color = color.black,pickable = False)
s1 = cylinder(pos = vector(10,-1.9,0),axis=vector(0.5,0,0),radius = 0.1,color=vector(229/255,229/255,229/255),pickable = False)
pich2=cylinder(pos=vector(10.5,-1.9,0),axis = vector(0.1,0,0),radius=0.2)
roof1 = cylinder(pos = vector(3.1,-1.9,0), axis = vector(7.4,0,0), radius = 0.06 , color=vector(229/255,229/255,229/255),pickable = False)
E1 = cylinder(pos = vector(2.75,-1.9,0), axis =vector(3.1,0,0), radius = 0.06 , color=vector(229/255,229/255,229/255),pickable = False)
E2 = extrusion(path=paths.arc(radius=0.5, angle2=pi), color=vector(229/255,229/255,229/255),pickable = False,
    shape=[ [ shapes.circle(pos=[0,0], radius=0.06)] ])
E2.axis=vector(0,0,1)
E2.pos = vector(2.9,0,1.9)
E2.rotate(angle=pi/2,
           axis=vec(1,0,0),
           origin=vector(0,0,0))
b1 = box(pos=vector(2.4,-1.9-.56+0.03,0.1),axis=vector(1,0,0),size=vector(0.6,0.1,0.1),color=vector(178/255,62/255,62/255),pickable = False)
b2 = box(pos=vector(2.4,-1.9-.56+1.03,0.1),axis=vector(1,0,0),size=vector(0.6,0.1,0.1),color=vector(178/255,62/255,62/255),pickable = False)
b3 = box(pos=vector(2.7,-1.9-.56+0.53,0.1),axis=vector(1,0,0),size=vector(0.1,0.1,0.1),color=vector(178/255,62/255,62/255),pickable = False)
b4 = box(pos=vector(1.3,-1.9-.56+0.53,0.1),axis=vector(1,0,0),size=vector(0.1,0.1,0.1),color=vector(178/255,62/255,62/255),pickable = False)
ground = box(pos=vector(4.2,-18.5,0),axis = vector(1,0,0),size=vector(14,0.8,0.1),color=vector(229/255,229/255,229/255),pickable = False)
spring = helix(pos = vector(0,0,0) , axis = vector(0,-8,0)   , radius = 0.8, coils = 15 , color = color.gray(0.1),thickness=0.07 )
"""ruler"""
rul = box(pos = vector(2,-8.4,0), axis = vector(1,0,0), size = vector(1.3,16.13,0.1),color = vector(12/255,244/255,252/255),pickable = False)
a = [box(pos = vector(1.7,(-0.02 -8.4),0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = color.black,pickable = False)]
L = [text(pos = vector(2.1,(-0.2 -8.4),0.1), text = '0', height = 0.3,color=color.black,depth =0,pickable = False)]
for n in range(1,(8*10)+1):
    if n % 10 == 0:
        a.append(box(pos = vector(1.7,(-0.02-8.4)+n*0.1,0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = color.black,pickable = False))
        d = n*0.1
        d = str(d)
        L.append(text(pos = vector(2.1,-0.1-8+n*0.1,0.1), text = d , height = 0.3,depth=0,color = color.black,pickable = False))
    elif n % 5 ==0:
        a.append(box(pos = vector(1.6,-0.02-8+n*0.1,0),axis = vector(1,0,0), size = vector(0.5,-0.04,0.1),color = color.black,pickable = False))
    else:
        a.append(box(pos = vector(1.5,-0.02-8+0.1*n,0),axis = vector(1,0,0), size = vector(0.3,-0.04,0.1),color = color.black,pickable = False))
for n in range(1,(16 -8)*10 + 1):
    if n % 10 == 0:
        a.append(box(pos = vector(1.7,(-0.02-8)-n*0.1,0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = color.black,pickable = False))
        d = n*0.1
        d = str(d)
        L.append(text(pos = vector(2.1,-0.1-8-n*0.1,0.1), text = d , height = 0.3,depth=0,color=color.black,pickable = False))
    elif n % 5 ==0:
        a.append(box(pos = vector(1.6,-0.02-8-n*0.1,0),axis = vector(1,0,0), size = vector(0.5,-0.04,0.1),color = color.black,pickable = False))
    else:
        a.append(box(pos = vector(1.5,-0.02-8-0.1*n,0),axis = vector(1,0,0), size = vector(0.3,-0.04,0.1),color = color.black,pickable = False))
"""Drag"""
def down():
    global drag,mass,obj
    obj = scene1.mouse.pick
    drag = True

def move():
    global drag, mass,obj,M1,eq
    if drag:# mouse button is down
        if obj.pos.y != eq.y and obj.pos.x != eq.x:
            obj.pos.x = scene1.mouse.pos.x
            obj.pos.y = scene1.mouse.pos.y
        else:
            mass = obj
            M1 = obj.mass
            obj.pos.x = 0
            obj.pos.y = scene1.mouse.pos.y
            spring.axis = obj.pos
            obj.velocity = vector(0,0,0)
        if mass.pos.y > -0.5 or mass.pos.y < -15.5:
            running = False
            Error.text = "Error: Mass position has to be between 0 and 15 ."
            mass.pos.y = -10
            spring.axis = mass.pos
        else:
            Error.text = "No Error"
def up():
    global drag, mass,obj

    drag = False
"""Run button"""
running = False
def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"
button(text = 'Run' , bind = Run)
"""Clear button"""
def Clear(c):
    global W1,t , mass , spring,eq
    t = 0
    eq = vector(0,-8-((M1+m/2)*g/k1),0)
    mass.pos = eq
    spring.axis = mass.pos
    mass.velocity = vector(0,0,0)
    v.visible = False
    W1.text = 'Elapsed time : 0'
button(text = 'Clear',bind = Clear)
"""Reset button"""
def Reset(c):
    global  W1,t , mass , spring,mass1,eq,s1,M1
    t = 0
    M1 = 0
    mass1.pos=vector(-5,-19.75,0)
    mass2.pos=vector(-7,-19.75,0)
    mass3.pos=vector(-9,-19.75,0)
    mass4.pos=vector(-11,-19.75,0)
    mass5.pos=vector(-13,-19.75,0)
    mass = box(pos = eq,axis = vector(1,0,0),size=vector(0.01,0.01,0.01),velocity = vector(0,0,0),visible = False)
    eq = vector(0,-8-((M1+m/2)*g/k1),0)
    spring.axis = vector(0,eq.y,0)
    mass.velocity = vector(0,0,0)
    v.visible = False
    W1.text = 'Elapsed time : 0'
button(text = 'Reset' , bind = Reset)
scene1.append_to_caption('\n\n')
"""diffrent springs"""
def Springs(c):
    global spring,k1
    if r1.checked == True:
        k1=pi**2
        spring.color = color.gray(0.1)
        spring.radius=0.8
        spring.thickness = 0.1
    if r2.checked == True :
        k1 = 2
        spring.color = color.gray(0.8)
        spring.radius = 0.6
        spring.thickness = 0.05
        r1.checked = False
r1 = radio(bind=Springs,checked = True, text='First Spring')
r2 = radio(bind = Springs , text='Second Spring')
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
while True:
    scene1.bind("mousedown", down)

    scene1.bind("mousemove", move)

    scene1.bind("mouseup", up)

    if t == 0:
        r1.disabled = False
        r2.disabled = False
        gravity.disabled = False
        g = gravity.number
        eq.y = -8-((M1+m/2)*g/k1)
        if eq.y < -10:
            Error.text = 'Error : Change g'
            eq.y = -8
        else:
            for i in range(0,len(L)):
                L[0].visible = False
                del L[0]
            for i in range(0,len(a)):
                a[0].visible = False
                del a[0]
            a = [box(pos = vector(1.7,(-0.02 + eq.y),0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = color.black,pickable = False)]
            L = [text(pos = vector(2.1,(-0.2 + eq.y),0.1), text = '0', height = 0.3,color=color.black,depth =0,pickable = False)]
            for n in range(1,((-eq.y-0.4)*10)+1):
                if n % 10 == 0:
                    a.append(box(pos = vector(1.7,(-0.02+eq.y)+n*0.1,0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = color.black,pickable = False))
                    d = n*0.1
                    d = str(d)
                    L.append(text(pos = vector(2.1,-0.2+eq.y+n*0.1,0.1), text = d, height = 0.3,color=color.black,depth =0,pickable = False))
                elif n % 5 ==0:
                    a.append(box(pos = vector(1.6,-0.02+eq.y+n*0.1,0),axis = vector(1,0,0), size = vector(0.5,-0.04,0.1),color = color.black,pickable = False))
                else:
                    a.append(box(pos = vector(1.5,-0.02+eq.y+0.1*n,0),axis = vector(1,0,0), size = vector(0.3,-0.04,0.1),color = color.black,pickable = False))
            for n in range(1,(16.4 + eq.y)*10 + 1):
                if n % 10 == 0:
                    a.append(box(pos = vector(1.7,(-0.02+eq.y)-n*0.1,0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = color.black,pickable = False))
                    d = n*0.1
                    d = str(d)
                    L.append(text(pos = vector(2.1,-0.2+eq.y-n*0.1,0.1), text = d, height = 0.3,color=color.black,depth =0,pickable = False))
                elif n % 5 ==0:
                    a.append(box(pos = vector(1.6,-0.02+eq.y-n*0.1,0),axis = vector(1,0,0), size = vector(0.5,-0.04,0.1),color = color.black,pickable = False))
                else:
                    a.append(box(pos = vector(1.5,-0.02+eq.y-0.1*n,0),axis = vector(1,0,0), size = vector(0.3,-0.04,0.1),color = color.black,pickable = False))
    else:
        gravity.disabled = True
        r1.disabled = True
        r2.disabled = True

    rate(1e3)
    if running :
        mass.pos = mass.velocity*dt + mass.pos
        mass.velocity = ((k1/(M1+m/3))*(eq - mass.pos) - g*vector(0,1,0))* dt + mass.velocity
        spring.axis = mass.pos
        t = t + dt
        v.visible = True
        v.pos = mass.pos
        """Timer"""
        t1 = str(t)
        s = t1.find('.')
        t1 = t1[0:s+3]
        W1.text = "Elapsed time :" , t1
    k = keysdown()
    if 'up' in k: scene1.center =scene1.center +  vector(0,0.01,0)
    if 'down' in k: scene1.center =scene1.center + vector(0,-0.01,0)
    if 'left' in k: scene1.center = scene1.center + vector(-0.01,0,0)
    if 'right' in k: scene1.center = scene1.center + vector(0.01,0,0)
