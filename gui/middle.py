from settings import *
# from static_functions import *
# from project import *
# from switchboard import *
# from circuit import *
# from load import *


# class Middle(ttk.Frame):
class Middle(ttk.Treeview):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.tree = None    # Substituiu self.tree = controller
        self.configure(height=self.controller.screen_height)
        self.values = []
        self.table_setting = [('#1', 'Tag', 'tag'),
                              ('#2', 'Phase Voltage', 'phase_voltage'),
                              ('#3', 'Phases', 'phases'),
                              ('#4', 'Active', 'active'),
                              ('#5', 'Apparent', 'apparent'),
                              ('#6', 'Power factor', 'average_power_factor'),
                              ('#7', 'R S T', 'current'),
                              ]

    def treeview_create(self):
        column = tuple(str(i+1) for i in range(len(self.table_setting)))
        return ttk.Treeview(self, column=column, show='headings', height=self.controller.screen_height)

    def refresh(self, table):
        self.configure(height=self.controller.screen_height)
        self.tree = self.treeview_create()
        self.screen(table)
        self.tree.grid(columnspan=4, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    def screen(self, table):
        if table is None:
            return False
        width = [100, 70, 10, 70, 70, 20, 100]
        counter = 0
        for x in table:
            for y in x['elements']:
                print(x['elements'][y].tag)
        for (x, y, z) in self.table_setting:
            self.tree.column(x, anchor=tk.CENTER, width=width[counter])
            self.tree.heading(x, text=y)
            counter += 1

        sum_columns = [0, 0]
        for line in table:
            values = tuple(line[z] for x, y, z in self.table_setting)
            self.tree.insert('', 'end', values=values)
            sum_columns[0] += line['active']
            sum_columns[1] += line['apparent']
            print(sum_columns[0], sum_columns[1])
        return True
