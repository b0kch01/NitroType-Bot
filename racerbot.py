# Nitro Type bot by b0kch01
# Thanks Google for tesseract

print("Nitro Type Bot by b0kch01\n\n")
print("Checking for dependencies...")

try:
    # Important Libraries
    from box import Box
    from PIL import Image, ImageGrab  # Image processing, Screenshoting
    import pytesseract  # ML Library to detect words in image
    import keyboard  # fast keyboard emulating
    import time  # Loop control, delays
except:
    print("Error: Could not import modules")
    print("Please check to:")
    print("\t1) Tesseract installed with correct PATH")
    print("\t2) Other modules are installed with pip")
    exit()

print("Remember, hold [esc] to formally exit the bot")
print("Enjoy! :)")


def isfloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


try:
    # Set delay (seconds)
    delay = input("Set the bot delay in seconds (0 is bannable, 4 is not) >")
    while (not isfloat(delay)):
        delay = input("Sorry, I don't think that was in seconds (try again) >")

    # Store the coordinates
    x1, y1, x2, y2 = get_box()

    print("\n[ Summary ]\n------------>")
    print("Delay: " + delay)
    print("Top left corner: {}, {}".format(x1, y1))
    print("Bottom right corner: {}, {}".format(x2, y2))
    print("\n\nPress [Esc] at the last yellow light")

    keyboard.wait("esc")  # Wait for [esc] until proceeeding
    print("Wait a second...")
    time.sleep(1)
    # Main Typing bot
    print("And it's off!")

    text = ""
    while not keyboard.is_pressed("esc"):
        # Take the screen shot, given box coordinates.
        # Convert to grayscale image for better accuracy from tesseract
        image = ImageGrab.grab(bbox=(x1, y1, x2, y2)).convert("LA")
        # Get text from the image_to_string model and remove new lines
        text = pytesseract.image_to_string(image, lang="eng").replace("\n", "")
        # Write the text from tesseract
        keyboard.write(text)
        time.sleep(float(delay))

except KeyboardInterrupt:
    print("\n\nexited with KeyboardInterrupt")

except:
    print("An unexpected error occurred :(")
    print("")

# Done with code
exit()
