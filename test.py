from PIL import ImageGrab  # तेज़ स्क्रीनशॉट के लिए
import time
import keyboard

# सिर्फ गेम एरिया का स्क्रीनशॉट लें (आपके स्क्रीन रेजोल्यूशन के अनुसार एडजस्ट करें)
GAME_REGION = (700, 280, 900, 350)  # (x, y, width, height)

def is_white(pixel):
    """पिक्सेल वाइट है या नहीं"""
    return pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255

def is_black(pixel):
    """पिक्सेल ब्लैक है या नहीं"""
    return pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0

print("बॉट शुरू हो रहा है... 's' दबाकर बंद करें!")

while True:
    # सिर्फ गेम एरिया का स्क्रीनशॉट लें (फास्ट प्रोसेसिंग के लिए)
    im = ImageGrab.grab(bbox=GAME_REGION)

    # स्क्रीन पिक्सल और ऑब्स्टेकल पिक्सल                                  
    screen = im.getpixel((45, 35))

    nearby_pixels = [
        im.getpixel((45, 40)),  # नीचे का पिक्सेल
        im.getpixel((50, 35)),  # दाएं
        im.getpixel((40, 35)),  # बाएं
        im.getpixel((45, 30))   # ऊपर
    ]

    # ऑब्स्टेकल डिटेक्शन और स्पेस प्रेस
    if is_white(screen):
        if any(not is_white(p) for p in nearby_pixels):
            keyboard.press('space')
            time.sleep(0.01)
            keyboard.release('space')

    else:
        if any(not is_black(p) for p in nearby_pixels):
            keyboard.press('space')
            time.sleep(0.01)
            keyboard.release('space')

    # 's' दबाकर बंद करें
    if keyboard.is_pressed('s'):
        print("बॉट बंद हो रहा है...")
        break
       