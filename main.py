import os
import pyautogui
import time
import PIL


def sleep(duration):
    time.sleep(duration)


def press(button):
    pyautogui.press(button)


def position(x, y, d):
    pyautogui.moveTo(x, y, d)


def get_mouse_location():
    sleep(3)
    print(pyautogui.position())


def get_pixel(x, y):
    sleep(5)
    im = pyautogui.screenshot()
    print(im.getpixel((x, y)))


pyautogui.FAILSAFE = False


def get_to_location():
    loopo = True
    while loopo:
        sleep(3)
        press("esc")
        sleep(1)
        im = pyautogui.screenshot()
        if im.getpixel((1400, 500)) == (52, 23, 53):
            press("enter")
            sleep(1)
            with pyautogui.hold("s"):
                with pyautogui.hold("d"):
                    sleep(5)
            position(1366, 0, 0)
            with pyautogui.hold("w"):
                sleep(0.1)
            position(1429, 481, 0)
            press("x")
            sleep(0.2)
            press("enter")
            loopo = False
            print("get_to_location() if")
        else:
            print("Something went wrong in get_to_location")


def prep_race():
    loopo = True
    while loopo:
        sleep(10)
        im = pyautogui.screenshot()
        if im.getpixel((69, 445)) == (255, 255, 255):
            sleep(1)
            press("enter")  # Enter Race Setup
            sleep(0.5)
            press("enter")  # Choose "Race"
            sleep(1)
            press("left")  # Go to custom Events
            sleep(0.1)
            press("left")
            sleep(0.1)
            press("enter")
            sleep(2)
            press("backspace")  # Enter Search
            sleep(1)
            press("up")
            sleep(1)
            press("enter")
            sleep(0.2)
            pyautogui.typewrite('678864875\n', 0.1)
            sleep(0.1)
            press("down")  # select Track
            pyautogui.press("enter")
            sleep(1)
            press("enter")
            loopo = False
            print("prep_race if")
        else:
            press("esc")
            sleep(5)
            press("esc")
            sleep(5)
            press("esc")
            sleep(5)
            press("esc")
            sleep(5)
            press("esc")
            print("something went wrong in prep_race")


def select_car():  # This is stupid, i know.
    loopo = True
    while loopo:
        sleep(10)
        im = pyautogui.screenshot()
        if im.getpixel((240, 350)) == (0, 110, 163):
            press("enter")
            loopo = False
            print("select_car if")
        else:
            loopo = False
            sleep(10)
            press("y")
            sleep(1)
            position(1000, 750, 1)
            sleep(1)
            press("enter")
            sleep(0.1)
            press("esc")
            sleep(1)
            press("y")
            sleep(0.1)
            press("enter")
            sleep(0.1)
            press("esc")
            sleep(0.5)
            press("right")
            sleep(0.1)
            press("enter")
            print("select_car else")


def start_race():  # This is also stupid, i know.
    loop = True
    sleep(5)
    while loop:
        im = pyautogui.screenshot()
        if im.getpixel((374, 191)) == (234, 204, 52):
            loop = False
            position(357, 351, 0)
            sleep(0.1)
            pyautogui.click()
            sleep(0.1)
            press("enter")
            print("start_race if")
        else:
            print("start_race() else")
            sleep(1)


def drive():
    sleep(10)
    loop = True
    with pyautogui.hold("w"):
        while loop:
            im = pyautogui.screenshot()
            if im.getpixel((127, 74)) == (247, 247, 247):
                sleep(5)
                print("drive() if")
            else:
                loop = False
                print("drive() else")


def finishing_up():
    loop = True
    sleep(5)
    while loop:
        im = pyautogui.screenshot()
        if im.getpixel((1400, 500)) == (52, 23, 53):
            press("esc")
            loop = False
            print("finishing_up() If")
        elif im.getpixel((700, 800)) == (255, 0, 134):
            press("down")
            sleep(0.1)
            press("down")
            sleep(0.1)
            press("enter")
        elif im.getpixel((470, 200)) == (255, 0, 134):
            press("esc")
            loop = False
        else:
            print("finishing_up() else")
            sleep(1)
            press("enter")
            sleep(1)
            press("esc")
            sleep(1)
            press("esc")
            sleep(1)
            press("esc")
            sleep(1)


while True:
    get_to_location()
    prep_race()
    select_car()
    start_race()
    drive()
    finishing_up()

# get_mouse_location()
# get_pixel(470, 200)
