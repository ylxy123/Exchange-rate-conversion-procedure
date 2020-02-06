# @Time : 2020/2/6 21:22
# @Author : YLXY
# @File : CallFirstMainWin.py
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from firstMainWin import *

class MyMainWindow(QMainWindow, Ui_name):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__  == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())