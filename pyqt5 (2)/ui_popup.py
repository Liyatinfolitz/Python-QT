# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.send = QtWidgets.QFrame(self.centralwidget)
        self.send.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.send.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.send.setFrameShadow(QtWidgets.QFrame.Raised)
        self.send.setObjectName("send")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.send)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.send)
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.send)
        self.loading = QtWidgets.QFrame(self.centralwidget)
        self.loading.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.loading.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loading.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loading.setObjectName("loading")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.loading)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.loading)
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.loading)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Sending profile......"))
        self.label.setText(_translate("MainWindow", "Loading In Progress....."))
