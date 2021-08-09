from PyQt5.QtWidgets import *


class TreeView(QTreeView):
    def init(self):
        self.treeView = QTreeView(self)
        self.treeView.setModel(self.proxy_model)
        self.treeView.setRootIndex(self.indexRoot)
        self.treeView.setAnimated(True)
        self.treeView.setIndentation(20)
        self.treeView.setSortingEnabled(True)
        self.treeView.setDragEnabled(False)
        self.treeView.setAcceptDrops(False)
        self.treeView.setDropIndicatorShown(True)
        self.treeView.setEditTriggers(QTreeView.NoEditTriggers)
        for i in range(1, self.treeView.model().columnCount()):
            self.treeView.header().hideSection(i)