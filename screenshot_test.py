# Important Libraries
from PIL import Image, ImageGrab # Image processing, Screenshoting
import pyautogui # Mouse position
import pytesseract # ML Algorithm to detect language in image
import keyboard # Emulating Input
import time # Time controlling

print("Nitro Type Bot by b0kch01\nEnjoy! :)\n")

# This method returns coordinates of mouse
def get_box():
	while(not keyboard.is_pressed("1")):
		coord1 = pyautogui.position()
	while(not keyboard.is_pressed("2")):
		coord2 = pyautogui.position()
	return (coord1.x, coord1.y, coord2.x, coord2.y)

# Store the coordinates into global varibles
x1, y1, x2, y2 = get_box()
keyboard.wait("esc") # Wait for [esc] until proceeeding

# Main Typing bot
print("And it's off!\n")
# Take the screen shot, given box coordinates.
# Convert to grayscale image for better accuracy from tesseract
image = ImageGrab.grab(bbox=(x1, y1, x2, y2)).convert("LA")
image.save("screenshot_test.png")
# Get text from the image_to_string model and remove new lines
text = pytesseract.image_to_string(image, lang="eng").replace("\n", "")
# Write the text from tesseract
print(text)

print("Zoomed to the finish line!")
