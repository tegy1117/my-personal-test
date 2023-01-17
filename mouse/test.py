import pyautogui
import pyperclip

pyautogui.hotkey('win','r')
pyautogui.press("notepad")
pyautogui.press('enter')
pyautogui.sleep(0.1)
pyautogui.write('Why do you come here again?')
pyperclip.copy("왜 다시 여기로 돌아온거야?")
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
