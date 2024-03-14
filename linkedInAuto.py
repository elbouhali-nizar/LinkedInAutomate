import pyautogui as auto
import pyscreeze
from time import sleep

# ********** Note: lines with comments eniding with !! can be changed based on your screen **********

# the following code is to know the exact position of the mouse in order to pass it with in the click method 

"""import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')"""




auto.click(x=966,y=1048) # it opens the browser
sleep(2)
auto.click(x=970,y=990) # click on the second open browser
sleep(1)

def connect_fun():
    for j in range(0,2): # to scroll down and show all available connections

        try:
            sleep(5)
            pos = list(auto.locateAllOnScreen('connect.png',confidence=0.9)) # to locate all connect buttons on the screen using ai
            for i in range(0,len(pos)):
                auto.click(pos[i][0]+30,pos[i][1]+20)
                sleep(5)
                try:
                    sleep(5)
                    posWith = auto.locateCenterOnScreen('sendWithout.png', confidence=0.9) # to locate send without note button on the screen using ai
                    auto.click(posWith)
                    sleep(2)
                    
                    
                    
                except auto.ImageNotFoundException: # when send without note is not available
                    sleep(5)
                    CloseButt = auto.locateCenterOnScreen('closeButt.png', confidence=0.9) # to locate close button on the screen using ai
                    auto.click(CloseButt)
                    sleep(2)
                    
        except pyscreeze.ImageNotFoundException: # when connect button cannot be found
            auto.moveTo(900,443)
            sleep(1)
        sleep(1)
        auto.moveTo(900,443)
        sleep(1)
        auto.scroll(-800) # to scroll down
        sleep(1)



for i in range(1,5): # number of pages you want the script to run on
    auto.click(x=575,y=81) # clicks on the search bar !!
    sleep(1)
    
    auto.write(f"https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=data%20engineer&origin=GLOBAL_SEARCH_HEADER&page={i}&sid=HH(") # link for linkedIn search while i is the number of the page
    auto.press('enter')
    sleep(10)
    
    connect_fun() # check previous function
    
    
    


    
    
