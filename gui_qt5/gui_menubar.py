from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import  QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

class MenuBar(QMenuBar):
    sig_new_file = pyqtSignal()
    sig_open_file = pyqtSignal()
    sig_save_file = pyqtSignal()
    sig_page_setup = pyqtSignal()
    sig_print = pyqtSignal()
    sig_exit = pyqtSignal()
    sig_status_bar = pyqtSignal(bool)


def __init__(self):
    super().__init__()
    self.init_menu_file()

    # self.init_menu_edit()
    # self.init_menu_format()
    # self.init_menu_view()
    # self.init_menu_help()
    # self.set_all_text()


def init_menu_file(self):
    self.act_new_file = QAction('File', self)
    self.act_new_file.setShortcut(QKeySequence('Ctrl+N'))
    self.act_new_file.triggered.connect(lambda: self.sig_new_file.emit())

    self.act_open_file = QAction('Open', self)
    self.act_open_file.setShortcut(QKeySequence('Ctrl+O'))
    self.act_new_file.triggered.connect(lambda: self.sig_open_file.emit())

    self.act_save_file = QAction('Save', self)
    self.act_save_file.setShortcut(QKeySequence('Ctrl+S'))
    self.act_save_file.triggered.connect(lambda: self.sig_save_file.emit())

    self.act_print = QAction('Print', self)
    self.act_print.setShortcut(QKeySequence('Ctrl+P'))
    self.act_print.triggered.connect(lambda: self.sig_print.emit())

    self.act_quit = QAction('Quit', self)
    self.act_quit.setShortcut(QKeySequence('Ctrl+Q'))
    self.act_quit.triggered.connect(lambda: self.sig_exit.emit())

    self.menu_file = self.addMenu('&File')
    self.menu_file.addAction(self.act_new_file)
    self.menu_file.addAction(self.act_open_file)
    self.menu_file.addAction(self.act_save_file)
    self.menu_file.addSeparator()
    self.menu_file.addAction(self.act_print)
    self.menu_file.addSeparator()
    self.menu_file.addAction(self.act_quit)
