import  pyautogui
import time

previous_color = None
    
while True:
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((100,100))
    
    if previous_color is not None and pixel_color != previous_color:
        print("Pixel color changed!")
    
    previous_color = pixel_color
    # Sleep for ten seconds
    time.sleep(10)