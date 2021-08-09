from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


class MyProperties(QTableView):
    def __init__(self):
        super().__init__()
        self.table_view = QTableView()

    def build(self):
        data = [
            [4, 9, 2],
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, 8, 9],
        ]
        self.table_view.model = TableModel(data)
        self.table_view.setModel(self.table_view.model)
        # tableView = model

        self.popup()
        # # popup menu
        # self.table_view.setContextMenuPolicy(Qt.ActionsContextMenu)
        # action1 = QAction("First Action", self)
        # quitAction = QAction("Quit", self)
        # action1.triggered.connect(self.acao1)
        # quitAction.triggered.connect(qApp.quit)
        # self.table_view.addAction(action1)
        # self.table_view.addAction(quitAction)
        # # popup menu FIM

        return self.table_view

    def acao1(self):
        return

    def popup(self):
        # popup menu
        self.table_view.setContextMenuPolicy(Qt.ActionsContextMenu)
        action1 = QAction("First Action", self)
        quitAction = QAction("Quit", self)
        action1.triggered.connect(self.acao1)
        quitAction.triggered.connect(qApp.quit)
        self.table_view.addAction(action1)
        self.table_view.addAction(quitAction)
        # popup menu FIM
