GlowScript 3.0 VPython
ground=box(pos=vector(0,0,0),size=vector(200,200,1),color=color.green)
bline1=box(pos=vector(0,-100,1),size=vector(200,1,1),color=color.red)
bline2=box(pos=vector(100,0,1),size=vector(1,200,1),color=color.red)
bline3=box(pos=vector(-100,0,1),size=vector(1,200,1),color=color.red)
bline4=box(pos=vector(0,100,1),size=vector(200,1,1),color=color.red)
ptch=box(pos=vector(0,0,0),size=vector(15,40,2),color=color.white)
s11=arrow(pos=vector(-1,-20,1),color=color.black,axis=vector(0,0,3))
s12=arrow(pos=vector(0,-20,1),color=color.black,axis=vector(0,0,3))
s13=arrow(pos=vector(1,-20,1),color=color.black,axis=vector(0,0,3))
s21=arrow(pos=vector(-1,20,1),color=color.black,axis=vector(0,0,3))
s22=arrow(pos=vector(0,20,1),color=color.black,axis=vector(0,0,3))
s23=arrow(pos=vector(1,20,1),color=color.black,axis=vector(0,0,3))
striker=arrow(pos=vector(0,18,1),color=color.yellow,axis=vector(0,0,5))
nonstriker=arrow(pos=vector(5,-18,1),color=color.yellow,axis=vector(0,0,5))
bowler=arrow(pos=vector(-1,-18,1),color=color.blue,axis=vector(0,0,5))
keeper=arrow(pos=vector(-3,30,1),color=color.blue,axis=vector(0,0,5))
slip1=arrow(pos=vector(-6,33,1),color=color.blue,axis=vector(0,0,5))
extracoverf=arrow(pos=vector(-85,-70,1),color=color.blue,axis=vector(0,0,5))
coverf=arrow(pos=vector(-45,-10,1),color=color.blue,axis=vector(0,0,5))
longonf=arrow(pos=vector(-30,-90,1),color=color.blue,axis=vector(0,0,5))
longofff=arrow(pos=vector(30,-90,1),color=color.blue,axis=vector(0,0,5))
legf=arrow(pos=vector(45,-10,1),color=color.blue,axis=vector(0,0,5))
thirdmanf=arrow(pos=vector(-90,90,1),color=color.blue,axis=vector(0,0,5))
leggf=arrow(pos=vector(10,85,1),color=color.blue,axis=vector(0,0,5))
gullyf=arrow(pos=vector(-35,15,1),color=color.blue,axis=vector(0,0,5))
umpire=arrow(pos=vector(0,-22,1),color=color.red,axis=vector(0,0,5))
batcrease=box(pos=vector(0,17,0),color=color.black,size=vector(15,0.3,2))
bowlcrease=box(pos=vector(0,-17,0),color=color.black,size=vector(15,0.3,2))
wide1=box(pos=vector(-5,18.5,0),color=color.black,size=vector(0.3,3,2))
wide2=box(pos=vector(5,18.5,0),color=color.black,size=vector(0.3,3,2))
ball=sphere(pos=vector(-1,-18,4),color=color.cyan,radius=0.5)
while True:
    rate(10)
    k=keysdown()
    scene.camera.follow(ball)
    if 'home' in k:
        for i in range(17):
            rate(10)
            ball.pos.y=ball.pos.y+1
            ball.pos.z=ball.pos.z+0.5 
        for j in range(18):
            rate(10)
            ball.pos.y=ball.pos.y+1
            ball.pos.z=ball.pos.z-0.5
    if 'down' in k:
        if(ball.pos.y>=16 and ball.pos.y<=18):
            for ii in range(60):
                rate(10)
                ball.pos.y=ball.pos.y-1
                ball.pos.z=ball.pos.z+1
                longonf.pos.x=longonf.pos.x+0.2
            for jj in range(62):
                rate(10)
                ball.pos.y=ball.pos.y-1
                ball.pos.z=ball.pos.z-1
                longonf.pos.x=longonf.pos.x+0.2
            t = text(text='That is a huge six', align='center', color=color.red,height=10,depth=5)
        break
    if 'left' in k:
        if(ball.pos.y>=16 and ball.pos.y<=18):
            for ii in range(50):
                rate(10)
                ball.pos.x=ball.pos.x-1
                ball.pos.z=ball.pos.z+1
                extracoverf.pos.y=extracoverf.pos.y+0.8
            for jj in range(52):
                rate(10)
                ball.pos.x=ball.pos.x-1
                ball.pos.z=ball.pos.z-1
                extracoverf.pos.y=extracoverf.pos.y+0.8
            t = text(text='That is a huge six', align='center', color=color.red,height=10,depth=5)
        break
    if 'right' in k:
        if(ball.pos.y>=16 and ball.pos.y<=18):
            for ii in range(50):
                rate(10)
                ball.pos.x=ball.pos.x+1
                ball.pos.z=ball.pos.z+1
                legf.pos.x=legf.pos.x+0.5
            for jj in range(52):
                rate(10)
                ball.pos.x=ball.pos.x+1
                ball.pos.z=ball.pos.z-1
                legf.pos.x=legf.pos.x+0.5
            t = text(text='That is a huge six', align='center', color=color.red,height=10,depth=5)
        break
    if 'up' in k:
        for ii in range(2):
            rate(10)
            ball.pos.y=ball.pos.y+1
            ball.pos.z=ball.pos.z-0.5
        for jj in range(5):
            rate(10)
            s21.pos.y=s21.pos.y+0.4
            s21.axis=vector(0,3,0)
        t = text(text='Well bowled...!!!...Sticks off', align='center', color=color.red,height=10,depth=5)
        break
            
