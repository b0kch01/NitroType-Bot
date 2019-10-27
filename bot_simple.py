# Nitro Type bot by b0kch01
# Thanks Google for tesseract

# Important Libraries
from PIL import Image, ImageGrab
from pynput.keyboard import Key, Listener
from tkinter import *
from tkinter.ttk import * 
import pyautogui 
import pytesseract 
import keyboard 
from time import sleep

print("Nitro Type Bot by b0kch01\n\nRemember, hold [Esc] to *formally* exit the bot\nEnjoy! :)\n")

def get_box(): 
	print("\nPress [1] with the cursor on the upper left corner of the text box")
	while(not keyboard.is_pressed("1")):
		coord1 = pyautogui.position()
	print("Press [2] with the cursor on the lower right corner of the text box")
	while(not keyboard.is_pressed("2")):
		coord2 = pyautogui.position()
	return (coord1.x, coord1.y, coord2.x, coord2.y)

def scanning():
	global ok
	global running
	if running:
		image = ImageGrab.grab(bbox=(x1, y1, x2, y2)).convert("LA")
		text = pytesseract.image_to_string(image, lang="eng").replace("\n", "")
		keyboard.write(text)
		print(text)
		if ("Borge" in text or "$0" in text or "XP" in text or len(text) == 0 or text == ""):
			runnning = False
			sleep(3)
			ok = True
		root.after(1, scanning)
	else:
		root.after(3000, scanning)

def stop():
	global ok
	print("stop")
	global running
	running = False
	ok = True
	sleep(3)

def start():
	global ok
	if ok:
		print("start")
		global running
		running = True
		ok = False


running = False
ok = True
root = Tk()
root.title("NitroType Bot by b0kch01")
root.geometry("350x60")

stop = Button(root, text="Emergency Stop", command=stop)
start = Button(root, text="Go!", command=start)
stop.pack(side="top")
start.pack(side="top")


x1, y1, x2, y2 = get_box()
print("Done.")

scanning()
root.attributes("-topmost", True)
root.mainloop()
	