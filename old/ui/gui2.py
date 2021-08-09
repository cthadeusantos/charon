import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTableView, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QMenu, QMenuBar)
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class GUI(QWidget):
    def __init__(self):
        super(GUI, self).__init__()
        self.initializeUI()

    def menu(self):
        self.menubar = QMenuBar(self)
        viewMenu = self.menubar.addMenu('View')
        settingsMenu = self.menubar.addMenu('Configuration')

    def initializeUI(self):
        """ Initialize the window and display its contents to the screen. """
        self.setGeometry(100, 100, 450, 300)
        self.setWindowTitle('TreeWidget2 Example')
        self.menu()
        self.setupModelView()
        self.show()

    def setupModelView(self):
        """ Set up standard item model and table view. """
        tw = TreeWidget()
        tw.add_header(['name', 'Cost ($)'])
        item = tw.add_item(['Carrots'])
        layout = QVBoxLayout(self)
        layout.addWidget(tw)


class TreeWidget(QTreeWidget):
    def __init__(self):
        super(QTreeWidget, self).__init__()

    def add_header(self, header):
        self.setHeaderLabels(header)

    def add_item(self, label):
        return QTreeWidgetItem(self, label)

    def mousePressEvent(self,QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print('left') #FOR DEBUGGING
            # row = self.currentRow()
            # column = self.currentColumn()
            # new_text = round(float(self.item(row,column).text()) + 1,2)
            # self.item(row,column).setText(str(new_text))

        elif QMouseEvent.button() == Qt.RightButton:
            print('right') #FOR DEBUGGING
            self.contextMenuEvent
            # row = self.currentRow()
            # column = self.currentColumn()
            # new_text = round(float(self.item(row,column).text()) - 1,2)
            # self.item(row,column).setText(str(new_text))

    # def mouse_release_event(self, event):
    #     if event.button() == Qt.RightButton:
    #         super(TreeWidget, self).mouse_release_event(event)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        quitAction = menu.addAction("Quit")
        action = menu.exec_(self.mapToGlobal(event.pos()))