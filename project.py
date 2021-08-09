import json
from switchboard import *
from circuit import *
from datetime import *

class Project(object):
    counter = 1

    def __init__(self, tag=None, idt=None):
        self._idt = str(datetime.now().microsecond)
        self._tag = tag if tag is not None else "Project_" + str(Project.counter)
        self._elements = {}
        Project.counter += 1

    @property
    def elements(self):
        """ Return load type """
        return self._elements

    @property
    def idt(self):
        return self._idt

    @idt.setter
    def idt(self, value):
        self._idt = value

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    def quantity_elements(self):
        return len(self.elements)

    def attributes(self, parameter=None):
        parameters = {
                "tag": self.tag,
            }
        try:
            if parameter is not None:
                return json.dumps(parameters[parameter])
        except (KeyError, NameError):
            raise Exception("Error at parameters!")
        return json.dumps(parameters)

    def format(self, parameter=None):
        parameters = {
                "tag": "^\w{0,10}$",
            }
        try:
            if parameter is not None:
                return json.dumps(parameters[parameter])
        except (KeyError, NameError):
            raise Exception("Error at parameters!")
        return json.dumps(parameters)

    #
    # def delete(self, element):
    #     assert (self.quantity_elements() > 0), "You cannot delete! The Project has no elements"
    #     for item in self.elements:
    #         if item == element:
    #             self.elements.remove(item)
    #             return True
    #     return False

    def delete(self):
        for item in self.elements:
            self.elements.remove(item)
            item.delete()
        del self

    # def add(self, element):
    #     self.elements[self.tag] = element

    def add(self, *elements):
        """Add new load"""
        for element in elements:
            assert (isinstance(element, SwitchBoard)), \
                "You must can only add switchboards to a project."
            assert (self != element), "You cannot add a project to yourself."
            assert (element not in self.elements), "The element already exists in this project."
            self._elements[element.tag] = element

    def copy(self):
        new = self.__class__(*self.parameters())
        for element in self.elements:
            instance = self.elements[element]
            new.add(instance.copy())
            # copy_instance = instance.__class__(*instance.parameters())
            # new.add(copy_instance)
        return new

    def parameters(self):
        return self.tag, self.idt

    def show(self):
        print('|', self.tag)
        for item in self.elements:
            item.show('\t')
