import pyautogui

# 마우스를 끝에 갖다놓아도 동작함 / 비추천 사용하지마세요
pyautogui.FAILSAFE = False

# 모든 동작에 1초씩 sleep 적용
# 자동화 다 짜고 나서 동작 시간 설정 가능
pyautogui.PAUSE = 1

pyautogui.mouseInfo()

# F1 누르면 좌표 정보 복사 가능 x, y, R, G, B

# 자동화 중에 실패할 경우 취소하려면
# 마우스를 네 귀퉁이 중 암데나 갖다놓으면 됩니다

for i in range(10):
    pyautogui.move(100,100)
    pyautogui.move(1)


