# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_name(object):
    def setupUi(self, name):
        name.setObjectName("name")
        name.resize(671, 595)
        self.pushButton = QtWidgets.QPushButton(name)
        self.pushButton.setGeometry(QtCore.QRect(190, 520, 301, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(name)
        QtCore.QMetaObject.connectSlotsByName(name)

    def retranslateUi(self, name):
        _translate = QtCore.QCoreApplication.translate
        name.setWindowTitle(_translate("name", "Form"))
        self.pushButton.setText(_translate("name", "关    闭"))
