# -*- coding: utf-8 -*-
try:
    import tkinter as tk
    from tkinter import ttk as ttk
except ImportError:
    import Tkinter as tk
    from Tkinter import ttk as ttk

from sys import platform as _platform

# Define settings from specific OS
if _platform == "linux" or _platform == "linux2":
    # linux
    right_click = "<Button-3>"
elif _platform == "darwin":
    # MAC OS X
    right_click = "<Button-2>"
elif _platform == "win32":
    # Windows
    right_click = "<Button-3>"
elif _platform == "win64":
    # Windows 64-bit
    right_click = "<Button-3>"
