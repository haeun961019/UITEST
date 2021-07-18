import pyautogui
import sys
import time
#file_menu = pyautogui.locateOnScreen('filemenu.png')
#print(file_menu)
#pyautogui.click(file_menu)

#screen = pyautogui.locateOnScreen("screenshot.png")
#print(screen)

# 동일한 이미지 여러개인 경우 반복문 사용하여 동작
# locateAllOnScreen
pyautogui.locateAllOnScreen("checkbox.png")


for i in pyautogui.locateAllOnScreen("checkbox.png"):
    print(i)
    pyautogui.click(i)


#속도 개선
#1. GrayScale
# pyautogui.locateAllOnScreen("checkbox.png", grayscale=True)

#2. 범위 지정
#pyautogui.mouseInfo()

#3. 정확도 조정
#pip install opencv-python 하여 confidence 값 조정
#confidence=0.7인 경우 70퍼 비슷하면 클릭
#run_btn = pyautogui.locateOnScreen("run_btn.png", confidence = 0.7)

# 자동화 대상이 바로 보여지지 않는 경우 (이미지 처리 - 대기)
file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#1. 계속 기다리기
if file_menu_notepad :
    pyautogui.click(file_menu_notepad)
else:
    print("발견 실패")

#2.
while file_menu_notepad is None :
    file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")

pyautogui.click(file_menu_notepad)

#3. 일정 시간 기다리기 (Timeout)
Timeout = 10
start =time.time() # 시작시간 설정
file_menu_notepad = None

while file_menu_notepad is None :
    file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
    end = time.time() # 종료시간 설정
    if end - start > Timeout:
        print("ㅅ간 종료")
        sys.exit()

pyautogui.click(file_menu_notepad)


#함수로

def find_target(img_file, timeout=30):
    start = time.time()
    target=None
    while target is None :
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png", 10)