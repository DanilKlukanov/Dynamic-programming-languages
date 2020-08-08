import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import html
 
class MyWidget(QMainWindow, html.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.runex)
    def runex(self):
        textex="<body><p><b>Пороша</b></p></body>"
        self.plainTextEdit.insertPlainText(textex)
    
    def run(self):
        Htext = self.plainTextEdit 
        tx = Htext.toPlainText()
        self.textBrowser.setText(tx)

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())