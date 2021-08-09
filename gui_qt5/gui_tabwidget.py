from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.tabs = QTabWidget()

    def build(self):
        # Initialize tab screen
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        # tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(tab1, "Geeks")
        self.tabs.addTab(tab2, "For")
        self.tabs.addTab(tab3, "Geeks")

        # Create first tab
        # tab1.layout = QVBoxLayout(self)
        tab1.layout = QVBoxLayout()
        l = QLabel()
        l.setText("This is the first tab")
        tab1.layout.addWidget(l)
        tab1.setLayout(tab1.layout)
        # popup menu
        self.tabs.setContextMenuPolicy(Qt.ActionsContextMenu)
        quitAction = QAction("Quit", self)
        quitAction.triggered.connect(qApp.quit)
        self.tabs.addAction(quitAction)
        # popup menu FIM
        return self.tabs