# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 481)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.enter = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.enter.sizePolicy().hasHeightForWidth())
        self.enter.setSizePolicy(sizePolicy)
        self.enter.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.enter.setObjectName("enter")
        self.gridLayout.addWidget(self.enter, 5, 0, 1, 2)
        self.six = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.six.sizePolicy().hasHeightForWidth())
        self.six.setSizePolicy(sizePolicy)
        self.six.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.six.setObjectName("six")
        self.gridLayout.addWidget(self.six, 3, 2, 1, 1)
        self.back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 127);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.back.setObjectName("back")
        self.gridLayout.addWidget(self.back, 4, 3, 1, 1)
        self.five = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.five.sizePolicy().hasHeightForWidth())
        self.five.setSizePolicy(sizePolicy)
        self.five.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.five.setObjectName("five")
        self.gridLayout.addWidget(self.five, 3, 1, 1, 1)
        self.output = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 0, 0, 1, 4)
        self.three = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.three.sizePolicy().hasHeightForWidth())
        self.three.setSizePolicy(sizePolicy)
        self.three.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.three.setObjectName("three")
        self.gridLayout.addWidget(self.three, 2, 2, 1, 1)
        self.one = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.one.sizePolicy().hasHeightForWidth())
        self.one.setSizePolicy(sizePolicy)
        self.one.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.one.setObjectName("one")
        self.gridLayout.addWidget(self.one, 2, 0, 1, 1)
        self.four_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.four_2.sizePolicy().hasHeightForWidth())
        self.four_2.setSizePolicy(sizePolicy)
        self.four_2.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.four_2.setObjectName("four_2")
        self.gridLayout.addWidget(self.four_2, 3, 0, 1, 1)
        self.two = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.two.sizePolicy().hasHeightForWidth())
        self.two.setSizePolicy(sizePolicy)
        self.two.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.two.setObjectName("two")
        self.gridLayout.addWidget(self.two, 2, 1, 1, 1)
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.nine.sizePolicy().hasHeightForWidth())
        self.nine.setSizePolicy(sizePolicy)
        self.nine.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.nine.setObjectName("nine")
        self.gridLayout.addWidget(self.nine, 4, 2, 1, 1)
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.eight.sizePolicy().hasHeightForWidth())
        self.eight.setSizePolicy(sizePolicy)
        self.eight.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.eight.setObjectName("eight")
        self.gridLayout.addWidget(self.eight, 4, 1, 1, 1)
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.seven.sizePolicy().hasHeightForWidth())
        self.seven.setSizePolicy(sizePolicy)
        self.seven.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.seven.setObjectName("seven")
        self.gridLayout.addWidget(self.seven, 4, 0, 1, 1)
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.zero.sizePolicy().hasHeightForWidth())
        self.zero.setSizePolicy(sizePolicy)
        self.zero.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border-radius: 15px;\n"
"\n"
"\n"
"")
        self.zero.setObjectName("zero")
        self.gridLayout.addWidget(self.zero, 5, 2, 1, 1)
        self.dot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.dot.sizePolicy().hasHeightForWidth())
        self.dot.setSizePolicy(sizePolicy)
        self.dot.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 127);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.dot.setObjectName("dot")
        self.gridLayout.addWidget(self.dot, 5, 3, 1, 1)
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.minus.sizePolicy().hasHeightForWidth())
        self.minus.setSizePolicy(sizePolicy)
        self.minus.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 127);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.minus.setObjectName("minus")
        self.gridLayout.addWidget(self.minus, 3, 3, 1, 1)
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)
        self.clear.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.clear.setObjectName("clear")
        self.gridLayout.addWidget(self.clear, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enter.setText(_translate("MainWindow", "ENTER"))
        self.six.setText(_translate("MainWindow", "6"))
        self.back.setText(_translate("MainWindow", "<-"))
        self.five.setText(_translate("MainWindow", "5"))
        self.output.setText(_translate("MainWindow", "0"))
        self.three.setText(_translate("MainWindow", "3"))
        self.one.setText(_translate("MainWindow", "1"))
        self.four_2.setText(_translate("MainWindow", "4"))
        self.two.setText(_translate("MainWindow", "2"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.dot.setText(_translate("MainWindow", "."))
        self.minus.setText(_translate("MainWindow", "-"))
        self.clear.setText(_translate("MainWindow", "Clear"))
