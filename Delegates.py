from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class IntegerItemDelegate(QStyledItemDelegate):
    def __init__(self, parent):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        try:
            editor = QLineEdit(parent)
            editor.setValidator(QIntValidator())
            return editor
        except Exception as e:
            print(e)

    def setEditorData(self, editor, index):
        try:
            value = str(index.model().data(index, Qt.DisplayRole))
            editor.setText(value)
        except Exception as e:
            print(e)


class StringItemDelegate(QStyledItemDelegate):
    def __init__(self, parent):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        try:
            editor = QLineEdit(parent)
            editor.setValidator(QRegExpValidator(QRegExp("[A-Za-z\s]*")))
            return editor
        except Exception as e:
            print(e)

    def setEditorData(self, editor, index):
        try:
            value = str(index.model().data(index, Qt.DisplayRole))
            editor.setText(value)
        except Exception as e:
            print(e)