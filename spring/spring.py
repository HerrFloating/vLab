from vpython import *
from math import *
import random
"""constants"""
k1 = pi**2
M1 = 0
m = 0.07
eq = vector(0,-8,0)
t = 0
dt = 1e-3
eq.y = -8-((M1+m/2)*g/k1)
g = 9.8

"""background setting"""
scene1 = canvas(center = vector(0,-8,0),background = color.white)
mass = box(pos = eq,axis = vector(1,0,0),size=vector(0.01,0.01,0.01),velocity = vector(0,0,0),visible = False,pickable = False)
"""Masses"""
mass1e=cylinder(pos = vector(-5,-19,0),axis=vector(0,-1.5,0),radius = 0.8,color = vector(229/255,137/255,57/255))
t1 = text(pos = mass1e.pos + vector(0,-0.75,1),color=color.black,text = '50 g',height = 0.3 , depth=0)
mass1 = compound([mass1e,t1])
mass1e.visible = False
t1.visible = False
del t1
del mass1e
mass1.pos.z = 0
mass1.mass = random.uniform(49.9,50.1)/1000
mass2e=cylinder(pos = vector(-7,-19,0),axis=vector(0,-1.3,0),radius = 0.8,color = vector(229/255,123/255,57/255))
t2 = text(pos = mass2e.pos + vector(0,-1.3/2,1),color=color.black,text = '40 g',height = 0.3 , depth=0)
mass2 = compound([mass2e,t2])
mass2e.visible = False
t2.visible = False
del mass2e
del t2
mass2.pos.z=0
mass2.mass = random.uniform(39.9,40.1)/1000
mass3e=cylinder(pos = vector(-9,-19,0),axis=vector(0,-1.1,0),radius = 0.8,color = vector(229/255,109/255,57/255))
t3 = text(pos = mass3e.pos + vector(0,-1.1/2,1),color=color.black,text = '30 g',height = 0.3 , depth=0)
mass3 = compound([mass3e,t3])
mass3e.visible = False
t3.visible = False
del mass3e
del t3
mass3.pos.z=0
mass3.mass = random.uniform(29.9,30.1)/1000
mass4e=cylinder(pos = vector(-11,-19,0),axis=vector(0,-0.9,0),radius = 0.8,color = vector(229/255,91/255,57/255))
t4 = text(pos = mass4e.pos + vector(0,-0.9/2,1),color=color.black,text = '20 g',height = 0.3 , depth=0)
mass4 = compound([mass4e,t4])
mass4e.visible = False
t4.visible = False
del mass4e
del t4
mass4.pos.z = 0
mass4.mass = random.uniform(19.9,20.1)
mass5e=cylinder(pos = vector(-13,-19,0),axis=vector(0,-0.7,0),radius = 0.8,color = vector(229/255,57/255,57/255))
t5 = text(pos = mass5e.pos + vector(0,-0.7/2,1),color=color.black,text = '10 g',height = 0.3 , depth=0)
mass5 = compound([mass5e,t5])
mass5e.visible = False
t5.visible = False
del mass5e
del t5
mass5.pos.z = 0
mass5.mass = random.uniform(9.9,10.1)
mass1.pos=vector(-5,-19.75,0)
mass2.pos=vector(-7,-19.75,0)
mass3.pos=vector(-9,-19.75,0)
mass4.pos=vector(-11,-19.75,0)
mass5.pos=vector(-13,-19.75,0)
v = arrow(pos = vector(-4,0,0),axis = vector(3.5,0,0),shaftwidth = 0.1,length = 2,visible = False,color = color.red)
"""ruler"""
eq.y = -8
rul = box(pos = vector(2,-8.4,0), axis = vector(1,0,0), size = vector(1.3,16.13,0.1),color = vector(12/255,184/255,252/255))
c = color.black
a = [box(pos = vector(1.7,(-0.02 + eq.y),0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = c)]
L = [text(pos = vector(2.1,(-0.2 + eq.y),0.2), text = '0', height = 0.3,color=c,depth =0)]
for n in range(1,((-eq.y-0.4)*10)+1):
    if n % 10 == 0:
        a.append(box(pos = vector(1.7,(-0.02+eq.y)+n*0.1,0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = c))
        d = n*0.1
        d = str(d)
        L.append(text(pos = vector(2.1,-0.2+eq.y+n*0.1,0.2), text = d, height = 0.3,color=c,depth =0))
    elif n % 5 ==0:
        a.append(box(pos = vector(1.6,-0.02+eq.y+n*0.1,0),axis = vector(1,0,0), size = vector(0.5,-0.04,0.1),color = c))
    else:
        a.append(box(pos = vector(1.5,-0.02+eq.y+0.1*n,0),axis = vector(1,0,0), size = vector(0.3,-0.04,0.1),color = c))
for n in range(1,(16.4 + eq.y)*10 + 1):
    if n % 10 == 0:
        a.append(box(pos = vector(1.7,(-0.02+eq.y)-n*0.1,0),axis = vector(1,0,0), size = vector(0.7,-0.04,0.1),color = c))
        d = n*0.1
        d = str(d)
        L.append(text(pos = vector(2.1,-0.2+eq.y-n*0.1,0.2), text = d, height = 0.3,color=c,depth =0))
    elif n % 5 ==0:
        a.append(box(pos = vector(1.6,-0.02+eq.y-n*0.1,0),axis = vector(1,0,0), size = vector(0.5,-0.04,0.1),color = c))
    else:
        a.append(box(pos = vector(1.5,-0.02+eq.y-0.1*n,0),axis = vector(1,0,0), size = vector(0.3,-0.04,0.1),color = c))
ruller = compound([rul,L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8],L[9],L[10],L[11],L[12],L[13],L[14],L[15],a[ 0 ],a[ 1 ],a[ 2 ],a[ 3 ],a[ 4 ],a[ 5 ],a[ 6 ],a[ 7 ],a[ 8 ],a[ 9 ],a[ 10 ],a[ 11 ],a[ 12 ],a[ 13 ],a[ 14 ],a[ 15 ],a[ 16 ],a[ 17 ],a[ 18 ],a[ 19 ],a[ 20 ],a[ 21 ],a[ 22 ],a[ 23 ],a[ 24 ],a[ 25 ],a[ 26 ],a[ 27 ],a[ 28 ],a[ 29 ],a[ 30 ],a[ 31 ],a[ 32 ],a[ 33 ],a[ 34 ],a[ 35 ],a[ 36 ],a[ 37 ],a[ 38 ],a[ 39 ],a[ 40 ],a[ 41 ],a[ 42 ],a[ 43 ],a[ 44 ],a[ 45 ],a[ 46 ],a[ 47 ],a[ 48 ],a[ 49 ],a[ 50 ],a[ 51 ],a[ 52 ],a[ 53 ],a[ 54 ],a[ 55 ],a[ 56 ],a[ 57 ],a[ 58 ],a[ 59 ],a[ 60 ],a[ 61 ],a[ 62 ],a[ 63 ],a[ 64 ],a[ 65 ],a[ 66 ],a[ 67 ],a[ 68 ],a[ 69 ],a[ 70 ],a[ 71 ],a[ 72 ],a[ 73 ],a[ 74 ],a[ 75 ],a[ 76 ],a[ 77 ],a[ 78 ],a[ 79 ],a[ 80 ],a[ 81 ],a[ 82 ],a[ 83 ],a[ 84 ],a[ 85 ],a[ 86 ],a[ 87 ],a[ 88 ],a[ 89 ],a[ 90 ],a[ 91 ],a[ 92 ],a[ 93 ],a[ 94 ],a[ 95 ],a[ 96 ],a[ 97 ],a[ 98 ],a[ 99 ],a[ 100 ],a[ 101 ],a[ 102 ],a[ 103 ],a[ 104 ],a[ 105 ],a[ 106 ],a[ 107 ],a[ 108 ],a[ 109 ],a[ 110 ],a[ 111 ],a[ 112 ],a[ 113 ],a[ 114 ],a[ 115 ],a[ 116 ],a[ 117 ],a[ 118 ],a[ 119 ],a[ 120 ],a[ 121 ],a[ 122 ],a[ 123 ],a[ 124 ],a[ 125 ],a[ 126 ],a[ 127 ],a[ 128 ],a[ 129 ],a[ 130 ],a[ 131 ],a[ 132 ],a[ 133 ],a[ 134 ],a[ 135 ],a[ 136 ],a[ 137 ],a[ 138 ],a[ 139 ],a[ 140 ],a[ 141 ],a[ 142 ],a[ 143 ],a[ 144 ],a[ 145 ],a[ 146 ],a[ 147 ],a[ 148 ],a[ 149 ],a[ 150 ],a[ 151 ],a[ 152 ],a[ 153 ],a[ 154 ],a[ 155 ],a[ 156 ],a[ 157 ],a[ 158 ],a[ 159 ],a[ 160 ]])
ruller.pickable = False
rul.visible = False
del rul
for i in range(len(a)):
    a[0].visible = False
    del a[0]
for i in range(len(L)):
    L[0].visible
    del L[0]
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
S = compound([paye1,sh,s,pich1,roof,sh1,s1,pich2,roof1,E1,E2,b1,b2,b3,b4,ground])
S.pickable = False
paye1.visible = False
del paye1
sh.visible = False
del sh
s.visible = False
del s
pich1.visible = False
del pich1
roof.visible = False
del roof
sh1.visible = False
del sh1
s1.visible = False
del s1
pich2.visible = False
del pich2
roof1.visible = False
del roof1
E1.visible = False
del E1
E2.visible = False
del E2
b1.visible = False
del b1
b2.visible = False
del b2
b3.visible = False
del b3
b4.visible = False
del b4
ground.visible = False
del ground
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
def Springs1(c):
    global spring,k1
    if r1.checked == True :
            k1=pi**2
            spring.color = color.gray(0.1)
            spring.radius=0.8
            spring.thickness = 0.1
            r2.checked = False
def Springs2(c):
    global spring,k1
    if r2.checked == True :
            k1 = 2
            spring.color = color.gray(0.8)
            spring.radius = 0.6
            spring.thickness = 0.05
            r1.checked = False
r1 = radio(bind=Springs1,checked = True, text='First Spring')
r2 = radio(bind = Springs2 , text='Second Spring')
scene1.append_to_caption('\n\n')
"""gravity acceleraion"""
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
        eq.y = -8-((M1+m/2)*g/k1)
        if eq.y < -10:
            Error.text = 'Error : Change g'
            eq.y = -8
        else:
            ruller.pos.y = eq.y-0.4
    else:
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
