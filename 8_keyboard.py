import pyautogui

#w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 한개 띄운 상태에서 가져옴
#w.activate()

pyautogui.write('12345')

#automate the boring stuff with python 홈페이지 참고

import pyperclip

pyperclip.copy("나도코딩")
pyautogui.hotkey("ctrl", "v")


def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("나도코딩")