from load import *
import json
from datetime import *


class Circuit(object):
    """
    Create a circuit
    """
    counter = 1

    def __init__(self,  description=None, phases=1, distance=0.0, demand_factor=1.0, vertical_lines=0, height=0.0,
                 fct=1.0, fca=1.0, fcs=1.0, method=0, remarks=None, tag=None, idt=None):
        assert (0 <= phases <= 3), "Phases must be a integer between 1 and 3"
        assert (distance >= 0), "Distance must be a non-negative number"
        assert (0 < demand_factor <= 1), "Demand factor must be greater than 0 until 1"
        assert (vertical_lines >= 0), "Vertical lines must be a non-negative number"
        assert (height >= 0), "Height must be a non-negative number"
        self._idt = str(datetime.now().microsecond)
        self._tag = tag if tag is not None else "Circuit_" + str(Circuit.counter)
        self._description = description
        self._remarks = remarks
        self._phases = phases
        self._distance = distance
        self._demand_factor = demand_factor
        self._vertical_lines = vertical_lines
        self._height = height
        self._fct = fct
        self._fca = fca
        self._fcs = fcs
        self._method = method
        self._elements = {}
        Circuit.counter += 1

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value

    @property
    def phases(self):
        return self._phases

    @phases.setter
    def phases(self, value):
        self._phases = value

    @property
    def demand_factor(self):
        return self._demand_factor

    @demand_factor.setter
    def demand_factor(self, value):
        self._demand_factor = value
        
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def vertical_lines(self):
        return self._vertical_lines

    @vertical_lines.setter
    def vertical_lines(self, value):
        self._vertical_lines = value
        
    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        self._method = value

    @property
    def idt(self):
        return self._idt

    @idt.setter
    def idt(self, value):
        self._idt = value

    @property
    def fct(self):
        return self._fct

    @fct.setter
    def fct(self, value):
        self._fct = value

    @property
    def fca(self):
        return self._fca

    @fca.setter
    def fca(self, value):
        self._fca = value

    @property
    def fcs(self):
        return self._fcs

    @fcs.setter
    def fcs(self, value):
        self._fcs = value

    @property
    def specie(self):
        """ Return load type """
        return type(self).__name__

    @property
    def elements(self):
        """ Return load type """
        return self._elements

    # def add(self, load):
    #     """Add new load"""
    #     assert isinstance(load, Load), "ADD parameter must be a LOAD!"
    #     self.elements[load.tag] = load

    def add(self, *loads):
        """Add new load"""
        for load in loads:
            assert isinstance(load, Load), "ADD parameter must be a LOAD!"
            self.elements[load.tag] = load

    def delete(self, item=None):
        if item is None:
            del self
        else:
            del self.elements[item.tag]
            del item

    def copy(self):
        new = self.__class__(*self.parameters())
        for element in self.elements:
            instance = self.elements[element]
            new.add(instance.copy())
            # copy_instance = instance.__class__(*instance.parameters())
            # new.add(copy_instance)
        return new

    def sum_apparent_power(self):
        accumulator = sum(self.elements[load].apparent_power() for load in self.elements)
        return round(accumulator, 2)

    def sum_active_power(self):
        accumulator = sum(self.elements[load].active_power() for load in self.elements)
        return round(accumulator, 2)

    def sum_reactive_power(self):
        accumulator = sum(self.elements[load].reactive_power() for load in self.elements)
        return round(accumulator, 2)

    def average_power_factor(self):
        """Calculate the average power factor from the circuit"""
        list_power_factor = [self.elements[load].power_factor for load in self.elements]
        return round(sum(list_power_factor) / self.quantity_loads(), 2)

    # def sum_distances(self):
    #     accumulator = sum(self.loads[load].distance for load in self.loads)
    #     return round(accumulator + (self._vertical_lines * self._height), 2)

    def quantity_loads(self):
        return len(self.elements)

    def list_types(self):
        value = set()
        for load in self.elements:
            value.add(self.elements[load].specie)
        return value

    def attributes(self, parameter=None):
        """ Return circuit attributes """
        parameters = {
                "tag": self.tag,
                "description": self.description,
                "remarks": self.remarks,
                "phases": self.phases,
                "distance": self.distance,
                "demand_factor": self._demand_factor,
                "vertical_lines": self._vertical_lines,
                "height": self._height,
                "fct": self.fct,
                "fca": self.fca,
                "fcs": self.fcs,
                "active_power": self.sum_active_power(),
                "apparent_power": self.sum_apparent_power(),
                "reactive_power": self.sum_reactive_power(),
            }
        try:
            if parameter is not None:
                return json.dumps(parameters[parameter])
        except (KeyError, NameError):
            raise Exception("Error at parameters!")
        return json.dumps(parameters)

    def format(self, parameter=None):
        """ Return circuit format """
        parameters = {
                "tag": "^\w{0,10}$",
                "description": "^\w{0,10}$",
                "remarks": "^\w{0,10}$",
                "phases": "^\w{0,10}$",
                "distance": "^\w{0,10}$",
                "demand_factor": "^\w{0,10}$",
                "vertical_lines": "^\w{0,10}$",
                "height": "^\w{0,10}$",
                "fct": "^\w{0,10}$",
                "fca": "^\w{0,10}$",
                "fcs": "^\w{0,10}$",
                "active_power": "^\w{0,10}$",
                "apparent_power": "^\w{0,10}$",
                "reactive_power": "^\w{0,10}$",
            }
        try:
            if parameter is not None:
                return json.dumps(parameters[parameter])
        except (KeyError, NameError):
            raise Exception("Error at parameters!")
        return json.dumps(parameters)

    def parameters(self):
        return self.description, self.phases, self.distance, self.demand_factor,\
               self.vertical_lines, self.height, self.fct, self.fca, self.method,\
               self.remarks, self.tag, self.idt

    def table_line(self):
        return self.tag, self.description,\
               self.phases, self.distance,\
               self.sum_active_power(), self.sum_apparent_power(),\
               self.elements
