import sys
import pyautogui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.open_btn = QPushButton('Open Image')
        self.label = QLabel()
        self.x_le = QLineEdit()
        self.y_le = QLineEdit()
        self.n_le = QLineEdit()
        self.t_le = QLineEdit()
        self.click_btn = QPushButton('Click')
        self.fname = ''
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label)
        hbox.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel('x: '))
        hbox2.addWidget(self.x_le)
        hbox2.addWidget(QLabel('y: '))
        hbox2.addWidget(self.y_le)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(QLabel('횟수: '))
        hbox3.addWidget(self.n_le)
        hbox3.addWidget(QLabel('딜레이: '))
        hbox3.addWidget(self.t_le)

        vbox = QVBoxLayout()
        vbox.addWidget(self.open_btn)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(self.click_btn)
        self.setLayout(vbox)

        self.open_btn.clicked.connect(self.show_dialog)
        self.click_btn.clicked.connect(self.click_btn_clicked)

        self.setWindowTitle('Image')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def show_dialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            pixmap = QPixmap(fname[0])
            self.label.setPixmap(pixmap.scaledToWidth(pixmap.width()*1.1))
            self.fname = fname[0]

    def click_btn_clicked(self):

        n = int(self.n_le.text())
        t = float(self.t_le.text())

        if self.x_le.text() and self.y_le.text():
            x_pos = int(self.x_le.text())
            y_pos = int(self.y_le.text())
            pyautogui.click(x_pos, y_pos, clicks=n, interval=t)
        elif self.fname:
            center = pyautogui.locateCenterOnScreen(self.fname)
            pyautogui.click(center, clicks=n, interval=t)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())