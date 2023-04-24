import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QStackedLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create the widgets that will be stacked
        self.widget1 = QPushButton('Page 1')
        self.widget2 = QLabel('Page 2')

        # Create the stacked layout and add the widgets to it
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.widget1)
        self.stacked_layout.addWidget(self.widget2)

        # Create a vertical layout for the main window and add the stacked layout to it
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.stacked_layout)

        # Set the layout for the main window
        self.setLayout(self.layout)

        # Connect the button to switch to the second page
        self.widget1.clicked.connect(self.switch_to_page2)

    def switch_to_page2(self):
        # Switch to the second page
        self.stacked_layout.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())