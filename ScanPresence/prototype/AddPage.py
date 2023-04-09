from PyQt5.QtWidgets import QPushButton, QLineEdit, QHBoxLayout, QWidget, QLabel, QSizePolicy, QVBoxLayout, QSpacerItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Add(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        font = QFont('Inter Black', 50)
        VLayout = QVBoxLayout(self)

        self.space1 = QSpacerItem(1, 14, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.space2 = QSpacerItem(40, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.space3 = QSpacerItem(1, 100, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.space4 = QSpacerItem(1, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.space5 = QSpacerItem(14, 1, QSizePolicy.Minimum, QSizePolicy.Minimum)

        VLayout.addSpacerItem(self.space3)
        
        PTitle = QLabel('Test', self)
        PTitle.setFont(font)
        PTitle.setStyleSheet("color: #2195DB;")
        PTitle.setAlignment(Qt.AlignHCenter)
        VLayout.addWidget(PTitle)

        VLayout.addSpacerItem(self.space4)

        new_class = QLabel('Class name', self)
        VLayout.addWidget(new_class)
        new_class.setFont(QFont('Inter Bold', 12))
        new_class.setStyleSheet("color: white; margin-right: 180px;")
        new_class.setAlignment(Qt.AlignHCenter)

        self.line = QLineEdit()
        self.line.setPlaceholderText('Enter class name')
        VLayout.addWidget(self.line)
        self.line.setFixedSize(300, 55)
        VLayout.setAlignment(self.line, Qt.AlignHCenter)
        self.line.setStyleSheet("""
            QLineEdit {
                background-color: #f2f2f0;
                color: black;
                font: Inter Bold;
                font-size:20px;
                border-radius: 10px;
                padding-left: 10;
            }
        """)

        VLayout.addSpacerItem(self.space1)

        HLayout = QHBoxLayout()
        VLayout.addLayout(HLayout)

        HLayout.addSpacerItem(self.space2)

        self.cancel = QPushButton('cancel', self)
        HLayout.addWidget(self.cancel)
        self.cancel.setFixedSize(143, 46)
        self.cancel.setStyleSheet("""
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

        self.next = QPushButton('Next', self)
        HLayout.addWidget(self.next)
        self.next.setFixedSize(143, 46)
        self.next.setStyleSheet("""
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
