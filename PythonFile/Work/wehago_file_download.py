#-*- coding: utf-8 -*-                              #한글 인코딩
from selenium import webdriver                      #셀레니움 import
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import os

def wehago_test():
    """
    # chromedriver download url
    https://sites.google.com/a/chromium.org/chromedriver/downloads
    """

    options = webdriver.chrome.options.Options()
    # options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    """
    options.add_argument("disable-extensions")
    options.add_argument("disable-popup-blocking")
    options.add_argument("disable-infobars")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36)")

    #chrome_prefs = {}
    #options.experimental_options["prefs"] = chrome_prefs
    #chrome_prefs["profile.default_content_settings"] = {"popups": 1}
    """

    driver = webdriver.Chrome('c:\\chromedriver_win32\chromedriver.exe', chrome_options=options)
    # driver.set_window_size('1280','1024')
    driver.maximize_window()
    driver.implicitly_wait(2)  # seconds



    # WEHAGO
    driver.get('https://www.wehago.com/#/login')
    # pageFirst = ui.WebDriverWait(driver, 15).until(lambda browser: browser.find_element_by_tag_name('body'))
    mainWindow = driver.current_window_handle
    # pageFirst.send_keys(Keys.COMMAND+ 't')
    elem_id = driver.find_element_by_id("inputId")
    elem_id.send_keys('primekjt')
    elem_pwd = driver.find_element_by_id("inputPw")
    elem_pwd.send_keys('password')
    #elem_pwd.send_keys(Keys.RETURN)

    elem_btn = driver.find_element_by_css_selector('#contnt > div.content_box.login_process > div > fieldset > button')
    elem_btn.click()

    time.sleep(10)

    """
    try:
        WebDriverWait(driver, 5).until(driver.find_element_by_xpath('//*[@id="storageMainTree"]/li/ul/li[4]/span/label').click())
    except:
        pass
    """
    driver.get('https://www.wehago.com/#/smartsquare/cloudstorage')
    storageWindow = driver.current_window_handle

    driver.implicitly_wait(10)  # seconds

    web_page_title = 'WEHAGO 클라우드스토리지'

    # chrom browser '팝업창을 여시겠습니까?' 닫기
    try:
        WebDriverWait(driver, 0).until(EC.alert_is_present())
        #alert = driver.switch_to_alert()
        alert = driver.switch_to.alert
        alert.accept()
        # alert.dismiss()   # cancel
    except TimeoutException:
        pass

    driver.implicitly_wait(1)  # 크롬 드라이버 1초 대기

    if "WEHAGO 클라우드스토리지" not in driver.title:
        raise Exception("Unable to load \'WEHAGO 클라우드스토리지\' page!")

    """
    # popup window close
    for handle in driver.window_handles:
        # driver.switch_to_window(handle)   # DeprecationWarning
        driver.switch_to.window(handle)
        print('page title is \'' + driver.title + '\'')
        if not mainWindow == handle:
            driver.close()

    #driver.switch_to_default_content()
    #driver.switch_to.window(mainWindow)
    #driver.find_element_by_xpath('//*[@id="storageMainTree"]/li/ul/li[4]/span/label').click()
    """

    print('page title is \'' + driver.title + '\'')

    time.sleep(5)

    driver.quit()
    print('quit OK')

def main():
    wehago_test()
    print(os.getcwd())

if __name__ == "__main__":
    main()

    #또다른 파이썬 프로그램 실행하는 법
    #exec("anotherprogram.py")