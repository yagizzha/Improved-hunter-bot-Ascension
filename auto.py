import numpy as np
import cv2
from time import time
from time import sleep
import win32gui
import win32ui
import win32con
import win32api
import pyautogui
import keyboard
import tkinter
from skimage.metrics import structural_similarity as compare_ssim
from impwincap import WindowCapture
from skilltrack import SkillTrack


numarr=[]
for i in range(12):
    numarr.append(cv2.imread("numbs/"+str(i)+".jpg"))
    print(i)
wincap=WindowCapture("Ascension")

hwnd=win32gui.FindWindow(None,wincap.windowname)

win=win32ui.CreateWindowFromHandle(hwnd)
dt=cv2.imread("dot.jpg")
img=wincap.windowcap()
cv2.imwrite("scr.jpg",img)
#cv2.imshow("img",img)


path="skills/"
chimerashot=SkillTrack("Chimera Shot",718,771,555,608,cv2.imread(path+"Chimera Shot.jpg"),dt)#
insectswarm=SkillTrack("Insect Swarm",778,823,615,659,cv2.imread(path+"Insect Swarm.jpg"),dt)#
blackarrow=SkillTrack("Black Arrow",719,772,714,768,cv2.imread(path+"Black Arrow.jpg"),dt)#
blackarrowdebuff=SkillTrack("Black Arrow Debuff",774,827,716,769,cv2.imread(path+"Black Arrow Debuff.jpg"),dt)#
earthshock=SkillTrack("Earth Shock",718,772,609,661,cv2.imread(path+"Earth Shock.jpg"),dt)#
earthshockdebuff=SkillTrack("Earth Shock Debuff",661,714,660,712,cv2.imread(path+"Earth Shock Debuff.jpg"),dt)#
serpentsting=SkillTrack("Serpent Sting",719,771,662,713,cv2.imread(path+"Serpent Sting.jpg"),dt)#
wildwrath=SkillTrack("Wild Wrath",719,772,499,552,cv2.imread(path+"Wild Wrath.jpg"),dt)#
gcd=SkillTrack("gcd",360,410,620,635,cv2.imread(path+"gcd.jpg"),dt)#[620:635,360:410]
curse=SkillTrack("Curse of the Elements",664,717,501,553,cv2.imread(path+"Curse of the Elements.jpg"),dt)
mana=SkillTrack("Mana",593,654,483,505,cv2.imread(path+"mana.jpg"),dt)#[483:505,593:654]
bigneed=SkillTrack("Mana",593,654,483,505,cv2.imread(path+"bigneed.jpg"),dt)
innervate=SkillTrack("Innervate",553,605,664,715,cv2.imread(path+"Innervate.jpg"),dt)
meditate=SkillTrack("Meditate",773,827,555,608,cv2.imread(path+"Meditate.jpg"),dt)
piercing=SkillTrack("Piercing",774,826,663,714,cv2.imread(path+"Piercing.jpg"),dt)



"""
chimimg=piercing.cut(img)
cv2.imwrite(piercing.name+".jpg",chimimg)

chimimg=innervate.cut(img)
cv2.imwrite(innervate.name+".jpg",chimimg)

chimimg=blackarrowdebuff.cut(img)
cv2.imwrite(blackarrowdebuff.name+".jpg",chimimg)

chimimg=earthshock.cut(img)
cv2.imwrite(earthshock.name+".jpg",chimimg)

chimimg=earthshockdebuff.cut(img)
cv2.imwrite(earthshockdebuff.name+".jpg",chimimg)

chimimg=serpentsting.cut(img)
cv2.imwrite(serpentsting.name+".jpg",chimimg)

chimimg=wildwrath.cut(img)
cv2.imwrite(wildwrath.name+".jpg",chimimg)
"""
usewrath=True
fornowused=True
continuable=False
while True:
    img=wincap.windowcap()
    #chimerashot.cdLeft(img,numarr)
    """
    print("CHIM",chimerashot.cdLeft(img,numarr),end=" ")
    print("INSC",insectswarm.cdLeft(img,numarr),end=" ")
    print("BLAC",blackarrow.cdLeft(img,numarr),end=" ")
    print("BLCD",blackarrowdebuff.cdLeft(img,numarr),end=" ")
    print("ERTS",earthshock.cdLeft(img,numarr),end=" ")
    print("ERTD",earthshockdebuff.cdLeft(img,numarr),end=" ")
    print("SPST",serpentsting.cdLeft(img,numarr),end=" ")
    print("WDWT",wildwrath.cdLeft(img,numarr))
    """
    chimcd=chimerashot.cdLeft(img,numarr)
    insect=insectswarm.cdLeft(img,numarr)
    blackcd=blackarrow.cdLeft(img,numarr)
    blackdb=blackarrowdebuff.cdLeft(img,numarr)
    earthcd=earthshock.cdLeft(img,numarr)
    earthdb=earthshockdebuff.cdLeft(img,numarr)
    serpentdb=serpentsting.cdLeft(img,numarr)
    wild=wildwrath.cdLeft(img,numarr)
    piercingdb=piercing.cdLeft(img,numarr)
    print(piercingdb)
    if keyboard.is_pressed('ü'):
        print("C O N T I N U E ")
        continuable=True
    if keyboard.is_pressed(','):
        print("S T O P")
        continuable=False
        usewrath=True
    if continuable:
        if gcd.match(img):
            if usewrath and serpentdb==0 and wild>0 and not curse.match(img):
                win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x58, 0)
                win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x58, 0)
                img=wincap.windowcap()
                if not gcd.match(img):
                    usewrath=False
            else:
                if serpentdb!=None and serpentdb==0 and not curse.match(img):
                    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x31, 0)
                    win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x31, 0)
                else:
                    if serpentdb!=None and serpentdb==0 and piercingdb<=2 and insect==0:
                        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x31, 0)
                        win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x31, 0)
                    else:
                        if serpentdb!=None and serpentdb==0 and insect!=None and insect==0:
                            win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x45, 0)
                            win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x45, 0)
                        else:
                            if serpentdb!=None and serpentdb==0 and earthcd!=None and earthdb!=None and earthcd==0 and earthdb==0:
                                win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x35, 0)
                                win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x35, 0)
                            else:
                                if serpentdb!=None and serpentdb==0 and blackcd!=None and  blackcd==0 :
                                    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x5A, 0)
                                    win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x5A, 0)
                                    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x47, 0)
                                    win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x47, 0)
                                else:
                                    if serpentdb!=None and serpentdb==0:
                                        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x32, 0)
                                        win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x32, 0)
                                        img=wincap.windowcap()
                                        if not gcd.match(img):
                                            usewrath=True
                                    else:
                                        if wild!=None and wild>0 and ((insect!=None and insect<1.8 )or not curse.match(img) ):
                                            win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x58, 0)
                                            win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x58, 0)
                                        else:
                                            if insect!=None and insect==0:
                                                win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x45, 0)
                                                win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x45, 0) 
                                            else:
                                                if blackcd!=None and blackcd==0 and chimcd!=None and  chimcd<3:
                                                    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x5A, 0)
                                                    win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x5A, 0)
                                                    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x47, 0)
                                                    win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x47, 0)
                                                else:
                                                    if serpentdb!=None and serpentdb>0 and chimcd!=None and chimcd==0:
                                                        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x52, 0)
                                                        win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x52, 0)
                                                    else:
                                                        if innervate.match(img) and (mana.match(img) or bigneed.match(img)):
                                                            win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x51, 0)
                                                            win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x51, 0)
                                                            img=wincap.windowcap()
                                                        else:
                                                            if bigneed.match(img):
                                                                win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x54, 0)
                                                                win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x54, 0)
                                                            else:
                                                                if meditate.match(img):
                                                                    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x33, 0)
                                                                    win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x33, 0)
                                                                else:
                                                                    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x31, 0)
                                                                    win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x31, 0)
                                                    
           
                










































    









