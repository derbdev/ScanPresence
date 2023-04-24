#This is the main app file
#all other modules' functionalities are added here

from PyQt5.QtWidgets import QWidget, QStackedWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QPushButton
from AddPage import addPage
from MainPage import mainPage
from SessionPage import sessionPage


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(200, 50, 1100, 900)
        self.app = QStackedWidget(self)
        self.setCentralWidget(self.app)

        self.main_page = mainPage()
        self.app.addWidget(self.main_page)
        self.main_page.add.clicked.connect(lambda: self.app.setCurrentIndex(1))
        self.main_page.mark.clicked.connect(lambda: self.app.setCurrentIndex(2))

        self.add_page = addPage()
        self.app.addWidget(self.add_page)
        self.add_page.cancel.clicked.connect(lambda: self.app.setCurrentIndex(0))

        self.session_page = sessionPage()
        self.app.addWidget(self.session_page)
        self.session_page.cancel.clicked.connect(lambda: self.app.setCurrentIndex(0))

    
if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    app.exec_()