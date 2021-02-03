# 가끔씩 카카오톡 실행 오류가 발생하므로, 마우스 매크로 버전 제작
# 20210203

import os
import pyautogui
import pyperclip
import platform
import subprocess
import time

# 좌표 확인단
'''
time.sleep(5)
x, y = pyautogui.position()
print(x, y)
'''

# 숨겨진 아이콘 표시 1677 1055
# 카카오톡 1645 1017
# 채팅방 위치 1441 256
# 파일전송 1291 828
# 주소창 1402 300
# 폴더 여백 1320 532



# 카카오톡 실행 및 채팅방 접속
def run_kakao():
    pyautogui.click(1677, 1055)
    pyautogui.doubleClick(1645, 1017)
    pyautogui.doubleClick(1441, 256)

# 카카오톡 지정 메시지 전송
def send_msg(arg):
    pyperclip.copy(arg)
    pyautogui.hotkey(cmd_key, 'v')
    pyautogui.press('enter')

# 출근
def start():
    direc = "C:\\Users\\yoonjun\\Desktop\\알바\\제출\\출근"
    msg = '안녕하세요, 테스트 중입니다.'

    while True:
        time.sleep(3)
        ctime = time.strftime('%H:%M')

        if ctime == '08:58':
            run_kakao()
            pyautogui.click(1291, 828)
            pyautogui.click(1402, 300)
            pyperclip.copy(direc)
            pyautogui.hotkey('ctrl','v')
            pyautogui.click(1320, 532)
            pyautogui.hotkey('ctrl','a')
            pyautogui.hotkey('alt','o')
            time.sleep(1)
            send_msg(msg)
            time.sleep(5)
            pyautogui.hotkey('esc')
            print('출근 완료')
            return True
            break

        else:
            print(f'출근 매크로 실행 예정입니다. 현재 시각 : {ctime}')

# 오전 보고
def report_am():
    msg = '1000개 검수했습니다!'

    while True:
        time.sleep(3)
        ctime = time.strftime('%H:%M')

        if ctime == '10:57':
            run_kakao()
            send_msg(msg)
            pyautogui.hotkey('esc')
            print('오전 보고 완료')
            return True
            break

        else:
            print(f'오전 보고 매크로 실행 예정입니다. 현재 시각 : {ctime}')

# 오후 보고
def report_pm():
    msg = '3000개 검수했습니다!'

    while True:
        time.sleep(3)
        ctime = time.strftime('%H:%M')

        if ctime == '14:57':
            run_kakao()
            send_msg(msg)
            pyautogui.hotkey('esc')
            print('오후 보고 완료')
            return True
            break

        else:
            print(f'오후 보고 매크로 실행 예정입니다. 현재 시각 : {ctime}')  

# Config changed by OS
cmd_key = 'ctrl'
home_key = ('home', '')
is_retina = False

if platform.system() == "Darwin":
    is_retina = subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True)
    cmd_key = 'command'
    home_key = ('option', 'up')

pyautogui.PAUSE = 1

# 매크로 실행
if __name__ == "__main__":
    #start = start()
    #time.sleep(1)
    report_am = report_am()
    time.sleep(1)
    report_pm = report_pm()

    if report_am & report_pm:
        exit(0)
