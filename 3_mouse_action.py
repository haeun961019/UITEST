import pyautogui
pyautogui.sleep(3)

# 마우스 위치 알아내기
print(pyautogui.position())


pyautogui.click(pyautogui.position())

pyautogui.mouseDown() # 클릭하고 있는 상태
pyautogui.mouseUp() # 클릭 뗀 상태

pyautogui.doubleClick()
pyautogui.click(clicks=500)

pyautogui.moveTo(100, 100)
pyautogui.mouseDown()
pyautogui.moveTo(200,300)
pyautogui.mouseUp()

pyautogui.sleep(3) # 3초 대기
pyautogui.rightClick()
pyautogui.middleClick()

pyautogui.moveTo()
pyautogui.drag(100, 0) # 현재 위치 기준 100, 0 만큼 드래그
pyautogui.dragTo(100, 0) # 절대 위치 기준 100, 0 만큼 드래그

pyautogui.scroll(300)