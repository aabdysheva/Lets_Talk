# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/signs.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget


# Окно, которое открывается по кнопке "Available signs"
class Ui_available_signs(object):
    def setupUi(self, available_signs):
        available_signs.setObjectName("available_signs")
        available_signs.setFixedSize(600, 861)
        available_signs.move(QDesktopWidget().availableGeometry().center() + QtCore.QPoint(250, -430))
        self.resources_label = QtWidgets.QLabel(available_signs)
        self.resources_label.setGeometry(QtCore.QRect(50, 530, 500, 200))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.resources_label.setFont(font)
        self.resources_label.setTextFormat(QtCore.Qt.AutoText)
        self.resources_label.setScaledContents(False)
        self.resources_label.setWordWrap(True)
        self.resources_label.setObjectName("resources_label")
        self.letters_label = QtWidgets.QLabel(available_signs)
        self.letters_label.setGeometry(QtCore.QRect(50, 10, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.letters_label.setFont(font)
        self.letters_label.setAlignment(QtCore.Qt.AlignCenter)
        self.letters_label.setObjectName("letters_label")
        self.label = QtWidgets.QLabel(available_signs)
        self.label.setGeometry(QtCore.QRect(50, 60, 500, 500))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("pictures/alphabet.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")

        font = QtGui.QFont()
        font.setPointSize(15)
        self.reference = QtWidgets.QLabel(available_signs)
        self.reference.setFont(font)
        self.reference.setTextFormat(QtCore.Qt.AutoText)
        self.reference.setScaledContents(False)
        self.reference.setWordWrap(True)
        self.reference.setOpenExternalLinks(True)
        self.reference.setGeometry(QtCore.QRect(50, 710, 500, 100))

        self.retranslateUi(available_signs)
        QtCore.QMetaObject.connectSlotsByName(available_signs)

    def retranslateUi(self, available_signs):
        _translate = QtCore.QCoreApplication.translate
        available_signs.setWindowTitle(_translate("available_signs", "Let\'s Talk - Available signs"))
        self.resources_label.setText(_translate("available_signs", "<html><head/><body><p><span style=\" font-weight:600;\">Words</span>: I(me), like, play, need, eat, clothes, motorcycle, boots, thank you</p><p><span style=\" font-weight:600;\">Control signs</span>: model_stop, model_start, NaN </p></body></html>"))
        self.letters_label.setText(_translate("available_signs", "Available signs"))
        self.reference.setText(
            _translate("available_signs", '<html><head/><body><p><span style=\" font-weight:600;\">Useful resources</span>: <a href="https://youtu.be/u3HoC9_ir3s">Learn alphabet on YouTube</a>, </p><p> <a href="https://www.handspeak.com">Learn ASL on handspeak.com</a> </p></body></html>'))