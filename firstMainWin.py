# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(292, 249)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 201, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(40, 130, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 130, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 170, 221, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 80, 221, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "汇率查询"))
        self.label.setText(_translate("Form", "当日实时汇率查询"))
        self.comboBox.setItemText(0, _translate("Form", "货币名称"))
        self.comboBox.setItemText(1, _translate("Form", "美元"))
        self.comboBox.setItemText(2, _translate("Form", "韩元"))
        self.comboBox.setItemText(3, _translate("Form", "日元"))
        self.comboBox.setItemText(4, _translate("Form", "港币"))
        self.comboBox.setItemText(5, _translate("Form", "英镑"))
        self.comboBox.setItemText(6, _translate("Form", "欧元"))
        self.comboBox.setItemText(7, _translate("Form", "加拿大元"))
        self.comboBox.setItemText(8, _translate("Form", "澳大利亚元"))
        self.comboBox_2.setItemText(0, _translate("Form", "查询类别"))
        self.comboBox_2.setItemText(1, _translate("Form", "现汇买入价"))
        self.comboBox_2.setItemText(2, _translate("Form", "现钞买入价"))
        self.comboBox_2.setItemText(3, _translate("Form", "现钞卖出价"))
        self.comboBox_2.setItemText(4, _translate("Form", "中行折算价"))
        self.pushButton.setText(_translate("Form", "查询"))
