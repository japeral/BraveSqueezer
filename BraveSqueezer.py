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
numberOfBrowsers = 60
browsersLocationsInTaskbar = arr.array('i')
mouseShakingRecording      = arr.array('i')
deleteAdsSequence          = arr.array('i')
adsThisMonthCounters       = arr.array('i')
workbook = Workbook()
sheet = workbook.active

#Laptop--------------------------------------------------------------------------------------------------------------------------------
deleteAdsSequence=[1883,1057,1861,660,1883,1059]
mouseShakingRecording=[ 649,308,796,254,984,266,1043,390,1051,543,999,644,905,723,800,735,645,673,603,507,690,321,852,249,
                        993,313,1098,485,1086,598,1035,645,1024,646,1024,646,1024,646,1024,646,1024,646,1024,646,1024,646,
                        1024,646,1024,646,1024,646,1024,646]
browsersLocationsInTaskbar=[]
Xx,Xy=[1898,11]
searchBar_x,searchBar_y=[818,46]
adsCounterx,adsCountery=[1004,591]
captchaX,captchaY=[1205,408]
adsNotificationX,adsNotificationY=[1747,931]

#-------------------------------------------------------------------------------------------------------------------------------------

#Sharkon--------------------------------------------------------------------------------------------------------------------------------
#deleteAdsSequence=[1246,1000,1219,756,1246,1007]
#mouseShakingRecording=[1929,321,2047,254,2114,245,2184,242,2261,306,2300,370,2316,457,2306,579,2260,655,2214,698,2121,748,2019,782,1902,784,
#                       1816,766,1708,691,1647,614,1599,518,1568,399,1577,283,1625,217,1735,193,1925,202,2095,231,2182,260,2235,323,2257,434,
#                       2219,552,2071,743,1878,838,1654,756,1508,445,1551,226,1760,140,1953,167,2087,251,2090,403,1897,626,1619,759,1454,658,
#                       1437,459,1571,333,1697,330,1878,433,1926,502,1928,607,1887,689,1854,711,1829,695,1782,604,1773,503,1776,381,1799,281,
#                       1836,201,1901,164,2019,168,2147,188,2212,219,2273,295,2316,439,2300,553,2215,632,2100,670,1961,656,1718,582,1562,556,
#                       1496,603,1448,743,1491,809,1721,841,2073,827,2339,734,2441,464,2448,291,2403,141,2190,74,2069,76,1801,152,1615,220,
#                       1501,292,1444,385,1490,491,1641,562,1833,526,1981,516,2089,575,2097,646,2022,721,1899,709,1869,673,1920,642,2013,634,
#                       2029,602,2028,586]
#browsersLocationsInTaskbar=[]
#Xx = 2537
#Xy = 8
#searchBar_x=1610
#searchBar_y=38
#adsCounterx=1973
#adsCountery=714
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


print("Brave ADs Squeezer v1.3")
print("                                          by Jose Peral, 3rd March 2021")
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
    print("  Type  '2'  to run the automated Ads extraction loop! ")
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
    print("    Type  '0'  to launch the %d Brave Browser instances only" %numberOfBrowsers)
    print("    Type  '1'  to launch the %d Brave Browser search /rewards and collect ads balances into a spreadsheet" %numberOfBrowsers)
    print("    Type  '2'  to Close all browsers ")  
    print("    Type  '3'  to Solve monthly Captcha")
    print("    Type  '4'  to Click all 21 notifications")
    print("    Type  '5'  to Click the browsers icons in the taskbar")
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
        searchRewards()        
        time.sleep(0.5)
        pyautogui.moveTo(adsCounterx,adsCountery,duration=1)
        pyautogui.vscroll(200)
        time.sleep(0.5)                
        pyautogui.doubleClick(adsCounterx,adsCountery)
        time.sleep(0.5)        
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
    filename=[]
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
        pyautogui.click(x, y, clicks=1, interval=4, button='left')
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

def clickAdsNotifications():
    print("Clicking on the Ads Notifications...")
    pyautogui.moveTo(adsNotificationX,adsNotificationY,duration=1)
    pyautogui.click(adsNotificationX, adsNotificationX, clicks=21, interval=3, button='left')
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
                closeBrowsers()      
                printManualMenu()

            if(keyboard.is_pressed('3')):

                print("Solving the monthly captcha...")
                #opening rewards
                pyautogui.press('esc')         #to close the 'Restore pages?' popup
                time.sleep(0.5)                
                pyautogui.hotkey('win','up')   #Maximize all browser windows to align the [x] buttons on the same coordinates.
                time.sleep(0.5)        
                searchRewards()        
                time.sleep(0.5)

                #check if the orange rewards button is present
                rewardsButtonLocation = pyautogui.locateOnScreen('QRCode_button.png')
                #rewardsButtonLocation = pyautogui.locateOnScreen('Rewards_button.png')
                try:                    
                    rewardsButtonCenter = pyautogui.center(rewardsButtonLocation)
                    x,y=rewardsButtonCenter
                    #pyautogui.click(x,y)
                except:
                    print("Rewards button not present!, exiting...")
                    break
                time.sleep(1)

                #capture the target
                pyautogui.moveTo(captchaX,captchaY,duration=1)
                pyautogui.vscroll(200)
                time.sleep(0.5)
                pyautogui.doubleClick(captchaX,captchaY)
                time.sleep(0.5)        
                pyautogui.hotkey('ctrl','c')
                target=pyperclip.paste()
                print("Detected target: %s" %target)

                #img=pyautogui.screenshot("screenshot.png", region=(int(captchaX),int(captchaY),400,500))
                #open_cv_image = numpy.array(img)
                open_cv_image = cv2.imread("screenshot.png")

                #open_cv_image = open_cv_image[:, :, ::-1].copy()         # Convert RGB to BGR 
                open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2RGB)
                

                #cv2.imshow('image',open_cv_image)
                #cv2.waitKey(0)        
                    
                gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
                #cv2.imshow('gray',gray)
                #cv2.waitKey(0)        

                blurred = cv2.GaussianBlur(gray, (17, 17), 0)
                #cv2.imshow('blurred',blurred)
                #cv2.waitKey(0)        

                thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)[1]
                #cv2.imshow('thresh',thresh)
                #cv2.waitKey(0)        

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
                        shape = "triangle"
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

                    # show the image
                    cv2.imshow("Image", open_cv_image)
                    cv2.waitKey(0)
                    i=i+1

                    # save the icons locations
                    if (i<3 and shape == "square"):
                        square_X=captchaX+cX
                        square_Y=captchaY+cY
                        print("square detected at %d,%d" %(square_X,square_Y))
                    if (i<3 and shape == "circle"):
                        circle_X=captchaX+cX
                        circle_Y=captchaY+cY
                        print("circle detected at %d,%d" %(circle_X,circle_Y))
                    if (i<3 and shape == "triangle"):
                        triangle_X=captchaX+cX
                        triangle_Y=captchaY+cY
                        print("triangle detected at %d,%d" %(triangle_X,triangle_Y))
                    if (i>=3 and shape == "triangle"):
                        redtriangle_X=captchaX+cX
                        redtriangle_Y=captchaY+cY
                        print("red triangle detected at %d,%d" %(redtriangle_X,redtriangle_Y))                        
                    if (i==4):
                        break  # Discard the rest of the contours           

                #debug
                target="circle"

                # drag from red triangle and drop on target.
                if(redtriangle_X!=0 and redtriangle_Y!=0):
                    print("Red Triangle shape detected!, solving the captcha...")
                    pyautogui.moveTo(redtriangle_X,redtriangle_Y,duration=4,tween=pyautogui.easeInOutElastic)
                    pyautogui.mouseDown(button='left')
                    if  (target == "circle"):
                        print("dropping into the circle target...")
                        pyautogui.moveTo(circle_X,circle_Y,duration=4,tween=pyautogui.easeInOutElastic)
                    elif(target == "square"):
                        print("dropping into the square target...")                
                        pyautogui.moveTo(square_X,square_Y,duration=4,tween=pyautogui.easeInOutElastic)                
                    elif(target == "triangle"):
                        print("dropping into the triangle target...")                                
                        pyautogui.moveTo(triangle_X,triangle_Y,duration=4,tween=pyautogui.easeInOutElastic)

                    pyautogui.mouseUp(button='left')
                    print("Captcha solved!")
                else:
                    print("Error! Red Triangle not detected.")
                
                cv2.destroyAllWindows()        
                cv2.waitKey(0)
                printManualMenu()

            if(keyboard.is_pressed('4')):
                print ("Clicking Ads Notification Area...")
                clickAdsNotifications()
                print("Done")
                printManualMenu()        

            if(keyboard.is_pressed('5')):
                print ("Clicking Browsers Icons...")
                touchBrowsers()
                print("Done")
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
                searchSomething()    
                time.sleep(2)
                deleteAdsNotifications()
                time.sleep(2)
                if(keyboard.is_pressed('esc')):
                    break
            closeBrowsers()
        printMainMenu()


    if(keyboard.is_pressed('esc')):
        print("Bye bye")
        time.sleep(1)        
        break
