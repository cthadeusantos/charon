# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
import tkinter as tk
from gui_tkinter.gui_charon import GUI
from gui_qt5.gui_charon import *

import sys

choice = 0
# while not choice:
#     choice = int(input("1. tkinter GUI or 2. pyqt5 GUI:"))
    # if choice != 1 and choice != 2:
    #     choice = 0
    # else:
    #     if choice == 1:
    #         if __name__ == "__main__":
root = tk.Tk()
GUI(root)
root.mainloop()
        # elif choice == 2:
        #     app = QApplication(sys.argv)
        #     window = Charon().get_main_window()
        #     window.show()
        #     app.exec_()


