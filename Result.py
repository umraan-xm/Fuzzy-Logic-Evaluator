from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class TableResultModel(QAbstractTableModel):
    def __init__(self, columns=1, rows=100, rollStart=1):
        super().__init__()
        self.columns = columns
        self.rows = rows
        self.tableData = list()
        self.header = ["Result"]
        self.rollStart = rollStart
        self.rollEnd = rollStart + rows

        for i in range(self.rows):
            self.tableData.append("")

    def rowCount(self, parent):
        return self.rows

    def columnCount(self, parent):
        return self.columns

    def data(self, index, role):

        if not index.isValid():
            return None

        value = self.tableData[index.row()]

        if role == Qt.DisplayRole:
            return value

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[section]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return [str(i) for i in range(self.rollStart, self.rollEnd)][section]

        return None

    def setData(self, index, value, role):

        if role == Qt.EditRole or role == Qt.DisplayRole:
            self.tableData[index.row()][index.column()] = value
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def setAllRecords(self, data):
        for i in range(len(data)):
            self.tableData[i] = data[i]

    def getAllRecords(self):
        data = self.tableData.copy()
        result = [x for x in data if x != '']
        return result

    def updateRoll(self, start, end):
        self.rollStart = start
        self.rollEnd = end
        self.rows = end - start

        for i in range(self.rows):
            self.tableData.append("")

    def clear(self):
        self.tableData.clear()
        for i in range(self.rows):
            self.tableData.append("")
