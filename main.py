import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Diletant')
        self.setWindowIcon(QIcon('Assets\icon.png'))

        self.ui.input_link.setPlaceholderText('Ссылка на конференцию')
        self.ui.input_name.setPlaceholderText('Введите имя')

app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())