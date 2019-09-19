# Nitro Type bot by b0kch01
# Thanks Google for tesseract

# [press 1]-----------------------
# |	     Cover the whole         |
# |	     textbox                 |
# |	     for the best            |
# |	     result!                 |
# |	     Happy Racing!           |
# |----------------------[press 2]


# Controls: 1 to set first mouse coordinate, 2 to set the second.
# 			After coordinates are set, press [esc] to start! 
#			There is a 1 second delay before the bot starts	
# 			To stop the typing, press [esc]


# Important Libraries
from PIL import Image, ImageGrab # Image processing, Screenshoting
import pyautogui # Mouse position
import pytesseract # ML Algorithm to detect language in image
import keyboard # Emulating Input
import time # Time controlling
import platform # Cross-Platform Capatbillity
import os # clear

print("Nitro Type Bot by b0kch01\n\nRemember, hold [Esc] to *formally* exit the bot\nEnjoy! :)\n")

f = open("output.txt", "w")

def isfloat(number):
	try:
		float(number)
		return True
	except ValueError:
		return False

try :
	# Set delay (seconds)
	delay = input("Set the bot delay in seconds (4 is unbannable, 0 is not) >")
	while (not isfloat(delay)):
		delay = input("Sorry, I don't think that was in seconds (try again )>")

	# This method returns coordinates of mouse
	def get_box(): 
		print("\nPress [1] with the cursor on the upper left corner of the text box")
		while(not keyboard.is_pressed("1")):
			coord1 = pyautogui.position()
		print("Press [2] with the cursor on the upper left corner of the text box")
		while(not keyboard.is_pressed("2")):
			coord2 = pyautogui.position()
		return (coord1.x, coord1.y, coord2.x, coord2.y)

	# Store the coordinates into global varibles
	os = platform.system();
	x1, y1, x2, y2 = get_box()
	if os == "Darwin":
		x2 *= 2
		y2 *= 2

	print("\n[ Summary ]\n------------>")
	print("Delay: " + delay)
	print("Top left corner: {}, {}".format(x1, y1))
	print("Bottom right corner: {}, {}".format(x2, y2))

	print("\n[ Summary ]\n------------>", file=f)
	print("Delay: " + delay, file=f)
	print("Top left corner: {}, {}".format(x1, y1), file=f)
	print("Bottom right corner: {}, {}".format(x2, y2), file=f)

	print("\n\nPress [Esc] at the last yellow light")
	keyboard.wait("esc") # Wait for [esc] until proceeeding
	time.sleep(1)

	# Main Typing bot
	print("And it's off!", file=f)
	print("And it's off!")

	text = ""
	while (not (keyboard.is_pressed("esc") or "Your Money" in text)):
		# Take the screen shot, given box coordinates.
		# Convert to grayscale image for better accuracy from tesseract
		image = ImageGrab.grab(bbox=(x1, y1, x2, y2)).convert("LA")
		# Get text from the image_to_string model and remove new lines
		text = pytesseract.image_to_string(image, lang="eng").replace("\n", "")
		# Write the text from tesseract
		keyboard.write(text, delay=0)
		print(time.strftime("\n[%H:%M:%S]:  ", time.gmtime()) + text, file=f)
		# Add delay to control WPM speeds!
		if (keyboard.is_pressed("esc")):
			break
		time.sleep(float(delay))

except KeyboardInterrupt:
	print("\n\n---> EXITED", file=f)
	f.close()

except SystemError:
	print("\nOops! Make sure to click [1] on the upper left and [2] on the lower right.")
	print("\nOops! Make sure to click [1] on the upper left and [2] on the lower right.", file=f)
	print("\n\n---> EXITED")
	print("\n\n---> EXITED", file=f)

