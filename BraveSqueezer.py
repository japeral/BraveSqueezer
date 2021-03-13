from config_sharkon import *
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
import cv2
import imutils
import numpy

#Global variables
numberOfBrowsers = 61
browsersLocationsInTaskbar = arr.array('i')
mouseShakingRecording      = arr.array('i')
deleteAdsSequence          = arr.array('i')
adsThisMonthCounters       = arr.array('i')
workbook = Workbook()
sheet = workbook.active

deleteAdsSequence=[1245,1003,1220,754,1243,1001]
mouseShakingRecording=[417,247,442,221,491,192,543,165,596,148,663,141,733,142,795,148,865,168,891,187,918,222,954,293,966,400,942,522,884,604,783,664,668,704,535,717,367,684,253,591,192,415,174,262,172,179,372,178,653,554,532,685,353,613,391,403,468,321,529,261,569,220,639,182,779,154,900,165,1020,227,1083,342,1086,484,1044,578,973,676,844,766,596,836,394,804,265,690,180,442,193,307,267,237,334,227,482,244,637,289,741,350,759,377,762,390,762,391,762,391,762,391,759,396,751,409,746,420,743,426,743,426,743,426]
browsersLocationsInTaskbar=[182,1002,261,1003,297,1004,372,1008,411,1005,445,1004,486,1004,524,1004,556,1005,597,1002,643,1007,677,1006,718,1002,749,1004,794,1006,823,1006,862,1006,900,1003,942,1003,973,1003,1007,1006,1037,1014,1014,1004,976,1001,934,1002,900,1001,867,1001,825,1001,781,999,753,999,713,1001,676,1001,637,999,598,1000,561,1003,521,1002,479,996,448,1002,418,1003,376,1002,337,1003,300,1001,263,999,219,1004,185,1002,151,1000,108,998,68,999,1038,1015,610,1000,562,1003,515,1003,471,1000,419,999,372,1000,316,998,269,998,224,998,174,1000,132,1000,72,1000]

print("--------------------------------------------------------------------------------------------------")
print(" Brave ADs Squeezer v1.3")
print("                                                         by Jose Peral, 3rd March 2021")
print(" ")

def printMainMenu():
    print("--------------------------------------------------------------------------------------------------")
    print("  NOTE: Close all brave browser instances, and the open one and close one on the primary display  ")
    print("        that will force all the new instances to open on the primary display.                     ")
    print("                                                                                                  ")
    print("        If you lose control, press (ctrl + alt + del) to trigger the failsafe mechanism and stop  ")
    print("        the execution.                                                                            ")
    print("                                                                                                  ")
    print("MAIN MENU")
    print("---------")
    print("  Type  '0'  to enter the Locations Recording Menu")
    print("  Type  '1'  to enter the Manual Menu")
    print("  Type  '2'  automated loop. Open + shake search 5 times 5 minutes + Close all ")
    print("  Type  '3'  automated loop. Open once, shake + search, close once.")
    print("  Type  '4'  Solve monthly Captcha on %d browsers" %numberOfBrowsers)  
    print("  Type  '5'  Donate BAT balances")      
    print("  Type 'esc' to terminate this program")

def printRecordingMenu():
    print("  RECORDING MENU")
    print("    Type  '0'  to Record Ads Notification deletion sequence")    
    print("    Type  '1'  to Record mouse Shaking sequence")
    print("    Type  '2'  to Record the icons locations in the task bar")
    print("    Type  '3'  to record the close [X] button location")
    print("    Type  '4'  to record the Search Bar location")
    print("    Type  '5'  to record the Ads Counter location")    
    print("    Type  '6'  to Record the captcha target shape text location")
    print("    Type  '7'  to Record the Ads Notifications Area location (windows pop-ups)")    
    print("    Type 'esc' to return to Main Menu")    

def printManualMenu():
    print("  MANUAL MENU")
    print("    Type  '0'  Launch %d Browser" %numberOfBrowsers)
    print("    Type  '1'  Launch %d Browser + Collect balances into a spreadsheet" %numberOfBrowsers)
    print("    Type  '2'  Click the browsers icons in the taskbar")
    print("    Type  '3'  Shake mouse")
    print("    Type  '4'  Search Github")
    print("    Type  '5'  Click 21 notifications")    
    print("    Type  '6'  Close %d browsers" %numberOfBrowsers)        
    print("    Type 'esc' to return to Main Menu")        

def launchBrowsersGetBalances():
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
        pyautogui.press('esc')         #to close the 'Restore pages?' popup
        time.sleep(0.5)                
        pyautogui.hotkey('win','up')   #Maximize all browser windows to align the [x] buttons on the same coordinates.
        time.sleep(0.5)        
        searchSomething("brave://rewards")        
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

def launchBrowsers():
    os.chdir ('C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\')
    for i in range(2,numberOfBrowsers):
        command = 'brave.exe --profile-directory="Profile %d"' % i
        os.system(command)
        while(psutil.cpu_percent() > 90.0): #Wait for the CPU load to go below 90% before launching a new instance
            pass
        time.sleep(1)
        pyautogui.press('esc')         #to close the 'Restore pages?' popup        
        time.sleep(0.5)                
        pyautogui.hotkey('win','up')   #Maximize all browser windows to align the [x] buttons on the same coordinates.
        time.sleep(0.5)        
    print("Done")

def closeBrowsers():
    print("Closing Browsers...")                
    pyautogui.moveTo(Xx,Xy,duration=2)
    pyautogui.click(Xx, Xy, clicks=numberOfBrowsers, interval=0.5, button='left')
    print("Done")

def touchBrowsers():
    i=0
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
        pyautogui.click(x, y, clicks=1, interval=4, button='left')
        i=i+2
    else:
        print("Done") 

def shakeMouse():
    i=0
    print("Shaking Mouse to call the Ads... recording lenght=%d" % (len(mouseShakingRecording)) )                
    while i < len(mouseShakingRecording):     
        x=mouseShakingRecording[i]
        y=mouseShakingRecording[i+1]
        print("sample: ", i, "x=",x, "y=",y )
        pyautogui.moveTo(x,y,duration=0.1)
        i=i+2
    else:
        print("Done")               

def searchSomething(url):
    print("  Searching something in the browser...")                
    pyautogui.moveTo(searchBar_x,searchBar_y,duration=1)
    pyautogui.click(searchBar_x, searchBar_y, clicks=1, interval=0.1, button='left')    
    pyautogui.write(url, interval=0.05)
    pyautogui.press('enter')
    print("  Done")

def clickAdsNotifications():
    print("Clicking on the Ads Notifications...")
    pyautogui.moveTo(adsNotificationX,adsNotificationY,duration=1)
    pyautogui.click(adsNotificationX, adsNotificationY, clicks=21, interval=3, button='left')
    print("Done")            

printMainMenu()
while(True):
    time.sleep(0.2)

    if(keyboard.is_pressed('0')):

        printRecordingMenu()
        while(True):
            time.sleep(0.2)

            if(keyboard.is_pressed('0')):
                print ("Recording the ADS Notification deletion sequence... Press ENTER to finish")        
                deleteAdsSequence=[]  # delete the array        
                time.sleep(1)   
                print("deleteAdsSequence=[",end='')     
                while (True):
                    if (mouse.is_pressed("left")):
                        x,y=mouse.get_position()
                        while (mouse.is_pressed("left")==True):
                            pass
                        deleteAdsSequence.extend([x,y])
                        print("%d,%d," % (x,y),end='')
                    if(keyboard.is_pressed('enter')):
                        break
                print("\b]")                
                printRecordingMenu()

            if(keyboard.is_pressed('1')):
                print ("Recording Mouse Shaking Movements sequence... Press ENTER to finish")        
                mouseShakingRecording=[]  # delete the array                
                time.sleep(1)        
                i=0
                mouseShakingRecording.clear()
                print("mouseShakingRecording=[",end='')
                while(True):
                    time.sleep(0.1)
                    x,y=mouse.get_position()
                    mouseShakingRecording.extend([x,y])
                    print("%d,%d," % (x,y), end='')
                    if(keyboard.is_pressed('enter')):
                        break
                print("\b]")
                printRecordingMenu()

            if(keyboard.is_pressed('2')):
                print ("Recording opened Brave browsers icons locations... Press ENTER to finish")        
                browsersLocationsInTaskbar=[]  # delete the array                
                time.sleep(1)        
                print("browsersLocationsInTaskbar=[",end='')
                while (True):
                    if (mouse.is_pressed("left")):
                        x,y=mouse.get_position()
                        while (mouse.is_pressed("left")==True):
                            pass
                        browsersLocationsInTaskbar.extend([x,y])
                        print("%d,%d," %(x,y),end='')
                    if(keyboard.is_pressed('enter')):
                        break
                print("\b]")
                printRecordingMenu()

            if(keyboard.is_pressed('3')):
                print ("Recording [X] button coordinates...")
                time.sleep(1)        
                while (mouse.is_pressed("left")==False):
                    pass
                Xx,Xy=mouse.get_position()
                print("Xx,Xy=[%d,%d]" %(Xx,Xy))
                printRecordingMenu()

            if(keyboard.is_pressed('4')):
                print ("Recording the Search Bar coordinates...")
                time.sleep(1)        
                while (mouse.is_pressed("left")==False):
                    pass
                searchBar_x,searchBar_y=mouse.get_position()
                print("searchBar_x,searchBar_y=[%d,%d]" % (searchBar_x,searchBar_y))
                printRecordingMenu()

            if(keyboard.is_pressed('5')):
                print ("Recording 'Ads received this month' counter coordinates...")
                time.sleep(1)        
                while (mouse.is_pressed("left")==False):
                    pass
                adsCounterx,adsCountery=mouse.get_position()
                print("adsCounterx,adsCountery=[%d,%d]" % (adsCounterx,adsCountery))
                printRecordingMenu()

            if(keyboard.is_pressed('6')):
                print ("Recording Record the captcha target shape text coordiantes...")
                time.sleep(1)
                while (mouse.is_pressed("left")==False):
                    pass
                captchaX,captchaY=mouse.get_position()
                try:
                    pyautogui.screenshot("month.png", region=(captchaX,captchaY,50,50))
                except:
                    print("Error taking the snapshot. You need to place your Brave browser on your primary monitor.")
                print("captchaX,captchaY=[%d,%d]" %(captchaX,captchaY))
                printRecordingMenu()

            if(keyboard.is_pressed('7')):
                print ("Recording Ads Notification Area (Windows pop-ups)...")
                time.sleep(1)        
                while (mouse.is_pressed("left")==False):
                    pass
                adsNotificationX,adsNotificationY=mouse.get_position()
                print("adsNotificationX,adsNotificationY=[%d,%d]" %(adsNotificationX,adsNotificationY))
                printRecordingMenu()

            if(keyboard.is_pressed('esc')):
                printMainMenu()
                time.sleep(1)
                break

    if(keyboard.is_pressed('1')):

        printManualMenu()
        while(True):
            time.sleep(0.2)

            if(keyboard.is_pressed('0')):
                launchBrowsers()
                printManualMenu()
    
            if(keyboard.is_pressed('1')):
                launchBrowsersGetBalances()
                printManualMenu()

            if(keyboard.is_pressed('2')):
                print ("Clicking Browsers Icons in taskbar...")
                touchBrowsers()
                print("Done")
                printManualMenu()

            if(keyboard.is_pressed('3')):
                print ("Shaking the mouse...")
                shakeMouse()
                print("Done")
                printManualMenu()

            if(keyboard.is_pressed('4')):
                print ("Searching Github...")
                searchSomething("www.github.com/japeral")
                print("Done")
                printManualMenu()

            if(keyboard.is_pressed('5')):
                print ("Clicking Ads Notification Area...")
                clickAdsNotifications()
                print("Done")
                printManualMenu()        

            if(keyboard.is_pressed('6')):
                closeBrowsers()      
                printManualMenu()

            if(keyboard.is_pressed('esc')):
                printMainMenu()
                time.sleep(1)                
                break

    if(keyboard.is_pressed('2')):
        print ("Open at least 1 Brave Browser Profile manually and then and press ENTER")
        os.system("pause")
        while (True):
            launchBrowsers()
            for i in range(1,5):
                shakeMouse()            
                print ("Waiting 60 seconds... iteration %d" %i)
                time.sleep(60)          
                searchSomething("www.github.com/japeral")
                time.sleep(2)
                deleteAdsNotifications()
                time.sleep(2)
                if(keyboard.is_pressed('esc')):
                    break
            closeBrowsers()
        printMainMenu()

    if(keyboard.is_pressed('3')):
        print ("Open at least 1 Brave Browser Profile manually and then and press ENTER")
        os.system("pause")
        launchBrowsers()
        while (True):        
            touchBrowsers()        
            print ("Waiting 3 minutes... iteration %d")
            time.sleep(60*3)          
            searchSomething("www.github.com/japeral")
            time.sleep(5)
            deleteAdsNotifications()
            time.sleep(2)
            if(keyboard.is_pressed('esc')):
                break
        closeBrowsers()
        printMainMenu()

    if(keyboard.is_pressed('4')):
        print("Solving the monthly captcha...")
        cwd_backup = os.getcwd()
        for i in range(1,numberOfBrowsers):
            os.chdir ('C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\')         
            command = 'brave.exe --profile-directory="Profile %d"' % i
            os.system(command)
            time.sleep(0.5)
            pyautogui.press('esc')         #to close the 'Restore pages?' popup
            time.sleep(0.5)                
            pyautogui.hotkey('win','up')   #Maximize all browser windows to align the [x] buttons on the same coordinates.
            time.sleep(0.5)        
            print(">Profile %d launched:" % i )
            searchSomething("brave://rewards")
            time.sleep(1)   #Important to wait for the rewards to fully load.            

            #check if the orange rewards button is present
            os.chdir (cwd_backup)
            try:                 
                location = pyautogui.locateOnScreen('claim.png')                   
                center = pyautogui.center(location)
                x,y=center
                pyautogui.click(x, y, clicks=1, interval=0.5, button='left')
                print("  Rewards 'Claim' Button detected @ %d,%d" %(x,y) )
            except:
                #check if the X orange rewards button is present
                try:                    
                    location = pyautogui.locateOnScreen('claim_x.png')
                    center = pyautogui.center(location)
                    x,y=center
                    pyautogui.click(x, y, clicks=2, interval=1, button='left')  # Close and reload captcha
                    print("  Rewards 'Claim X' Button detected @ %d,%d" %(x,y) )
                except:
                    print("  Rewards 'Claim' or 'Claim X' buttons are not present!, continue...")
                    pyautogui.hotkey('ctrl','w')  #close browaser tab
                    continue

            pyautogui.click(captchaX+200, captchaY, clicks=1, interval=0.5, button='left')
            pyautogui.vscroll(200)  #click in needed before of scrolling
            time.sleep(1)    

            #capture the target
            pyautogui.moveTo(captchaX,captchaY,duration=1)
            pyautogui.doubleClick(captchaX,captchaY)       
            pyautogui.hotkey('ctrl','c')
            target=pyperclip.paste()
            print("  Detected target: %s" %target)
            time.sleep(0.5)  
            pyautogui.click(captchaX+200, captchaY, clicks=1, interval=0.5, button='left')

            xSnapShift=180
            ySnapShift=50
            xSnapSize=350
            ySnapSize=375
            img=pyautogui.screenshot("captcha_snap.png", region=(int(captchaX)-xSnapShift,int(captchaY)-ySnapShift,xSnapSize,ySnapSize))
            open_cv_image = numpy.array(img)
            open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2RGB)

            # Mask text
            cv2.rectangle(open_cv_image,  
                         (int(xSnapSize/5*2),int(0)),           #upper left corner
                         (int(xSnapSize),int(ySnapSize/5)), #bottom right corner
                         (255,255,255), -1)                     # color, fill solid

            gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (7, 7), 0)
            thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)[1]

            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            
            #init the captcha icons locations
            square_X=0
            square_Y=0
            circle_X=0
            circle_Y=0
            triangle_X=0
            triangle_Y=0
            redtriangle_X=0
            redtriangle_Y=0

            # loop over the contours
            i=0
            for c in cnts:
                # compute the center of the contour
                M = cv2.moments(c)
                try:
                    cX = int(M["m10"] / M["m00"])
                except:
                    cX=0
                try:
                    cY = int(M["m01"] / M["m00"])
                except:
                    cY=0

                #identify the shape by the number of vertices, 3=triangle, 4=square,5=pentagon,5+=circle
                shape = "unidentified"
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.04 * peri, True)
                if len(approx) == 3:
                    if i<3:
                        shape = "triangle"
                    if i==3:
                        shape = "red triangle"
                elif len(approx) == 4:
                    (x, y, w, h) = cv2.boundingRect(approx)
                    ar = w / float(h)
                    shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
                elif len(approx) == 5:
                    shape = "pentagon"
                else:
                    shape = "circle"            

                # draw the contour and center of the shape on the image
                cv2.drawContours(open_cv_image, [c], -1, (0, 255, 0), 2)
                cv2.circle(open_cv_image, (cX, cY), 7, (255, 0, 0), -1)
                cv2.putText(open_cv_image, shape, (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                # save the icons locations
                if shape == "square":
                    square_X=cX-xSnapShift+captchaX
                    square_Y=cY-ySnapShift+captchaY
                    print("  square detected at %d,%d" %(square_X,square_Y))
                if shape == "circle":
                    circle_X=cX-xSnapShift+captchaX
                    circle_Y=cY-ySnapShift+captchaY
                    print("  circle detected at %d,%d" %(circle_X,circle_Y))
                if shape == "triangle":
                    triangle_X=cX-xSnapShift+captchaX
                    triangle_Y=cY-ySnapShift+captchaY
                    print("  triangle detected at %d,%d" %(triangle_X,triangle_Y))
                if shape == "red triangle":
                    redtriangle_X=cX-xSnapShift+captchaX
                    redtriangle_Y=cY-ySnapShift+captchaY
                    print("  red triangle detected at %d,%d" %(redtriangle_X,redtriangle_Y))

                if(i==3):
                    # Discard the rest of the contours
                    break   
                i=i+1

            # Uncoment to Debug image procesing
            #cv2.imshow("gray", gray) 
            #cv2.imshow("blurred", blurred) 
            #cv2.imshow("thresh", thresh) 
            #cv2.imshow("shape detection", open_cv_image)  # show the image with 4 shapes detected
            #cv2.waitKey(0)

            # drag from red triangle and drop on target.
            if(redtriangle_X!=0 and redtriangle_Y!=0 and       #check if all the figures got detected
                    circle_X!=0 and      circle_Y!=0 and
                  triangle_X!=0 and    triangle_Y!=0 and
                    square_X!=0 and      square_X!=0     ):
                print("  Red Triangle shape detected!, solving the captcha...")
                pyautogui.moveTo(redtriangle_X,redtriangle_Y,duration=1,tween=pyautogui.easeInOutElastic)
                print("  Red Triangle grabbed!")
                if  target == "circle ":
                    print("  dropping into the circle target...")
                    pyautogui.dragTo(circle_X, circle_Y, duration=1,button='left',tween=pyautogui.easeInOutElastic)
                if target == "square ":
                    print("  dropping into the square target...")                 
                    pyautogui.dragTo(square_X, square_Y, duration=1,button='left',tween=pyautogui.easeInOutElastic)              
                if target == "triangle ":
                    print("  dropping into the triangle target...")                                
                    pyautogui.dragTo(triangle_X, triangle_Y, duration=1,button='left',tween=pyautogui.easeInOutElastic)                
                print("  Captcha solved!")
            else:
                i=i-2  # retry this browser
                print("  Error! one or more shapes where not properly detected, retry %d..." %i)                
                continue
            time.sleep(2)  #important, give time for the OK button to appear.

            #click in the OK button
            os.chdir (cwd_backup)
            rewardsButtonLocation = pyautogui.locateOnScreen('ok.png')
            try:                    
                rewardsButtonCenter = pyautogui.center(rewardsButtonLocation)
                x,y=rewardsButtonCenter
                pyautogui.click(x, y, clicks=1, interval=1, button='left')
                print("  Rewards 'OK' Button detected @ %d,%d" %(x,y) )
            except:
                print("  Rewards 'OK' Button is not present!, continue...")
                continue
            time.sleep(0.5)
            pyautogui.hotkey('ctrl','w')  #close browaser tab

        printMainMenu()


    if(keyboard.is_pressed('5')):
        print("Donating all the BAT balances...")
        cwd_backup = os.getcwd()
        for i in range(8,numberOfBrowsers):
            os.chdir ('C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\')         
            command = 'brave.exe --profile-directory="Profile %d"' % i
            os.system(command)
            time.sleep(0.5)
            pyautogui.press('esc')         #to close the 'Restore pages?' popup
            time.sleep(0.5)                
            pyautogui.hotkey('win','up')   #Maximize all browser windows to align the [x] buttons on the same coordinates.
            time.sleep(0.5)        
            print(">Profile %d launched:" % i )
            searchSomething("www.github.com/japeral")
            time.sleep(2)   #Important to wait for the rewards to fully load.            

            os.chdir (cwd_backup)

            #click in the Donate Triangle button
            try:
                rewardsButtonLocation = pyautogui.locateOnScreen('donate_triangle.png')
                rewardsButtonCenter = pyautogui.center(rewardsButtonLocation)
                x,y=rewardsButtonCenter
                pyautogui.click(x, y, clicks=1, interval=1, button='left')
            except:
                rewardsButtonLocation = pyautogui.locateOnScreen('donate_triangle_bluetick.png')
                rewardsButtonCenter = pyautogui.center(rewardsButtonLocation)
                x,y=rewardsButtonCenter
                pyautogui.click(x, y, clicks=1, interval=1, button='left')
            time.sleep(0.5)

            #click in the Send A Tip button
            rewardsButtonLocation = pyautogui.locateOnScreen('send_a_tip.png')
            rewardsButtonCenter = pyautogui.center(rewardsButtonLocation)
            x,y=rewardsButtonCenter
            pyautogui.click(x, y, clicks=1, interval=1, button='left')
            time.sleep(0.5)

            #click in the 5BAT Button
            try:
                rewardsButtonLocation = pyautogui.locateOnScreen('5BAT.png')
                rewardsButtonCenter = pyautogui.center(rewardsButtonLocation)
                x,y=rewardsButtonCenter
                pyautogui.click(x, y, clicks=1, interval=1, button='left')
                time.sleep(0.5)
            except:
                print("  5BAT button not detected...")

            #click in the Send a TIp Button
            try:
                rewardsButtonLocation = pyautogui.locateOnScreen('SendTipButton.png')
                rewardsButtonCenter = pyautogui.center(rewardsButtonLocation)
                x,y=rewardsButtonCenter
                pyautogui.click(x, y, clicks=1, interval=1, button='left')
                time.sleep(0.5)
            except:
                print("  Not enough Balance, continue...")

            pyautogui.hotkey('ctrl','w')  #close browaser tab

        printMainMenu()


    if(keyboard.is_pressed('esc')):
        print("Bye bye")
        time.sleep(1)        
        break
