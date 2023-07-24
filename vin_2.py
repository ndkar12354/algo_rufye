from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from instr import *
from vin_3 import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

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
        self.timer_test1 = QLabel(timer_test_1)
        self.timer_test1.setFont(QFont("Times", 36, QFont.Bold))

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

        self.r_line.addWidget(self.timer_test1, alignment= Qt.AlignRight)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    

    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.line_age.text()), self.line_prised.text(), self.line_final_1.text(), self.line_final_2.text())
        self.fw = FinalWin(self.exp)

    def timer_test(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_test1.setText(time.toString('hh:mm:ss'))
        self.timer_test1.setFont(QFont('Times', 36, QFont.Bold))
        self.timer_test1.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_test1.setText(time.toString('hh:mm:ss')[6:8])
        self.timer_test1.setFont(QFont('Times', 36, QFont.Bold))
        self.timer_test1.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_final(self):
       global time
       time = QTime(0, 1, 0)
       self.timer = QTimer()
       self.timer.timeout.connect(self.timer3Event)
       self.timer.start(1000)


    def timer3Event(self):
       global time
       time = time.addSecs(-1)
       self.timer_test1.setText(time.toString("hh:mm:ss"))
       if int(time.toString("hh:mm:ss")[6:8]) >= 45:
           self.timer_test1.setStyleSheet("color: rgb(0,255,0)")
       elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
           self.timer_test1.setStyleSheet("color: rgb(0,255,0)")
       else:
           self.timer_test1.setStyleSheet("color: rgb(0,0,0)")
       self.timer_test1.setFont(QFont("Times", 36, QFont.Bold))
       if time.toString("hh:mm:ss") == "00:00:00":
           self.timer.stop()


    def connects(self):
        self.results.clicked.connect(self.next_click)
        self.btn_start.clicked.connect(self.timer_test)
        self.start_prised.clicked.connect(self.timer_sits)
        self.final_test.clicked.connect(self.timer_final)