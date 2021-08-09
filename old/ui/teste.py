import sys
from PyQt5 import QtGui, QtCore, QtWidgets


class demowind(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('Demo window')
        quit = QtWidgets.QPushButton('Close', self)
        quit.setGeometry(10,10,70,40)
        self.connect(quit, QtCore.PYQT_SIGNAL('clicked()'), QtGui.qApp, QtCore.PYQT_SLOT('quit()'))

