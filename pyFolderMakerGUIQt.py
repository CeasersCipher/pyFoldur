# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyFolderMaker.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_folderMaker(object):
    def setupUi(self, folderMaker):
        folderMaker.setObjectName("folderMaker")
        folderMaker.resize(240, 320)
        folderMaker.setMinimumSize(QtCore.QSize(240, 320))
        folderMaker.setMaximumSize(QtCore.QSize(240, 320))
        self.destinationButton = QtWidgets.QPushButton(folderMaker)
        self.destinationButton.setGeometry(QtCore.QRect(10, 240, 113, 32))
        self.destinationButton.setObjectName("destinationButton")
        self.startButton = QtWidgets.QPushButton(folderMaker)
        self.startButton.setGeometry(QtCore.QRect(10, 270, 113, 32))
        self.startButton.setObjectName("startButton")
        self.topFolders = QtWidgets.QTextEdit(folderMaker)
        self.topFolders.setGeometry(QtCore.QRect(10, 30, 221, 121))
        self.topFolders.setObjectName("topFolders")
        self.bottomFolders = QtWidgets.QTextEdit(folderMaker)
        self.bottomFolders.setGeometry(QtCore.QRect(10, 180, 221, 51))
        self.bottomFolders.setObjectName("bottomFolders")
        self.topFolders_2 = QtWidgets.QLabel(folderMaker)
        self.topFolders_2.setGeometry(QtCore.QRect(20, 10, 211, 16))
        self.topFolders_2.setObjectName("topFolders_2")
        self.label = QtWidgets.QLabel(folderMaker)
        self.label.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.label.setObjectName("label")

        self.retranslateUi(folderMaker)
        QtCore.QMetaObject.connectSlotsByName(folderMaker)

    def retranslateUi(self, folderMaker):
        _translate = QtCore.QCoreApplication.translate
        folderMaker.setWindowTitle(_translate("folderMaker", "Folder Maker"))
        self.destinationButton.setText(_translate("folderMaker", "Destination"))
        self.startButton.setText(_translate("folderMaker", "Start"))
        self.topFolders_2.setText(_translate("folderMaker", "Top Folders (seperate by comma)"))
        self.label.setText(_translate("folderMaker", "Bottom Folders"))

