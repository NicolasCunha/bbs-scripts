import pyautogui

def locate_with_confidence(file):
    return pyautogui.locateOnScreen(file, grayscale=False, confidence=.8)

def check_bleach_brave_souls_window_open():
    return locate_with_confidence('./resources/bleach-brave-souls-window-title.png') != None

def locate_and_click_multiples(*locations):
    for location in locations:
        if (not locate_and_click(location)):
            return False
    return True

def locate_and_click(location):

    foundLocation = locate_with_confidence(location)
    if (foundLocation):
        tmpLocation = pyautogui.center(foundLocation)
        pyautogui.click(tmpLocation)
        return True
    return False

while (True):

    # Wait for Bleach Brave Souls to be opened
    if (not check_bleach_brave_souls_window_open()):
        continue

    # Prepare for Quest & Other Clicks
    if (locate_and_click('./resources/prepare-for-quest.png')
        or locate_and_click_multiples('./resources/stamina-bonus.png',
                                      './resources/atk-bonus.png',
                                      './resources/def-bonus.png',
                                      './resources/focus-bonus.png')
        or locate_and_click('./resources/start-quest.png')
        or locate_and_click('./resources/skip.png')
        or locate_and_click('./resources/next-quest.png')
        #or locate_and_click('./resources/retry.png')
        or locate_and_click('./resources/clear-time.png')
        or locate_and_click('./resources/quest-clear.png')
        or locate_and_click_multiples('./resources/friend-request-confirm.png', 
                                      './resources/cancel.png')):
        continue
