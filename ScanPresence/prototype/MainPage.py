from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QApplication, QWidget, QLabel, QSizePolicy, QVBoxLayout, QSpacerItem, QComboBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        font = QFont('Inter Black', 50)
        VLayout = QVBoxLayout(self)
        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor("#2195DB"))

        self.space1 = QSpacerItem(1, 14, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.space2 = QSpacerItem(40, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.space3 = QSpacerItem(1, 100, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.space4 = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.space5 = QSpacerItem(14, 1, QSizePolicy.Minimum, QSizePolicy.Minimum)

        VLayout.addSpacerItem(self.space3)
        
        PTitle = QLabel('Test', self)
        PTitle.setFont(font)
        PTitle.setAlignment(Qt.AlignHCenter)
        VLayout.addWidget(PTitle)

        VLayout.addSpacerItem(self.space4)
        VLayout.addSpacerItem(self.space3)
        VLayout.addSpacerItem(self.space4)


        HHLayout = QHBoxLayout()
        VLayout.addLayout(HHLayout)

        HHLayout.addSpacerItem(self.space2)

        self.box = QComboBox()
        HHLayout.addWidget(self.box)
        self.box.addItem('------------Select class-----------')
        self.box.setFixedSize(300, 55)
        VLayout.setAlignment(self.box, Qt.AlignHCenter)
        self.box.setStyleSheet("""
            QComboBox {
                background-color: #f2f2f0;
                color: #25252c;
                font: Inter Bold;
                font-size:20px;
                border-radius: 10px;
                padding-left: 10px;
            }
        """)

        self.delete = QPushButton('', self)     
        self.delete.setFixedSize(55, 55)
        self.delete.setStyleSheet("""
            QPushButton {
                background-color: #25252C;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #323239;
            }

            QPushButton:pressed {
                background-color: #25252C;
            }
        """)
        delete_icon = QIcon('icons/delete.png')
        self.delete.setIcon(delete_icon)
        self.delete.setIconSize(delete_icon.actualSize(QSize(35, 35)))
        HHLayout.addWidget(self.delete)

        HHLayout.addSpacerItem(self.space2)

        VLayout.addSpacerItem(self.space1)

        HLayout = QHBoxLayout()
        VLayout.addLayout(HLayout)

        HLayout.addSpacerItem(self.space2)

        self.add = QPushButton('Add +', self)
        HLayout.addWidget(self.add)
        self.add.setFixedSize(150, 46)
        self.add.setStyleSheet("""
            QPushButton {
                background-color: #25252C;
                color: white;
                font-weight: bold;
                font-size: 20px;
                border-radius: 10px;
                border: 2px solid #727276;
            }

            QPushButton:hover {
                border: 2px solid #f2f2f0;
            }

            QPushButton:pressed {
                border: 4px solid #727276;
            }
        """)

        HLayout.addSpacerItem(self.space5)

        next = QPushButton('Next', self)
        HLayout.addWidget(next)
        next.setFixedSize(150, 46)
        next.setStyleSheet("""
            QPushButton {
                background-color: #2195db;
                color: #25252C;
                font-size: 20px;
                font-weight: bold;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #3CA1DE;
            }

            QPushButton:pressed {
                background-color: #2195db;
            }
        """)

        HLayout.addSpacerItem(self.space2)        

        VLayout.addSpacerItem(self.space4)
        VLayout.addSpacerItem(self.space3)

        self.setPalette(palette)
    


if __name__ == "__main__":
    app = QApplication([])
    window = MainPage()
    window.show()
    app.exec_()
        