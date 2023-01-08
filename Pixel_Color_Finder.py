import time
import pyautogui as pg

# --- Wait 2 seconds --- #
time.sleep(2) 

while (True):
# --- Get the current mouse position --- #
    x, y = pg.position()

# --- Get the RGB value of the pixel at the mouse position --- #
    r, g, b = pg.screenshot().getpixel((x, y))

# --- Print the result and wait 1 second before continuing the loop --- #
    print("")
    print(f"RGB value of pixel at ({x}, {y})is: ({r}, {g}, {b})")
    time.sleep(1)
