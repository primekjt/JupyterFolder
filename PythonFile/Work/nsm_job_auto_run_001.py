#-*- coding: utf-8 -*-                              #한글 인코딩
import pyautogui
import os
import sys
import time
import datetime
import pyperclip

"""
https://anaconda.org 사이트에서 필요한 모듈을 검색하여 사용하면 된다.
conda install -c conda-forge pyperclip
"""

# setting fail safes
pyautogui.FAIL_SAFE = True
pyautogui.PAUSE = 1

def nsm_login():
    pyperclip.copy('prime200*')
    pyautogui.click(x=567, y=550)   # login dailog setFocus
    pyautogui.hotkey('ctrl', 'v', interval = 0.15)
    pyautogui.click(x=711, y=541)   # 로그인 버튼 클릭

def job_page_open_001():
    # move mouse pointer to center of screen
    screenWidth, screenHeight = pyautogui.size()
    print('Screen size : width(%d) , height(%d)' %(screenWidth, screenHeight))
    #pyautogui.moveTo(screenWidth/2, screenHeight/2)

    pyautogui.moveTo(1118, 143)   # maximize
    pyautogui.click()
    #pyautogui.moveTo(1250, 8)   # minimize
    #pyautogui.click()

    """
    pyautogui.moveTo(93, 863)   # 수발주관리 
    pyautogui.click()
    pyautogui.moveTo(9, 345)   # 보고서 
    pyautogui.click()
    pyautogui.moveTo(45, 470)   # 주문고객현황
    pyautogui.click()
    """
    pyautogui.click(x=93, y=863)   # 수발주관리
    pyautogui.click(x=9, y=345)   # 보고서
    pyautogui.click(x=45, y=470)   # 주문고객현황

def job_page_set_001(from_day, to_day):
    pyautogui.moveTo(307, 156)  # 나의 주문
    pyautogui.click()
    pyautogui.moveRel(None, 54)  # 전체 주문
    pyautogui.click()
    pyautogui.moveTo(441, 174)  # 대분류
    pyautogui.click()
    pyautogui.moveRel(None, 65)  # IDC서비스
    pyautogui.click()
    pyautogui.moveTo(589, 174)  # 중분류
    pyautogui.click()
    pyautogui.moveRel(None, 18)  # IDC서비스
    pyautogui.click()

    pyautogui.moveTo(789, 174)   # 주문일 from
    pyautogui.click()
    pyautogui.typewrite(from_day, interval=0.25)
    pyautogui.moveTo(918, 174)   # 주문일 to
    pyautogui.click()
    pyautogui.typewrite(to_day, interval=0.25)

def job_main_001(order_day):
    pyautogui.moveTo(304, 47)  # 조회
    pyautogui.click()

    pyautogui.moveTo(758, 47)   # 엑셀 저장
    #pyautogui.moveRel(455, None)   # 엑셀 저장
    pyautogui.click()
    pyautogui.press(['tab', 'enter'])   # NSM 'Excel 파일을 저장하시겠습니까?' -> 아니오(N)

    pyautogui.click(x=640, y=10)   # excel 'File' setFocus

    pyautogui.hotkey('alt', 'f2')   # 다른 이름으로 저장
    #save_file_name = 'order_' + type_day
    save_file_name = '000_' + order_day
    pyautogui.typewrite(save_file_name, interval=0.25)   #999
    #pyautogui.typewrite(['a', 'b', 'c'])
    pyautogui.press('enter')    # 저장(S)
    try:
    #  주의) Sheet1.xlsx 기존 파일이 있어 덮어 쓰기를 한다.
        pyautogui.press(['tab', 'enter'])    # 다른 이름으로 저장 확인 -> 예(Y) -> enter
    except Exception as ex:
        print(ex)
        pyautogui.click(x=640, y=10)   # excel 'File' setFocus
    pyautogui.hotkey('ctrl', 'f12')   # 열기

    pyautogui.click(x=640, y=10)   # excel 'File' setFocus
    pyautogui.hotkey('ctrl', 'f12')   # 열기
    pyautogui.click(x=222, y=141)   # excel File select
    pyautogui.hotkey('ctrl', 'c')   # 클립보드 복사
    pyautogui.hotkey('alt', 'f4')    # '열기' 창 종료

    pyautogui.hotkey('alt', 'f4')    # 'excel' 창 종료

def main():
    today = datetime.datetime.today() # datetime.datetime.now
    yesterday = today + datetime.timedelta(days = -1) # 오늘에서 1일을 빼서 어제를 구한다
    order_day = yesterday.strftime('%Y%m%d')

    nsm_login()
    job_page_open_001()
    job_page_set_001(order_day, order_day)
    job_main_001(order_day)

if __name__ == '__main__':
    main()