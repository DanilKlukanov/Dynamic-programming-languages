import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import designer

class MyWidget(QMainWindow, designer.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cal_0.clicked.connect(lambda: self.plainTextEdit.insertPlainText("0"))
        self.cal_1.clicked.connect(lambda: self.plainTextEdit.insertPlainText("1"))
        self.cal_2.clicked.connect(lambda: self.plainTextEdit.insertPlainText("2"))
        self.cal_3.clicked.connect(lambda: self.plainTextEdit.insertPlainText("3"))
        self.cal_4.clicked.connect(lambda: self.plainTextEdit.insertPlainText("4"))
        self.cal_5.clicked.connect(lambda: self.plainTextEdit.insertPlainText("5"))
        self.cal_6.clicked.connect(lambda: self.plainTextEdit.insertPlainText("6"))
        self.cal_7.clicked.connect(lambda: self.plainTextEdit.insertPlainText("7"))
        self.cal_8.clicked.connect(lambda: self.plainTextEdit.insertPlainText("8"))
        self.cal_9.clicked.connect(lambda: self.plainTextEdit.insertPlainText("9"))
        self.cal_tochka.clicked.connect(lambda: self.plainTextEdit.insertPlainText("."))
        self.cal_left.clicked.connect(lambda: self.plainTextEdit.insertPlainText("("))
        self.cal_right.clicked.connect(lambda: self.plainTextEdit.insertPlainText(")"))
        self.cal_plus.clicked.connect(lambda: self.plainTextEdit.insertPlainText("+"))
        self.cal_minus.clicked.connect(lambda: self.plainTextEdit.insertPlainText("-"))
        self.cal_X.clicked.connect(lambda: self.plainTextEdit.insertPlainText("*"))
        self.cal_div.clicked.connect(lambda: self.plainTextEdit.insertPlainText("/"))
        self.cal_ster.clicked.connect(lambda: self.plainTextEdit.textCursor().deletePreviousChar())
        self.cal_C.clicked.connect(self.clc)
        self.cal_eq.clicked.connect(self.Equal)

    def Equal(self):
        thing = self.plainTextEdit.toPlainText()
        self.plainTextEdit.clear()
        try:
            result = str(eval(thing))
            self.plainTextEdit.insertPlainText(result)
        except Exception:
            self.plainTextEdit.clear()
            self.switch(False)
            self.plainTextEdit.insertPlainText("Неправильный ввод!")

    def switch(self, mode):
        self.cal_0.setEnabled(mode)
        self.cal_1.setEnabled(mode)
        self.cal_2.setEnabled(mode)
        self.cal_3.setEnabled(mode)
        self.cal_4.setEnabled(mode)
        self.cal_5.setEnabled(mode)
        self.cal_6.setEnabled(mode)
        self.cal_7.setEnabled(mode)
        self.cal_8.setEnabled(mode)
        self.cal_9.setEnabled(mode)
        self.cal_tochka.setEnabled(mode)
        self.cal_left.setEnabled(mode)
        self.cal_right.setEnabled(mode)
        self.cal_plus.setEnabled(mode)
        self.cal_minus.setEnabled(mode)
        self.cal_X.setEnabled(mode)
        self.cal_div.setEnabled(mode)
        self.cal_ster.setEnabled(mode)
        self.cal_eq.setEnabled(mode)
    
    def clc(self):
        self.plainTextEdit.clear()
        self.switch(True)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())