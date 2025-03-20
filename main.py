import pyautogui
import time
import keyboard

while True:
    im = pyautogui.screenshot()

    # स्क्रीन और आस-पास के पिक्सल
    screen = im.getpixel((745, 298))
    
    x1 = im.getpixel((745, 300))
    x2 = im.getpixel((736, 284))
    x3 = im.getpixel((792, 308))
    x4 = im.getpixel((820, 287))        

    y1 = im.getpixel((746, 301))
    y2 = im.getpixel((734, 285))
    y3 = im.getpixel((740, 298))
    y4 = im.getpixel((737, 298))
                
    # RGB वैल्यू चेक करना
    def is_white(pixel):
        return pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255

    def is_black(pixel):
        return pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0

    # स्पेस प्रेस करने की कंडीशन
    nearby_pixels = [x1, x2, x3, x4, y1, y2, y3, y4]

    if is_white(screen):
        if any(not is_white(p) for p in nearby_pixels):
            pyautogui.press('space')
            time.sleep(0.05)  # थोड़ा पॉज़ रखने के लिए

    else:
        if any(not is_black(p) for p in nearby_pixels):
            pyautogui.press('space')            
            time.sleep(0.05)

    # 's' दबाने पर लूप ब्रेक
    if keyboard.is_pressed('s'):
        print("Exiting...")
        break
