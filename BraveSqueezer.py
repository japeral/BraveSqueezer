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

#Global variables
numberOfBrowsers = 5
browsersLocationsInTaskbar = arr.array('i')
mouseShakingRecording      = arr.array('i')
deleteAdsSequence          = arr.array('i')
adsThisMonthCounters       = arr.array('i',(0,))

#Laptop--------------------------------------------------------------------------------------------------------------------------------
deleteAdsSequence=[1884,1063,1852,658,1883,1058,2730,860]
mouseShakingRecording=[1110,856,1460,633,1615,580,1953,507,2953,241,3165,206,3165,206,2966,282,2711,477,2528,611,2370,533,2330,425,2377,339,2585,251,2918,187,3137,207,3140,364,
                       2949,521,2398,630,2216,407,2355,316,2458,411,2412,595,2237,643,2214,493,2496,362,2803,416,2887,368,2768,328,2808,444,2737,576,2620,547,2643,471,2754,446,
                       2835,465,2807,413,2739,381,2719,410,2656,463,2596,476,2582,480,2566,477,2566,477,2566,477,2566,477,2365,520,2096,601,1540,752,1325,835,1270,858,1331,808]
browsersLocationsInTaskbar=[]
Xx = 3261
Xy = 123
searchBar_x=2485
searchBar_y=160
adsCounterx=2649
adsCountery=716
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
#                      1106,215,1140,238,1142,264,1122,297,1095,324,1054,354,1012,405,962,477,939,532,956,575,1068,629,1192,665,
#                      1318,614,1300,531,1191,472,1076,412,975,365,845,321,818,229,854,162,971,164,1094,201,1171,271,1270,351,
#                      1270,353,1252,228,1221,186,1221,186,1222,180,1222,180,1222,180,1212,201,1180,269,1133,329,1073,425,1031,496,
#                      999,577,929,667,905,723,903,727,916,734,1071,737,1233,705,1316,658,1245,624,1071,589,991,525,995,514,1009,504,
#                      1009,504,1009,504,1009,504,1009,504]
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
    for i in range(1,numberOfBrowsers):
        command = 'brave.exe --profile-directory="Profile %d"' % i
        os.system(command)
        while(psutil.cpu_percent() > 90.0):
            pass
        time.sleep(0.5)
        pyautogui.hotkey('win','up')   #Maximize all the browser window to align the [x] buttons on the same coordinates.
        time.sleep(0.5)
        searchRewards()        
        time.sleep(1)        
        pyautogui.doubleClick(adsCounterx,adsCountery)
        pyautogui.hotkey('ctrl','c')
        ads=int(pyperclip.paste())
        adsThisMonthCounters.append(ads)
        print("Profile %d launched, Ads this mount counter: %d" % (i,ads))
    print("Summary:")             
    print("Done")             

def closeBrowsers():
    print("Closing Browsers...")                
    pyautogui.moveTo(Xx,Xy,duration=2)
    pyautogui.click(Xx, Xy, clicks=numberOfBrowsers-1, interval=1, button='left')
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
    pyautogui.write("www.github.com/japeral", interval=0.25)
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
            shakeMouse()            
            print ("Waiting 30 seconds...")
            time.sleep(30)            
            deleteAdsNotifications()                   
            closeBrowsers()

    if(keyboard.is_pressed('9')):
        closeBrowsers()      
        printMenu()
