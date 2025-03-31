import pyautogui
import keyboard
import time
import random
import numpy as np
from questions1 import programming_requests as questions1
from questions2 import programming_requests as questions2

# Combine both question lists
programming_requests = questions1 

def auto_type(text):
    """
    Function to automatically type text
    :param text: Text to type
    """
    # Type each character
    for char in text:
        pyautogui.write(char)
        time.sleep(0.01)  # Wait 0.1 seconds between each character

def main():
    print("Auto typing program is ready!")
    print("Press F3 to exit")
    
    for i in range(100):
        # Choose a random request
        request = random.choice(programming_requests)
        
        # Type the request
        auto_type(request)
        auto_type("\n")
        auto_type("def \t")   
        auto_type("\n")                   
        # Wait 2 seconds before pressing tab
        print("\nWaiting 2 seconds before pressing tab...")
        time.sleep(2)
        
        # Press tab
        pyautogui.press('tab')
        auto_type("\n")
        time.sleep(1)
        pyautogui.press('tab')
        auto_type("\n")
        time.sleep(1)
        pyautogui.press('tab')
        auto_type("\n")
        time.sleep(1)
        pyautogui.press('tab')
        auto_type("\n")
        time.sleep(1)
        pyautogui.press('tab')
        auto_type("\n")
        time.sleep(1)
        pyautogui.press('tab')
        auto_type("\n")
        time.sleep(1)
        pyautogui.press('tab')
        auto_type("\n")
        auto_type("\n")
        
        # Delete all content
        pyautogui.hotkey('ctrl', 'a')  # Select all
        time.sleep(0.5)
        pyautogui.press('delete')      # Delete selected content
        time.sleep(0.5)
                
        # Wait 30 seconds before typing next request
        print("Waiting 1 seconds before typing next request...")
        time.sleep(1)
        
        # Check if user wants to exit
        if keyboard.is_pressed('f3'):
            print("Goodbye!")
            break

if __name__ == "__main__":
    # Wait 5 seconds for user to switch to Cursor window
    print("You have 5 seconds to switch to Cursor window...")
    time.sleep(5)
    main() 