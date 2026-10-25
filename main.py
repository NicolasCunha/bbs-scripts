import pyautogui
import time

def locate_with_confidence(file):
    try:
        return pyautogui.locateOnScreen(file, grayscale=False, confidence=.8)
    except pyautogui.ImageNotFoundException:
        return None

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
        x, y = pyautogui.center(foundLocation)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        return True
    return False

msg_waiting_bbs = False

while (True):

    # Wait for Bleach Brave Souls to be opened
    if (not check_bleach_brave_souls_window_open()):
        if (not msg_waiting_bbs):
            print("Waiting for Bleach Brave Souls to be opened...")
            msg_waiting_bbs = True
        continue

    # Prepare for Quest & Other Clicks
    if (locate_and_click('./resources/prepare-for-quest.png')
        or locate_and_click_multiples('./resources/stamina-bonus.png',
                                      './resources/atk-bonus.png',
                                      './resources/def-bonus.png',
                                      './resources/focus-bonus.png')
        or locate_and_click('./resources/start-quest.png')
        or locate_and_click('./resources/skip.png')
        or locate_and_click_multiples('./resources/rewards-close.png', './resources/rewards-close-btn.png')
        or locate_and_click('./resources/next-quest.png')
        #or locate_and_click('./resources/retry.png')
        or locate_and_click('./resources/clear-time.png')
        or locate_and_click('./resources/quest-clear.png')
        or locate_and_click_multiples('./resources/friend-request-confirm.png', 
                                      './resources/cancel.png')
        or locate_and_click_multiples('./resources/network-error.png', './resources/network-error-retry-btn.png')):
        continue
