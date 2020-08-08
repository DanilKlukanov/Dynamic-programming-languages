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
        uic.loadUi('c.ui',self)
        #table init
        self.con = sqlite3.connect("films.db")
        self.cur = self.con.cursor()
        tit = ('Название','Год','Продолжительность')
        self.table.setColumnCount(len(tit))
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(tit)
        self.table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.pushButton.clicked.connect(self.press)
        #combo-box init
        cry = self.cur.execute(f'SELECT * FROM genres').fetchall()
        cry = [el[1] for el in cry]
        cry.sort()
        self.combo.addItems(cry)

    def press(self):
        self.table.setRowCount(0)
        yet = self.combo.currentText()
        if yet == 'Не выбрано':
            aLL = self.cur.execute('SELECT * FROM Films').fetchmany(100)
        else:
            i = self.cur.execute(f'SELECT * FROM Genres WHERE title = \'{yet}\'').fetchall()
            aLL = self.cur.execute(f'SELECT * FROM Films WHERE genre = \'{i[0][0]}\'').fetchmany(100)
        for j, col in enumerate(aLL):
            self.table.setRowCount(self.table.rowCount() + 1)
            self.table.setItem(j, 0, QTableWidgetItem(col[1]))
            self.table.setItem(j, 1, QTableWidgetItem(str(col[2])))
            self.table.setItem(j, 2, QTableWidgetItem(str(col[4])))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())