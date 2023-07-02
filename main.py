usern = input("请告诉我你的名字: >>> ")
import pgzrun,pygame,win32
from random import randint,choice
from win32 import win32api, win32gui, win32print
from win32.lib import win32con
from win32.win32api import GetSystemMetrics
def get_real_resolution():
    hDC = win32gui.GetDC(0)
    # 横向分辨率
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    # 纵向分辨率
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h
pcwidth,pcheight = get_real_resolution()
"""IMPORTANT: Size of the game"""
WIDTH = 700
HEIGHT = 390
"""Up here"""
WIDT = WIDTH
HEIGH = HEIGHT
"""Under Here we process the scores and top10"""
times = 0
maxscore = 666
aw =  WIDT - WIDTH
ah = HEIGH - HEIGHT
# read and show top.10
top10score = open("ts", mode="r", encoding="utf-8")
t1stf = open("tts",mode = 'r',encoding='utf-8')
top10player = open("tp", mode="r", encoding="utf-8")
t1ptf = open("ttp",mode = 'r',encoding='utf-8')
tpp = open("tbp",mode = 'r',encoding='utf-8')
tps = open("tbs",mode='r',encoding="utf-8")
t1s = top10score.readline().split("ɞ")
t1st = t1stf.readline().split('ɞ')
t1p = top10player.readline().split("ɞ")
t1pt = t1ptf.readline().split('ɞ')
tppb = tpp.readline().split('ɞ')
tpsb = tps.readline().split('ɞ')
tip = open('tip',mode = 'r',encoding = 'utf-8')
tis = open("tis",mode='r',encoding="utf-8")
tii = tip.readline().split('ɞ')
tss = tis.readline().split('ɞ')
print("---------------------------------------------------------")
print("榜上前九:(正常模式中) ")
for num in range(0, 9):
    if num + 1 == 1:
        pl = '1st'
    elif num + 1 == 2:
        pl = '2nd'
    elif num + 1 == 3:
         pl = '3rd'
    else:
        pl = '%sth' % (num + 1)
    print("%s. %s  by  %s" % (pl, t1s[num], t1p[num]))
print()
print("榜上前九:(传送模式中)")
for num in range(0, 9):
    if num + 1 == 1:
        pl = '1st'
    elif num + 1 == 2:
        pl = '2nd'
    elif num + 1 == 3:
        pl = '3rd'
    else:
        pl = '%sth' % (num + 1)
    print("%s. %s  by  %s" % (pl, t1st[num], t1pt[num]))
print()
print("榜上前九:(奇怪模式中)")
for num in range(0, 9):
    if num + 1 == 1:
        pl = '1st'
    elif num + 1 == 2:
        pl = '2nd'
    elif num + 1 == 3:
        pl = '3rd'
    else:
        pl = '%sth' % (num + 1)
    print("%s. %s  by  %s" % (pl, tpsb[num], tppb[num]))
print("---------------------------------------------------------")
print()
print("榜上前九:(计时模式中)")
for num in range(0, 9):
    if num + 1 == 1:
        pl = '1st'
    elif num + 1 == 2:
        pl = '2nd'
    elif num + 1 == 3:
        pl = '3rd'
    else:
        pl = '%sth' % (num + 1)
    print("%s. %s  by  %s" % (pl, tss[num], tii[num]))
print("---------------------------------------------------------")
"""UP HERE"""
gotime = 0
naton = 0
ct = 0
ppp = 0
got = 0
state = -1
mine = True
lock = False
lives = 1
gamemode = -1
et = 0
st = 0
gs = 0
gs1 = 0
mapn = -1
score = 0
sp_m = 3
sp_c = 2
sp_b = 2.1
sp_bat = 1.0
title = Actor("title.png")
title.x,title.y = 350,80
wm = Actor("welcome.png")
wm.x = 350
wm.y = 260
start = Actor("start.png")
start.x = 340
start.y = 190
selectMode = Actor("selectmode")
selectMode.x,selectMode.y = -1000,-2000
normal = Actor("normal")
transit = Actor("transit")
bizarre = Actor("bizarre")
normal.x,normal.y = -1000,-1000
transit.x,transit.y = -1000,-1000
bizarre.x,bizarre.y = -1000,-1000
cheese = Actor("cheese")
cheese.x = -500
cheese.y = -500
ball1 = Actor("ball")
ball1.x,ball1.y = -50,-50
ball2 = Actor("ball")
ball2.x,ball2.y = -50,-50
gameover = Actor("gameover")
gameover.x,gameover.y = -1600,-1600
bat = Actor("bat")
bat.x,bat.y = -100,-100
trap = Actor("trap")
trap.x,trap.y = -123,-213
vac = Actor("vac")
vac.x,vac.y = -233,-322
te = Actor("te")
te.x,te.y = 695,385
home = Actor("home")
home.x,home.y = -350,-260
nat = Actor("nat")
nat.x,nat.y = -333,-333
falsecheese = Actor("cheese2")
fc = falsecheese
fc.x,fc.y = -123,-321
warn = Actor("oh")
warn.x,warn.y = -100,-100
tme = Actor("timern")
tme.x,tme.y = -655,-370
# under here is initing
diet = 60*100
ntt = 10
tisc = 0
nnnnn = 0
playt = 0
stayt = 0
timer = 0
tm = False
direction = ''
dc = ''
db1 = ''
db2 = ''
dbat = 's'
diss = ['w','a','s','d']
dc = choice(diss)
db1 = choice(diss)
db2 = choice(diss)
m0 = Actor('lr')
m1 = Actor('lr')
m2 = Actor('lr')
m3 = Actor('lr')
m4 = Actor('lr')
m5 = Actor('lr')
m6 = Actor('lr')
m7 = Actor('lr')
m8 = Actor('lr')
m9 = Actor('lr')
l = Actor('lr')
l.x,l.y = -1,HEIGHT//2
r = Actor('lr')
r.x,r.y = 699,HEIGHT//2
t = Actor('tb')
t.x,t.y = WIDTH//2,0
b = Actor('tb')
b.x,b.y = WIDTH//2,389
def changeplace(s):
    global HEIGH,WIDT,nnnnn,aw,ah
    if s == 1:
        nnnnn = 1
        WIDT = (pcwidth - WIDTH) // 2 + WIDTH
        HEIGH = (pcheight - HEIGHT) // 2 + HEIGHT
        l.x += (pcwidth - WIDTH) // 2
        r.x += (pcwidth - WIDTH) // 2
        b.x += (pcwidth - WIDTH) // 2
        t.x += (pcwidth - WIDTH) // 2
        ball1.x += (pcwidth - WIDTH) // 2
        ball2.x += (pcwidth - WIDTH) // 2
        cheese.x += (pcwidth - WIDTH) // 2
        home.x += (pcwidth - WIDTH) // 2
        wm.x += (pcwidth - WIDTH) // 2
        nat.x += (pcwidth - WIDTH) // 2
        vac.x += (pcwidth - WIDTH) // 2
        m1.x += (pcwidth - WIDTH) // 2
        m2.x += (pcwidth - WIDTH) // 2
        m3.x += (pcwidth - WIDTH) // 2
        m4.x += (pcwidth - WIDTH) // 2
        m5.x += (pcwidth - WIDTH) // 2
        m6.x += (pcwidth - WIDTH) // 2
        m7.x += (pcwidth - WIDTH) // 2
        m8.x += (pcwidth - WIDTH) // 2
        m9.x += (pcwidth - WIDTH) // 2
        m0.x += (pcwidth - WIDTH) // 2
        trap.x += (pcwidth - WIDTH) // 2
        bat.x += (pcwidth - WIDTH) // 2

        l.y += (pcheight-HEIGHT)//2
        r.y+= (pcheight-HEIGHT)//2
        b.y+= (pcheight-HEIGHT)//2
        t.y+= (pcheight-HEIGHT)//2
        ball1.y+= (pcheight-HEIGHT)//2
        ball2.y+= (pcheight-HEIGHT)//2
        cheese.y+= (pcheight-HEIGHT)//2
        home.y+= (pcheight-HEIGHT)//2
        wm.y+= (pcheight-HEIGHT)//2
        nat.y+= (pcheight-HEIGHT)//2
        vac.y+= (pcheight-HEIGHT)//2
        m1.y+=(pcheight-HEIGHT)//2
        m2.y+= (pcheight-HEIGHT)//2
        m3.y+= (pcheight-HEIGHT)//2
        m4.y+= (pcheight-HEIGHT)//2
        m5.y+= (pcheight-HEIGHT)//2
        m6.y+= (pcheight-HEIGHT)//2
        m7.y+= (pcheight-HEIGHT)//2
        m8.y+= (pcheight-HEIGHT)//2
        m9.y+= (pcheight-HEIGHT)//2
        m0.y += (pcheight - HEIGHT) // 2
        trap.y+= (pcheight-HEIGHT)//2
        bat.y+= (pcheight-HEIGHT)//2
    if s == 2:
        nnnnn = 0
        WIDT = WIDTH
        HEIGH = HEIGHT
        l.x -= (pcwidth - WIDTH) // 2
        r.x -= (pcwidth - WIDTH) // 2
        b.x -= (pcwidth - WIDTH) // 2
        t.x -= (pcwidth - WIDTH) // 2
        ball1.x -= (pcwidth - WIDTH) // 2
        ball2.x -= (pcwidth - WIDTH) // 2
        cheese.x -= (pcwidth - WIDTH) // 2
        home.x -= (pcwidth - WIDTH) // 2
        wm.x -= (pcwidth - WIDTH) // 2
        nat.x -= (pcwidth - WIDTH) // 2
        vac.x -= (pcwidth - WIDTH) // 2
        m1.x -= (pcwidth - WIDTH) // 2
        m2.x -= (pcwidth - WIDTH) // 2
        m3.x -= (pcwidth - WIDTH) // 2
        m4.x -= (pcwidth - WIDTH) // 2
        m5.x -= (pcwidth - WIDTH) // 2
        m6.x -= (pcwidth - WIDTH) // 2
        m7.x -= (pcwidth - WIDTH) // 2
        m8.x -= (pcwidth - WIDTH) // 2
        m9.x -= (pcwidth - WIDTH) // 2
        m0.x -= (pcwidth - WIDTH) // 2
        trap.x -= (pcwidth - WIDTH) // 2
        bat.x -= (pcwidth - WIDTH) // 2

        l.y -= (pcheight - HEIGHT) // 2
        r.y -= (pcheight - HEIGHT) // 2
        b.y -= (pcheight - HEIGHT) // 2
        t.y -= (pcheight - HEIGHT) // 2
        ball1.y -= (pcheight - HEIGHT) // 2
        ball2.y -= (pcheight - HEIGHT) // 2
        cheese.y -= (pcheight - HEIGHT) // 2
        home.y -= (pcheight - HEIGHT) // 2
        wm.y -= (pcheight - HEIGHT) // 2
        nat.y -= (pcheight - HEIGHT) // 2
        vac.y -= (pcheight - HEIGHT)// 2
        m1.y -= (pcheight - HEIGHT) // 2
        m2.y -= (pcheight - HEIGHT) // 2
        m3.y -= (pcheight - HEIGHT) // 2
        m4.y -= (pcheight - HEIGHT) // 2
        m5.y -= (pcheight - HEIGHT) // 2
        m6.y -= (pcheight - HEIGHT) // 2
        m7.y -= (pcheight - HEIGHT) // 2
        m8.y -= (pcheight - HEIGHT) // 2
        m9.y -= (pcheight - HEIGHT) // 2
        m0.y -= (pcheight - HEIGHT) // 2
        trap.y -= (pcheight - HEIGHT) // 2
        bat.y -= (pcheight - HEIGHT) // 2
    aw = WIDT - WIDTH
    ah = HEIGH - HEIGHT
def thanks():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("致谢人名单：\n"
          "首席工程师：周东宜\n"
          "游戏想法框架：朱航（老鼠吃奶酪）\n"
          "实测人员：周东宜  朱航  杨辰宇\n"
          "评测人员：朱航  熊杨  李杨奥珊  杨辰宇  夏诚博  陆勤睿\n"
          "想法提供（非我原创）：\n"
          "  朱航：正常模式撞墙，奶酪会跑，加入配乐，白色地图，配乐El Dorado\n"
          "  熊杨：传送模式撞墙，捕鼠夹（现防疫卡口）\n"
          "  潘天乐：迷惑外卖\n"
          "  陈君禾：家的想法和功能\n"
          "  李杨奥珊：（未采纳）猫吃鱼加速\n"
          "  杨辰宇：（未采纳）奖励时间\n"
          "其中，朱航予以部分流程指导和精神支持，熊杨予以极大精神支持，\n"
          "夏诚博对本项目十分关注，提出要测试“特性”，但没有实现。\n"
          "我，朱航，熊杨三人共同提出游戏模式的选择。")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def sMode():
    global diet
    gameover.x, gameover.y = -1600 + aw, -1600 + ah
    animate(title,pos=(title.x, -128))
    animate(start,pos=(start.x, -128))
    animate(selectMode,duration=1.2,pos=(350 + aw,90 + ah))
    animate(normal,duration=1.2,pos=(330 + aw,190 + ah))
    animate(transit,duration=1.2,pos=(400 + aw,300 + ah))
    animate(bizarre,duration=1.2,pos=(280 + aw,245 + ah))
    if tm:
        diet = 6660
    tme.x,tme.y = 655 + aw,370 + ah
def drawmap():
    global m0, m1, m2, m3, m4, m5, m6, m7, m8,m9,mapn,WIDT,HEIGH
    b = randint(0,9)
    if 0 <= b and b < 4:
        mapn = 0
    elif 4 <= b and b < 7:
        mapn = 1
    elif 7 <= b and b < 9:
        mapn = 2
    elif b == 9:
        mapn = 3
    m0 = Actor('.\\%s\\m0'%(mapn))
    m1 = Actor('.\\%s\\m1'%(mapn))
    m2 = Actor('.\\%s\\m2'%(mapn))
    m3 = Actor('.\\%s\\m3'%(mapn))
    m4 = Actor('.\\%s\\m4'%(mapn))
    m5 = Actor('.\\%s\\m5'%(mapn))
    m6 = Actor('.\\%s\\m6'%(mapn))
    m7 = Actor('.\\%s\\m7'%(mapn))
    m8 = Actor('.\\%s\\m8'%(mapn))
    m9 = Actor('.\\%s\\m9'%(mapn))
    if mapn == 0:
        """
        (pcwidth - WIDTH) // 2 + WIDTH
        """
        m0.x, m0.y = 60 + WIDT - WIDTH, 160 + HEIGH - HEIGHT
        m1.x, m1.y = 60 + WIDT - WIDTH, 40 + HEIGH - HEIGHT
        m2.x, m2.y = 50 + WIDT - WIDTH, 300 + HEIGH - HEIGHT
        m3.x, m3.y = 475 + WIDT - WIDTH, 75 + HEIGH - HEIGHT
        m4.x, m4.y = 550 + WIDT - WIDTH, 120 + HEIGH - HEIGHT
        m5.x, m5.y = 380 + WIDT - WIDTH, 150 + HEIGH - HEIGHT
        m6.x, m6.y = 430 + WIDT - WIDTH, 175 + HEIGH - HEIGHT
        m7.x, m7.y = 610 + WIDT - WIDTH, 345 + HEIGH - HEIGHT
        m8.x, m8.y = 670 + WIDT - WIDTH, 80 + HEIGH - HEIGHT
        m9.x,m9.y = 200 + WIDT - WIDTH,338 + HEIGH - HEIGHT
    if mapn == 1:
        m0.x, m0.y = 75 + WIDT - WIDTH,90 + HEIGH - HEIGHT
        m1.x, m1.y = 90 + WIDT - WIDTH,200 + HEIGH - HEIGHT
        m2.x, m2.y = 180 + WIDT - WIDTH,280 + HEIGH - HEIGHT
        m3.x, m3.y = 240 + WIDT - WIDTH,90 + HEIGH - HEIGHT
        m4.x, m4.y = 300 + WIDT - WIDTH,120 + HEIGH - HEIGHT
        m5.x, m5.y = 520 + WIDT - WIDTH,85 + HEIGH - HEIGHT
        m6.x, m6.y = 360 + WIDT - WIDTH,340 + HEIGH - HEIGHT
        m7.x, m7.y = 605 + WIDT - WIDTH,300 + HEIGH - HEIGHT
        m8.x, m8.y = 461 + WIDT - WIDTH,185 + HEIGH - HEIGHT
        m9.x, m9.y = 469 + WIDT - WIDTH,367 + HEIGH - HEIGHT
    if mapn == 2:
        m0.x, m0.y = 95 + WIDT - WIDTH,55 + HEIGH - HEIGHT
        m1.x, m1.y = 100 + WIDT - WIDTH,200 + HEIGH - HEIGHT
        m2.x, m2.y = 205 + WIDT - WIDTH,300 + HEIGH - HEIGHT
        m3.x, m3.y = 295 + WIDT - WIDTH,100 + HEIGH - HEIGHT
        m4.x, m4.y = 340 + WIDT - WIDTH,200 + HEIGH - HEIGHT
        m5.x, m5.y = 405 + WIDT - WIDTH,335 + HEIGH - HEIGHT
        m6.x, m6.y = 455 + WIDT - WIDTH,175 + HEIGH - HEIGHT
        m7.x, m7.y = 530 + WIDT - WIDTH,63 + HEIGH - HEIGHT
        m8.x, m8.y = 520 + WIDT - WIDTH,363 + HEIGH - HEIGHT
        m9.x, m9.y = 617 + WIDT - WIDTH,275 + HEIGH - HEIGHT
    if mapn == 3:
        m0.x, m0.y =60 + WIDT - WIDTH,140 + HEIGH - HEIGHT
        m1.x, m1.y =145 + WIDT - WIDTH,80 + HEIGH - HEIGHT
        m2.x, m2.y =180 + WIDT - WIDTH,240 + HEIGH - HEIGHT
        m3.x, m3.y = 240 + WIDT - WIDTH,240 + HEIGH - HEIGHT
        m4.x, m4.y = 330 + WIDT - WIDTH,120 + HEIGH - HEIGHT
        m5.x, m5.y = 350 + WIDT - WIDTH,350 + HEIGH - HEIGHT
        m6.x, m6.y = 420 + WIDT - WIDTH,200 + HEIGH - HEIGHT
        m7.x, m7.y = 580 + WIDT - WIDTH,125 + HEIGH - HEIGHT
        m8.x, m8.y = 610 + WIDT - WIDTH,80 + HEIGH - HEIGHT
        m9.x, m9.y = 611 + WIDT - WIDTH,300 + HEIGH - HEIGHT
        sounds.what.play()
def gamo1():
    global gamemode
    gamemode = 1
    animate(normal, pos=(-1000, -1000))
    animate(transit, pos=(-1000, -1000))
    animate(bizarre, pos=(-1000, -1000))
    animate(selectMode, pos=(-1000, -2000))
    stArt()
def gamo2():
    global gamemode
    gamemode = 2
    animate(transit, pos=(-1000, -1000))
    animate(normal, pos=(-1000, -1000))
    animate(bizarre, pos=(-1000, -1000))
    animate(selectMode, pos=(-1000, -2000))
    stArt()
def gamo3():
    global gamemode
    gamemode = 3
    animate(transit, pos=(-1000, -1000))
    animate(normal, pos=(-1000, -1000))
    animate(bizarre, pos=(-1000, -1000))
    animate(selectMode, pos=(-1000, -2000))
    stArt()
def on_mouse_down(pos):
    global tm
    if start.collidepoint(pos):
        sMode()
    if transit.collidepoint(pos):
        gamo2()
    if normal.collidepoint(pos):
        gamo1()
    if bizarre.collidepoint(pos):
        gamo3()
    if te.collidepoint(pos):
        thanks()
    if tme.collidepoint(pos):
        if tm:
            tm = False
            tme.image = 'timern'
        else:
            tm = True
            tme.image = 'timery'
def on_key_down(key):
    global direction,state,nnnnn,pcwidth,pcheight
    if key == keys.RETURN and state == 1:
        sMode()
    if key == keys.W or key == keys.UP:
        direction = 'w'
        wm.angle = 0
    if key == keys.A or key == keys.LEFT:
        direction = 'a'
        wm.angle = 90
    if key == keys.D or key == keys.RIGHT:
        direction = 'd'
        wm.angle = -90
    if key == keys.S or key == keys.DOWN:
        direction = 's'
        wm.angle = 180
    if key == keys.E or key == keys.Q:
        if wm.colliderect(home):
            direction = ''
    if key == keys.U:
        sounds.deads.stop()
        sounds.deads.play()
    if key == keys.I:
        sounds.stop.stop()
        sounds.stop.play()
    if key == keys.L and state == 0:
        if nnnnn == 0:
            screen.surface = pygame.display.set_mode((pcwidth,pcheight), pygame.FULLSCREEN)
            changeplace(1)
        else:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
            changeplace(2)
def on_key_up(key):
    global gamemode,direction
    if gamemode == 1 or gamemode == 2:
        if key == keys.W or key == keys.UP:
            if direction == 'w':
                direction = ''
        if key == keys.A or key == keys.LEFT:
            if direction == 'a':
                direction = ''
        if key == keys.S or key == keys.DOWN:
            if direction == 's':
                direction = ''
        if key == keys.D or key == keys.RIGHT:
            if direction == 'd':
                direction = ''
def stArt():
    global dc,db1,db2,dbat,direction,state,trap,sp_c,sp_b,sp_m,sp_bat,score,maxscore,times,mapn,playt,st,gs,mine,\
        gamemode,lives,gs1,et,vt,got,naton,stayt,ppp,gotime,timer,ntt,tisc
    drawmap()
    sounds.start.play()
    if mapn == 3:
        music.play("m")
    else:
        music.play('m0')
    sounds.dead.stop()
    sounds.cough.stop()
    lives = 1
    ntt = 1
    cheese.image = 'cheese'
    mine = True
    gotime = 0
    ppp = 0
    tisc = 0
    naton = 0
    stayt = 0
    timer = 0
    got = 0
    et = 0
    vt = 0
    st = 0
    gs = 0
    gs1 = 0
    score = 0
    sp_m = 3
    sp_c = 2
    sp_b = 2.1
    sp_bat = 1.0
    playt = 0
    tme.x,tme.y = -100,-100
    nx, ny = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
    while nx in range(int(wm.x) - 16, int(wm.x) + 16) and ny in range(int(wm.y) - 16, int(wm.y) + 16):
        nx, ny = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
    trap.x, trap.y = nx, ny
    while trap.colliderect(m0) or trap.colliderect(m1) or trap.colliderect(m2) or trap.colliderect(
            m3) or trap.colliderect(m4) \
            or trap.colliderect(m5) or trap.colliderect(m6) or trap.colliderect(m7) or trap.colliderect(m8) \
            or trap.colliderect(m9):
        nx, ny = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
        trap.x, trap.y = nx, ny
    state = 0
    bat.x,bat.y = WIDT-650,HEIGH-350
    dbat = 's'
    direction = ''
    # Here we check if balls colliderected wall if so,then it changes another place
    cheese.x, cheese.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
    ball1.x, ball1.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
    ball2.x, ball2.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
    while ball1.colliderect(m0) or ball1.colliderect(m1) or ball1.colliderect(m2) or ball1.colliderect(m3) or ball1.colliderect(m4) \
            or ball1.colliderect(m5) or ball1.colliderect(m6) or ball1.colliderect(m7) or ball1.colliderect(m8)\
            or ball1.colliderect(m9) \
        or ball2.colliderect(m0) or ball2.colliderect(m1) or ball2.colliderect(m2) or ball2.colliderect(m3) or ball2.colliderect(m4) \
        or ball2.colliderect(m5) or ball2.colliderect(m6) or ball2.colliderect(m7) or ball2.colliderect(m8) \
        or ball2.colliderect(m9):
        ball1.x, ball1.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
        ball2.x, ball2.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
    dc,db1,db2 = choice(diss),choice(diss),choice(diss)
    wm.image = "mou1"
    while wm.colliderect(m0) or wm.colliderect(m1) or wm.colliderect(m2) or wm.colliderect(m3) or wm.colliderect(m4) \
            or wm.colliderect(m5) or wm.colliderect(m6) or wm.colliderect(m7) or wm.colliderect(m8) or wm.colliderect(m9):
        wm.x,wm.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
    top10score = open("ts", mode="r", encoding="utf-8")
    t1stf = open("tts",mode = 'r',encoding='utf-8')
    top10player = open("tp", mode="r", encoding="utf-8")
    t1ptf = open("ttp",mode = 'r',encoding='utf-8')
    tpp = open("tbp",mode = 'r',encoding='utf-8')
    tps = open("tbs",mode='r',encoding="utf-8")
    t1s = top10score.readline().split("ɞ")
    t1st = t1stf.readline().split('ɞ')
    t1p = top10player.readline().split("ɞ")
    t1pt = t1ptf.readline().split('ɞ')
    tppb = tpp.readline().split('ɞ')
    tpsb = tps.readline().split('ɞ')
    if gamemode == 1:
        maxscore = t1s[0]
    elif gamemode == 2:
        maxscore = t1st[0]
    elif gamemode == 3:
        maxscore = tpsb[0]
    top10score.close()
    top10player.close()
    t1stf.close()
    t1ptf.close()
    tpp.close()
    tps.close()
    home.x, home.y = wm.x,wm.y
def lunlock():
    global lock
    lock = False
def nomine():
    global mine
    mine = True
def gameOver(why=0):
    global gameover,wm,ball1,ball2,direction,dc,db1,dbat,db2,score,nnnnn,maxscore,stayt,t1s,t1p,t1st,t1pt,\
        tppb,tpsb,tii,tss,usern,mapn,state,gamemode,times,lives,tisc
    direction, dc, db1, db2,dbat = '','','','',''
    # animate(cheese,pos = (-160,-160))
    cheese.x,cheese.y = -160,-160
    stayt = 0
    ball1.x,ball1.y,ball2.x,ball2.y = -33,-33,-55,-55
    while bat.x != -100 and bat.y != -100:
        bat.x,bat.y = -100,-100
    music.stop()
    sounds.dead.stop()
    sounds.cough.stop()
    if nnnnn == 1:
        gameover.x, gameover.y = pcwidth//2,pcheight//2
    elif nnnnn == 0:
        gameover.x, gameover.y = WIDTH // 2, HEIGHT // 2
    nat.x, nat.y = -333, -333
    home.x,home.y = -1233,-3211
    if why == 9:
        wm.image = 'tk'
        gameover.image = 'gm4'
    elif why == 1:
        wm.image = 'die2'
        gameover.image = 'go2'
        sounds.dead.play()
    elif why == 0:
        wm.image = 'die'
        gameover.image = 'gameover'
        sounds.cough.play()
    elif why == 2:
        wm.image = 'die2'
        gameover.image = 'g3'
        sounds.deadl.play()
    elif why == 7:
        wm.image = 'die2'
        gameover.image = 'go2'
        sounds.deads.play()
    elif why == 3:
        wm.image = "die2"
        gameover.image="gm3"
        sounds.deadl.play()

    trap.x,trap.y = -33,111
    bat.x,bat.y = -100,-100
    vac.x,vac.y = -233,-322
    # find if you made a record
    if gamemode == 1:
        if not tm:
            for i in range(9):
                if score > int(t1s[i]):
                    t1s.insert(i,t1s[i-1])
                    t1s[i] = str(score)
                    t1s = t1s[0:10]
                    t1p.insert(i,t1p[i-1])
                    if mapn == 3:
                        t1p[i] = str(usern) + " At StrangeMap3"
                    else:
                        t1p[i] = str(usern) + " 在正常模式"
                    t1p = t1p[0:10]
                    break
            top10playe = open("tp", mode='w', encoding="utf-8")
            top10scor = open("ts", mode="w", encoding="utf-8")
            top10scor.write("ɞ".join(t1s))
            top10playe.write("ɞ".join(t1p))
            top10playe.close()
            top10scor.close()
        else:
            for i in range(9):
                if tisc > int(tss[i]):
                    tss.insert(i,tss[i-1])
                    tss[i] = str(int(tisc))
                    tss = tss[0:10]
                    tii.insert(i,tii[i-1])
                    if mapn == 3:
                        tii[i] = str(usern) + " At StrangeMap3"
                    else:
                        tii[i] = str(usern) + " 在正常模式"
                    tii = tii[0:10]
                    break
            top10playe = open("tip", mode='w', encoding="utf-8")
            top10scor = open("tis", mode="w", encoding="utf-8")
            top10scor.write("ɞ".join(tss))
            top10playe.write("ɞ".join(tii))
            top10playe.close()
            top10scor.close()
    if gamemode == 2:
        if not tm:
            for i in range(9):
                if score > int(t1st[i]):
                    t1st.insert(i,t1st[i-1])
                    t1st[i] = str(score)
                    t1st = t1st[0:10]
                    t1pt.insert(i,t1pt[i-1])
                    if mapn == 3:
                        t1pt[i] = str(usern) + " At StrangeMap3"
                    else:
                        t1pt[i] = str(usern) + " 在传送模式"
                    t1pt = t1pt[0:10]
                    break
            top10playe = open("ttp", mode='w', encoding="utf-8")
            top10scor = open("tts", mode="w", encoding="utf-8")
            top10scor.write("ɞ".join(t1st))
            top10playe.write("ɞ".join(t1pt))
            top10playe.close()
            top10scor.close()
        else:
            for i in range(9):
                if tisc > int(tss[i]):
                    tss.insert(i,tss[i-1])
                    tss[i] = str(int(tisc))
                    tss = tss[0:10]
                    tii.insert(i,tii[i-1])
                    if mapn == 3:
                        tii[i] = str(usern) + " At StrangeMap3"
                    else:
                        tii[i] = str(usern) + " 在传送模式"
                    tii = tii[0:10]
                    break
            top10playe = open("tip", mode='w', encoding="utf-8")
            top10scor = open("tis", mode="w", encoding="utf-8")
            top10scor.write("ɞ".join(tss))
            top10playe.write("ɞ".join(tii))
            top10playe.close()
            top10scor.close()
    if gamemode == 3:
        if not tm:
            for i in range(9):
                if score > int(tpsb[i]):
                    tpsb.insert(i,tpsb[i-1])
                    tpsb[i] = str(score)
                    tpsb = tpsb[0:10]
                    tppb.insert(i,tppb[i-1])
                    if mapn == 3:
                        tppb[i] = str(usern) + " At StrangeMap3"
                    else:
                        tppb[i] = str(usern) + " 在奇怪模式"
                    tppb = tppb[0:10]
                    break
            top10playe = open("tbp", mode='w', encoding="utf-8")
            top10scor = open("tbs", mode="w", encoding="utf-8")
            top10scor.write("ɞ".join(tpsb))
            top10playe.write("ɞ".join(tppb))
            top10playe.close()
            top10scor.close()
        else:
            for i in range(9):
                if tisc > int(tss[i]):
                    tss.insert(i, tss[i - 1])
                    tss[i] = str(int(tisc))
                    tss = tss[0:10]
                    tii.insert(i, tii[i - 1])
                    if mapn == 3:
                        tii[i] = str(usern) + " At StrangeMap3"
                    else:
                        tii[i] = str(usern) + " 在奇怪模式"
                    tii = tii[0:10]
                    break
            top10playe = open("tip", mode='w', encoding="utf-8")
            top10scor = open("tis", mode="w", encoding="utf-8")
            top10scor.write("ɞ".join(tss))
            top10playe.write("ɞ".join(tii))
            top10playe.close()
            top10scor.close()
    times += 1
    if times != 0:
        """Under Here we process the scores and top9"""
        # read and show top.10
        top10score = open("ts", mode="r", encoding="utf-8")
        t1stf = open("tts", mode='r', encoding='utf-8')
        top10player = open("tp", mode="r", encoding="utf-8")
        t1ptf = open("ttp", mode='r', encoding='utf-8')
        tpp = open("tbp", mode='r', encoding='utf-8')
        tps = open("tbs", mode='r', encoding="utf-8")
        t1s = top10score.readline().split("ɞ")
        t1st = t1stf.readline().split('ɞ')
        t1p = top10player.readline().split("ɞ")
        t1pt = t1ptf.readline().split('ɞ')
        tppb = tpp.readline().split('ɞ')
        tpsb = tps.readline().split('ɞ')
        tip = open('tip', mode='r', encoding='utf-8')
        tis = open("tis", mode='r', encoding="utf-8")
        tii = tip.readline().split('ɞ')
        tss = tis.readline().split('ɞ')
        print("---------------------------------------------------------")
        print("榜上前九:(正常模式中)")
        for num in range(0, 9):
            if num + 1 == 1:
                pl = '1st'
            elif num + 1 == 2:
                pl = '2nd'
            elif num + 1 == 3:
                pl = '3rd'
            else:
                pl = '%sth' % (num + 1)
            print("%s. %s  by  %s" % (pl, t1s[num], t1p[num]))
        print()
        print("榜上前九:(传送模式中)")
        for num in range(0, 9):
            if num + 1 == 1:
                pl = '1st'
            elif num + 1 == 2:
                pl = '2nd'
            elif num + 1 == 3:
                pl = '3rd'
            else:
                pl = '%sth' % (num + 1)
            print("%s. %s  by  %s" % (pl, t1st[num], t1pt[num]))
        print()
        print("榜上前九:(奇怪模式中)")
        for num in range(0, 9):
            if num + 1 == 1:
                pl = '1st'
            elif num + 1 == 2:
                pl = '2nd'
            elif num + 1 == 3:
                pl = '3rd'
            else:
                pl = '%sth' % (num + 1)
            print("%s. %s  by  %s" % (pl, tpsb[num], tppb[num]))
        print("---------------------------------------------------------")
        print()
        print("榜上前九:(计时模式中)")
        for num in range(0, 9):
            if num + 1 == 1:
                pl = '1st'
            elif num + 1 == 2:
                pl = '2nd'
            elif num + 1 == 3:
                pl = '3rd'
            else:
                pl = '%sth' % (num + 1)
            print("%s. %s  by  %s" % (pl, tss[num], tii[num]))
        print("---------------------------------------------------------")
        top10score.close()
        top10player.close()
        t1stf.close()
        t1ptf.close()
        tpp.close()
        tps.close()
        tip.close()
        tis.close()
        print("")
def donat():
    global naton
    if naton >= 15:
        naton = 0
        sounds.enhen.play()
        cheese.x, cheese.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
        nat.x,nat.y = -100,-100
    else:
        pass
def update():
    global direction,dc,diss,db1,db2,wm,top,left,right,bot,m0, m1, m2, m3, m4, m5,\
        m6, m7, m8,m9,score,sp_m,sp_c,sp_b,sp_bat,ball2,ball1,trap,dbat,playt,et,mapn,\
        st,gs,gamemode,et,lives,gs1,lock,vt,mine,mines,got,naton,stayt,ppp,gotime,timer,\
        diet,ntt,tisc,state
    if tm and state == 0:
        if not wm.colliderect(cheese):
            ntt += 1
        timer += 1
        tisc += 0.1
    if timer >= diet and state == 0:
        state = 1
        gameOver(why=9)
    if state == 1:
        wm.angle+=1
    if stayt >= 726:
        if not tm:
            state = 1
            gameOver(why=3)
        else:
            state = 1
            gameOver(why=9)
    # Do nat
    if nat.colliderect(wm):
        donat()
    # When Touched cheese
    if wm.colliderect(cheese):
        tisc += 4800 // ntt
        ntt = 1
        if not wm.colliderect(home):
            stayt = 0
        if mine:
            if sp_c < 3.2:
                sp_c += 0.05
                sp_b += 0.03
                sp_m += 0.01
                sp_bat += 0.01
            got += 2
            gs += 2
            gs1 += 2
            naton += 2
            if naton <= 15:
                cheese.x, cheese.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
            else:
                sounds.nope.play()
                nat.x, nat.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
                cheese.x, cheese.y = -100,-100
            et = 1
            sounds.pick.play()
            dc = choice(diss)
            mines = randint(0, 5)
        if naton <= 15:
            if mines < 2:
                mine = False
            else:
                mine = True
    if wm.colliderect(falsecheese) and falsecheese.image == 'cheese2':
        if not tm:
            state = 1
            gameOver(why=2)
        else:
            state = 1
            gameOver(why=9)
    # Bring them back home
    if wm.colliderect(home):
        score += got
        stayt += 1
        if got != 0:
            sounds.bb.play()
        got = 0
    # When touched wm
    if ball1.colliderect(wm) or ball2.colliderect(wm):
        if not wm.colliderect(home):
            if direction == 's':
                direction = 'w'
                wm.y -= sp_b * 1.4
            elif direction == 'd':
                direction = 'a'
                wm.x -= sp_b * 1.4
            elif direction == 'w':
                direction = 's'
                wm.y += sp_b * 1.4
            elif direction == 'a':
                direction = 'd'
                wm.x += sp_b * 1.4
            if not lock:
                lives -= 1
                db1,db2 = choice(diss),choice(diss)
                vt -= 1
                sounds.min.play()
                clock.schedule(lunlock,1.5)
        else:
            sounds.stop.stop()
            sounds.stop.play()
            # db1,db2 = choice(diss),choice(diss)
            if ball1.colliderect(wm):
                ball1.x,ball1.y = randint(50,650),randint(50,340)
            elif ball2.colliderect(wm):
                ball2.x, ball2.y = randint(50, 650), randint(50, 340)
    if trap.colliderect(wm):
        if state == 0:
            if not tm:
                state = 1
                gameOver(why=1)
            else:
                state = 1
                gameOver(why=9)
    if wm.colliderect(bat):
        if state == 0:
            if not tm:
                state = 1
                gameOver(why=7)
            else:
                state = 1
                gameOver(why=9)
    if lives <= 0 and state != 1:
        if not tm:
            state = 1
            gameOver()
        else:
            state = 1
            gameOver(why=9)
    if wm.colliderect(vac) and lives <= 3:
        lives += 1
        sounds.get.play()
        vac.x,vac.y = -222,-222
        vt += 1
    # cat who likes to eat cheese
    if ball2.colliderect(cheese) or ball1.colliderect(cheese):
        if et == 1 and (score - 2) > 0:
            yn = randint(0,7)
            if yn == 1 or yn == 2 or yn == 3 or yn == 6:
                cheese.x, cheese.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
                score -= 1
                sounds.yummy.play()
                et = 0
            et = 0
        else:
            pass
    # Just get some vaccines!
    if gs1 == 12:
        if vt < 3:
            vac.x,vac.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
        gs1 = 0
    # Go somewhere
    if direction == 'w' and wm.top > HEIGH - 390 and state != 1 and state != -1:
        wm.y -= sp_m
    if direction == 'a' and wm.left > WIDT-700 and state != 1 and state != -1:
        wm.x -= sp_m
    if direction == 'd' and wm.right < WIDT and state != 1 and state != -1:
        wm.x += sp_m
    if direction == 's' and wm.bottom < HEIGH and state != 1 and state != -1:
        wm.y += sp_m
    #bat moving
    if dbat == 's':
        if bat.colliderect(b):
            dbat = 'd'
        bat.y += sp_bat
    elif dbat == 'w':
        if bat.colliderect(t):
            dbat = 'a'
        bat.y -= sp_bat
    elif dbat == 'a':
        if bat.colliderect(l):
            dbat = 's'
        bat.x -= sp_bat
    elif dbat == 'd':
        if bat.colliderect(r):
            dbat = 'w'
        bat.x += sp_bat
    #cheese moving
    if mine:
        cheese.image = 'cheese'
        if dc == 'w' and cheese.top > 0:
            cheese.y -= sp_c * 1.1
        if dc == 'a' and cheese.left >0:
            cheese.x -= sp_c * 1.1
        if dc == 'd' and cheese.right < WIDT:
            cheese.x += sp_c * 1.1
        if dc == 's' and cheese.bottom < HEIGH:
            cheese.y += sp_c * 1.1
    else:
        if gotime == 0:
            falsecheese.x,falsecheese.y = cheese.x,cheese.y
            gotime = 1
        cheese.x,cheese.y = -100,-100
        if nnnnn == 1:
            warn.x,warn.y = pcwidth//2,pcheight//2
        elif nnnnn == 0:
            warn.x,warn.y = WIDTH//2,HEIGHT//2
        animate(falsecheese,tween='linear',duration=1.4,pos=(int(trap.x),int(trap.y)))
        # What's this?
        if int(falsecheese.x) in list(range(int(trap.x) - 20, int(trap.x) + 20)) and int(falsecheese.y) in list(
                range(int(trap.y) - 15, int(trap.y) + 15)) and not mine:
            mine = True
            sounds.en.play()
            if gotime == 1:
                if state == 0:
                    cheese.x, cheese.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
                gotime = 0
    if falsecheese.x == trap.x and falsecheese.y == trap.y:
        falsecheese.x,falsecheese.y = -100,-100
        warn.x,warn.y = -100,-100
    #ball moving
    if db1 == 'w' and ball1.top > 0:
        ball1.y -= sp_c
    if db1 == 'a' and ball1.left >0:
        ball1.x -= sp_c
    if db1 == 'd' and ball1.right < WIDT:
        ball1.x += sp_c
    if db1 == 's' and ball1.bottom < HEIGH:
        ball1.y += sp_c
    if db2 == 'w' and ball2.top > 0:
        ball2.y -= sp_c
    if db2 == 'a' and ball2.left >0:
        ball2.x -= sp_c
    if db2 == 'd' and ball2.right < WIDT:
        ball2.x += sp_c
    if db2 == 's' and ball2.bottom < HEIGH:
        ball2.y += sp_c
    # When Meet Walls
    if wm.colliderect(m0) or wm.colliderect(m1) or wm.colliderect(m2) or wm.colliderect(m3) or wm.colliderect(m4) \
            or wm.colliderect(m5) or wm.colliderect(m6) or wm.colliderect(m7) or wm.colliderect(m8) or wm.colliderect(m9):
        if gamemode == 1:
            if direction == 's':
                direction = 'w'
                wm.y -= sp_m * 1.25
            elif direction == 'd':
                direction = 'a'
                wm.x -= sp_m * 1.25
            elif direction == 'w':
                direction = 's'
                wm.y += sp_m * 1.25
            elif direction == 'a':
                direction = 'd'
                wm.x += sp_m * 1.25
        if gamemode == 2:
            wm.x,wm.y = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
        if gamemode == 3:
            if direction == 's':
                direction = choice(diss)
                wm.y -= sp_m * 1.25
            elif direction == 'd':
                direction = choice(diss)
                wm.x -= sp_m * 1.25
            elif direction == 'w':
                direction = choice(diss)
                wm.y += sp_m * 1.25
            elif direction == 'a':
                direction = choice(diss)
                wm.x += sp_m * 1.25
    # When cheese meets walls
    if dc == 'w' and cheese.angle != 0:
        cheese.angle = 270
    if dc == 'a' and cheese.angle != 90:
        cheese.angle = 0
    if dc == 'd' and cheese.angle != -90:
        cheese.angle = 180
    if dc == 's' and cheese.angle != 180:
        cheese.angle = 90
    if cheese.colliderect(m0) or cheese.colliderect(m1) or cheese.colliderect(m2) or cheese.colliderect(m3) or cheese.colliderect(m4) \
            or cheese.colliderect(m5) or cheese.colliderect(m6) or cheese.colliderect(m7) or cheese.colliderect(m8)\
            or cheese.colliderect(m9) or cheese.colliderect(l) or cheese.colliderect(r) or cheese.colliderect(b) or cheese.colliderect(t):
         if mine:
            if dc == 's':
                cheese.y -= sp_c * 1.4
                dc = choice(diss)
            elif dc == 'd':
                cheese.x -= sp_c * 1.4
                dc = choice(diss)
            elif dc == 'w':
                cheese.y += sp_c * 1.4
                dc = choice(diss)
            elif dc == 'a':
                cheese.x += sp_c * 1.4
                dc = choice(diss)
    # When Ball met walls
    if ball1.colliderect(m0) or ball1.colliderect(m1) or ball1.colliderect(m2) or ball1.colliderect(m3) or ball1.colliderect(m4) \
            or ball1.colliderect(m5) or ball1.colliderect(m6) or ball1.colliderect(m7) or ball1.colliderect(m8)\
            or ball1.colliderect(m9) or ball1.colliderect(l) or ball1.colliderect(r) or ball1.colliderect(b) or ball1.colliderect(t) \
        or ball2.colliderect(m0) or ball2.colliderect(m1) or ball2.colliderect(m2) or ball2.colliderect(
            m3) or ball2.colliderect(m4) \
        or ball2.colliderect(m5) or ball2.colliderect(m6) or ball2.colliderect(m7) or ball2.colliderect(m8) \
        or ball2.colliderect(m9) or ball2.colliderect(l) or ball2.colliderect(r) or ball2.colliderect(
            b) or ball2.colliderect(t):
        if db1 == 's':
            db1 = choice(diss)
            ball1.y -= sp_b * 1.25
        elif db1 == 'd':
            db1 = choice(diss)
            ball1.x -= sp_b * 1.25
        elif db1 == 'w':
            db1 = choice(diss)
            ball1.y += sp_b * 1.25
        elif db1 == 'a':
            db1 = choice(diss)
            ball1.x += sp_b * 1.25
        if db2 == 's':
            db2 = choice(diss)
            ball2.y -= sp_b * 1.25
        elif db2 == 'd':
            db2 = choice(diss)
            ball2.x -= sp_b * 1.25
        elif db2 == 'w':
            db2 = choice(diss)
            ball2.y += sp_b * 1.25
        elif db2 == 'a':
            db2 = choice(diss)
            ball2.x += sp_b * 1.25
    # Trap
    if gs == 10:
        nx,ny = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
        while nx in range(int(wm.x)-16,int(wm.x)+16) and ny in range(int(wm.y)-16,int(wm.y)+16):
            nx, ny = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
        trap.x, trap.y = nx, ny
        while trap.colliderect(m0) or trap.colliderect(m1) or trap.colliderect(m2) or trap.colliderect(
                m3) or trap.colliderect(m4) \
                or trap.colliderect(m5) or trap.colliderect(m6) or trap.colliderect(m7) or trap.colliderect(m8) \
                or trap.colliderect(m9):
            nx, ny = randint(WIDT-650, WIDT), randint(HEIGH-340, HEIGH)
            trap.x, trap.y = nx, ny
        gs = 0
    # Prize
    if score >= 46:
        ppp += 1
    elif score >= 31:
        ppp += 1
    elif score >= 16:
        ppp += 1
    if ppp == 1:
        playt = 1
    elif ppp == 2:
        playt = 2
    elif ppp == 3:
        playt = 3
    if score >= 16 and playt == 1:
        wm.image = 'mous'
        if mapn != 3:
            music.stop()
            music.play('m4')
        sounds.nb.play()
        playt += 1
    elif score >= 31 and playt == 2:
        wm.image = 'mou2'
        if mapn != 3:
            music.stop()
            music.play("m1")
        sounds.nb.play()
        playt += 1
    elif score >= 46 and playt == 3:
        wm.image = 'mou3'
        if mapn != 3:
            music.stop()
            music.play("m2")
        sounds.nb.play()
        playt += 1
def draw():
    global m0, m1, m2, m3, m4, m5, m6, m7, m8,score,ball1,ball2,gameover,maxscore,lives,got,stayt
    screen.fill((0,0,129))
    screen.draw.text('得分: '+str(score),(605,5),fontname='msyh.ttc',fontsize=16)
    screen.draw.text("榜上第一: "+str(maxscore),(595,25),fontname='msyh.ttc',fontsize=16)
    screen.draw.text("命数:"+str(lives),(608,45),fontname='msyh.ttc',fontsize=16)
    screen.draw.text("负载："+str(got),(605,65),fontname='msyh.ttc',fontsize=16)
    screen.draw.text("宅家时间：" + str(stayt//60)+"s", (587, 85), fontname='msyh.ttc', fontsize=16)
    if tm:
        screen.draw.text("计时：" + str(timer//60)+'s', (605,105), fontname='msyh.ttc', fontsize=16)
    title.draw()
    nat.draw()
    home.draw()
    te.draw()
    selectMode.draw()
    transit.draw()
    normal.draw()
    bizarre.draw()
    wm.draw()
    start.draw()
    cheese.draw()
    ball1.draw()
    ball2.draw()
    gameover.draw()
    bat.draw()
    vac.draw()
    trap.draw()
    l.draw()
    r.draw()
    t.draw()
    b.draw()
    m0.draw()
    m1.draw()
    m2.draw()
    m3.draw()
    m4.draw()
    m5.draw()
    m6.draw()
    m7.draw()
    m8.draw()
    m9.draw()
    falsecheese.draw()
    warn.draw()
    tme.draw()
pgzrun.go()
