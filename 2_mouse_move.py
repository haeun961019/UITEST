import pyautogui

# 절대 좌표 마우스 이동
#pyautogui.moveTo(100, 100) # 지정한 위치로 마우스 이동 "왼쪽 위가 0,0"
#pyautogui.moveTo(100, 200, duration=5) # 5 초 동안 100, 200 위치로 이동
#pyautogui.moveTo(100, 100)
#pyautogui.moveTo(300, 300)
#pyautogui.moveTo(500, 500)


# 상대 좌표 마우스 이동 (현재 커서가 있는 위치로부터)
pyautogui.moveTo(100, 200, duration=.5)
print(pyautogui.position()) # Point(x, y)
pyautogui.move(100, 100, duration=.5) # 100, 200 기준으로 +100, +100 -> 200, 300
print(pyautogui.position()) # Point(x, y)
pyautogui.move(100, 100, duration=.5) # 200, 300 기준으로 +100, +100 -> 300, 400
print(pyautogui.position()) # Point(x, y)

p = pyautogui.position()
print(p[0], p[1]) # x,y
print(p.x, p.y) # x,y 