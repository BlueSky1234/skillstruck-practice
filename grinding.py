'''
This program is for automating random wasd string combos. 
You need to adjust the region near line 49 for the keys to be detectable.
Ensure the following is installed- 'pip install pyautogui pytesseract pillow keyboard pynput'
Ctrl+shift+q to abort or hold 'l.'
Check games TOS before using this software.

Once the script is started, click onto the designated window.
The 'grinding' variable is used to control the main loop.
A failsafe check starts the loop followed by a screenshot and image enhancements(for better letter detection).
Letters are then found, sanatized, and enter a for loop where the letters are inputed/outputed into the computer.
Typing speed varies to reflect human input.
'''
import pyautogui as pag
import time
import pytesseract
from PIL import Image, ImageEnhance
import keyboard
import os
from pynput.keyboard import Controller
import random
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
keyboard_controller = Controller()
grinding = True

#Failsafe Number 1
def l_check():
    global grinding
    if keyboard.is_pressed('l') or keyboard.is_pressed('ctrl+shift+q'):
        grinding = False

def enhancements(screenshot):
    #Changes the Image for better letter recognition
    screenshot = screenshot.convert('L')  #GrayScale
    contrast_enhancer = ImageEnhance.Contrast(screenshot)
    screenshot = contrast_enhancer.enhance(2)
    sharpness_enhancer = ImageEnhance.Sharpness(screenshot)
    screenshot = sharpness_enhancer.enhance(2)
    brightness_enhancer = ImageEnhance.Brightness(screenshot)
    screenshot = brightness_enhancer.enhance(1.2)
    return screenshot    

try:

    while grinding:
        l_check()
        
        #Capture Screenshot in designated area  and uses tesseract to extract readable text
        image = pag.screenshot(region=(1371, 531, 542, 150)) 
        
        image = enhancements(image)
        
        #Filters readable string
        text = pytesseract.image_to_string(image, config='--psm 7 -c tessedit_char_whitelist=WASDwasd')
        text = text.replace('\n', '').strip()
        
        l_check()
        for character in text:
            if not grinding:
                break
            #Random time range replicates natural human input
            random_time = random.uniform(0.15, 0.2)
            if character.lower() in 'wasd':
                print(character)
                #Simulate key press
                keyboard_controller.press(character.lower())
                keyboard_controller.release(character.lower())
                # Time performance to simulate random human input
                keypress_start_time = time.perf_counter()
                delay = random_time - (time.perf_counter() - keypress_start_time)
                if delay > 0:
                    time.sleep(delay)

except KeyboardInterrupt:
    print("KeyboardInterrupt: Exiting the loop.")
    grinding = False
except Exception as e:
    print(f"An error occured: {e}")
    grinding = False
finally:
    print("Exiting the loop.")
