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





#check tooltip under mouse for image
def matchtooltip(image):
    cx,cy = pyautogui.position()
    box = (cx-120,cy-75,240,150)  
    return len(imgmatchscreenall(image,region1=box))>0


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
def humanmovexy(x,y,safe='no',speed=3,sleep=0.0025):
    try:
        if (safe=='no'):
            overshoot(x,y)
        sleep = uniform(0.0010,0.0025)
        bezmouse.go((x,y),sleep=sleep,speed=speed)
        time.sleep(uniform(0.01,0.03))
    except:
        print("Move failed")
        return



#move to (x,y,w,h) object
def humanmoveobj(obj, safe='no',speed=2,sleep=0.0025):
    sleep = uniform(0.0018,0.0032)
    x = randint(obj[0], obj[0]+obj[2]-1)
    y = randint(obj[1], obj[1]+obj[3]-1)
    time.sleep(uniform(0.01,0.02))
    
    if safe=='no':
        overshoot(x,y)
        bezmouse.go((x,y),sleep=sleep,speed=speed)
    elif safe=='yes':
        bezmouse.go((x,y),deviation=10,speed=speed,sleep=sleep)
    time.sleep(uniform(0.01,0.03))
    # x2,y2 = pyautogui.position()
    # if  x+y != x2+y2:
    #     pyautogui.moveTo(x,y,uniform(0.01,0.02),tween=pyautogui.linear)



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
    x2=randint(10,25)
    y2=randint(10,25)
    bezmouse.go(((xdir*x2)+x,(ydir*y2)+y),sleep=sleep)


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
            humanmovexy(x,y)
            time.sleep(uniform(0.05,0.1))
        humanrclick()
        time.sleep(uniform(0.08,0.2))
        humanmoveobj(imgmatchscreen('img/trade.png',region1=gamewindow),safe='yes')
        time.sleep(uniform(0.08,0.2))
        humanclick()
        time.sleep(uniform(0.08,0.2))
        while len(list(imgmatchscreenall('img/instore.png',region1=(gamewindow),threshold=0.60))) == 0:
            time.sleep(0.1)
    except:
        print("openstore() failed")

def buy():
    try:
        humanmoveobj(imgmatchscreen('img/pack.png',region1=gamewindow))
        time.sleep(uniform(0.08,0.2))
        humanrclick()
        time.sleep(uniform(0.08,0.2))
        humanmoveobj(imgmatchscreen('img/buy10.png',region1=gamewindow),safe='yes')
        time.sleep(uniform(0.08,0.2))
        humanclick()
        time.sleep(uniform(0.08,0.2))
        humanmoveobj(imgmatchscreen('img/x.png',region1=gamewindow))
        time.sleep(uniform(0.08,0.2))
        humanclick()
    except:
        print("buy() failed")

def unpack():
    global profit
    global startgp
    try:
        try:
            while matchtooltip('img/open.png') == False:
                humanmoveobj(imgmatchscreen('img/pack.png',region1=inventory))
                time.sleep(uniform(0.08,0.2))
            humanclick()
            time.sleep(uniform(0.4,6.5))
            while len(list(imgmatchscreenall('img/pack.png',region1=(inventory),threshold=0.60))) != 0:
                time.sleep(0.1)
                x,y = colormatch((94,255,112))
                humanmovexy(x,y)
            profit +=910
            startgp-=2.09
        except:
            print("Ran out of gold, quitting")
            print("ran for " + str(time.time() - start))
            quit()
    except:
        print("buy() failed")

def checkout():
        if len(imgmatchscreenall('img/nogp.png',region1=textnotif))>0:
            print("Out of gold, quitting")
            time.sleep(2)
            quit()

############## G U I  ################
def setlabel():
    global startgp
    value = entry_gp.get()
    lbl_start['text'] = value + "k GP"
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
        openstore()
        lbl_status_right["text"] = "Buying Feathers "
        top.update()
        buy()
        checkout()
        randomcameramove(steps=randint(1,3),honly='yes')
        lbl_status_right["text"] = "Unpacking Feathers "
        top.update()
        unpack()
        top.update()
        ## Time
        sectime = time.time() - start
        runtime = time.gmtime(time.time() - start)
        gphr = int((3600/sectime)*profit)
        costph = (gphr/1000)*2

        lbl_profit_right['text'] = "%sgp " % profit
        lbl_gphr_right['text'] = str(gphr) + " "
        lbl_timeleft_right['text'] = time.strftime('%H:%M:%S', time.gmtime(((startgp/costph)*3600)))
        lbl_perc['text'] = str(round(((sectime / (sectime+((startgp/costph)*3600)))*100),2)) + '%' + " complete"
        # print("You have made " + str(profit) + "gp in " + time.strftime("%H:%M:%S", runtime))
        # print(" Thats " + str(gphr) + "gp p/hr!")
        # print("You will run out of gold in " + str(round((startgp/costph),1)) + " hours!")

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

while startgp == None:
    top.update()
start = time.time()
bot()

#MAIN LOOP
