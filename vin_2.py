from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from vin_3 import *

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

        self.line_name = QLineEdit(line_name)
        self.line_age = QLineEdit(line_age)
        self.line_prised = QLineEdit(line_prised)
        self.line_final_1 = QLineEdit(line_final_1)
        self.line_final_2 = QLineEdit(line_final_2)

        self.l_line.addWidget(self.name, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment= Qt.AlignLeft)

        self.l_line.addWidget(self.age, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment= Qt.AlignLeft)

        self.l_line.addWidget(self.text_1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.btn_start, alignment= Qt.AlignLeft)

        self.l_line.addWidget(self.line_prised, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.text_2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.start_prised, alignment= Qt.AlignLeft)

        self.l_line.addWidget(self.text_3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.final_test, alignment= Qt.AlignLeft)

        self.l_line.addWidget(self.line_final_1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.line_final_2, alignment= Qt.AlignLeft)

        self.l_line.addWidget(self.results, alignment= Qt.AlignCenter)

        self.r_line.addWidget(self.timer, alignment= Qt.AlignRight)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.results.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.fw = FinalWin()
