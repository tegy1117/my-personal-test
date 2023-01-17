import pyautogui
pyautogui.countdown(3)
result = pyautogui.confirm("에헤","에헤")
print(result)
if result is "OK":
    pyautogui.alert("에헤","에헤")
else:
    pyautogui.alert("에헤때 난다요!","에헤때 난다요!")
print(pyautogui.prompt("뭐해","뭐해?"))
print(pyautogui.password("비밀이네?","비밀이니?"))