#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cal(object):
    def setupUi(self, cal):
        cal.setObjectName("cal")
        cal.resize(857, 398)
        font = QtGui.QFont()
        font.setPointSize(12)
        cal.setFont(font)
        self.txtEventList = QtWidgets.QTextEdit(cal)
        self.txtEventList.setGeometry(QtCore.QRect(430, 11, 401, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtEventList.setFont(font)
        self.txtEventList.setObjectName("txtEventList")
        self.calWidget = QtWidgets.QCalendarWidget(cal)
        self.calWidget.setGeometry(QtCore.QRect(10, 10, 392, 361))
        self.calWidget.setObjectName("calWidget")
        self.btnSave = QtWidgets.QPushButton(cal)
        self.btnSave.setGeometry(QtCore.QRect(550, 350, 171, 31))
        self.btnSave.setObjectName("btnSave")

        self.retranslateUi(cal)
        QtCore.QMetaObject.connectSlotsByName(cal)

    def retranslateUi(self, cal):
        _translate = QtCore.QCoreApplication.translate
        cal.setWindowTitle(_translate("cal", "Календарь событий"))
        self.btnSave.setText(_translate("cal", "Сохранить"))