GlowScript 3.0 VPython
flag=1
while(flag==1):
    w1=sphere(pos=vector(0,0,0),color=color.red,radius=0.5)
    w2=sphere(pos=vector(0,2,0),color=color.red,radius=0.5)
    w3=sphere(pos=vector(2,0,0),color=color.red,radius=0.5)
    w4=sphere(pos=vector(2,2,0),color=color.red,radius=0.5)
    body=box(pos=vector(1,1,1),color=color.red,length=3,width=1,height=2)
    platform1=box(pos=vector(0,0,-1),color=color.green,length=70,width=1,height=6)
    wall=box(pos=vector(34,0,1.5),color=color.yellow,length=2,width=4,height=6)
    platform2=box(pos=vector(30,25,-1),color=color.green,length=6,width=1,height=50)
    platform3=box(pos=vector(-1,50,-1),color=color.green,length=68,width=1,height=6)
    platform4=box(pos=vector(-32,25,-1),color=color.green,length=6,width=1,height=55)
    while True:
        scene.camera.follow(body)
        rate(40)
        k=keysdown()
        if 'right' in k:
            w1.pos.x=w1.pos.x+0.5
            w2.pos.x=w2.pos.x+0.5
            w4.pos.x=w4.pos.x+0.5
            w3.pos.x=w3.pos.x+0.5
            body.pos.x=body.pos.x+0.5
            if(w3.pos.x>=32.5 and w3.pos.y<=3):
                t = text(text="You've crashed your car!! Try again", align='center', color=color.red,height=3,depth=1,up=vector(40,40,0))
                for j in range(10):
                    rate(10)
                    body.pos.x=body.pos.x-1
                    body.pos.z=body.pos.z+1
                for l in range(22):
                    rate(10)
                    body.pos.x=body.pos.x-0.5
                    body.pos.z=body.pos.z-0.5
                t.visible=False
                break
            if((w3.pos.x>=34 and w3.pos.y>3) or ((w3.pos.y>3 and w4.pos.y<48) and w3.pos.x>-29)):
                for m in range(4):
                    rate(5)
                    w1.pos.x=w1.pos.x+0.5
                    w2.pos.x=w2.pos.x+0.5
                    w4.pos.x=w4.pos.x+0.5
                    w3.pos.x=w3.pos.x+0.5
                    body.pos.x=body.pos.x+0.5
                for n in range(10):
                    rate(5)
                    w1.pos.z=w1.pos.z-0.5
                    w2.pos.z=w2.pos.z-0.5
                    w4.pos.z=w4.pos.z-0.5
                    w3.pos.z=w3.pos.z-0.5
                    body.pos.z=body.pos.z-0.5
                
                break
                    
        
        elif 'up' in k:
            w1.pos.y=w1.pos.y+0.5
            w2.pos.y=w2.pos.y+0.5
            w4.pos.y=w4.pos.y+0.5
            w3.pos.y=w3.pos.y+0.5
            body.pos.y=body.pos.y+0.5
            if(w2.pos.y>=55 or ((w2.pos.x<26 and w2.pos.x>-31)and w2.pos.y>3)):
                for m in range(4):
                    rate(5)
                    w1.pos.y=w1.pos.y+0.5
                    w2.pos.y=w2.pos.y+0.5
                    w4.pos.y=w4.pos.y+0.5
                    w3.pos.y=w3.pos.y+0.5
                    body.pos.y=body.pos.y+0.5
                for n in range(10):
                    rate(5)
                    w1.pos.z=w1.pos.z-0.5
                    w2.pos.z=w2.pos.z-0.5
                    w4.pos.z=w4.pos.z-0.5
                    w3.pos.z=w3.pos.z-0.5
                    body.pos.z=body.pos.z-0.5
                break
        elif 'down' in k:
            if(w1.pos.y<-4):
                for m in range(4):
                    rate(5)
                    w1.pos.y=w1.pos.y-0.5
                    w2.pos.y=w2.pos.y-0.5
                    w4.pos.y=w4.pos.y-0.5
                    w3.pos.y=w3.pos.y-0.5
                    body.pos.y=body.pos.y-0.5
                for n in range(10):
                    rate(5)
                    w1.pos.z=w1.pos.z-0.5
                    w2.pos.z=w2.pos.z-0.5
                    w4.pos.z=w4.pos.z-0.5
                    w3.pos.z=w3.pos.z-0.5
                    body.pos.z=body.pos.z-0.5
                break
            w1.pos.y=w1.pos.y-0.5
            w2.pos.y=w2.pos.y-0.5
            w4.pos.y=w4.pos.y-0.5
            w3.pos.y=w3.pos.y-0.5
            body.pos.y=body.pos.y-0.5
        elif 'left' in k:
            w1.pos.x=w1.pos.x-0.5
            w2.pos.x=w2.pos.x-0.5
            w4.pos.x=w4.pos.x-0.5
            w3.pos.x=w3.pos.x-0.5
            body.pos.x=body.pos.x-0.5
            if((w2.pos.x<26 and(w2.pos.y>3 and w1.pos.y<48)) or w2.pos.x<-35):
                for m in range(4):
                    rate(5)
                    w1.pos.x=w1.pos.x-0.5
                    w2.pos.x=w2.pos.x-0.5
                    w4.pos.x=w4.pos.x-0.5
                    w3.pos.x=w3.pos.x-0.5
                    body.pos.x=body.pos.x-0.5
                for n in range(10):
                    rate(5)
                    w1.pos.z=w1.pos.z-0.5
                    w2.pos.z=w2.pos.z-0.5
                    w4.pos.z=w4.pos.z-0.5
                    w3.pos.z=w3.pos.z-0.5
                    body.pos.z=body.pos.z-0.5
                break
    w1.visible=False
    w2.visible=False
    w3.visible=False
    w4.visible=False
    body.visible=False
    wall.visible=False
    platform1.visible=False
    platform2.visible=False
    platform3.visible=False
    platform4.visible=False
    print("Do you want to continue? Press 1 if yes else press 0")
    fl=int(input())
    flag=fl
