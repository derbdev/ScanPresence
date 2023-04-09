from PyQt5.QtWidgets import QStackedWidget, QMainWindow, QApplication
from PyQt5.QtGui import QPalette, QColor
import MainPage, AddPage, yaml


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.LoadSave()

    def initUi(self):
        self.setGeometry(600, 250, 600, 700)
        self.app = QStackedWidget(self)
        self.setCentralWidget(self.app)

        self.main_page = MainPage.MainPage()
        self.app.addWidget(self.main_page)
        self.main_page.add.clicked.connect(lambda: self.SetIndex(1))
        self.main_page.delete.clicked.connect(self.DeleteItem)

        self.add_page = AddPage.Add()
        self.app.addWidget(self.add_page)
        self.add_page.next.clicked.connect(self.AddToBox)
        self.add_page.next.clicked.connect(lambda: self.SetIndex(0))
        self.add_page.cancel.clicked.connect(self.AddCancel)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#25252C"))
        self.setPalette(palette)

    
    def SetIndex(self, i):
        self.app.setCurrentIndex(i)

    def AddToBox(self):
        self.text = self.add_page.line.text()
        if (len(self.text) > 0):
            self.main_page.box.addItem(self.text)
            self.AddBoxSave()
            self.add_page.line.clear()

    def AddCancel(self):
        self.SetIndex(0)
        self.add_page.line.clear()

    def LoadSave(self):
        self.items_list = []
        with open('save.yaml', 'r') as file:
            self.items_dict = yaml.load(file, Loader=yaml.FullLoader)
            try:
                self.items_list = self.items_dict['QComboBoxItems']
                for item in self.items_list:
                    self.main_page.box.addItem(item)
            except:
                pass

    def AddBoxSave(self):
        self.items_list.append(self.text)
        self.items_dict = {'QComboBoxItems': self.items_list}
        with open('save.yaml', 'w') as file:
            yaml.dump(self.items_dict, file)

    def DeleteItem(self):
        self.box_text = self.main_page.box.currentText()
        if self.box_text != '------------Select class-----------':
            self.DeleteBoxItem()
            self.DeleteSave()

    def DeleteBoxItem(self):
        index = self.main_page.box.findText(self.box_text)
        self.main_page.box.removeItem(index)

    def DeleteSave(self):
        self.items_list.remove(self.box_text)
        self.items_dict = {'QComboBoxItems': self.items_list}
        with open('save.yaml', 'w') as file:
            yaml.dump(self.items_dict, file)
            

if __name__ == "__main__":
    app = QApplication([])
    window = Application()
    window.show()
    app.exec_()
        
