#in this page the user adds a new class

from PyQt5.QtWidgets import (QWidget, QLineEdit, QLabel, QVBoxLayout,
    QHBoxLayout, QSpacerItem, QSizePolicy, QPushButton)
from PyQt5.QtCore import Qt


class addPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        label = QLabel("Class name", self)
        main_layout.addWidget(label)

        self.line = QLineEdit(self)
        self.line.setPlaceholderText("Enter class name")
        main_layout.addWidget(self.line)

        self.add = QPushButton("Add class", self)
        main_layout.addWidget(self.add)

        self.cancel = QPushButton("Cancel", self)
        main_layout.addWidget(self.cancel)
