import sys
import sqlite3
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit, QTableWidgetItem

class MyWindow(QMainWindow):
    result = []
    def __init__(self):
        super().__init__()
        uic.loadUi('g.ui',self)
        self.con = sqlite3.connect("films.db")
        self.cur = self.con.cursor()
        #button init
        self.button_name.clicked.connect(self.find_name)
        self.button_genre.clicked.connect(self.find_genre)
        self.button_save.clicked.connect(self.edit_save)
        self.button_add.clicked.connect(self.edit_add)
        self.button_del.clicked.connect(self.edit_del)
        #table init
        self.table.setColumnCount(4)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(['ID','Название','Год','Продолжительность'])
        self.table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        #combo-box init
        cry = self.cur.execute(f'SELECT * FROM genres').fetchall()
        cry = [el[1] for el in cry]
        cry.sort()
        self.combo.addItems(cry)

    def edit_add(self):
        add.show()

    def edit_del(self):
        pop.show()

    def find_name(self):
        self.result = self.cur.execute(f'SELECT * FROM Films WHERE Title LIKE \'%{self.line_name.text()}%\'').fetchmany(99)
        self.cout()

    def find_genre(self):
        year = self.line_year.text().isnumeric()
        time = self.line_time.text().isnumeric()
        fall = self.combo.currentText()
        yeaR = self.line_year.text()
        timE = self.line_time.text()

        sup = ''
        if fall == 'не выбрано':
            if year == True and time == True:
               sup = f'SELECT * FROM Films WHERE year = \'{yeaR}\' AND duration = \'{timE}\'' 
            if year == True and time == False:
                sup = f'SELECT * FROM Films WHERE year = \'{yeaR}\''
            if time == True and year == False:
                sup = f'SELECT * FROM Films WHERE duration = \'{timE}\''
            if year == False and time == False:
                sup = f'SELECT * FROM Films'
        else:
            i = self.cur.execute(f'SELECT * FROM Genres WHERE title = \'{fall}\'').fetchall()
            sup = f'SELECT * FROM Films WHERE genre = \'{i[0][0]}\''
            if year == True and time == True:
               sup += f'AND year = \'{yeaR}\' AND duration = \'{timE}\''
            if year == True and time == False:
                sup += f' AND year = \'{yeaR}\''
            if time == True and year == False:
                sup += f' AND duration = \'{timE}\''
        self.result = self.cur.execute(sup).fetchmany(99)
        self.cout()

    def cout(self):
        self.table.setRowCount(0)
        for i, col in enumerate(self.result):
            self.table.setRowCount(self.table.rowCount() + 1)
            item = QTableWidgetItem(str(col[0]))
            item.setFlags(Qt.ItemIsEnabled)
            self.table.setItem(i, 0, item)
            self.table.setItem(i, 1, QTableWidgetItem(col[1]))
            self.table.setItem(i, 2, QTableWidgetItem(str(col[2])))
            self.table.setItem(i, 3, QTableWidgetItem(str(col[4])))
    
    def edit_save(self):
        new = []
        old = []
        for i in range(len(self.result)):
            idd = str(self.result[i][0])
            name = str(self.result[i][1])
            year = str(self.result[i][2])
            time = str(self.result[i][3])
            old.append((idd, name, year, time))
            idd = self.table.item(i, 0).text()
            name = self.table.item(i, 1).text()
            year = self.table.item(i, 2).text()
            time = self.table.item(i, 3).text()
            new.append((idd, name, year, time))
        for i in new:
            if i[1] not in old:
                self.cur.execute(f'UPDATE films SET title = \'{i[1]}\' WHERE id = \'{i[0]}\'')
            if i[2] not in old:
                self.cur.execute(f'UPDATE films SET year = \'{i[2]}\' WHERE id = \'{i[0]}\'')
            if i[3] not in old:
                self.cur.execute(f'UPDATE films SET duration = \'{i[3]}\' WHERE id = \'{i[0]}\'')
        self.con.commit()

class Add(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('add.ui',self)

        List_one = main.cur.execute(f'SELECT * FROM genres').fetchall()
        List_one = [el[1] for el in List_one]
        List_one.sort()
        self.new_combo.addItems(List_one)

        self.new_el.clicked.connect(self.add_el)
    
    def add_el(self):
        new_g = self.new_combo.currentText()
        new_n = self.new_name.text()
        new_d = self.new_year.text()
        new_t = self.new_dur.text()
        
        new_gener = main.cur.execute(f'SELECT * FROM genres WHERE title = \'{new_g}\'').fetchall()

        if len(new_n) != 0:
            main.cur.execute(f'INSERT INTO films(title, duration, genre,year) VALUES(\'{new_n}\',\'{new_t}\',\'{new_gener[0][0]}\',\'{new_d}\')')
            self.new_name.clear()
            self.new_year.clear()
            self.new_dur.clear()
            main.con.commit()
            self.close()

class Del(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('notice.ui',self)

        self.button_no.clicked.connect(self.no)
        self.button_yes.clicked.connect(self.yes)

    def no(self):
        self.close()

    def yes(self):
        #selectedRows возвращает список индексов выделенных элементов из указанной строки
        i = main.table.selectionModel().selectedRows()
        #идем по строчечкам
        for j in range(len(i)-1, -1, -1):
            #row() возвращает индекс строки
            main.cur.execute(f'DELETE from Films WHERE id = \'{main.result[i[j].row()][0]}\'')
            main.table.removeRow(i[j].row())
        main.con.commit()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    add = Add()
    pop = Del()
    sys.exit(app.exec_())