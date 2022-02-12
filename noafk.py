from pynput.mouse import Button, Controller
import time

mouse = Controller()
starttime = time.time()

while True:
    print("Click")
    mouse.position = (100, 464)
    mouse.click(Button.left, 1)
    time.sleep(240.0 - ((time.time() - starttime) % 240.0))


nokickpls()
