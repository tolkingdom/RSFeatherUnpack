import cv2
import pyautogui
from random import randint,uniform
import time
import pyscreeze
import math
import numpy 
import datetime
import bezmouse
import os
import tkinter as tk

from pathlib import Path
from PIL import Image

dirname1 = os.path.dirname(os.path.abspath(__file__))
print(dirname1)
os.chdir(dirname1)
login_file = open('login.txt','r')
lines = login_file.read().splitlines()

msglist = ["this takes so long ",
        "i dont know if i like this method :",
        "is anyone at 20mil gold yet? ",
        "hey get on discord ",
        "join the discord ",
        "im on discord ",
        "go on discord so we can talk ",
        "i am making a lot i think ",
        "does anyone know a better way? ",
        "gotta get food soon ",
        "probobly made atleast 1m by now ",
        "do you guys get bored playing all day? ",
        "Ben get on the discord ",
        "late reply but yes ",
        "no not really ",
        "half talking in chat half discord huh xD? ",
        "these feathers dont really sell tho :p ",
        "when do we do another method? ",
        "this is boring... ",
        "i fell like a machine xD ",
        "all i do is grind this all day ",
        "why did i have to lose my job... ",
        "what is the purpose of playing anymore? ",
        "so annoying ",
        "hey get onto discord!!!!! ",
        "GET ON DISCORD ",
        "jeremy diod you make an ironman? ",
        "so we save up money then skill magic? ",
        "wow.... ",
        "i can't beleive you anymore lol ",
        "this is unreal ",
        "you guys are such losers hahahaa ",
        "hahahah wow ",
        "my mic broke ",
        "no my mic broke the other day ",
        "why? ",
        "what do you have to say huh? ",
        "the other day ther was 4 ppl here ",
        "lets go to GE soon? ",
        "yeah when school is back up LOL ",
        "why is Ben not on discord? ",
        "Idk anymore ",
        "hahahahahaaa wtf ",
        "yoooooooo for real? ",
        "I DID IT ",
        "lolololol check what i posted on discord ",
        "whoopdie doo! ",
        "have you seen the movie the machinist? ",
        "whats the plan tomorrow?",
        "idk ",
        "i dont kno "]




#check tooltip under mouse for image
def matchtooltip(image):
    cx,cy = pyautogui.position()
    box = (cx-120,cy-75,240,150)  
    return len(imgmatchscreenall(image,region1=box,threshold=0.9))>0


#human right click
def humanrclick():
    timer=(uniform(0.005,0.015))
    time.sleep((timer/2) - 0.00005)
    pyautogui.mouseDown(button='right')
    time.sleep(timer)
    pyautogui.mouseUp(button='right')
    time.sleep((timer/2) - 0.00009)

#human click
def humanclick():
    timer=(uniform(0.01,0.015))
    time.sleep((timer/2) - 0.0005)
    pyautogui.mouseDown()
    time.sleep(timer)
    pyautogui.mouseUp()
    #time.sleep((timer/2) - 0.0009)


#move to x,y coorinates
def humanmovexy(x,y,safe='no',speed=1,sleep=0.0025):
    try:
        if (safe=='no'):
            overshoot(x,y)
        sleep = uniform(0.0010,0.0025)
        bezmouse.go((x,y),sleep=sleep,speed=speed)
        time.sleep(uniform(0.01,0.03))
    except:
        print("Move failed")



#move to (x,y,w,h) object
def humanmoveobj(obj, safe='no',speed=1,sleep=0.0025):
    try:
        sleep = uniform(0.0018,0.0032)
        x = randint(obj[0], obj[0]+obj[2]-1)
        y = randint(obj[1], obj[1]+obj[3]-1)
        time.sleep(uniform(0.01,0.02))
        
        if safe=='no':
            #if randint(1,100)<=50:
                #bezmouse.go((randint(client[0],client[2])),(randint(client[1],client[3])))
            overshoot(x,y)
            bezmouse.go((x,y),speed=speed,sleep=uniform(sleep-0.0005,sleep+0.0005))
        elif safe=='yes':
            bezmouse.go((x,y),deviation=(12),speed=speed,sleep=uniform(sleep-0.0005,sleep+0.0005))
        time.sleep(uniform(0.01,0.03))
        # x2,y2 = pyautogui.position()
        # if  x+y != x2+y2:
        #     pyautogui.moveTo(x,y,uniform(0.01,0.02),tween=pyautogui.linear)
    except:
        print("human move obj failed")


#overshoots xy then brings it back to xy
def overshoot(x,y):
    sleep = uniform(0.0018,0.0032)
    if randint(0,10)>=3:
        return 
    currentx,currenty = pyautogui.position()
    if currentx<=x:
        xdir = 1
    else:
        xdir = -1
    if currenty<=y:
        ydir = 1
    else:
        ydir = -1
    x2=randint(2,45)
    y2=randint(2,25)
    bezmouse.go(((xdir*x2)+x,(ydir*y2)+y),sleep=sleep,speed=(randint(1,2)))


#random camera movement
def randomcameramove(steps,honly='no'):
    if randint(1,100) >=90:
        for i in range (steps):
            key = randint(1,4)
            if honly=='yes':
                key = randint(1,2)
            delay = uniform(0.005,0.01)
            hold = uniform(0.1,2.0)
            if key == 1:
                print('pressing left')
                pyautogui.keyDown('left')
                time.sleep(hold)
                pyautogui.keyUp('left')
                time.sleep(delay)
            if key == 2:
                print('pressing right')            
                pyautogui.keyDown('right')
                time.sleep(hold)
                pyautogui.keyUp('right')
                time.sleep(delay)
            if key == 3:
                print('pressing up')            
                pyautogui.keyDown('up')
                time.sleep(hold)
                pyautogui.keyUp('up')
                time.sleep(delay)
            if key == 4:
                print('pressing down')
                pyautogui.keyDown('down')
                time.sleep(hold)
                pyautogui.keyUp('down')
                time.sleep(delay)


#Returns how many packs are in your inventory
def packcount():
    return len(list(imgmatchscreenall('img/pack.png',region1=(inventory))))

#Hops to the next world
def worldhop():
    print("Hopping worlds")
    time.sleep(uniform(0.5,1.2))
    pyautogui.hotkey("ctrl","shift","right")
    time.sleep(10.0)
    pyautogui.press("esc")


#Matches image on in region and returns list of xywh's
def imgmatchscreenall(small, region1=None, threshold=0.6):
    locbox = []
    img = numpy.array(pyautogui.screenshot(region=region1))
    image = img[:, :, ::-1].copy()
    template = cv2.imread(small) 
    h,w,ch = template.shape
    result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED) 
    locations = numpy.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    #print(len(locations))
    for i in locations:
        #print(i)
        x,y =  i
        if region1!=None:
            x0,y0 = region1[:2]
            x=x+x0
            y=y+y0
        locbox.append((x,y,w-1,h-1))
    return locbox


#Matches image on screen and returns XYWH
def imgmatchscreen(small, region1=None, threshold=0.7):
    max_val=0.0
    counter=0
    ssht = pyautogui.screenshot(imageFilename=None, region=region1)
    img = numpy.array(ssht)
    image = img[:, :, ::-1].copy()
    template = cv2.imread(small,cv2.IMREAD_COLOR) 
    h,w,ch = template.shape
    result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)  
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val <= threshold:
        return
    x,y = max_loc
    counter+=1
    #print("max val for this match was "+str(max_val))
    if region1!=None:
        x0,y0 = region1[:2]
        x=x+x0
        y=y+y0
    imgbox = x,y,w-1,h-1
    #print ("returning" + str(imgbox))
    return imgbox


#searches screen for (R,G,B) and returns xy
def colormatch(color):
    try:
        im = pyautogui.screenshot(region=gamewindow)
        
        pimpg = im.load()
        w,h = im.size
        for k in range(0,(w*h)):
            x = randint(0,w-1)
            y = randint(0,h-1)
            if pimpg[x,y] == color:
                x=x+gamewindow[0]
                y=y+gamewindow[1]
                return x,y
    except:
        print("No color found")
        return None

#calibrate mouse
def calibrate():
    l,t,w,h = imgmatchscreen('img/runelite.png')
    print ("calibrated to : " + str((l,t,w,h)))
    return l,t+27







def openstore():
    try:
        while matchtooltip('img/talk.png') == False:
            x,y = colormatch((94,255,112))
            humanmovexy(x,y,speed=2,sleep=0.004)
            time.sleep(uniform(0.35,0.5))
        humanrclick()
        time.sleep(uniform(0.08,0.4))
        humanmoveobj(imgmatchscreen('img/trade.png',region1=client,threshold=0.8),safe='yes')
        time.sleep(uniform(0.08,0.45))
        humanclick()
        time.sleep(uniform(0.08,0.38))
        increment=0
        while len(list(imgmatchscreenall('img/instore.png',region1=(gamewindow),threshold=0.8))) == 0 and increment < 30:
            time.sleep(0.1)
            increment+=1
    except:
        print("openstore() failed")

def buy():
    try:
        if len(list(imgmatchscreenall('img/instore.png',region1=(gamewindow),threshold=0.8))) == 0:
            return
        humanmoveobj(imgmatchscreen('img/pack.png',region1=gamewindow,threshold=0.8))
        time.sleep(uniform(0.07,0.27))
        humanrclick()
        time.sleep(uniform(0.09,0.23))
        humanmoveobj(imgmatchscreen('img/buy10.png',region1=gamewindow,threshold=0.8),safe='yes')
        time.sleep(uniform(0.08,0.29))
        humanclick()
        time.sleep(uniform(0.07,0.21))
        humanmoveobj(imgmatchscreen('img/x.png',region1=gamewindow,threshold=0.8),safe='yes')
        time.sleep(uniform(0.08,0.25))
        humanclick()
    except:
        print("buy() failed")

def unpack():
    global profit
    global startgp
    try:
        try:
            if len(list(imgmatchscreenall('img/pack.png',region1=(inventory),threshold=0.8))) == 0:
                return
            increment = 0
            while matchtooltip('img/open.png') == False and increment < 50:
                humanmoveobj(imgmatchscreen('img/pack.png',region1=inventory,threshold=0.8))
                time.sleep(uniform(0.08,0.2))
                increment+=1
            humanclick()
            if randint(1,100)<=3:
                humanmovexy(10,pyautogui.size()[1]*(uniform(0.15,0.85)),speed=2)
            time.sleep(uniform(0.4,11.5))
            increment=0
            while len(list(imgmatchscreenall('img/pack.png',region1=(inventory),threshold=0.8))) != 0 and increment < 100:
                time.sleep(uniform(0.1,1))
                x,y = colormatch((94,255,112))
                humanmovexy(x,y)
                increment+=1
            if increment>=100:
                return
            profit +=910
            startgp-=2.09
        except:
            print("Ran out of gold, quitting")
            print("ran for " + str(time.time() - start))
            quit()
    except:
        print("unpack() failed")

def checkout():
    try:
        if len(imgmatchscreenall('img/nogp.png',region1=textnotif,threshold=0.95))>0:
            lbl_status_right["text"] = "Out of gold! "
            top.update()
            print("Out of gold, quitting")
            time.sleep(2)
            quit()
        elif len(imgmatchscreenall('img/outofstock.png',region1=textnotif,threshold=0.95))>0:
            lbl_status_right["text"] = "Out of Stock! "
            top.update()
            print("Out of stock, world hop")
            time.sleep(0.05)
            worldhop()
    except:
        print("checkout failed")

        

def logout():
    try:
        humanmoveobj(imgmatchscreen('img/logout1.png',region1=client,threshold=0.8))
        time.sleep(uniform(0.05,0.12))
        humanclick()
        time.sleep(uniform(0.05,0.12))
        if len(imgmatchscreenall('img/logoutx.png',region1=client,threshold=0.8))>0:
            humanmoveobj(imgmatchscreen('img/logoutx.png',region1=client,threshold=0.8))
            time.sleep(uniform(0.05,0.12))
            humanclick()
            time.sleep(uniform(1.5,2))
        humanmoveobj(imgmatchscreen('img/logouttext.png',region1=client,threshold=0.8))
        time.sleep(uniform(0.05,0.12))
        humanclick()
        time.sleep(uniform(0.05,0.12))
    except:
        pyautogui.press('esc')
        print("logout failed")


def login():
    try:
        if len(imgmatchscreenall('img/existinguser.png',region1=client))>0:
            time.sleep(uniform(1.0,1.5))
            pyautogui.press('enter')
            time.sleep(uniform(0.5,1))
            pyautogui.write(username, interval=uniform(0.04,0.3))
            time.sleep(uniform(0.5,1))
            pyautogui.press('enter')
            time.sleep(uniform(0.5,1.1))
            pyautogui.write(password, interval=uniform(0.06,0.4))
            time.sleep(uniform(0.5,1))
            pyautogui.press('enter')
            while len(imgmatchscreenall("img/clicktoplay.png",region1=client))==0:
                time.sleep(0.1)
            humanmoveobj(imgmatchscreen('img/clicktoplay.png',region1=client))
            time.sleep(uniform(0.1,0.3))
            humanclick()
            time.sleep(uniform(4.1,5.2))
    except:
        print("login failed")

def antiban():
    try:
        #moves mouse offscreen to simulate multitasking
        if randint(1,100)<=3:
            lbl_status_right["text"] = "Multitask Sim"
            top.update()
            humanmovexy(10,pyautogui.size()[1]*(uniform(0.15,0.85)),speed=2)
            print("simulating multitask")
            time.sleep(uniform(0.5,10.5))

        #types into clan chat
        if randint(1,1000)<=10:
            lbl_status_right["text"] = "Typing Message"
            top.update()
            pyautogui.press('tab')
            time.sleep(uniform(0.1,0.3))
            pyautogui.write(msglist[randint(0,len(msglist)-1)], interval=uniform(0.04,0.2))
            time.sleep(uniform(0.2,1))
            pyautogui.press('enter')

        #randomly afk's to simulate bathroom break + mouse move offscreen
        if randint(1,1000)<=6:
            lbl_status_right["text"] = "Medium Break"
            top.update()
            humanmovexy(10,pyautogui.size()[1]*(uniform(0.15,0.85)),speed=2)
            print("Simulating bathroom break")
            time.sleep(uniform(120.24,240.1))
        

        #simulates longer 12-18ish minute break and types in clan chat
        if randint(1,1000)<=1:
            lbl_status_right["text"] = "Long break"
            top.update()
            print("Simulating food break")
            chat=randint(0,5)
            pyautogui.press('tab')
            time.sleep(uniform(0.1,0.2))
            chatlist = ["brb food","ill be back in a sec","i need to go eat","gota do something","foods done","brb"]
            pyautogui.write(chatlist[chat], interval=uniform(0.04,0.2))
            time.sleep(uniform(0.2,1))
            pyautogui.press('enter')
            lbl_status_right["text"] = "Logging In "
            top.update()
            logout()
            time.sleep(uniform(720.17,1000.1))
            lbl_status_right["text"] = "Logging In "
            top.update()
            login()
    except:
        print("antibad failed")



############## G U I  ################
start = time.time()
def setlabel():

    global startgp
    value = entry_gp.get()
    lbl_start['text'] = time.strftime("%H:%M:%S", time.gmtime(time.time()-start))
    entry_gp.delete(0, tk.END)
    btn_start.pack_forget()
    entry_gp.pack_forget()
    startgp = float(value)
    origgp = float(value)

def killbot():
    os._exit(1)


top = tk.Tk()
top.title('RSFeatherUnpack 1.0')
top.minsize(300,100)


#TOP SECTION
frmleft = tk.Frame(top)
frmright = tk.Frame(top)

lbl_start = tk.Label(
    top, text="Enter GP in thousands"

)

entry_gp = tk.Entry(
    
)

btn_start = tk.Button(
    top,text ="START",
    height=2,
    width = 20,
    command = setlabel
 )

btn_kill = tk.Button(
     top,text = "Kill Process",
     height =3,
     width = 14,
     command = killbot
 )

 #MIDDLE SECTIONS
lbl_status_left = tk.Label(
    frmleft,text = " Status:"
)

lbl_status_right = tk.Label(
    frmright,text= "Value "
)

lbl_profit_left = tk.Label(
    frmleft,text = " Total Profit:"
)
lbl_profit_right = tk.Label(
    frmright,text = "XXXX GP "
)


lbl_gphr_left = tk.Label(
    frmleft,text = " GP/hr:"
)
lbl_gphr_right = tk.Label(
    frmright,text = "XXXX GP "
)

lbl_timeleft_left = tk.Label(
    frmleft,text = " Time Left:"
)
lbl_timeleft_right = tk.Label(
    frmright,text = "00:00:00 "
)

#BOTTOM
lbl_perc = tk.Label(
    text='0%s complete' % "%"
)




lbl_start.pack()
entry_gp.pack()
entry_gp.insert(0,"ex. 5000 = 5m")
btn_start.pack()


frmleft.pack(side=tk.LEFT)
lbl_status_left.pack()
lbl_profit_left.pack()
lbl_gphr_left.pack()
lbl_timeleft_left.pack()

frmright.pack(side=tk.RIGHT)
lbl_status_right.pack()
lbl_profit_right.pack()
lbl_gphr_right.pack()
lbl_timeleft_right.pack()
lbl_perc.pack(side=tk.BOTTOM)

btn_kill.pack(side=tk.BOTTOM)

################ G U I ###################

#MAIN LOOP
def bot():
    while True:
        lbl_status_right["text"] = "Opening Store "
        top.update()
        time.sleep(uniform(0.001,0.2))
        openstore()
        lbl_status_right["text"] = "Buying Feathers "
        top.update()
        time.sleep(uniform(0.001,0.2))
        buy()
        time.sleep(uniform(0.001,0.2))
        checkout()
        randomcameramove(steps=randint(1,3),honly='yes')
        lbl_status_right["text"] = "Unpacking Feathers "
        top.update()
        time.sleep(uniform(0.001,0.2))
        unpack()
        top.update()

        antiban()

        ## Time
        sectime = time.time() - start
        runtime = time.gmtime(time.time() - start)
        gphr = int((3600/sectime)*profit)
        costph = (gphr/1000)*2

        lbl_profit_right['text'] = "%sgp " % profit
        lbl_gphr_right['text'] = str(gphr) + " "
        lbl_timeleft_right['text'] = time.strftime('%H:%M:%S', time.gmtime(((startgp/costph)*3600)))
        lbl_perc['text'] = str(round(((sectime / (sectime+((startgp/costph)*3600)))*100),2)) + '%' + " complete"
        lbl_start['text'] = time.strftime("%H:%M:%S", time.gmtime(time.time()-start))
        # print("You have made " + str(profit) + "gp in " + time.strftime("%H:%M:%S", runtime))
        # print(" Thats " + str(gphr) + "gp p/hr!")
        # print("You will run out of gold in " + str(round((startgp/costph),1)) + " hours!")



#341 249
#Global variables and calibrating mouse pos
lbl_status_right['text'] = "Initializing "
x0,y0 = calibrate()
profit = 1
print("Calibrated to game window at: " + str((x0,y0)))
oldmousepos = (x0,y0)
bottomright = x0+765,y0+502
client=(x0,y0,765,502)
textnotif=(x0+3,y0+440,236,25)
gamewindow=(x0+5,y0+4,515,334)
inventory=(x0+549,y0+210,183,253)
motionbox=(x0+300,y0,45,45)
mapbox=(x0+568,y0+11,151,151)
bankdep = (228,83,83),(227,82,82)
price10 = 2090
startgp = None #int(input("Enter starting gold in thousands: "))
origgp = None
username = lines[0]
password = lines[1]

time.sleep(3)
login()
while startgp == None:
    top.update()
time.sleep(3)
start = time.time()
bot()

#MAIN LOOP
