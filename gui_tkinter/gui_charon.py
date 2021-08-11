from settings import *
from static_functions import *

from load import Load, Lighting, Socket, Motor, Specific
from circuit import Circuit
from switchboard import SwitchBoard
from project import Project
from sys import platform as _platform

import json


class Middle(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.values = []
        label = ttk.Label(self, text='Middle name:')
        label.grid(columnspan=4, row=0, stick=(tk.N, tk.W, tk.E, tk.S))

        # take the data
        lst = [(1, 'Raj', 'Mumbai', 19, 2, 4, 5, 6, 7, 8, 9, 19, 2, 4, 5, 6, 7, 8, 9),
               (2, 'Aaryan', 'Pune', 18, 2, 4, 5, 6, 7, 8, 9, 19, 2, 4, 5, 6, 7, 8, 9),
               (3, 'Vaishnavi', 'Mumbai', 20, 2, 4, 5, 6, 7, 8, 9, 19, 2, 4, 5, 6, 7, 8, 9),
               (4, 'Rachna', 'Mumbai', 21, 2, 4, 5, 6, 7, 8, 9, 19, 2, 4, 5, 6, 7, 8, 9),
               (5, 'Shubham', 'Delhi', 21, 2, 4, 5, 6, 7, 8, 9, 19, 2, 4, 5, 6, 7, 8, 9),
               (6, 'Shubham', 'Delhi', 21, 2, 4, 5, 6, 7, 8, 9, 19, 2, 4, 5, 6, 7, 8, 9),
               (7, 'Shubham', 'Delhi', 21, 2, 4, 5, 6, 7, 8, 9, 19, 2, 4, 5, 6, 7, 8, 9),
               (8, 'Shubham', 'Delhi', 21, 2, 4, 5, 6, 7, 8, 9, 19, 2, 4, 5, 6, 7, 8, 9),
               (9, 'Shubham', 'Delhi', 21, 2, 4, 5, 6, 7, 8, 9, 19, 2, 4, 5, 6, 7, 8, 9),
               ]
        # code for creating table
        for i in range(9):
            for j in range(len(lst[i])):
                label = tk.Entry(self,
                                 width=3,
                                 fg="blue",
                                 font=('Arial', 10))
                label.grid(column=j,
                           row=1+i,
                           stick=(tk.N, tk.W, tk.E, tk.S),
                           ipadx=0)
                label.insert(tk.END, lst[i][j])


        #
        # # code for creating table
        # for i in range(3):
        #     for j in range(3):
        #         testString = tk.StringVar()
        #         testString.trace("w", lambda name, index, mode, testString=testString: self.callback(testString))
        #         testString.set("1")
        #         self.controller.frames[self].values = tk.Entry(self, width=8, text=testString)
        #         self.controller.frames[self].grid(row=i, column=j)
        #         self.controller.frames[self].insert(tk.END, lst[i][j])


class Table(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text='Middle name:')
        label.grid(column=1, row=0, stick=(tk.N, tk.W, tk.E, tk.S))


class WhichProperties(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.labels = {}
        self.values = {}
        self.box_property = {}
        self.label = ttk.Label(self, text='Properties')
        self.label.grid(column=1, row=0, stick=(tk.N, tk.W, tk.E, tk.S))

    def callback(self, event):
        if self.controller.frames[Tree].selected is not None:
            element = getvalue(self.controller.frames[Tree].elements, self.controller.frames[Tree].selected[0])
            g = self.focus_get().__str__().split("!")[-1]
            try:
                key = list(self.box_property[g].keys())[0]
                old_value = type(getattr(element, key))
                new_value = event.get()
                # if isinstance(old_value, int):
                if old_value == int:
                    new_value = int(new_value)
                # elif isinstance(old_value, float):
                elif old_value == float:
                    new_value = float(new_value)
                setattr(element, key, new_value)
            except:
                pass

    def screen(self, attributes=None):
        if attributes is None:
            attributes = json.dumps({})
        self.labels = {}
        self.values = {}
        self.box_property = {}
        attributes = json.loads(attributes)

        # for index, item in enumerate(attributes):
        #     index += 1
        #     self.labels[item] = ttk.Label(self, text=item)
        #     self.labels[item].grid(column=0, row=index, stick=(tk.N, tk.W, tk.E, tk.S))
        #     testString = tk.StringVar()
        #     testString.trace("w", lambda name, index, mode, testString=testString: self.callback(testString))
        #     testString.set(attributes[item]['value'])
        #     self.values[item] = tk.Entry(self, width=8, text=testString)
        #     self.values[item].grid(column=1, row=index, stick=(tk.N, tk.W, tk.E, tk.S))
        #     string = self.values.__str__().split("!")[-1][:-2]
        #     self.box_property[string] = {item: testString}
        index = 0
        for key in attributes:
            index += 1
            self.labels[key] = ttk.Label(self, text=key)
            self.labels[key].grid(column=0, row=index, stick=(tk.N, tk.W, tk.E, tk.S))
            testString = tk.StringVar()
            testString.trace("w", lambda name, index, mode, testString=testString: self.callback(testString))
            testString.set(attributes[key])
            self.values[key] = tk.Entry(self, width=8, text=testString)
            self.values[key].grid(column=1, row=index, stick=(tk.N, tk.W, tk.E, tk.S))
            string = self.values.__str__().split("!")[-1][:-2]
            self.box_property[string] = {key: testString}


class Tree(ttk.Treeview):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # self.heading("#0", text="VISAO")
        # self.columnconfigure(1, weight=2)
        self.controller = controller
        self.elements = {}
        self.selected = None
        popup1 = [
            {'label': 'Add project', 'command': self.add_project},
            {'label': '&&---', 'command': ''},
            {'label': 'Delete', 'command': ''}
        ]
        popup2 = [
            {'label': 'Add switchboard', 'command': self.add_switchboard},
            {'label': 'Delete', 'command': ''},
            {'label': '&&---', 'command': ''},
            {'label': 'Copy', 'command': ''},
            {'label': 'Paste', 'command': ''},
        ]
        popup3 = [
            {'label': 'Add Circuit', 'command': self.add_circuit},
            {'label': 'Add Switchboard', 'command': self.add_switchboard},
            {'label': 'Delete', 'command': ''},
            {'label': '&&---', 'command': ''},
            {'label': 'Copy', 'command': ''},
            {'label': 'Paste', 'command': ''},
        ]
        popup4 = [
            {'label': 'Add lighting', 'command': self.add_lighting},
            {'label': 'Add motor', 'command': self.add_motor},
            {'label': 'Add specific', 'command': self.add_specific},
            {'label': 'Add socket', 'command': self.add_socket},
            {'label': 'Delete', 'command': ''},
            {'label': '&&---', 'command': ''},
            {'label': 'Copy', 'command': ''},
            {'label': 'Paste', 'command': ''},
        ]
        popup5 = [
            {'label': 'Delete', 'command': ''},
        ]
        self.bind(right_click, self.callback)
        self.bind("<ButtonRelease-1>", self.select)

        self.popup1 = self.build_popup(self, popup1)
        self.popup2 = self.build_popup(self, popup2)
        self.popup3 = self.build_popup(self, popup3)
        self.popup4 = self.build_popup(self, popup4)
        self.popup5 = self.build_popup(self, popup5)

    # Open popup menu when right button clicked
    def callback(self, event):
        try:
            self.selected = self.selection()
            # element = self.item(self.selected)['tags'][0]
            element = self.selected[0]
            # select = getvalue(self.elements, element)
            select = getvalue(self.elements, element)
            if isinstance(select, Project):
                self.popup2.post(event.x_root, event.y_root)  # elements popup menu
            elif isinstance(select, SwitchBoard):
                self.popup3.post(event.x_root, event.y_root)  # Load popup menu
            elif isinstance(select, Circuit):
                self.popup4.post(event.x_root, event.y_root)  # Load popup menu
            elif isinstance(select, Load):
                self.popup5.post(event.x_root, event.y_root)  # elements popup menu
        except IndexError:
            self.popup1.post(event.x_root, event.y_root)

    def select(self, event):
        self.selected = self.selection()
        # print(self.elements, self.selected)
        # print(type(getvalue(self.elements, self.selected[0])) == SwitchBoard)
        # if type(getvalue(self.elements, self.selected[0])) == SwitchBoard:
        #     try:
        #         print(getvalue(self.elements, self.selected[0]).board())
        #     except AssertionError:
        #         pass
        try:
            for item in self.controller.frames[WhichProperties].values:
                self.controller.frames[WhichProperties].labels[item].destroy()
                self.controller.frames[WhichProperties].values[item].destroy()
            selected = getvalue(self.controller.frames[Tree].elements, self.selected[0])
            if isinstance(selected, SwitchBoard):
                x = json.loads(selected.board())
                print(x)
            self.controller.frames[WhichProperties].screen(selected.attributes())
        except IndexError:
            pass
        finally:
            if self.selected == 0:
                return
            return self.selected

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
                          'end', text=my_object.tag,
                          tags=(my_object.tag,))  # add new child to treeview
        self.add_to_dict_key(selected, {key: my_object})  # Add new item to self.elements

    def add_to_dict_key(self, parent, item):
        """ Build Returns key to the path to self.elements """
        if parent is None:
            self.elements.update(item)
        else:
            key = getvalue(self.elements, parent)
            k = list(item.keys())[0]
            key.elements[k] = item[k]

    def build_popup(self, container, listing):
        ''' Event popup menu '''
        menu = tk.Menu(container, tearoff=0)
        for item in listing:
            if item['label'] == '&&---':
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


class GUI:
    def __init__(self, toplevel):
        super().__init__()
        # Screen settings
        self.toplevel = toplevel
        self.screen_width = 0
        self.screen_height = 0
        self.frames = {}
        self.initial_settings()
        self.initialize()
        self.toplevel.bind('<Configure>', self.resize)

    def initial_settings(self):
        self.set_title("Charon")
        self.set_init_size_window()

    def set_title(self, title):
        self.toplevel.title(title)

    def set_init_size_window(self):
        self.screen_width = self.toplevel.winfo_screenwidth()*.80
        self.screen_height = self.toplevel.winfo_screenheight()*.80

    def resize(self, event):
        if event.widget == self.toplevel:
            self.screen_width = event.width
            self.screen_height = event.height
            self.initialize()

    def initialize(self):
        self.toplevel.geometry(str(int(self.screen_width)) + "x" + str(int(self.screen_height)))
        # self.toplevel.rowconfigure(9, {'minsize': 30})
        # self.toplevel.columnconfigure(2, {'minsize': 30})
        
        # Main container
        master = ttk.Frame(self.toplevel, padding="3 3 12 12")
        master.grid(column=0, row=0, stick=(tk.N, tk.W, tk.E, tk.S))

        position = [tk.N + tk.W + tk.NW, tk.N, tk.N + tk.E + tk.NE]
        # Build three columns (frame1=Tree, Frame2=Middle, Frame3=WhichProperties)
        # Frame 1 is size X
        # Frame 2 is size X * 3
        # Frame 3 is size X
        height = int(self.screen_height) * .95
        for index_frame, F in enumerate([Tree, Middle, WhichProperties]):
            width = int(self.screen_width / 5)
            if index_frame == 1:
                width *= 3
            frame = tk.Frame(master, width=width, height=height)
            frame.grid_propagate(False)
            frame.grid(column=index_frame, row=0)
            container = F(frame, self)
            self.frames[F] = container
            frame.grid(column=index_frame, row=0, stick=(tk.N, tk.W, tk.E, tk.S))
            container.grid(column=0, row=0, stick=position[index_frame])
            if index_frame == 1 or index_frame == 2:
                yscrollbar = tk.Scrollbar(container, width=10, orient=tk.VERTICAL)
                yscrollbar.grid(column=19, row=0, rowspan=50, stick=tk.N+tk.S+tk.W+tk.E)
                xscrollbar = tk.Scrollbar(container, width=10, orient=tk.HORIZONTAL)
                xscrollbar.grid(column=0, row=50, columnspan=19, stick=tk.N+tk.E+tk.S+tk.W)


        
