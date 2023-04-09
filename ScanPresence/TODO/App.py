#This is the main app file
#all other modules' functionalities are added here

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QPushButton
from AddPage import addPage
from MainPage import mainPage
from SessionPage import sessionPage


class addPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        #TODO
        pass

    
if __name__ == "__main__":
    #TODO
    pass