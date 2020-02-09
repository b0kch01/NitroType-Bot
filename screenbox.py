# Nathan Choi Feb 2020
# Python box class for screen capture
import pyautogui


class Box:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_box():
        coords = []
        for i in range(1, 3):
            print(f"Press [{i}] "
                  "when cursor is on the upper-left corner of the text box")
            while(not keyboard.is_pressed("1")):
                coords[i - 1] = pyautogui.position()

        x1, y1, x2, y2 = (coord1.x, coord1.y, coord2.x, coord2.y)
