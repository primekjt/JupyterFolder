#-*- coding: utf-8 -*-                              #한글 인코딩

"""
2019.05.22
https://anaconda.org 사이트에서 필요한 모듈을 검색하여 사용하면 된다.

To install this package with conda run one of the following:
conda install -c conda-forge pyautogui
conda install -c conda-forge/label/cf201901 pyautogui
"""
import pyautogui
import os
import sys
import time
import pyperclip

def mspaint_test():
    # setting fail safes
    pyautogui.FAIL_SAFE = True
    pyautogui.PAUSE = 1

    # open MS paint
    os.system('START "" mspaint')

    # move mouse pointer to center of screen
    screenWidth, screenHeight = pyautogui.size()
    #pyautogui.moveTo(screenWidth/2, screenHeight/2)
    pyautogui.moveTo(screenWidth/4, screenHeight/4)

    # drag mouse
    distance = 200
    while distance > 0:
            pyautogui.dragRel(distance, 0, duration=0.1)   # move right
            distance -= 5
            pyautogui.dragRel(0, distance, duration=0.1)   # move down
            pyautogui.dragRel(-distance, 0, duration=0.1)  # move left
            distance -= 5
            pyautogui.dragRel(0, -distance, duration=0.1)  # move up

def notepad_test():
    # setting fail safes
    pyautogui.FAIL_SAFE = True
    pyautogui.PAUSE = 1

    # open MS paint
    os.system('START "" notepad')

    # move mouse pointer to center of screen
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

    pyautogui.typewrite("RPA Programming\n", interval=0.25)
    pyautogui.typewrite("(Robotic Process Automation)\n", interval=0.1)
    pyautogui.typewrite("---The End---\n", interval=0.25)
    #pyautogui.typewrite(u"업무환경 자동화", interval=0.5) #한글 안써짐

# - 이미지 File이름, 검출 대상이 될 영역을 입력받아 이미지를 검출하는 함수
def findLcationWithImage(fileName, startPos, confidence=.7):
    file_path = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'img' + '\\' + fileName
    result = pyautogui.locateOnScreen(file_path, confidence=confidence, region=startPos)
    #print('.', end=' ')
    sys.stdout.write('. ')
    sys.stdout.flush()
    if result != None:
        print('Find Image ' +  str(result))
    return result

def findImageUntil(fileName, startPos, cnt = 60, confidence=0.8, wait=0.1):
    for i in range(cnt):
        imgpos = findLcationWithImage(fileName, startPos, confidence= confidence)
        if imgpos != None:
            break
        else:
            time.sleep(wait)
    if imgpos == None:
        return None
    else:
        return imgpos

def nsm_test():
    # setting fail safes
    pyautogui.FAIL_SAFE = True
    pyautogui.PAUSE = 1

    screenWidth, screenHeight = pyautogui.size()
    print('screen size : (w{0}, h{1})'.format(screenWidth, screenHeight))

    region = (0, 0, screenWidth, screenHeight)
    #findImageUntil("NSM_LOGIN.PNG", region, cnt=60, confidence=0.8)

    find_box = pyautogui.locateOnScreen('NSM_LOGIN_PIECE.PNG')
    print(find_box)

    #center_box = pyautogui.locateCenterOnScreen('NSM_LOGIN.PNG')
    #print(center_box)

    if not find_box:
        print('exit program')
        exit()

    #print(find_box.left + find_box.width/2)


    x = find_box.left + find_box.width/2
    y = find_box.top + find_box.height/2 + 10
    #pyautogui.moveTo(x, y)
    pyautogui.click(x, y, 1)
    time.sleep(1)

    pyperclip.copy('prime200*')
    pyautogui.click(x=260, y=450)  # excel 'File' setFocus
    pyautogui.hotkey('ctrl', 'v', interval=0.15)

    pyautogui.moveRel(60, 0, 0.5)
    pyautogui.click()


"""
    #이미지 영역의 가운데 위치 얻기
    five_btn = pyautogui.locateOnScreen('NSM_LOGIN.PNG')
    center = pyautogui.center(five_btn)
    print(center)

    #클릭하기
    center = pyautogui.locateCenterOnScreen('NSM_LOGIN.PNG')
    #pyautogui.click(center)
"""
    #pyautogui.moveTo(1315, 256, 5)   # 5초안에 0,0으로 마우스 이동


def main():
    mspaint_test()

    #notepad_test()
    #nsm_test()

    #pyautogui.alert('This displays some text with an OK button.')

    print('Good By!')

if __name__ == '__main__':
    main()

