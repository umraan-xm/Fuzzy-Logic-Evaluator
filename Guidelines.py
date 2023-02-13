from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class GuidelinesDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Guidelines")
        self.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Hey! Thanks for downloading Fuzzy Evaluator. Please follow the guidelines"
                                     " for the most comfortable experience. \n\n\n"))
        self.layout.addWidget(QLabel("-- Please input data sequentially without leaving a row empty. \n"))
        self.layout.addWidget(QLabel("-- All columns for a given row need to be filled to compute the result. \n"))
        self.layout.addWidget(QLabel("-- Adjust the last roll number first and them move on to the first roll number. \n"))
        self.layout.addWidget(QLabel("-- Unsaved changes are not stored in memory. Please do not switch away from"
                                     " a file if there are unsaved changes. \n"))
        self.layout.addWidget(QLabel("-- Input range for marks is 0 - 100. \n"))
        self.layout.addWidget(QLabel("-- Output range for results is 0 - 100. \n"))
        self.lblLink = QLabel()
        self.lblLink.setText("If you want to know more about Fuzzy Logic, click <a href=\"https://en.wikipedia.org/wiki/Fuzzy_logic\">here</a>.")
        self.lblLink.setTextFormat(Qt.RichText)
        self.lblLink.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.lblLink.setOpenExternalLinks(True)
        self.layout.addWidget(self.lblLink)
        self.setLayout(self.layout)
