#in this page, the user adds a new session to the selected class

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QVBoxLayout, 
    QHBoxLayout, QSpacerItem, QSizePolicy, QPushButton)
from PyQt5.QtCore import Qt


class sessionPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        label = QLabel("Session name", self)
        main_layout.addWidget(label)

        self.line = QLineEdit(self)
        self.line.setPlaceholderText("Enter session name")
        main_layout.addWidget(self.line)

        self.generate = QPushButton("Generate QRcode", self)
        main_layout.addWidget(self.generate)

        self.cancel = QPushButton("Cancel", self)
        main_layout.addWidget(self.cancel)