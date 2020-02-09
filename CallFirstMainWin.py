# @Time : 2020/2/6 21:22
# @Author : YLXY
# @File : CallFirstMainWin.py
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from firstMainWin import Ui_Exchange
from getData import *


class Exchange(QWidget, Ui_Exchange):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        # self.connecter()
        self.show()

    def showmoneyname(self, money):
        self.display_bar2.setText(getmoneyname(money))









if __name__  == "__main__":
    app = QApplication(sys.argv)
    Ex = Exchange()

    sys.exit(app.exec())