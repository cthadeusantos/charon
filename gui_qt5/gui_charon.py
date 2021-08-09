from .gui_treeview import *
from .gui_properties import *
from .gui_tabwidget import *
from .gui_menubar import *

import sys


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        width = 1100
        height = 600
        self.setWindowTitle('Charon')
        # setting  the fixed width of window
        self.setFixedWidth(width)
        # setting  the fixed height of window
        self.setFixedHeight(height)
        self.frames = {}

        # left = MyTreeView()
        # middle = MyTabWidget()
        # right = MyProperties()
        elements = [MyTreeView,
                    MyTabWidget,
                    MyProperties
                    ]
        position = [(1, 1, 2, 1),
                    (1, 2, 2, 1),
                    (1, 3, 1, 1)
                    ]

        layout = QGridLayout()
        # # Build three columns (frame1=Tree, Frame2=Middle, Frame3=WhichProperties)
        # menu_main = MenuBar()
        # layout.addWidget(menu_main, 0, 0)
        # self.setMenuBar(menu_main)
        # self.createMenu()
        # layout.addWidget(x, 0, 0)


        for column, F in enumerate(elements):
            frame = F()
            self.frames[F] = frame
            a, b, c, d = position[column]
            layout.addWidget(self.frames[F].build(), a, b, c, d)
        # Add widgets to the layout
        # layout.addWidget(left.build(), 1, 1, 2, 1)
        # layout.addWidget(middle.build(), 1, 2, 2, 1)
        # layout.addWidget(right.build(), 1, 3, 1, 1) ERA (...., 1,3)
        self.setLayout(layout)

class Charon:

    def __init__(self):
        self.main_window = MainWindow()

    def get_main_window(self):
        return self.main_window
