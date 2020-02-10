# Nitro Type bot by b0kch01
# Thanks Google for tesseract

DEBUG = False

print("Checking for dependencies...")

try:
    # Important Libraries
    from os import system, getuid # UI
    from sys import platform # Check for device type
    from pyfiglet import Figlet  # Title text
    from termcolor import cprint  # Colorful terminal
    from screenbox import Box  # Storing screen-shot dimensions
    from PIL import Image, ImageGrab  # Image processing, Screenshoting
    from colorama import init  # Color support for legacy-consoles
    from pytesseract import image_to_string # ML Library to detect words in image
    import keyboard  # Fast keyboard emulating
    from time import sleep # Loop control, delays

    init()  # Legacy console fix for color
    print("Successfuly imported!\n")
except:
    print("Error: Could not import modules")
    print("Please check to:")
    print("\t1) Tesseract installed with correct PATH")
    print("\t2) Other modules are installed with pip")
    exit(0)


def clear():
    system("cls" if platform == "win32" else "clear")

def isfloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def compat_check():
    print("Checking for compatibility...")
    cprint(f"Release: v1.0 {platform}", "grey", "on_yellow")
    # If linux, warn the user
    # If macOS, elevate permissions if not present
    if (platform == "linux"):
        print("(Unsupported OS): Anything beyond this point might go crazy...")
    elif (platform == "darwin"):
        from elevate import elevate
        if getuid() != 0:
            print("Not adminstrator: It's needed to emulate keyboard on macOS")
            elevate(graphical=False)
        if getuid() == 0:
            cprint("Success: ", "green", end="")
            print("Got permission!")
        else:
            print("Couldn't get administrator priveledges :(")
            input("rip. press [Enter] to close this app.")
            exit(0)
    


def titlescreen():
    f = Figlet(font="doom")
    print(f.renderText("NitroType Bot"))
    print("============================")
    cprint(" Created with ♥ by b0kch01! ", "grey", "on_white")
    cprint(" OCR Tesseract  by Google!  ", "grey", "on_cyan")
    print("============================")

    print("Remember, hold [esc] to exit the bot")
    print("Enjoy! :)\n")


def start_bot():
    try:
        # Set delay between keyboard input
        started = False
        delay = input("Guess delay (seconds) >")
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
        sleep(1)
        # Main Typing bot
        print("And it's off!")
        started = True
        text = ""
        while not keyboard.is_pressed("esc"):
            # Take the screen shot, given box coordinates.
            # Convert to grayscale image for better accuracy from tesseract
            image = ImageGrab.grab(bbox=(x1, y1, x2, y2)).convert("LA")
            # Get text from the image_to_string model and remove new lines
            text = image_to_string(
                image, lang="eng").replace("\n", "")
            # Write the text from tesseract
            keyboard.write(text)
            sleep(float(delay))

    except:
        if started:
            print("\n\nExited Unofficially: Remember to hold [esc] instead!")
    

def prompt_continue():
    f = Figlet(font="doom")
    clear()
    print(f.renderText("Exit?"))
    try:
        cont = input("Would you like to continue? >").lower()
        return cont in "yes!yea!ya!" and cont != ""
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    clear()
    compat_check()
    titlescreen()
    while True:
        if not DEBUG:
            try:
                start_bot()
            except:
                print("Oh No! Something went terribly wrong!")
                print("Create an issue on GitHub and I'll try to fix it :)")
        else:
            start_bot()
        if not prompt_continue():
            break
    print("\nBye!")
    sleep(0.5)
    exit(0)
