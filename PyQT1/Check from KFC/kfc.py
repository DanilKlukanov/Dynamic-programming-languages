import sys
import os
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit, QLabel
import desug

class Window(QMainWindow, desug.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cb1.stateChanged.connect(lambda : self.sb1.setEnabled(self.cb1.isChecked()))
        self.cb2.stateChanged.connect(lambda : self.sb2.setEnabled(self.cb2.isChecked()))
        self.cb3.stateChanged.connect(lambda : self.sb3.setEnabled(self.cb3.isChecked()))
        self.cb4.stateChanged.connect(lambda : self.sb4.setEnabled(self.cb4.isChecked()))
        self.cb5.stateChanged.connect(lambda : self.sb5.setEnabled(self.cb5.isChecked()))
        self.tabWidget.currentChanged.connect(self.count)
        self.label_5.setPixmap(QtGui.QPixmap("11.png"))
        self.label_9.setPixmap(QtGui.QPixmap("32.png"))
        self.label_4.setPixmap(QtGui.QPixmap("12.png"))
        self.staff = [("Чизбургер с луком", 74), ("Шефбургер Джуниор", 109), ("Шефбургер Джуниор острый", 109), ("Чай черный", 74), ("Кофе Капучино", 64)] 
        self.state = [(self.cb1, self.sb1), (self.cb2, self.sb2), (self.cb3, self.sb3), (self.cb4, self.sb4), (self.cb5, self.sb5)]
    
    def count(self):
        if self.tabWidget.currentIndex() == 1:
            self.out.clear()
            self.summ = 0
            for i in range(5):
                if self.state[i][0].isChecked():
                    self.out.insertPlainText(self.staff[i][0] + "  " + str(self.staff[i][1]) + " x " + str(self.state[i][1].value()) + "   " + str(self.staff[i][1] * self.state[i][1].value()) + "\n")
                    self.summ = self.summ + self.staff[i][1] * self.state[i][1].value()
            self.out.insertPlainText(f"\n\nИтог   {str(self.summ)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())