# @Time : 2020/2/6 21:22
# @Author : YLXY
# @File : CallFirstMainWin.py
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QDateTime
from firstMainWin import Ui_Exchange
from getData import *


class Exchange(QWidget, Ui_Exchange):
    def __init__(self):
        self.frommoney = ''
        self.tomoney = ''
        self.moneyname = 0
        self.moneyclass = 0
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.connecter()
        self.show()
    # 显示动态时间
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.timelabel.setText(text)



    def showmoneyname(self, money):
        if money != '货币名称':
            self.display_bar2.setText(getmoneyname(money))
        else:
            self.display_bar2.clear()

    def cur_exchange_money(self, former, new):
        self.display_bar3.setText(cur_exchange(former, new))

    def cur_inq(self):
        self.display_bar1.setText(getdata('cd0ddf0d24e0291f18d0d519d04700af', self.moneyname, self.moneyclass)+'RMB')

    def from_money(self, former_money):
        self.frommoney =  getmoneyname(former_money)

    def to_money(self, new_money):
        self.tomoney =  getmoneyname(new_money)

    def name(self, cur_name):
        self.moneyname = int(cur_name)-1

    def moneyclasses(self, moneyclass):
        self.moneyclass = int(moneyclass)+1

    def inq(self):
        self.display_bar3.setText(cur_exchange('cd0ddf0d24e0291f18d0d519d04700af', self.frommoney, self.tomoney))

    def connecter(self):
        self.get_cur_name.currentIndexChanged['QString'].connect(self.showmoneyname)
        self.from_cur.currentIndexChanged['QString'].connect(self.from_money)
        self.cur_class.currentIndexChanged['int'].connect(self.moneyclasses)
        self.cur_name.currentIndexChanged['int'].connect(self.name)
        self.to_cur.currentIndexChanged['QString'].connect(self.to_money)
        self.exchange_inquiry.clicked.connect(self.inq)
        self.cur_inquiry.clicked.connect(self.cur_inq)


if __name__  == "__main__":
    app = QApplication(sys.argv)
    Ex = Exchange()
    sys.exit(app.exec())
