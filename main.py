from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/ui_caisse.ui',self)


#main
app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
try:
    sys.exit(app.exec_())
except:
    print("Exit")