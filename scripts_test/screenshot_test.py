# Important Libraries
from PIL import Image, ImageGrab # Image processing, Screenshoting
import pyautogui # Mouse position
import keyboard # Emulating Input
import platform

print("Testing Screen Shot accuracy\n")

def get_box():
	while(not keyboard.is_pressed("1")):
		coord1 = pyautogui.position()
	while(not keyboard.is_pressed("2")):
		coord2 = pyautogui.position()
	return (coord1.x, coord1.y, coord2.x, coord2.y)

x1, y1, x2, y2 = get_box()
if platform.system() == "Darwin":
	x2 *= 2
	y2 *= 2

# Main Typing bot
print("Coordinates Measured!\n")

print(x1, y1, x2, y2)
image = ImageGrab.grab(bbox=(x1, y1, x2, y2)).convert("LA")
image.save("screenshot_test.png")

print("Finished.")
