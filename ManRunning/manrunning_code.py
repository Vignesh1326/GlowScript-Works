GlowScript 3.0 VPython
face=sphere(color=color.green,pos=vector(-5,12,5),radius=3)
body=box(color=color.red,pos=vector(-5,6,5),length=6,width=6,height=6)
hand1=box(color=color.red,pos=vector(-8,7.5,5),length=2,width=2,height=1)
hand2=box(color=color.red,pos=vector(-2,7.5,5),length=2,width=2,height=1)
handd1=box(color=color.red,pos=vector(-1,6,5),length=1,width=2,height=4)
handd2=box(color=color.red,pos=vector(-9,6,5),length=1,width=2,height=4)
leg1=box(color=color.red,pos=vector(-3.5,1,5),height=7.5,length=1,width=1.8)
leg2=box(color=color.red,pos=vector(-6.5,1,5),height=7.5,length=1,width=1.8)
road=box(color=color.blue,pos=vector(0,-3.5,5),length=20,width=200,height=1)
for i in range(1,350):
    rate(40)
    if(i==1):
        rate(20)
        handd2.rotate(angle=-10,axis=vector(1,0,0),origin=handd2.pos)
        leg1.rotate(angle=-10,axis=vector(1,0,0),origin=leg1.pos)
    elif(i%2==0):
        rate(20)
        handd1.rotate(angle=-10,axis=vector(1,0,0),origin=handd1.pos)
        leg2.rotate(angle=-10,axis=vector(1,0,0),origin=leg2.pos)
        handd2.rotate(angle=10)         
        leg1.rotate(angle=10)
    else: 
        rate(20)
        handd2.rotate(angle=-10,axis=vector(1,0,0),origin=handd2.pos)
        leg1.rotate(angle=-10,axis=vector(1,0,0),origin=leg1.pos)                
        handd1.rotate(angle=10)
        leg2.rotate(angle=10)
    
        face.pos.z=face.pos.z+0.5
        body.pos.z=body.pos.z+0.5 
        hand1.pos.z=hand1.pos.z+0.5
        hand2.pos.z=hand2.pos.z+0.5
        handd1.pos.z=handd1.pos.z+0.5
        handd2.pos.z=handd2.pos.z+0.5
        leg1.pos.z=leg1.pos.z+0.5
        leg2.pos.z=leg2.pos.z+0.5
