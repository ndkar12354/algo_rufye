from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *
from vin_2 import *
from vin_3 import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_w, win_h)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(hello_text)
        self.instruction = QLabel(txt_instr)
        self.btn = QPushButton(btn_txt)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)
    def connects(self):
        self.btn.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()

app = QApplication([])
mw = MainWin()
app.exec_()