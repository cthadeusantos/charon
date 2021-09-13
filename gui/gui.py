import pickle
# from settings import *
from gui.charon import *
from settings import *


class GUI2:
    def __init__(self, toplevel):
        super().__init__()
        # Screen settings
        self.toplevel = toplevel
        self.screen_width = 0
        self.screen_height = 0
        self.frame = []
        self.frames = {}
        self.initial_settings()
        self.initialize_screen()
        # self.toplevel.bind('<Configure>', self.resize)

    def initial_settings(self):
        self.set_title("Charon")
        self.set_init_size_window()
        weight = [1, 3, 1]
        for index in range(3):
            self.toplevel.columnconfigure(index, weight=weight[index])

    def set_title(self, title):
        self.toplevel.title(title)

    def set_init_size_window(self):
        self.screen_width = self.toplevel.winfo_screenwidth()*.80
        self.screen_height = self.toplevel.winfo_screenheight()*.80

    def resize(self, event):
        if event.widget == self.toplevel:
            self.screen_width = event.width
            self.screen_height = event.height
            # self.resize_main_window()

    def initialize_screen(self):
        self.toplevel.geometry(str(int(self.screen_width)) + "x" + str(int(self.screen_height)))
        self.buttons_frame()
        self.mainframe()

    def buttons_frame(self):
        button_frame = ttk.Frame(self.toplevel)
        button_frame.grid(column=0, row=0, stick=tk.NW + tk.SE + tk.E)
        # Button Tuple (str:Button Text, str:Image Path, method: command)
        buttons = [("New", '', self.new),
                   ("Save", 'icons/upload.svg', self.save),
                   ("Load", '', self.load)]
        for index, item in enumerate(buttons):
            text, image, command = item
            button = tk.Button(button_frame, text=text, command=command, height=1, width=1)
            button.grid(column=index,  row=0, sticky=tk.NW)

    def mainframe(self):
        position = [(tk.N, tk.W, tk.E, tk.S), (tk.N, tk.W, tk.E, tk.S), tk.SW]
        # Build three columns (frame1=Tree, Frame2=Middle, Frame3=WhichProperties)
        height = int(self.screen_height) * .98
        for index_frame, F in enumerate([Tree, Middle, WhichProperties]):
            width = int(self.screen_width / 5)
            column = 1
            if index_frame == 1:
                width *= 3
                column = 3
            self.frame.append(tk.Frame(self.toplevel, width=width, height=height))
            self.frame[index_frame].grid_propagate(False)
            self.frame[index_frame].grid(column=index_frame, row=1, sticky=position[index_frame])
            container = F(self.frame[index_frame], self)
            self.frames[F] = container
            container.grid(column=index_frame, row=1, stick=position[index_frame], columnspan=column, sticky=position[index_frame])

    def new(self):
        container = Tree(self.frame[0], self)
        self.frames[Tree] = container
        container.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S), columnspan=1)

    def save(self):
        output_file = open('output.chr', "wb")
        pickle.dump(self.frames[Tree].elements, output_file)
        output_file.close()

    def load(self):
        self.new()
        input_file = open('output.chr', "rb")
        self.frames[Tree].elements = pickle.load(input_file)
        input_file.close()
        self.load_build_tree_after_load(self.frames[Tree].elements)

    def load_build_tree_after_load(self, nested_dict):
        result = self.load_organize(nested_dict)
        for index in range(len(result)):
            num = hex(index + 1)[2:].upper()
            num = "I000"[:(4 - len(num))] + num
            daddy, tag = result[num]
            self.frames[Tree].insert(daddy, 'end', text=tag, tags=(tag,))

    def load_organize(self, nested_dict, dict=None, daddy=''):
        """Input: nested dict, value"""
        if dict is None:
            dict = {}
        for key in nested_dict:
            value = nested_dict[key]
            dict.update({key: (daddy, value.tag)})
            if value.elements is not None:
                self.load_organize(value.elements, dict, key)  # recursive call
        return dict


# class GUI:
#     def __init__(self, toplevel):
#         super().__init__()
#         # Screen settings
#         self.toplevel = toplevel
#         self.screen_width = 0
#         self.screen_height = 0
#         self.frame = None
#         self.frames = {}
#         self.initial_settings()
#         self.initialize_screen()
#         # self.toplevel.bind('<Configure>', self.resize)
#
#     def initial_settings(self):
#         self.set_title("Charon")
#         self.set_init_size_window()
#         weight = [1, 3, 1]
#         for index in range(3):
#             self.toplevel.columnconfigure(index, weight=weight[index])
#
#     def set_title(self, title):
#         self.toplevel.title(title)
#
#     def set_init_size_window(self):
#         self.screen_width = self.toplevel.winfo_screenwidth()*.80
#         self.screen_height = self.toplevel.winfo_screenheight()*.80
#
#     def resize(self, event):
#         if event.widget == self.toplevel:
#             self.screen_width = event.width
#             self.screen_height = event.height
#             # self.resize_main_window()
#
#     def initialize_screen(self):
#         self.toplevel.geometry(str(int(self.screen_width)) + "x" + str(int(self.screen_height)))
#         self.buttons_frame()
#         self.main_widgets()
#
#     def buttons_frame(self):
#         button_frame = ttk.Frame(self.toplevel)
#         button_frame.grid(column=0, row=0, stick=tk.NW + tk.SE + tk.E)
#         # Button Tuple (str:Button Text, str:Image Path, method: command)
#         buttons = [("New", '', self.new),
#                    ("Save", 'icons/upload.svg', self.save),
#                    ("Load", '', self.load)]
#         for index, item in enumerate(buttons):
#             text, image, command = item
#             button = tk.Button(button_frame, text=text, command=command, height=1, width=1)
#             button.grid(column=index,  row=0, sticky=tk.NW)
#
#     def main_widgets(self):
#         position = [(tk.N, tk.W, tk.E, tk.S), (tk.N, tk.W, tk.E, tk.S), (tk.N, tk.W, tk.E, tk.S)]
#         # Build three columns (frame1=Tree, Frame2=Middle, Frame3=WhichProperties)
#         height = int(self.screen_height) * .95
#         for index_frame, F in enumerate([Tree, Middle, WhichProperties]):
#             width = int(self.screen_width / 5)
#             if index_frame == 1:
#                 width *= 3
#             self.frame = tk.Frame(self.toplevel, width=width, height=height)
#             self.frame.grid_propagate(False)
#             self.frame.grid(column=index_frame, row=1)
#             container = F(self.frame, self)
#             self.frames[F] = container
#             x = 3 if index_frame == 1 else 1
#             if index_frame == 1 or index_frame == 2:
#                 yscrollbar = tk.Scrollbar(container, width=10, orient=tk.VERTICAL)
#                 yscrollbar.grid(column=19, row=0, rowspan=1, stick=tk.N + tk.S + tk.W + tk.E)
#                 xscrollbar = tk.Scrollbar(container, width=10, orient=tk.HORIZONTAL)
#                 xscrollbar.grid(column=0, row=50, columnspan=1, stick=tk.N + tk.E + tk.S + tk.W)
#             # container.tree.configure(xscrollcommand=xscrollbar.set)
#                 container.grid(column=index_frame, row=1, stick=position[index_frame], columnspan=x)
#             else:
#                 container.grid(column=index_frame, row=1, stick=position[index_frame], columnspan=x)
#
#     def new(self):
#         # self.frames[Tree].delete(*self.frames[Tree].get_children())
#         container = Tree(self.toplevel, self)
#         self.frames[Tree] = container
#         container.grid(column=0, row=1, stick=(tk.N, tk.W, tk.E, tk.S))
#         yscrollbar = tk.Scrollbar(container, width=10, orient=tk.VERTICAL)
#         yscrollbar.grid(column=19, row=0, rowspan=50, stick=tk.N + tk.S + tk.W + tk.E)
#         xscrollbar = tk.Scrollbar(container, width=10, orient=tk.HORIZONTAL)
#         xscrollbar.grid(column=0, row=50, columnspan=19, stick=tk.N + tk.E + tk.S + tk.W)
#         container.grid(column=0, row=1, stick=(tk.N, tk.W, tk.E, tk.S), columnspan=1)
#
#     def save(self):
#         # self.elementos(self.frames[Tree].elements)
#         output_file = open('output.chr', "wb")
#         pickle.dump(self.frames[Tree].elements, output_file)
#         output_file.close()
#
#     def load(self):
#         self.new()
#         input_file = open('output.chr', "rb")
#         self.frames[Tree].elements = pickle.load(input_file)
#         input_file.close()
#         self.load_build_tree_after_load(self.frames[Tree].elements)
#
#     def load_build_tree_after_load(self, nested_dict):
#         result = self.load_organize(nested_dict)
#         for index in range(len(result)):
#             num = hex(index+1)[2:].upper()
#             num = "I000"[:(4 - len(num))] + num
#             daddy, tag = result[num]
#             self.frames[Tree].insert(daddy, 'end', text=tag, tags=(tag,))
#         # self.toplevel.update()
#
#     def load_organize(self,  nested_dict, dict=None, daddy=''):
#         """Input: nested dict, value"""
#         if dict is None:
#             dict = {}
#         for key in nested_dict:
#             value = nested_dict[key]
#             dict.update({key: (daddy, value.tag)})
#             if value.elements is not None:
#                 self.load_organize(value.elements, dict,  key)  # recursive call
#         return dict
