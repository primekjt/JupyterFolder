import pyautogui

"""
command>python mousePosition.py
"""

def mousePosition():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            # Get and print the mouse coordinates.
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\nDone.')

def main():
    mousePosition()

if __name__ == '__main__':

    # move mouse pointer to center of screen
    screenWidth, screenHeight = pyautogui.size()
    print('Screen size : width(%d) , height(%d)' %(screenWidth, screenHeight))

    main()