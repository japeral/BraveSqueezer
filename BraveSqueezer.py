import pyautogui
import mouse
import time
import keyboard
import array as arr
import os
import subprocess
import sys
import psutil
import pyperclip
from openpyxl import Workbook
from datetime import datetime

#Global variables
numberOfBrowsers = 61
browsersLocationsInTaskbar = arr.array('i')
mouseShakingRecording      = arr.array('i')
deleteAdsSequence          = arr.array('i')
adsThisMonthCounters       = arr.array('i')
workbook = Workbook()
sheet = workbook.active

#Sharkon--------------------------------------------------------------------------------------------------------------------------------
deleteAdsSequence=[1246,1000,1219,756,1246,1007]
mouseShakingRecording=[1929,321,2047,254,2114,245,2184,242,2261,306,2300,370,2316,457,2306,579,2260,655,2214,698,2121,748,2019,782,1902,784,
                       1816,766,1708,691,1647,614,1599,518,1568,399,1577,283,1625,217,1735,193,1925,202,2095,231,2182,260,2235,323,2257,434,
                       2219,552,2071,743,1878,838,1654,756,1508,445,1551,226,1760,140,1953,167,2087,251,2090,403,1897,626,1619,759,1454,658,
                       1437,459,1571,333,1697,330,1878,433,1926,502,1928,607,1887,689,1854,711,1829,695,1782,604,1773,503,1776,381,1799,281,
                       1836,201,1901,164,2019,168,2147,188,2212,219,2273,295,2316,439,2300,553,2215,632,2100,670,1961,656,1718,582,1562,556,
                       1496,603,1448,743,1491,809,1721,841,2073,827,2339,734,2441,464,2448,291,2403,141,2190,74,2069,76,1801,152,1615,220,
                       1501,292,1444,385,1490,491,1641,562,1833,526,1981,516,2089,575,2097,646,2022,721,1899,709,1869,673,1920,642,2013,634,
                       2029,602,2028,586]

browsersLocationsInTaskbar=[]
Xx = 2537
Xy = 8
searchBar_x=1610
searchBar_y=38
adsCounterx=1973
adsCountery=714
#-------------------------------------------------------------------------------------------------------------------------------------

#Baldo config-------------------------------------------------------------------------------------------------------------------------
#deleteAdsSequence=[1893,1053,1878,945,1895,1065]
#mouseShakingRecording=[606,492,602,452,620,426,644,408,719,403,752,422,793,457,886,479,997,479,1079,454,1123,397,1074,325,944,305,891,337,859,392,844,454,804,499,740,514,694,492,
#                       647,434,646,390,654,376,670,372,688,371,691,374,691,374,691,374,693,374,694,374,694,375,695,376,696,380,698,385,721,426,736,431,765,397,779,397,796,403,793,
#                       408,786,403,761,382,756,381,754,381,753,386,752,386]
#Xx = 1896
#Xy = 12
#searchBar_x = 766
#searchBar_y = 45
#-------------------------------------------------------------------------------------------------------------------------------------

#Valverde Coordinate Config------------------------------------------------------------------------------------------------------------
#deleteAdsSequence=[1405,877,1390,622,1405,880,1050,376]
#mouseShakingRecording=[1071,372,1071,372,1059,372,1041,368,1009,356,968,342,937,316,916,289,911,248,921,228,940,206,966,187,1014,188,
#                       1106,215,1140,238,1142,264,1122,297,1095,324,1054,354,1012,405,962,477,939,532,956,575,1068,629,1192,665,
#                       1318,614,1300,531,1191,472,1076,412,975,365,845,321,818,229,854,162,971,164,1094,201,1171,271,1270,351,
#                       1270,353,1252,228,1221,186,1221,186,1222,180,1222,180,1222,180,1212,201,1180,269,1133,329,1073,425,1031,496,
#                       999,577,929,667,905,723,903,727,916,734,1071,737,1233,705,1316,658,1245,624,1071,589,991,525,995,514,1009,504,
#                       1009,504,1009,504,1009,504,1009,504]
#Xx = 1415
#Xy = 10
#searchBar_x = 1062
#searchBar_y = 54
#-------------------------------------------------------------------------------------------------------------------------------------


print("Brave ADs Squeezer v1.2")
print("                                          by Jose Peral, 24st Feb 2021")
print(" ")

def printMenu():
    print("Type '1' to launch the Brave Browser instances")
    print("Type '2' to Record Ads Notification deletion sequence")    
    print("Type '3' to Record mouse Shaking sequence")
    print("Type '4' to Record the icons locations in the task bar")
    print("Type '5' to record the close [X] button location")
    print("Type '6' to record the Search Bar location")
    print("Type '7' to record the Ads Counter location")    
    print("Type '8' Ads extraction loop! ")        
    print("Type '9' Close all browsers ")            

def launchBrowsers():
    os.chdir ('C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\')
    adsThisMonthCounters=[]  # delete the array
    sheet['A1']="Profile"
    sheet['B1']="Ads this month"   
    for i in range(2,numberOfBrowsers):
        command = 'brave.exe --profile-directory="Profile %d"' % i
        os.system(command)
        while(psutil.cpu_percent() > 90.0):
            pass
        time.sleep(1)
        pyautogui.hotkey('win','up')   #Maximize all the browser window to align the [x] buttons on the same coordinates.
        searchRewards()        
        time.sleep(1)        
        pyautogui.moveTo(adsCounterx,adsCountery,duration=2)
        pyautogui.vscroll(100)
        time.sleep(1)                
        pyautogui.doubleClick(adsCounterx,adsCountery)
        pyautogui.hotkey('ctrl','c')
        try:
            ads=int(pyperclip.paste())
        except:
            ads=0
        adsThisMonthCounters.append(ads)
        print("Profile %d launched, Ads this month counter: %d" % (i,ads) )
        sheet['A%d' %i]=i
        sheet['B%d' %i]=ads
    now=datetime.now()
    dirname,filename = os.path.split(os.path.abspath(__file__))
    workbook.save(filename=dirname + "\\" + now.strftime("%Y_%m_%d__%H_%M_%S_") + "balances.xlsx")
    print("Done")

def closeBrowsers():
    print("Closing Browsers...")                
    pyautogui.moveTo(Xx,Xy,duration=2)
    pyautogui.click(Xx, Xy, clicks=numberOfBrowsers, interval=0.25, button='left')
    print("Done")            


def touchBrowsers():
    i=0
    print("Touching Browsers Icons in Task bar...")                
    while i < len(browsersLocationsInTaskbar):     
        x=browsersLocationsInTaskbar[i]
        y=browsersLocationsInTaskbar[i+1]
        print("sample: ", i, "x=",x, "y=",y )
        pyautogui.moveTo(x,y,duration=1)
        pyautogui.click(x, y, clicks=1, interval=1, button='left')
        i=i+2
    else:
        print("Done") 

def deleteAdsNotifications():
    i=0
    print("Deleting previous ads Notifications...")                
    while i < len(deleteAdsSequence):     
        x=deleteAdsSequence[i]
        y=deleteAdsSequence[i+1]
        print("sample: ", i, "x=",x, "y=",y )
        pyautogui.moveTo(x,y,duration=1)
        pyautogui.click(x, y, clicks=1, interval=1, button='left')
        i=i+2
    else:
        print("Done") 

def shakeMouse():
    i=0
    print("Shaking Mouse to call the Ads...")                
    while i < len(mouseShakingRecording):     
        x=mouseShakingRecording[i]
        y=mouseShakingRecording[i+1]
        print("sample: ", i, "x=",x, "y=",y )
        pyautogui.moveTo(x,y,duration=0.1)
        i=i+2
    else:
        print("Done")               

def searchSomething():
    print("Searching something in the browser...")                
    pyautogui.moveTo(searchBar_x,searchBar_y,duration=1)
    pyautogui.click(searchBar_x, searchBar_y, clicks=1, interval=0.1, button='left')    
    #pyautogui.write("www.github.com/japeral", interval=0.25)
    pyautogui.write("brave://rewards/", interval=0.25)
    pyautogui.press('enter')
    print("Done")               

def searchRewards():
    pyautogui.moveTo(searchBar_x,searchBar_y,duration=1)
    pyautogui.click(searchBar_x, searchBar_y, clicks=1, interval=0.1, button='left')    
    pyautogui.write("brave://rewards", interval=0.1)
    pyautogui.press('enter')


printMenu()

while(True):
    time.sleep(0.2)

    
    if(keyboard.is_pressed('1')):
        launchBrowsers()
        printMenu()

    if(keyboard.is_pressed('2')):
        print ("Recording the ADS notification sequence... Press ENTER to finish")        
        deleteAdsSequence=[]  # delete the array        
        time.sleep(1)        
        while (True):
            if (mouse.is_pressed("left")):
                x,y=mouse.get_position()
                while (mouse.is_pressed("left")==True):
                    pass
                deleteAdsSequence.extend([x,y])
                print("%d,%d" % (x,y))
            if(keyboard.is_pressed('enter')):
                break
        printMenu()

    if(keyboard.is_pressed('3')):
        print ("Recording Mouse Shaking Movements... Press ENTER to finish")        
        mouseShakingRecording=[]  # delete the array                
        time.sleep(1)        
        i=0
        mouseShakingRecording.clear()
        while(True):
            time.sleep(0.1)
            x,y=mouse.get_position()
            mouseShakingRecording.extend([x,y])
            print("%d,%d" % (x,y))
            if(keyboard.is_pressed('enter')):
                break
        printMenu()            

    if(keyboard.is_pressed('4')):
        print ("Recording opened Brave browsers icons coordinates... Press ENTER to finish")        
        browsersLocationsInTaskbar=[]  # delete the array                
        time.sleep(1)        
        while (True):
            if (mouse.is_pressed("left")):
                x,y=mouse.get_position()
                while (mouse.is_pressed("left")==True):
                    pass
                browsersLocationsInTaskbar.extend([x,y])
                print("x=",x,"y=",y)               
            if(keyboard.is_pressed('enter')):
                break
        printMenu()

    if(keyboard.is_pressed('5')):
        print ("Recording [X] button coordinates...")
        time.sleep(1)        
        while (mouse.is_pressed("left")==False):
            pass
        Xx,Xy=mouse.get_position()
        print("X Button located @ x=",Xx,"y=",Xy)
        printMenu()

    if(keyboard.is_pressed('6')):
        print ("Recording the Search Bar coordinates...")
        time.sleep(1)        
        while (mouse.is_pressed("left")==False):
            pass
        searchBar_x,searchBar_y=mouse.get_position()
        print("%d,%d" % (searchBar_x,searchBar_y))
        printMenu()

    if(keyboard.is_pressed('7')):
        print ("Recording 'Ads received this month' counter coordinates...")
        time.sleep(1)        
        while (mouse.is_pressed("left")==False):
            pass
        adsCounterx,adsCountery=mouse.get_position()
        print("adsCounterx=%d" % adsCounterx)
        print("adsCountery=%d" % adsCountery)
        printMenu()

    if(keyboard.is_pressed('8')):
        print ("Open at least 1 Brave Browser Profile manually and then and press ENTER")
        os.system("pause")
        while (True):
            launchBrowsers()
            print ("Waiting 5 minutes...")
            time.sleep(60*5)            
            shakeMouse()
            searchSomething()            
            deleteAdsNotifications()                   
            closeBrowsers()

    if(keyboard.is_pressed('9')):
        closeBrowsers()      
        printMenu()
