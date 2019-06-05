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

def klia_test():
    """
    # chromedriver download url
    https://sites.google.com/a/chromium.org/chromedriver/downloads
    """

    options = webdriver.chrome.options.Options()
    # options = webdriver.ChromeOptions()
    """
    options.add_argument("no-sandbox")
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

    # navigating to a webpage
    # driver.get("https://www.naver.com")
    # driver.find_element_by_class_name('lg_local_btn').click()

    # 생명보험협회
    driver.get('http://www.klia.or.kr/main/index.do')
    # pageFirst = ui.WebDriverWait(driver, 15).until(lambda browser: browser.find_element_by_tag_name('body'))
    mainWindow = driver.current_window_handle
    # pageFirst.send_keys(Keys.COMMAND+ 't')

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

    if "생명보험협회" not in driver.title:
        raise Exception("Unable to load 생명보험협회 page!")

    # popup window close
    for handle in driver.window_handles:
        # driver.switch_to_window(handle)   # DeprecationWarning
        driver.switch_to.window(handle)
        print('page title is \'' + driver.title + '\'')
        if not mainWindow == handle:
            driver.close()

    #driver.switch_to_default_content()
    driver.switch_to.window(mainWindow)
    driver.find_element_by_xpath('//*[@id="container"]/div[3]/ul/li[1]/a').click()

    print('page title is \'' + driver.title + '\'')
    """
    check_title = '월간생명보험통계 > 생명보험통계 > 소비자'
    try:
        # we have to wait for the page to refresh, the last thing that seems to be updated is the title
        WebDriverWait(driver, 10).until(EC.title_contains(check_title))
        # You should see "월간생명보험통계 > 생명보험통계 > 소비자"
        print(driver.title)
    except TimeoutException:
        pass
    finally:
        pass
        #driver.quit()
    """

    # 조회 조건 선택
    # 조회 년도
    element = driver.find_element_by_xpath('//*[@id="searchForm"]/fieldset/div[2]/span[2]/select[1]')
    """
    # select option value 값 확인
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        print("Value is: %s" % option.get_attribute("value"))
        #option.click()
    """
    select = ui.Select(element)
    #select.select_by_index(index)
    #select.select_by_visible_text("2017년")
    select.select_by_value('2019')
    #select.deselect_all()
    driver.implicitly_wait(0.5)                           #크롬 드라이버 1초 대기
    time.sleep(1)

    # 조회 월
    element = driver.find_element_by_xpath('//*[@id="searchForm"]/fieldset/div[2]/span[2]/select[2]')
    select = ui.Select(element)
    select.select_by_value("01")
    driver.implicitly_wait(0.5)                           #크롬 드라이버 1초 대기
    time.sleep(1)

    # 통계목록
    element = driver.find_element_by_xpath('//*[@id="searchForm"]/fieldset/div[2]/span[4]/select[1]')
    select = ui.Select(element)
    select.select_by_value("I.생명보험사업개황(총괄)")
    driver.implicitly_wait(1)                           #크롬 드라이버 1초 대기
    time.sleep(1)

    # 보고서 선택
    element = driver.find_element_by_xpath('//*[@id="searchForm"]/fieldset/div[2]/span[4]/select[2]')
    select = ui.Select(element)
    select.select_by_value("SM001")
    driver.implicitly_wait(1)                           #크롬 드라이버 1초 대기
    time.sleep(1)

    # 조회 버튼
    driver.find_element_by_xpath('//*[@id="btn_report_read"]').click()

    driver.implicitly_wait(1)                           #크롬 드라이버 1초 대기
    time.sleep(2)

    # 다운로드
    driver.find_element_by_xpath('//*[@id="btn_report_download"]').click()

    # 전체 다운로드
    #driver.find_element_by_xpath('//*[@id="btn_report_alldownload"]"]').click()

    """
    try:
        #WebDriverWait(driver, 5).until(lambda browser: )
        WebDriverWait(driver, 5).until(driver.find_element_by_xpath('//*[@id="btn_report_download"]').click())
    except:
        pass
   """

    driver.implicitly_wait(5)                           #크롬 드라이버 1초 대기
    time.sleep(5)

    driver.quit()
    print('quit OK')

def main():
    klia_test()
    print(os.getcwd())

if __name__ == "__main__":
    main()