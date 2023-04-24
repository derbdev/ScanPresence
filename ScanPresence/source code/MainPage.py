#this is the first page that appears to the user

from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QVBoxLayout, 
    QHBoxLayout, QSpacerItem, QSizePolicy, QPushButton)
from PyQt5.QtCore import Qt


class mainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        page_layout = QVBoxLayout(self)
        page_layout.setAlignment(Qt.AlignVCenter)

        label = QLabel("Select class", self)
        page_layout.addWidget(label)

        self.select = QComboBox(self)
        self.select.addItem("")
        page_layout.addWidget(self.select)

        self.delete = QPushButton("delete class",self)
        page_layout.addWidget(self.delete)

        self.mark = QPushButton("Mark presence", self)
        page_layout.addWidget(self.mark)

        self.add = QPushButton("Add new class", self)
        page_layout.addWidget(self.add)

        self.view = QPushButton("view sessions lists", self)
        page_layout.addWidget(self.view)