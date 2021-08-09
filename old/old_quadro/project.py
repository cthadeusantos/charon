class Project(object):
    counter = 1

    def __init__(self, tag=None, idt=None):
        self._idt = idt
        self._tag = tag if tag is not None else "Project_" + str(Project.counter)
        self.elements = {}
        Project.counter += 1

    def add(self, element):
        self.elements[self.tag] = element

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    def quantity_elements(self):
        return len(self.elements)

    def attributes(self):
        return {
            "tag": {"value": self.tag, "regex": "^\w{0,10}$"}
        }

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

    def show(self):
        print('|', self.tag)
        for item in self.elements:
            item.show('\t')
