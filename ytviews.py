import pyautogui
import sys
import time

def userinput():
    #no of time to watch
    no_time = input('enter no of view you want to increase : ')
    dur_video = input('enter the duration of video in seconds : ')
    url_video = input('enter link of video : ')
    time = int(dur_video)
    extratime = 25
    totaltime = time + extratime
    openterminal(totaltime,no_time)
    open_firefox()
    watch(no_time,dur_video,url_video)
    
    
def open_firefox():

    # Printing basic message
    print('Opening Firefox...')

    # Location the start button
    pyautogui.press('win')
    time.sleep(2)

    # Search for Firefox in the menu search
    pyautogui.typewrite('firefox')
    pyautogui.typewrite('\n')
    
    # Print message
    print('Firefox is now open and running.')
    #_location_=pyautogui.center(_start_button_)

   
# Function used to locate GMail
def type1(dur_video,url_video):
    
    #Sleep for a while and wait for Firefox to open
    time.sleep(6)

    # Printing message
    print('Opening youtube')
    
    #pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('a'); pyautogui.keyUp('ctrlleft')
    pyautogui.write(url_video)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('space')
    
    time.sleep(int(dur_video))
    

def newtab():
    #opens new tab
    print('opening new tab')
    pyautogui.hotkey('ctrl','t')
    
   
def watch(no_time,dur_video,url_video):
  
    for x in range(int(no_time)):
       pyautogui.hotkey('ctrl','t')
       time.sleep(3)
       type1(dur_video,url_video)
       
    print('done' +no_time+ 'watch')    

 
def ext():
    print('Exiting...')
    sys.exit()
    
    
def openterminal(totaltime,no_time):
    pyautogui.hotkey('ctrlleft','alt','t')
    time.sleep(6)
    pyautogui.write('aut')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.typewrite(str(totaltime))
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite(no_time)
    pyautogui.press('enter')
    time.sleep(2)
    print('vpn started success fully')


result = open("title.txt", "r")
print(result.read()) 

userinput()


