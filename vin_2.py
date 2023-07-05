from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *

class TestWin(QWidget):
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
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()        
        self.l_line = QVBoxLayout()

        self.name = QLabel(name)
        self.age = QLabel(age)
        self.text_1 = QLabel(text_1)
        self.text_2 = QLabel(text_2)
        self.text_3 = QLabel(text_3)
        self.timer = QLabel(timer)

        self.btn_start = QPushButton(btn_start)
        self.start_prised = QPushButton(start_prised)
        self.final_test = QPushButton(final_test)
        self.results = QPushButton(results)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
