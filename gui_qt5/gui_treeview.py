from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from project import *
from switchboard import *


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.len():
            return self.stack.pop()
        return None

    def len(self):
        return len(self.stack)

    def list(self):
        return self.stack

    def clean(self):
        self.stack = []


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)


class MyTreeView(QTreeView):
    def __init__(self):
        super().__init__()
        self.tree_view = QTreeView()
        self.stack = Stack()
        #
        self.tree = {}
        self.treeModel = None
        self.rootNone = None


    def build(self):
        # self.tree_view.columnWidth(30)
        # tree_view = QTreeView()
        self.tree_view.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        self.rootNode = treeModel.invisibleRootItem()

        # treeModel = QStandardItemModel()
        # rootNode = treeModel.invisibleRootItem()

        # # America
        # america = StandardItem('America', 16, set_bold=True)
        #
        # california = StandardItem('California', 14)
        # america.appendRow(california)
        #
        # oakland = StandardItem('Oakland', 12, color=QColor(155, 0, 0))
        # sanfrancisco = StandardItem('San Francisco', 12, color=QColor(155, 0, 0))
        # sanjose = StandardItem('San Jose', 12, color=QColor(155, 0, 0))
        #
        # california.appendRow(oakland)
        # california.appendRow(sanfrancisco)
        # california.appendRow(sanjose)
        #
        # texas = StandardItem('Texas', 14)
        # america.appendRow(texas)
        #
        # austin = StandardItem('Austin', 12, color=QColor(155, 0, 0))
        # houston = StandardItem('Houston', 12, color=QColor(155, 0, 0))
        # dallas = StandardItem('dallas', 12, color=QColor(155, 0, 0))
        #
        # texas.appendRow(austin)
        # texas.appendRow(houston)
        # texas.appendRow(dallas)
        #
        # # Canada
        # canada = StandardItem('America', 16, set_bold=True)
        #
        # alberta = StandardItem('Alberta', 14)
        # bc = StandardItem('British Columbia', 14)
        # ontario = StandardItem('Ontario', 14)
        # canada.appendRows([alberta, bc, ontario])
        #
        # rootNode.appendRow(america)
        # rootNode.appendRow(canada)

        self.tree_view.setModel(treeModel)
        self.tree_view.expandAll()
        self.tree_view.doubleClicked.connect(self.get_value)
        # self.tree_view.setModel(treeModel)
        # self.tree_view.expandAll()
        # self.tree_view.doubleClicked.connect(self.get_value)


        self.popup()
        # # popup menu
        # self.tree_view.setContextMenuPolicy(Qt.ActionsContextMenu)
        # quitAction = QAction("Quit", self)
        # quitAction.triggered.connect(qApp.quit)
        # self.tree_view.addAction(quitAction)
        # # popup menu FIM
        # self.setCentralWidget(self.tree_view)
        # self.setCentralWidget(tree_view)

        return self.tree_view

    def get_value(self, val):
        print(val.data())
        print(val.row())
        print(val.column())

    def acao1(self):
        print("SELF.ACAO1")
        index = self.tree_view.currentIndex()
        self.stack.push(index.data())
        objeto = index.parent()
        while objeto.data() is not None:
            self.stack.push(objeto.data())
            objeto = objeto.parent()
        self.get_value(index)
        print(self.stack.list())
        return

    def add(self):
        pass

    def add_project(self):
        b = self.tree_view.currentIndex()
        a = Project()
        america = StandardItem(a.tag, 16, set_bold=True)
        self.rootNode.appendRow(america)
        self.tree[a.tag] = a

    def add_switchboard(self):
        b = self.tree_view.currentIndex()
        a = SwitchBoard()
        america = StandardItem(a.tag, 14)
        print(self.rootNode)
        print(b.row().numerator, b.data(), b.column(), b.parent())

    def popup(self):
        # popup menu
        self.tree_view.setContextMenuPolicy(Qt.ActionsContextMenu)
        action1 = QAction("Add project", self)
        action2 = QAction("Add switchboard", self)
        # action2 = QAction("Add switchboard", self)
        # action3 = QAction("Add circuit", self)
        # action4 = QAction("Add load", self)
        quitAction = QAction("Quit", self)
        action1.triggered.connect(self.add_project)
        action2.triggered.connect(self.add_switchboard)
        # action2.triggered.connect(self.acao1)
        # action3.triggered.connect(self.acao1)
        # action4.triggered.connect(self.acao1)
        quitAction.triggered.connect(qApp.quit)
        self.tree_view.addAction(action1)
        self.tree_view.addAction(action2)
        # self.tree_view.addAction(action2)
        # self.tree_view.addAction(action3)
        # self.tree_view.addAction(action4)
        self.tree_view.addAction(quitAction)
        # popup menu FIM