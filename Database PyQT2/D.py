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
        uic.loadUi('d.ui',self)
        self.con = sqlite3.connect("films.db")
        self.cur = self.con.cursor()
        #button init
        self.button_name.clicked.connect(self.find_name)
        self.button_genre.clicked.connect(self.find_genre)
        #table init
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(('Название','Год','Продолжительность'))
        self.table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        #combo-box init
        cry = self.cur.execute(f'SELECT * FROM genres').fetchall()
        cry = [el[1] for el in cry]
        cry.sort()
        self.combo.addItems(cry)

    def find_name(self):
        result = self.cur.execute(f'SELECT * FROM Films WHERE Title LIKE \'%{self.line_name.text()}%\'').fetchmany(99)
        self.cout(result)

    def find_genre(self):
        year = self.line_year.text().isnumeric()
        time = self.line_time.text().isnumeric()
        fall = self.combo.currentText()
        yeaR = self.line_year.text()
        timE = self.line_time.text()

        result = ''
        if fall == 'не выбрано':
            if year == True and time == True:
               result = f'SELECT * FROM Films WHERE year = \'{yeaR}\' AND duration = \'{timE}\'' 
            if year == True and time == False:
                result = f'SELECT * FROM Films WHERE year = \'{yeaR}\''
            if time == True and year == False:
                result = f'SELECT * FROM Films WHERE duration = \'{timE}\''
            if year == False and time == False:
                result = f'SELECT * FROM Films'
        else:
            i = self.cur.execute(f'SELECT * FROM Genres WHERE title = \'{fall}\'').fetchall()
            result = f'SELECT * FROM Films WHERE genre = \'{i[0][0]}\''
            if year == True and time == True:
               result += f'AND year = \'{yeaR}\' AND duration = \'{timE}\''
            if year == True and time == False:
                result += f' AND year = \'{yeaR}\''
            if time == True and year == False:
                result += f' AND duration = \'{timE}\''
        self.cout(self.cur.execute(result).fetchmany(99))

    def cout(self, result):
        self.table.setRowCount(0)
        for i, col in enumerate(result):
            self.table.setRowCount(self.table.rowCount() + 1)
            self.table.setItem(i, 0, QTableWidgetItem(col[1]))
            self.table.setItem(i, 1, QTableWidgetItem(str(col[2])))
            self.table.setItem(i, 2, QTableWidgetItem(str(col[4])))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())