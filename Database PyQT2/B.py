import sys
import sqlite3
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit, QTableWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('b.ui',self)
        self.con = sqlite3.connect("films.db")
        self.cur = self.con.cursor()
        self.button.clicked.connect(self.press)
        tit = ('Название','Год','Продолжительность')
        self.table.setColumnCount(len(tit))
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(tit)
        self.table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        

    def press(self):
        fall = self.line.text()
        self.table.setRowCount(0)
        result = self.cur.execute(f'SELECT * FROM genres WHERE title = \'{fall}\'').fetchone()
        if len(result) != 0:
            da = self.cur.execute(f'SELECT * FROM Films WHERE genre = \'{result[0][0]}\'').fetchmany(500)
            for i, line in enumerate(da):
                self.table.setRowCount(self.table.rowCount() + 1)
                self.table.setItem(i, 0, QTableWidgetItem(line[1]))
                self.table.setItem(i, 1, QTableWidgetItem(str(line[2])))
                self.table.setItem(i, 2, QTableWidgetItem(str(line[4])))

            self.table.resizeColumnsToContents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())