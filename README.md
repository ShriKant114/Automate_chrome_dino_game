# Automate_chrome_dino_game

### 🕹️ **Automated Pixel Detection and Key Press Bot**

This script uses Python's `pyautogui` and `keyboard` libraries to automate key presses based on pixel color detection on the screen. 

---

### ⚙️ **Features**
- 🎯 **Pixel Detection:** Captures the current screen and analyzes specific pixel colors.  
- 🔍 **Color Conditions:**  
  - If the target pixel is white but nearby pixels are not white → Presses the `space` key.  
  - If the target pixel is black but nearby pixels are not black → Presses the `space` key.  
  - If quadrant pixels contain colors other than black or white → Presses the `down` arrow key.  
- 🛑 **Exit Condition:** Press the `s` key to stop the script.

---

### 🚀 **How to Use**
1. Install the required libraries:  
```bash
pip install pyautogui keyboard
```
2. Run the script:
```bash
python main.py
```
3. Press `s` anytime to exit the script.

---

### ⚠️ **Important Notes**
- The script continuously takes screenshots, which may consume significant system resources.  
- The pixel coordinates are hardcoded. You may need to adjust them according to your screen resolution and target area.  

---

✅ **Use Case:** This bot can be used for simple automation tasks like auto-clickers, auto-jumping in games, or automated testing scenarios.
