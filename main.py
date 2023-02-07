import pyautogui as pag
import random
import time

interval = 5  # interval time in seconds

print("Starting Keep-Awake program (Interval time: {} seconds)".format(interval))
print("Manually press pause to terminate it.")

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, 0.5)
    time.sleep(interval)


