# @Time : 2020/2/6 21:22
# @Author : YLXY
# @File : CallFirstMainWin.py
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from firstMainWin import Ui_name

class Calcular(QWidget, Ui_name):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.setupUi(self)
        self.connecter()
        self.show()

    def p_CE(self):
        self.lineEdit.clear()

    def p_Num_0(self):
        self.lineEdit.insert('0')

    def p_Num_1(self):
        self.lineEdit.insert('1')

    def p_Num_2(self):
        self.lineEdit.insert('2')

    def p_Num_3(self):
        self.lineEdit.insert('3')

    def p_Num_4(self):
        self.lineEdit.insert('4')

    def p_Num_5(self):
        self.lineEdit.insert('5')

    def p_Num_6(self):
        self.lineEdit.insert('6')

    def p_Num_7(self):
        self.lineEdit.insert('7')

    def p_Num_8(self):
        self.lineEdit.insert('8')

    def p_Num_9(self):
        self.lineEdit.insert('9')

    def p_plus(self):
        self.lineEdit.insert('+')

    def p_minus(self):
        self.lineEdit.insert('-')

    def p_multiply(self):
        self.lineEdit.insert('*')

    def p_div(self):
        self.lineEdit.insert('/')

    def calcu(self):
        text = self.lineEdit.text()
        try:
            result = eval(text)
            self.lineEdit.setText(str(eval(text)))
        except:
            self.lineEdit.setText('invalid syntax, check your input!')

    def connecter(self):
        self.Num_0.clicked.connect(self.p_Num_0)
        self.Num_1.clicked.connect(self.p_Num_1)
        self.Num_2.clicked.connect(self.p_Num_2)
        self.Num_3.clicked.connect(self.p_Num_3)
        self.Num_4.clicked.connect(self.p_Num_4)
        self.Num_5.clicked.connect(self.p_Num_5)
        self.Num_6.clicked.connect(self.p_Num_6)
        self.Num_7.clicked.connect(self.p_Num_7)
        self.Num_8.clicked.connect(self.p_Num_8)
        self.Num_9.clicked.connect(self.p_Num_9)
        self.Op_plus.clicked.connect(self.p_plus)
        self.Op_minus.clicked.connect(self.p_minus)
        self.Op_multiply.clicked.connect(self.p_multiply)
        self.Op_div.clicked.connect(self.p_div)
        self.Op_equal.clicked.connect(self.calcu)
        self.CE.clicked.connect(self.p_CE)

if __name__  == "__main__":
    app = QApplication(sys.argv)
    Ca = Calcular()
    sys.exit(app.exec())