# Nitro Type bot by b0kch01
# Thanks Google for tesseract

# [press 1]-----------------------
# |	     Cover the whole	     |
# |	     textbox 				 |
# |	     for the best 		     |
# |	     result!		         |
# |	     Happy Racing!	         |
# |----------------------[press 2]


# Controls: 1 to set first mouse coordinate, 2 to set the second.
# 			After coordinates are set, press [esc] to start! 
#			There is a 1 second delay before the bot starts	
# 			To stop the typing, press [esc]

# Set delay (seconds)
DELAY = 0

# Important Libraries
from PIL import Image, ImageGrab # Image processing, Screenshoting
import pyautogui # Mouse position
import pytesseract # ML Algorithm to detect language in image
import keyboard # Emulating Input
import time # Time controlling
import platform # Cross-Platform Capatbillity

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
if platform.system() == "Darwin":
	x2 *= 2
	y2 *= 2
keyboard.wait("esc") # Wait for [esc] until proceeeding
time.sleep(1)

# Main Typing bot
print("And it's off!\n")
while (not keyboard.is_pressed("esc")):
	# Take the screen shot, given box coordinates.
	# Convert to grayscale image for better accuracy from tesseract
	image = ImageGrab.grab(bbox=(x1, y1, x2, y2)).convert("LA")
	# Get text from the image_to_string model and remove new lines
	text = pytesseract.image_to_string(image, lang="eng").replace("\n", "")
	# Write the text from tesseract
	keyboard.write(text, delay=0)
	# Add delay to control WPM speeds!
	time.sleep(DELAY)

print("Zoomed to the finish line!")
