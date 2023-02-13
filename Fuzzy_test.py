from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Fuzzy

class TableResultModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self._result = []
        for i in range(5):
            self._result.append("")

    def rowCount(self, parent):
        return len(self._result)

    def columnCount(self, parent):
        return 1

    def data(self, index, role):
        if not index.isValid():
            return None

        value = self._result[index.row()]

        if role == Qt.DisplayRole:
            return value


    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._result[index.row()] = value
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def addRow(self):
        self._result.append("")

    def getValues(self):
        return self._result

    def setValues(self, values):
        self._result = values


class TableMarksModel(QAbstractTableModel):
    def __init__(self, columns):
        super().__init__()
        self._columns = columns
        self._data = []
        for i in range(5):
            self._data.append([""] * self._columns)

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._data[0])

    def data(self, index, role):
        if not index.isValid():
            return None

        value = self._data[index.row()][index.column()]

        if role == Qt.DisplayRole:
            return value

    def setData(self, index, value, role):
        if role == Qt.EditRole or role == Qt.DisplayRole:
            self._data[index.row()][index.column()] = value
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def addRow(self):
        self._data.append(["", "", ""])

    def getValues(self):
        return self._data




class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Fuzzy test")
        self.resize(1280, 720)


        self.tableMarks = QTableView()
        self.tableMarksModel = TableMarksModel(3)

        self.tableMarks.setModel(self.tableMarksModel)

        self.tableResult = QTableView()
        self.tableResultModel = TableResultModel()

        self.tableResult.setModel(self.tableResultModel)

        self.btnCompute = QPushButton("Compute")


        self.h_layout = QHBoxLayout(self)
        self.h_layout.addWidget(self.tableMarks)
        self.h_layout.addWidget(self.tableResult)
        self.h_layout.addWidget(self.btnCompute)

        self.setLayout(self.h_layout)


        self.btnCompute.clicked.connect(self.compute)

    def compute(self):
        data = self.tableMarksModel.getValues()
        result = []
        e1 = [int(row[0]) for row in data]
        e2 = [int(row[1]) for row in data]
        p = [int(row[2]) for row in data]
        # print(e1)
        # print(e2)
        # print(p)
        result = Fuzzy.compute_fuzzy_performance(e1, e2, p)
        result = [str(x) for x in result]
        print(result)
        # for i in range(len(data)):
        #     rowSum = sum([int(x) for x in data[i]])
        #     result.append(rowSum)

        self.tableResultModel.setValues(result)
        self.tableResult.setModel(None)
        self.tableResult.setModel(self.tableResultModel)




def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()