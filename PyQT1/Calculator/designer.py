# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desig.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 605)
        MainWindow.setMinimumSize(QtCore.QSize(380, 605))
        MainWindow.setMaximumSize(QtCore.QSize(380, 605))
        MainWindow.setStyleSheet("font: 75 16pt \"Segoe Script\";\n"
"background-color: rgb(98, 98, 95);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 90, 361, 436))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_6.setContentsMargins(5, 5, 1, 5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.cal_left = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_left.setMinimumSize(QtCore.QSize(70, 70))
        self.cal_left.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_left.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_left.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(203, 207, 202);\n"
"border:\"none\";")
        self.cal_left.setObjectName("cal_left")
        self.gridLayout_6.addWidget(self.cal_left, 4, 0, 1, 1)
        self.cal_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_0.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_0.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:\"none\";")
        self.cal_0.setObjectName("cal_0")
        self.gridLayout_6.addWidget(self.cal_0, 4, 1, 1, 1)
        self.cal_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_plus.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_plus.setStyleSheet("font: 75 24pt \"Segoe Script\";\n"
"background-color: rgb(255, 170, 0);\n"
"border:\"none\";")
        self.cal_plus.setObjectName("cal_plus")
        self.gridLayout_6.addWidget(self.cal_plus, 3, 3, 1, 1)
        self.cal_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_minus.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_minus.setStyleSheet("font: 75 24pt \"Segoe Script\";\n"
"background-color: rgb(255, 170, 0);\n"
"border:\"none\";")
        self.cal_minus.setObjectName("cal_minus")
        self.gridLayout_6.addWidget(self.cal_minus, 2, 3, 1, 1)
        self.cal_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_6.setMinimumSize(QtCore.QSize(70, 70))
        self.cal_6.setMaximumSize(QtCore.QSize(70, 16777215))
        self.cal_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_6.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:\"none\";")
        self.cal_6.setObjectName("cal_6")
        self.gridLayout_6.addWidget(self.cal_6, 2, 2, 1, 1)
        self.cal_C = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_C.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_C.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_C.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(203, 207, 202);\n"
"border:\"none\";")
        self.cal_C.setObjectName("cal_C")
        self.gridLayout_6.addWidget(self.cal_C, 0, 0, 1, 1)
        self.cal_X = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_X.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_X.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_X.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(255, 170, 0);\n"
"border:\"none\";")
        self.cal_X.setObjectName("cal_X")
        self.gridLayout_6.addWidget(self.cal_X, 1, 3, 1, 1)
        self.cal_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_9.setMinimumSize(QtCore.QSize(70, 70))
        self.cal_9.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_9.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:\"none\";")
        self.cal_9.setObjectName("cal_9")
        self.gridLayout_6.addWidget(self.cal_9, 1, 2, 1, 1)
        self.cal_ster = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_ster.setMinimumSize(QtCore.QSize(70, 70))
        self.cal_ster.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_ster.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_ster.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(203, 207, 202);\n"
"border:\"none\";")
        self.cal_ster.setObjectName("cal_ster")
        self.gridLayout_6.addWidget(self.cal_ster, 0, 1, 1, 1)
        self.cal_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_1.setMinimumSize(QtCore.QSize(70, 70))
        self.cal_1.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_1.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:\"none\";")
        self.cal_1.setObjectName("cal_1")
        self.gridLayout_6.addWidget(self.cal_1, 3, 0, 1, 1)
        self.cal_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_8.setMinimumSize(QtCore.QSize(70, 70))
        self.cal_8.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_8.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:\"none\";")
        self.cal_8.setObjectName("cal_8")
        self.gridLayout_6.addWidget(self.cal_8, 1, 1, 1, 1)
        self.cal_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_2.setMinimumSize(QtCore.QSize(70, 70))
        self.cal_2.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_2.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:\"none\";")
        self.cal_2.setObjectName("cal_2")
        self.gridLayout_6.addWidget(self.cal_2, 3, 1, 1, 1)
        self.cal_eq = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_eq.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_eq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_eq.setStyleSheet("font: 75 24pt \"Segoe Script\";\n"
"background-color: rgb(255, 170, 0);\n"
"border:\"none\";")
        self.cal_eq.setObjectName("cal_eq")
        self.gridLayout_6.addWidget(self.cal_eq, 4, 3, 1, 1)
        self.cal_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_3.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_3.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:\"none\";")
        self.cal_3.setObjectName("cal_3")
        self.gridLayout_6.addWidget(self.cal_3, 3, 2, 1, 1)
        self.cal_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_5.setMinimumSize(QtCore.QSize(70, 70))
        self.cal_5.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_5.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:\"none\";")
        self.cal_5.setObjectName("cal_5")
        self.gridLayout_6.addWidget(self.cal_5, 2, 1, 1, 1)
        self.cal_tochka = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_tochka.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_tochka.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_tochka.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(203, 207, 202);\n"
"border:\"none\";")
        self.cal_tochka.setObjectName("cal_tochka")
        self.gridLayout_6.addWidget(self.cal_tochka, 0, 2, 1, 1)
        self.cal_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_7.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_7.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:\"none\";")
        self.cal_7.setObjectName("cal_7")
        self.gridLayout_6.addWidget(self.cal_7, 1, 0, 1, 1)
        self.cal_right = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_right.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_right.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_right.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(203, 207, 202);\n"
"border:\"none\";")
        self.cal_right.setObjectName("cal_right")
        self.gridLayout_6.addWidget(self.cal_right, 4, 2, 1, 1)
        self.cal_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_4.setMinimumSize(QtCore.QSize(70, 70))
        self.cal_4.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_4.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:\"none\";")
        self.cal_4.setObjectName("cal_4")
        self.gridLayout_6.addWidget(self.cal_4, 2, 0, 1, 1)
        self.cal_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cal_div.setMaximumSize(QtCore.QSize(70, 70))
        self.cal_div.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_div.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cal_div.setStyleSheet("font: 75 22pt \"Segoe Script\";\n"
"background-color: rgb(255, 170, 0);\n"
"border:\"none\";")
        self.cal_div.setObjectName("cal_div")
        self.gridLayout_6.addWidget(self.cal_div, 0, 3, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 361, 71))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 39))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cal_left.setText(_translate("MainWindow", "("))
        self.cal_0.setText(_translate("MainWindow", "0"))
        self.cal_plus.setText(_translate("MainWindow", "+"))
        self.cal_minus.setText(_translate("MainWindow", "-"))
        self.cal_6.setText(_translate("MainWindow", "6"))
        self.cal_C.setText(_translate("MainWindow", "C"))
        self.cal_X.setText(_translate("MainWindow", "X"))
        self.cal_9.setText(_translate("MainWindow", "9"))
        self.cal_ster.setText(_translate("MainWindow", "<="))
        self.cal_1.setText(_translate("MainWindow", "1"))
        self.cal_8.setText(_translate("MainWindow", "8"))
        self.cal_2.setText(_translate("MainWindow", "2"))
        self.cal_eq.setText(_translate("MainWindow", "="))
        self.cal_3.setText(_translate("MainWindow", "3"))
        self.cal_5.setText(_translate("MainWindow", "5"))
        self.cal_tochka.setText(_translate("MainWindow", "."))
        self.cal_7.setText(_translate("MainWindow", "7"))
        self.cal_right.setText(_translate("MainWindow", ")"))
        self.cal_4.setText(_translate("MainWindow", "4"))
        self.cal_div.setText(_translate("MainWindow", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
