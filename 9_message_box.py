import pyautogui

#pyautogui.countdown(3)
#print("자동화시작")

pyautogui.alert("자동화 수행에 실패했습니다.", "경고") # 확인 버튼만 있는 팝업
result = pyautogui.confirm("계속 진행하시겠습니까?", "확인")
print(result)
if result == 'OK':
    print('a')