# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e.ui'
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 170, 781, 371))
        self.tableWidget.setMinimumSize(QtCore.QSize(781, 371))
        self.tableWidget.setMaximumSize(QtCore.QSize(781, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(10, 10, 781, 61))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalWidget)
        self.label.setMinimumSize(QtCore.QSize(255, 40))
        self.label.setMaximumSize(QtCore.QSize(255, 40))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(255, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(255, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(255, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(255, 40))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget1.setGeometry(QtCore.QRect(10, 80, 781, 61))
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalWidget1)
        self.label_2.setMinimumSize(QtCore.QSize(80, 40))
        self.label_2.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalWidget1)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(100, 40))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalWidget1)
        self.label_3.setMinimumSize(QtCore.QSize(80, 40))
        self.label_3.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalWidget1)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(100, 40))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(100, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget1)
        self.label_4.setMinimumSize(QtCore.QSize(80, 40))
        self.label_4.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.horizontalWidget1)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 40))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalWidget1)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 550, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите название фильма"))
        self.pushButton.setText(_translate("MainWindow", "Нажми"))
        self.label_2.setText(_translate("MainWindow", "Год"))
        self.label_3.setText(_translate("MainWindow", "Время"))
        self.label_4.setText(_translate("MainWindow", "Жанр"))
        self.comboBox.setItemText(0, _translate("MainWindow", "не выбрано"))
        self.pushButton_2.setText(_translate("MainWindow", "Нажми"))
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())