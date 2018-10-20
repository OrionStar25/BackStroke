import math
import pyautogui
import time


def draw():
	pyautogui.FAILSAFE = True
	time.sleep(5)

	cx, cy = pyautogui.size()
	cx /= 2
	cy /= 2
	radius = 100
	angle = 0
	omega = 0.3

	# parametric equation of circle
	x = cx + radius * math.cos(angle)
	y = cy + radius * math.sin(angle)
	pyautogui.click(x,y)

	while 2*math.pi - angle >= 0.001:
	    angle = angle + omega
	    x = x + radius * omega * math.cos(angle + math.pi / 2)
	    y = y + radius * omega * math.sin(angle + math.pi / 2)
	    pyautogui.dragTo(x, y, duration=0.2)

	pyautogui.moveTo(cx, cy-radius, duration=0.2)
	pyautogui.dragTo(cx, cy+radius, duration=0.2)
	pyautogui.moveTo(cx, cy, duration=0.2)
	pyautogui.dragTo(cx - radius * math.cos(math.pi/4), cy + radius * math.sin(math.pi/4), duration=0.2)
	pyautogui.moveTo(cx, cy, duration=0.2)
	pyautogui.dragTo(cx + radius * math.cos(math.pi/4), cy + radius * math.sin(math.pi/4), duration=0.2)

