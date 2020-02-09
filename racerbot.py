# Nitro Type bot by b0kch01
# Thanks Google for tesseract

print("Checking for dependencies...")

try:
    # Important Libraries
    from pyfiglet import Figlet  # Title text
    from termcolor import cprint  # Colorful terminal
    from screenbox import Box  # Storing screen-shot dimensions
    from PIL import Image, ImageGrab  # Image processing, Screenshoting
    import colorama  # Color support for legacy-consoles
    import pytesseract  # ML Library to detect words in image
    import keyboard  # Fast keyboard emulating
    import time  # Loop control, delays

    colorama.init()
    print("Successfuly imported!\n")
except:
    print("Error: Could not import modules")
    print("Please check to:")
    print("\t1) Tesseract installed with correct PATH")
    print("\t2) Other modules are installed with pip")
    exit()


def titlescreen():
    f = Figlet(font="doom")
    print(f.renderText("NitroType Bot"))
    cprint(" Created with ♥ by b0kch01! ", "grey", "on_white")
    cprint(" OCR Tesseract  by Google!  ", "grey", "on_cyan")
    print("==========================================")

    print("Remember, hold [esc] to exit the bot")
    print("- Enjoy! :)\n")


def isfloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def start_bot():
    try:
        # Set delay (seconds)
        delay = input("Guess delay in seconds >")
        while (not isfloat(delay)):
            delay = input(
                "Sorry, I don't think that was in seconds (try again) >")

        # Store the coordinates
        thisbox = Box()
        x1, y1, x2, y2 = thisbox.get_box()

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
            text = pytesseract.image_to_string(
                image, lang="eng").replace("\n", "")
            # Write the text from tesseract
            keyboard.write(text)
            time.sleep(float(delay))

    except KeyboardInterrupt:
        print("\n\nExited Unofficially: Remember to hold [esc] instead!")
    except:
        print("Oh No! Something went terribly wrong!")
        print("Create an issue on GitHub and I'll try to fix it :)")

    cprint("\nRaced to the finish line!", "green")


def prompt_continue():
    f = Figlet(font="doom")
    print(f.renderText("Zoom!"))
    return input("Would you like to continue? >").lower() in "yes!yea!ya!"


if __name__ == "__main__":
    titlescreen()
    while True:
        start_bot()
        if not prompt_continue():
            break
    print("Bye!")
