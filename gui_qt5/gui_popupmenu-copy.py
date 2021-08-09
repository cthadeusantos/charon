from PyQt5 import QtGui


class MyPopupMenu:
    def __init__(self):
        ##Enable Right
        self._category_table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self._category_table.customContextMenuRequested.connect(self.show_category_table_Popup)

        ##Create Popup Menu
        self._category_table_Popup = QtGui.QMenu(self)
        self._category_table_Popup.addAction('Activate', lambda: self.changeStatus('table', 'Active'))
        self._category_table_Popup.addAction('Ommit', lambda: self.changeStatus('table', 'Omitted'))
        self._category_table_Popup.addAction('Delete', lambda: self.changeStatus('table', 'Delete'))

    def show_category_table_Popup(self, point):
            '''
            Show Popup Menu on Category Table
            '''
            self._category_table_Popup.exec_(self._category_table.mapToGlobal(point))

    def changeStatus(self, mode, status=None):
            '''
            Delete selected Files
            '''
            if mode == 'table':
                ## Grab selected row
                selectedRow = self._category_table.selectionModel().selectedRows()[0].row()

                ## Edit First Column
                item = self._category_table.item(selectedRow, 0)
                Util.changeTextTable(item, status)

                ## Edit Second Column
                item = self._category_table.cellWidget(selectedRow, 1)

                if status != 'Active':
                    item.setEnabled(False)
                else:
                    item.setEnabled(True)

            if mode == 'tree':
                item = self._asset_tree.currentItem()

                Util.changeTextTree(item, status)