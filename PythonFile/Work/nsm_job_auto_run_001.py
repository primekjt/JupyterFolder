﻿#-*- coding: utf-8 -*-                              #한글 인코딩
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

def parameter_check():
    #print(len(sys.argv), sys.argv)
    result = tuple
    options_len = len(sys.argv)
    if options_len is 1:
        today = datetime.datetime.today()  # datetime.datetime.now
        yesterday = today + datetime.timedelta(days=-1)  # 오늘에서 1일을 빼서 어제를 구한다
        order_from_day = yesterday.strftime('%Y%m%d')
        order_to_day = order_from_day
    elif options_len is 3:
        order_from_day = sys.argv[2].replace('.', '')
        order_to_day = order_from_day
    elif options_len is 5:
        order_from_day = sys.argv[2].replace('.', '')
        order_to_day = sys.argv[4].replace('.', '')

    if not len(order_from_day) is 8:
        print('invalid from day %s' % order_from_day)
        sys.exit()
    if not len(order_to_day) is 8:
        print('invalid to day %s' % order_to_day)
        sys.exit()

    print('to day : %s, from day : %s' % (order_from_day, order_to_day))
    return (order_from_day, order_to_day)   # tuple return

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

    time.sleep(3)

    pyautogui.moveTo(758, 47, duration=1)   # 엑셀
    #pyautogui.moveRel(455, None)   # 엑셀
    pyautogui.click()
    pyautogui.press(['tab', 'enter'])   # NSM 'Excel 파일을 저장하시겠습니까?' -> 아니오(N)

    time.sleep(3)

    pyautogui.click(x=640, y=10)   # excel 'File' setFocus
    time.sleep(1)

    pyautogui.hotkey('alt', 'f2', interval = 0.5)  # 다른 이름으로 저장
    time.sleep(1)
    pyautogui.press('enter')    # 저장(S)
    try:
    #  주의) Sheet1.xlsx 기존 파일이 있어 덮어 쓰기를 한다.
        pyautogui.press(['tab', 'enter'])    # 다른 이름으로 저장 확인 -> 예(Y) -> enter
    except Exception as ex:
        print(ex)
    '''
    pyautogui.hotkey('alt', 'f2')   # 다른 이름으로 저장
    time.sleep(1)
    #save_file_name = 'order_' + type_day
    save_file_name = '000_' + order_day
    pyautogui.typewrite(save_file_name, interval=0.25)
    #pyautogui.typewrite(['a', 'b', 'c'])
    pyautogui.press('enter')    # 저장(S)
    '''
    pyautogui.click(x=640, y=10)   # excel 'File' setFocus

    pyautogui.hotkey('ctrl', 'f12', interval = 0.5)   # 열기
    time.sleep(0.5)
    pyautogui.click(x=222, y=141)   # excel File select
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c', interval = 0.5)   # 클립보드 복사
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'f4', interval = 0.5)    # '열기' 창 종료
    time.sleep(0.5)
    pyautogui.click(x=640, y=10)   # excel 'File' setFocus
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'f4', interval = 0.5)    # 'excel' 창 종료

# 해상도 1280 x 1024 기준
def main():

    # from, to
    order_day = parameter_check()

    nsm_login()
    time.sleep(5)
    job_page_open_001()
    job_page_set_001(order_day[0], order_day[1])
    job_main_001(order_day)

if __name__ == '__main__':
    main()