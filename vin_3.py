from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *



class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_w, win_h)
        self.move(win_x, win_y)
    def initUI(self):       
        self.final_text_2 = QLabel(final_text_2 + self.results())
        self.final_text_1 = QLabel(final_text_1 + str(self.index))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.final_text_1, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.final_text_2, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    
    def results(self):
        self.index = (4*(int(self.exp.test1) + int(self.exp.test2) + int(self.exp.test3))-200)/10
        if self.exp.age < 7:
            self.index = 0
            return 'нет данных для такого возвраста'

        if self.exp.age >= 15:
            if self.index >= 15:
                return test_res1
            elif self.index >= 11 and self.index < 15:
                return test_res2
            elif self.index >= 6 and self.index < 11:
                return test_res3
            elif self.index >= 0.5 and self.index < 6:
                return test_res4
            else:
                return test_res5
        
        elif self.exp.age >= 13 and self.exp.age < 15:
            if self.index >= 16.5:
                return test_res1
            elif self.index >= 12.5 and self.index <= 16.4:
                return test_res2
            elif self.index >= 7.5 and self.index <= 12.4:
                return test_res3
            elif self.index >= 2 and self.index <= 7.4:
                return test_res4
            else:
                return test_res5

        elif self.exp.age >= 11 and self.exp.age <= 12:
            if self.index >= 18:
                return test_res1
            elif self.index >= 14 and self.index <= 17.9:
                return test_res2
            elif self.index >= 9 and self.index <= 13.9:
                return test_res3
            elif self.index >= 3.5 and self.index <= 8.9:
                return test_res4
            else:
                return test_res5

        elif self.exp.age >= 9 and self.exp.age <= 10:
            if self.index >= 19.5:
                return test_res1
            elif self.index >= 15.5 and self.index <= 19.4:
                return test_res2
            elif self.index >= 10.5 and self.index <= 15.4:
                return test_res3
            elif self.index >= 5 and self.index <= 10.4:
                return test_res4
            else:
                return test_res5

        elif self.exp.age >= 8 and self.exp.age <= 9:
            if self.index >= 21:
                return test_res1
            elif self.index >= 17 and self.index <= 20.9:
                return test_res2
            elif self.index >= 12 and self.index <= 16.9:
                return test_res3
            elif self.index >= 6.5 and self.index <= 11.9:
                return test_res4
            else:
                return test_res5