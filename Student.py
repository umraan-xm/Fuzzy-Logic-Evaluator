from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class TableStudentModel(QAbstractTableModel):
    def __init__(self, columns=4, rows=100, rollStart=1):
        super().__init__()
        self.columns = columns
        self.rows = rows
        self.tableData = list()
        self.header = ["Name", "Exam1", "Exam2", "Practicals"]
        self.rollStart = rollStart
        self.rollEnd = rollStart + rows

        for i in range(self.rows):
            self.tableData.append([""] * self.columns)

    def rowCount(self, parent):
        return self.rows

    def columnCount(self, parent):
        return self.columns

    def data(self, index, role):

        if not index.isValid():
            return None

        value = self.tableData[index.row()][index.column()]

        if role == Qt.DisplayRole:
            return value

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[section]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return [str(i) for i in range(self.rollStart, self.rollEnd+1)][section]

        return None

    def setData(self, index, value, role):

        if role == Qt.EditRole or role == Qt.DisplayRole:
            self.tableData[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def getAllRecords(self):
        data = self.tableData.copy()
        for row in data[:]:
            if row[0] == '':
                data.remove(row)
        return data

    def setAllRecords(self, data):
        for i in range(len(data)):
            self.tableData[i] = data[i]

    def updateRoll(self, start, end):
        self.rollStart = start
        self.rollEnd = end
        self.rows = end - start

        for i in range(self.rows):
            self.tableData.append([""] * self.columns)

    def clear(self):

        self.tableData.clear()
        for i in range(self.rows):
            self.tableData.append([""] * self.columns)

    def sort(self, Ncol, order):
        try:
            data = self.getAllRecords()
            if Ncol > 0:
                data = sorted(data, key=lambda x: (x[Ncol], float(x[Ncol])))
            else:
                data = sorted(data, key=lambda x: (x[0]))
            if order == Qt.DescendingOrder:
                data.reverse()
            while len(data) < len(self.tableData):
                data.append(['', '', '', ''])
            self.tableData = data
            self.layoutChanged.emit()
        except Exception as e:
            print(e)
