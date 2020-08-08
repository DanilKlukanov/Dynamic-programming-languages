# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'b.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: rgb(73, 106, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(5, 160, 791, 431))
        self.table.setMinimumSize(QtCore.QSize(791, 431))
        self.table.setMaximumSize(QtCore.QSize(791, 431))
        self.table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(9, 30, 781, 80))
        self.horizontalWidget.setStyleSheet("font: 87 16pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalWidget)
        self.label.setMinimumSize(QtCore.QSize(255, 50))
        self.label.setMaximumSize(QtCore.QSize(255, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 87 16pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.button = QtWidgets.QPushButton(self.horizontalWidget)
        self.button.setMinimumSize(QtCore.QSize(255, 50))
        self.button.setMaximumSize(QtCore.QSize(255, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.button.setFont(font)
        self.button.setStyleSheet("background-color: rgb(83, 120, 255);")
        self.button.setObjectName("button")
        self.horizontalLayout.addWidget(self.button)
        self.line = QtWidgets.QLineEdit(self.horizontalWidget)
        self.line.setMinimumSize(QtCore.QSize(255, 50))
        self.line.setMaximumSize(QtCore.QSize(255, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.line.setFont(font)
        self.line.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.line.setAlignment(QtCore.Qt.AlignCenter)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Ведьмаку заплатите чеканной монетой</p></body></html>"))
        self.label.setText(_translate("MainWindow", "      Enter genre name"))
        self.button.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
