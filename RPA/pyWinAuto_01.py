#-*- coding: utf-8 -*-                              #한글 인코딩

"""
conda install -c conda-forge pywinauto
conda install -c conda-forge/label/cf201901 pywinauto
#pip install --upgrade pywinauto
"""
from pywinauto.application import Application
# Run a target application
app = Application().start("notepad.exe")

app.UntitledNotepad.print_control_identifiers()

# Select a menu item
app.UntitledNotepad.menu_select("도움말(&H)->메모장 정보(&A)")
#app['', '제목 없음 - 메모장'].menu_select("도움말(&H)->메모장 정보(&A)")# Click on a button

app['메모장 정보'].확인.click()
#app.AboutNotepad.확인.click()
# Type a text string
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)

app.UntitledNotepad.menu_select("파일(&F)->다른 이름으로 저장")
app.SaveAs.ComboBox5.select("UTF-8")
app.SaveAs.edit1.set_text("Example-utf8.txt")
#app.SaveAs.Save.click()