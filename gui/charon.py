from settings import *
from static_functions import *
from project import *
from switchboard import *
from circuit import *
from load import *
from gui.middle import *


class Tree(ttk.Treeview):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # self.heading("#0", text="VISAO")
        # self.columnconfigure(1, weight=2)
        self.controller = controller
        self.configure(height=self.controller.screen_height)
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
            if isinstance(select, Load):
                self.popup5.post(event.x_root, event.y_root)  # elements popup menu
                return
            if isinstance(select, Circuit):
                self.popup4.post(event.x_root, event.y_root)  # Load popup menu
                return
            if isinstance(select, SwitchBoard):
                self.popup3.post(event.x_root, event.y_root)  # Load popup menu
                return
            if isinstance(select, Project):
                self.popup2.post(event.x_root, event.y_root)  # elements popup menu
                return
            # if isinstance(select, Project):
            #     self.popup2.post(event.x_root, event.y_root)  # elements popup menu
            # elif isinstance(select, SwitchBoard):
            #     self.popup3.post(event.x_root, event.y_root)  # Load popup menu
            # elif isinstance(select, Circuit):
            #     self.popup4.post(event.x_root, event.y_root)  # Load popup menu
            # elif isinstance(select, Load):
            #     self.popup5.post(event.x_root, event.y_root)  # elements popup menu
        except IndexError:
            self.popup1.post(event.x_root, event.y_root)

    def select(self, event):
        self.selected = self.selection()
        # try:
        for item in self.controller.frames[WhichProperties].values:
            self.controller.frames[WhichProperties].labels[item].destroy()
            self.controller.frames[WhichProperties].values[item].destroy()
        selected = getvalue(self.controller.frames[Tree].elements, self.selected[0])
        if isinstance(selected, SwitchBoard):
            x = selected.distribution_board()
            print(x)
            self.controller.frames[Middle].refresh(selected.distribution_board())
            # self.controller.frames[WhichProperties].screen(selected.distribution_board())
        self.controller.frames[WhichProperties].screen(selected.attributes())
        # except IndexError:
        #     pass
        # finally:
        #     if self.selected == 0:
        #         return
        #     return self.selected

    def add_element(self, istype=None):
        selected = self.selected
        my_object = None
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


class WhichProperties(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        # self.configure(height=self.controller.screen_height, stick=tk.NE + tk.SW)
        self.labels = {}
        self.values = {}
        self.box_property = {}
        self.label = ttk.Label(self, text='Properties')
        self.label.grid(column=1, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

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

    # def refresh(self, table):
    #     self.table = table
    #     self.tree.destroy()
    #     self.tree = ttk.Treeview(self, column=("c1", "c2"), show='headings', height=8)
    #     self.screen(self.table)
    #     self.tree.grid(columnspan=4, row=0, stick=(tk.N, tk.W, tk.E, tk.S))

    def screen(self, attributes=None):
        if attributes is None:
            attributes = json.dumps({})
        self.labels = {}
        self.values = {}
        self.box_property = {}
        attributes = json.loads(attributes)
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