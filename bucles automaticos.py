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


launchBrowsers()
launchBrowsersGetBalances()
touchBrowsers()
clickAdsNotifications()
deleteAdsNotifications()
shakeMouse()
searchSomething("www.github.com/japeral")
searchSomething("brave://rewards")
closeBrowsers()