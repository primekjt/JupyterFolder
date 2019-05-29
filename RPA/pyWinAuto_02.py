import pywinauto as pwa
import sys
import time

# 특정 프로그램을 윈도우 Top으로 전환하는 함수
def setFocus(title_reg):
    app = pwa.application.Application()
    # title 이름 정규표현식
    t = title_reg
    print('find title : ' + str(title_reg))
    try:
        # title 을 기반으로 window handle 을 가져옴
        handle = pwa.findwindows.find_windows(title_re=t)[0]
        # 해당 윈도우 Control을 위해 라이브러리와 연결
        app.connect(handle=handle)
        print('title: ' + str(t) + 'handle: ' + str(handle) + ' Setted')
    except:
        print('No title exist on window ')
    # 어플리케이션의 window를 가져옴
    window = app.window(handle=handle)
    try:
        # 해당 윈도우를 탑으로 설정
        window.set_focus()
    except Exception as e:
        print('[error]setFocuse : ' + str(e))
    return window

def setFocusWindow():
    # 로스트아크 타이틀의 정규표현식
    title_name = u'NSM .*'
    return setFocus(title_name)

#    BIZ15990


if __name__=="__main__":
    #wnd = setFocusWindow()
    #wnd.DrawOutline()
    #wnd.print_control_identifiers()

    app = pwa.application.Application().Connect(title=u'NSM \ub85c\uadf8\uc778(\uc6d0\uaca9)', class_name='RAIL_WINDOW')
    railwindow = app.RAIL_WINDOW
    railwindow.draw_outline()
    railwindow.print_control_identifiers()

    #wnd.Edit2.type_keys('ABCDEFG')
