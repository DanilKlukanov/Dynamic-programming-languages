import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QTableWidget, QHBoxLayout
import csv

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.loadUI()
        self.loadTable('students.csv')

    def loadUI(self):
        self.setGeometry(100, 100, 800, 400)
        self.lay = QHBoxLayout()
        self.table = QTableWidget()
        self.lay.addWidget(self.table)
        self.setLayout(self.lay)

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            title = next(reader)
            self.table.setColumnCount(len(title))
            self.table.setHorizontalHeaderLabels(title)
            self.table.setRowCount(0)
            for i, row in enumerate(reader):
                self.table.setRowCount(self.table.rowCount() + 1)

                count = 0
                color = "#FFFFFF"
                for j in range(3, 10, 1):
                    count += float(row[j].replace(',','.')) / 7
                if count >= 95:
                    color = "#C2FF7C"
                elif count < 95 and count >= 80:
                    color  = "#FAFF7C"
                elif count < 80 and count >= 60:
                    color = "#FF7C7C"

                for j, elem in enumerate(row):
                    #добавляет элемент
                    self.table.setItem(i, j, QTableWidgetItem(elem))
                    #меняем цвет
                    self.table.item(i,j).setBackground(QtGui.QColor(color))
        self.table.resizeColumnsToContents()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())