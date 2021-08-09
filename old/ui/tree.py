#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import tkinter as tk
    from tkinter import ttk as ttk
except ImportError:
    raise Exception("Sorry, you need Python >= 3.5!")
    # import Tkinter as tk
    # from Tkinter import ttk as ttk

from sys import platform as _platform
from sys import version_info

from circuit import Circuit
from static_functions import getvalue
from load import Load, Lighting, Socket, Motor, Specific
from project import Project
from switchboard import SwitchBoard

try:
    assert version_info >= (3, 5)
except AssertionError:
    raise Exception("Sorry, you need Python >= 3.5!")

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


class Tree(ttk.Treeview):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.elements = {}
        self.selected = None
        popup1 = [
            {'label': 'Add project', 'command': self.add_project},
            {'label': '', 'command': ''},
            {'label': 'Delete', 'command': ''}
        ]
        popup2 = [
            {'label': 'Add switchboard', 'command': self.add_switchboard},
            {'label': 'Delete', 'command': ''},
            {'label': '', 'command': ''},
            {'label': 'Copy', 'command': ''},
            {'label': 'Paste', 'command': ''},
        ]
        popup3 = [
            {'label': 'Add Circuit', 'command': self.add_circuit},
            {'label': 'Add Switchboard', 'command': self.add_switchboard},
            {'label': 'Delete', 'command': ''},
            {'label': '', 'command': ''},
            {'label': 'Copy', 'command': ''},
            {'label': 'Paste', 'command': ''},
        ]
        popup4 = [
            {'label': 'Add lighting', 'command': self.add_lighting},
            {'label': 'Add motor', 'command': self.add_motor},
            {'label': 'Add specific', 'command': self.add_specific},
            {'label': 'Add socket', 'command': self.add_socket},
            {'label': 'Delete', 'command': ''},
            {'label': '', 'command': ''},
            {'label': 'Copy', 'command': ''},
            {'label': 'Paste', 'command': ''},
        ]
        popup5 = [
            {'label': 'Delete', 'command': ''},
            {'label': '', 'command': ''},
            {'label': 'Copy', 'command': ''},
            {'label': 'Paste', 'command': ''},
        ]
        self.bind(right_click, self.callback)
        self.bind("<ButtonRelease-1>", self.select)

        self.popup1 = self.build_popup(popup1)
        self.popup2 = self.build_popup(popup2)
        self.popup3 = self.build_popup(popup3)
        self.popup4 = self.build_popup(popup4)
        self.popup5 = self.build_popup(popup5)

    # Open popup menu when right button clicked
    def callback(self, event):
        try:
            self.selected = self.selection()
            element = self.selected[0]
            type_select = getvalue(self.elements, element)
            if isinstance(type_select, Project):
                self.popup2.post(event.x_root, event.y_root)  # elements popup menu
            elif isinstance(type_select, SwitchBoard):
                self.popup3.post(event.x_root, event.y_root)  # Load popup menu
            elif isinstance(type_select, Circuit):
                self.popup4.post(event.x_root, event.y_root)  # Load popup menu
            elif isinstance(type_select, Load):
                self.popup5.post(event.x_root, event.y_root)  # elements popup menu
        except IndexError:
            self.popup1.post(event.x_root, event.y_root)

    def select(self, event):
        self.selected = self.selection()
        if len(self.selected) == 0:
            return
        else:
            self.controller.frames[WhichProperties].item_properties(self.selected)

    def add_element(self, istype=None):
        selected = self.selected
        my_object = None
        # key = None
        try:
            selected = selected[0]
        except IndexError:
            selected = None
        if istype == Project:
            my_object = Project(idt="")
        elif istype == SwitchBoard:
            my_object = SwitchBoard(idt=selected)
        elif istype == Circuit:
            my_object = Circuit(idt=selected)
        elif issubclass(istype, Lighting):
            my_object = Lighting(idt=selected)
        elif issubclass(istype, Socket):
            my_object = Socket(idt=selected)
        elif issubclass(istype, Motor):
            my_object = Motor(idt=selected)
        elif issubclass(istype, Specific):
            my_object = Specific(idt=selected)

        key = self.insert("" if selected is None else selected,
                          'end',
                          text=my_object.tag,
                          tags=(my_object.tag,)
                          )  # add new child to treeview
        self.add_to_dict_key(selected, {key: my_object})  # Add new item to self.elements

    def add_to_dict_key(self, parent, item):
        """ Build Returns key to the path to self.elements """
        if parent is None:
            self.elements.update(item)
        else:
            key = getvalue(self.elements, parent)
            k = list(item.keys())[0]
            key.elements[k] = item[k]

    def build_popup(self, listing):
        ''' Event popup menu '''
        menu = tk.Menu(self, tearoff=0)
        for item in listing:
            if item['label'] == '' and item['command'] == '':
                menu.add_separator()
            else:
                menu.add_command(label=item['label'], command=item['command'])
        return menu

    def add_project(self):
        self.add_element(Project)

    def add_switchboard(self):
        self.add_element(SwitchBoard)

    def add_circuit(self):
        self.add_element(Circuit)

    def add_lighting(self):
        self.add_element(Lighting)

    def add_motor(self):
        self.add_element(Motor)

    def add_socket(self):
        self.add_element(Socket)

    def add_specific(self):
        self.add_element(Specific)


class WhichProperties(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.pattern = None
        self.controller = controller
        self.labels = {}
        self.values = {}
        self.entry_focus_widgetname = {}

        self.label = ttk.Label(self, text='Properties')
        self.label.grid(column=1,
                        row=0,
                        stick=(tk.N, tk.W, tk.E, tk.S)
                        )

    def callback(self, event):
        if self.controller.frames[Tree].selected is not None and len(self.controller.frames[Tree].selected) > 0:
            try:
                element = getvalue(self.controller.frames[Tree].elements,
                                   self.controller.frames[Tree].selected[0]
                                   )
                focused_element = self.focus_get().__str__().split("!")[-1]
                key = list(self.entry_focus_widgetname[focused_element].keys())[0]
                old_value = type(getattr(element, key))
                new_value = event.get()

                print(re.match(r"^$[a-zA-Z0-9]{0,10}$", new_value) )    # PARA TESTE

                if isinstance(old_value, int):
                    new_value = int(new_value)
                elif isinstance(old_value, float):
                    new_value = float(new_value)
                setattr(element, key, new_value)
            except:
                pass

    def item_properties(self, selected):
        for item in self.values:
            self.labels[item].destroy()
            self.values[item].destroy()
        selected = getvalue(self.controller.frames[Tree].elements, selected[0])
        self.show_properties2(selected.attributes())

    def show_properties(self, attributes):
        if attributes is None:
            # attributes = {}
            return
        self.labels = {}
        self.values = {}
        self.entry_focus_widgetname = {}
        _index = 0
        _testString = ''

        for _index, item in enumerate(attributes):
            self.labels[item] = ttk.Label(self, text=item)
            self.labels[item].grid(column=1,
                                   row=_index,
                                   stick=(tk.N, tk.W, tk.E, tk.S)
                                   )
            _testString = tk.StringVar()
            _testString.trace("w",
                              lambda name,
                                     index,
                                     mode,
                                     _testString=_testString: self.callback(_testString)
                              )
            _testString.set(attributes[item]['value'])
            self.values[item] = tk.Entry(self,
                                         width=12,
                                         text=_testString
                                         )
            self.values[item].grid(column=2,
                                   row=_index,
                                   stick=(tk.N, tk.W, tk.E, tk.S)
                                   )
            string = self.values.__str__().split("!")[-1][:-2]
            self.entry_focus_widgetname[string] = {item: _testString}

    def show_properties2(self, attributes):
        if attributes is None:
            # attributes = {}
            return
        # self.pattern1 = re.compile("^\w{0,10}$")
        # self.pattern1 = re.compile(r'(..)/(..)/(....)')
        self.labels = {}
        self.values = {}
        self.entry_focus_widgetname = {}
        _index = 0
        _testString = ''

        for _index, item in enumerate(attributes):
            self.labels[item] = ttk.Label(self, text=item)
            self.labels[item].grid(column=1, row=_index, stick=(tk.N, tk.W, tk.E, tk.S))
            self.pattern = re.compile("^\w{0,10}$")
            _testString = tk.StringVar()
            _testString.trace("w", lambda name, index, mode, _testString=_testString: self.callback(_testString))
            _testString.set(attributes[item]['value'])
            vcmd = (self.register(self.validate_username), "%i", "%P")
            # vcmd = (self.register(self.validate_username2),  "%P")
            self.values[item] = tk.Entry(self,
                                         width=12,
                                         text=_testString,
                                         validate="key",
                                         validatecommand=vcmd,
                                         invalidcommand=self.print_error
                                         )
            self.values[item].grid(column=2, row=_index, stick=(tk.N, tk.W, tk.E, tk.S))
            string = self.values.__str__().split("!")[-1][:-2]
            self.entry_focus_widgetname[string] = {item: _testString}

    def validate_username2(self, username):
        if re.match(username, self.pattern) is None:
            return False
        return True

    def validation(self, username):
        if re.match(username, self.pattern) is None:
            return False
        return True

    def validate_username(self, index, username):
        print("Modification at index " + index)
        return self.pattern.match(username) is not None



    def print_error(self):
        print("Invalid username character")


import re
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pattern = re.compile("^\w{0,10}$")
        self.label = tk.Label(self, text="Enter your username")
        vcmd = (self.register(self.validate_username), "%i", "%P")
        self.entry = tk.Entry(self, validate="key",
                              validatecommand=vcmd,
                              invalidcommand=self.print_error)
        self.label.pack()
        self.entry.pack(anchor=tk.W, padx=10, pady=10)

    def validate_username(self, index, username):
        print("Modification at index " + index)
        return self.pattern.match(username) is not None

    def print_error(self):
        print("Invalid username character")


if __name__ == "__main__":
    app = App()
    app.mainloop()