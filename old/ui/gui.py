# -*- coding: utf-8 -*-
try:
    import tkinter as tk
    from tkinter import ttk as ttk
except ImportError:
    import Tkinter as tk
    from Tkinter import ttk as ttk

from old.ui.tree import *


class Middle(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text='Middle name:')
        label.grid(column=1, row=0, stick=(tk.N, tk.W, tk.E, tk.S))


class MenuBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        # Create Menu Bar
        menuBar = tk.Menu(parent)
        parent.config(menu=menuBar)
        # File Menu
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command='')
        menuBar.add_cascade(label="File", menu=fileMenu)
        # Help Menu
        helpMenu = tk.Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About")
        menuBar.add_cascade(label="Help", menu=helpMenu)



class GUI:
    def __init__(self, toplevel):
        super().__init__()
        # Screen settings
        screen_width = toplevel.winfo_screenwidth()
        screen_height = toplevel.winfo_screenheight()
        # toplevel.geometry(str(screen_width-120)+"x"+str(screen_height-100))
        toplevel.geometry("640x480")
        toplevel.title("Proteus")

        # Main container
        container = ttk.Frame(toplevel, padding="3 3 12 12")
        container.grid(column=1, row=1, stick=(tk.N, tk.W, tk.E, tk.S))
        self.frames = {}

        menubar = MenuBar(toplevel)

        # Build three columns (frame1=Tree, Frame2=Middle, Frame3=WhichProperties)
        for column, F in enumerate([Tree, Middle, WhichProperties]):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(column=column, row=0, stick=(tk.N, tk.W, tk.E, tk.S))


