import pyautogui

size = pyautogui.size() # 현재 화면 스크린 사이즈
print(size) # 가로, 세로 크기

print(size[0])
print(size[1])