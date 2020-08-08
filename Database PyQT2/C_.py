# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c.ui'
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
        MainWindow.setStyleSheet("background-color: rgb(62, 113, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 130, 781, 451))
        self.table.setMinimumSize(QtCore.QSize(781, 451))
        self.table.setMaximumSize(QtCore.QSize(781, 451))
        self.table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(9, 30, 781, 91))
        self.horizontalWidget.setMinimumSize(QtCore.QSize(781, 91))
        self.horizontalWidget.setMaximumSize(QtCore.QSize(781, 91))
        self.horizontalWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalWidget)
        self.label.setMinimumSize(QtCore.QSize(256, 50))
        self.label.setMaximumSize(QtCore.QSize(256, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.combo = QtWidgets.QComboBox(self.horizontalWidget)
        self.combo.setMinimumSize(QtCore.QSize(250, 50))
        self.combo.setMaximumSize(QtCore.QSize(250, 50))
        self.combo.setStyleSheet("background-color: rgb(157, 158, 184);\n"
"color: rgb(255, 255, 255);")
        self.combo.setObjectName("combo")
        self.horizontalLayout.addWidget(self.combo)
        self.pushButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(256, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(256, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setStyleSheet("background-color: rgb(66, 107, 255);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "!Сhoose a genre!"))
        self.pushButton.setText(_translate("MainWindow", "!Press!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
