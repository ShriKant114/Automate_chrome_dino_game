import pyautogui as gui
import time
import keyboard

while True:
    img = gui.screenshot()

    # for screen pixel
    screen = img.getpixel((745, 298))
    
    x1 = img.getpixel((745, 310))
    x2 = img.getpixel((736, 311))
    x3 = img.getpixel((792, 309))                                                  
    x4 = img.getpixel((820, 308))        

    y1 = img.getpixel((746, 278))
    y2 = img.getpixel((734, 271))
    y3 = img.getpixel((740, 282))
    y4 = img.getpixel((737, 287))
                
    # it is check a color of white pixel
    def is_white(pixel):
        return pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255

    def is_black(pixel):
        return pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0

    # it is check a color of black pixel
    nearby_pixels = [x1, x2, x3, x4, y1, y2, y3, y4]

    if is_white(screen):
        if any(not is_white(p) for p in nearby_pixels):
            gui.press('space')
            # time.sleep(0.05)

    else:
        if any(not is_black(p) for p in nearby_pixels):
            gui.press('space')            
            # time.sleep(0.05)

    # press s for ending the game             
    if keyboard.is_pressed('s'):
        print("Exiting...")
        break
