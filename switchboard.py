from circuit import *

import math
import json
from datetime import *
# from random import randint

#
# Functions needs to Switchboard class
#


# Function to find minimum and maximum position in list
def maxminposition(A):

    # inbuilt function to find the position of minimum
    minposition = A.index(min(A))

    # inbuilt function to find the position of maximum
    maxposition = A.index(max(A))
    return minposition, maxposition


def equilibrium(loads, calls=1):
    """
    Build current balanced matrix
    """
    accumulate = [0, 0, 0]
    lenght_matrix = len(loads)
    for current in loads:
        #valor = sum(y for y in current)  # Sum currents at circuits
        accumulate[0] += current[0]
        accumulate[1] += current[1]
        accumulate[2] += current[2]
    average = (accumulate[0]+accumulate[1]+accumulate[2]) / 3
    # select column with max and
    min, max = maxminposition([accumulate[0], accumulate[1], accumulate[2]])
    loop_over = False   # Stop condition to main while loop
    pointer = calls     # auxiliary variable because 'calls' cannot be modified
    while not loop_over and (max != 0 or min !=0) :
        #index = randint(0, lenght_matrix-1)  # Random select index, this is the best, but return random results
        index = pointer % lenght_matrix   # Select one-by-one index load if conditions not deal, return stable results
        phases = 3 - loads[index].count(0)
        if phases < 3:  # if 3-phases circuit nothing to do
            if phases == 2 and loads[index][min] == 0:  # if 2-Phases circuit and min column empty
                accumulate[min] += loads[index][max]
                accumulate[max] -= loads[index][max]
                loads[index][min], loads[index][max] = loads[index][max], loads[index][min]
                loop_over = True    # stop loop
            elif phases == 1 and loads[index][min] == 0:    # if 1-Phase circuit and min column empty
                accumulate[min] += loads[index][max]
                accumulate[max] -= loads[index][max]
                loads[index][min], loads[index][max] = loads[index][max], loads[index][min]
                loop_over = True    # stop loop
        # If none of previous conditions are accept, then move pointer one position and go to next index(circuit)
        pointer += 1
    if equilibrium_check(accumulate, average, calls):
        return loads
    else:
        return equilibrium(loads, calls + 1)


def equilibrium_check(accumulate, average, calls):
    """
    Define stop conditions
    """
    if average != 0:
        vpA = abs(accumulate[0] - average) / average    # Calculate A-Phase imbalance
        vpB = abs(accumulate[1] - average) / average    # Calculate B-Phase imbalance
        vpC = abs(accumulate[2] - average) / average    # Calculate C-Phase imbalance
    else:
        vpA, vpB, vpC = 0, 0, 0
    PUI = max(vpA, vpB, vpC)                        # Stop condition , select maximum imbalance
    # PUI and calls is stop condition to recursion
    if (PUI < 0.03) or (PUI < 0.05 and calls > 20) or\
            (PUI < 0.07 and calls > 40) or (PUI < 0.10 and calls > 50) or \
            (PUI < 0.16 and calls > 60) or (PUI < 0.20 and calls > 70) or (PUI < 0.30 and calls > 80) or\
            (PUI < 0.35 and calls > 100) or (calls > 120):
        return True     # return Stop condition reach
    else:
        return False    # return try again


class SwitchBoard(object):
    """
    Create a switchboard
    """
    counter = 1

    def __init__(self,  label="Unnamed", line_voltage=220, phases=1, distance=0.0, demand_factor=1.0,
                 fct=1.0, fca=1.0, fcs=1.0, method=0, description=None, tag=None, idt=None):
        # assert (tag is not None), "SwitchBoard must be a tag"
        assert (label is not None), "SwitchBoard must be a label"
        assert (1 <= phases <= 4), "Phases must be a integer between 1 and 3"
        assert (distance >= 0), "Distance must be a non-negative number"
        assert (0 < demand_factor <= 1), "Demand factor must be greater than 0 until 1"
        assert (line_voltage > 0), "The phase voltage must be greater than 0"
        self._idt = str(datetime.now().microsecond)
        self._tag = "Unnamed" if tag is not None else "Switchboard_" + str(SwitchBoard.counter)
        self._label = label
        self._description = description
        self._phases = phases
        self._line_voltage = line_voltage
        self._distance = distance
        self._demand_factor = demand_factor
        self._fct = fct
        self._fca = fca
        self._fcs = fcs
        self._method = method
        self._elements = {}
        SwitchBoard.counter += 1

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def demand_factor(self):
        return self._demand_factor

    @demand_factor.setter
    def demand_factor(self, value):
        self._demand_factor = value

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value

    @property
    def phases(self):
        return self._phases

    @phases.setter
    def phases(self, value):
        self._phases = value

    @property
    def line_voltage(self):
        return round(self._line_voltage, 1)

    @line_voltage.setter
    def line_voltage(self, value):
        self._line_voltage = value

    @property
    def fct(self):
        """ correction factor  - temperature"""
        return self._fct

    @fct.setter
    def fct(self, value):
        self._fct = value

    @property
    def fca(self):
        """  correction factor - Grouping of conductors or cables"""
        return self._fca

    @fca.setter
    def fca(self, value):
        self._fca = value

    @property
    def fcs(self):
        """ correction factor - groups of several circuits or multi- core cables:"""
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

    @property
    def method(self):
        return self._method

    # @method.setter
    # def method(self, value):
    #     self._method = value

    @property
    def idt(self):
        return self._idt

    @idt.setter
    def idt(self, value):
        self._idt = value

    @staticmethod
    def average_power_factor():
        """Return power factor 1 to switchboards"""
        return round(1, 1)

    # def list_circuit_voltage(self, circuit):
    def phase_voltage(self, component):
        return round(self.line_voltage / math.sqrt(3), 2) if component.phases == 1 else round(self.line_voltage, 1)

    # def average_power_factor(self, circuit):
    #     return round(circuit.average_power_factor(), 2)

    def sum_active_power(self):
        accumulator = sum([self.elements[item].sum_active_power() for item in self.elements])
        return round(accumulator, 2)

    def sum_reactive_power(self):
        accumulator = sum([self.elements[item].sum_reactive_power() for item in self.elements])
        return round(accumulator, 2)

    def sum_apparent_power(self):
        accumulator = sum([self.elements[item].sum_apparent_power() for item in self.elements])
        return round(accumulator, 2)

    def current_without_correction(self, component):
        if component.phases == 1:
            return round(component.sum_apparent_power() / (self.line_voltage / math.sqrt(3)), 1)
        elif component.phases == 2:
            return round(component.sum_apparent_power() / self.line_voltage, 1)
        elif component.phases == 3:
            return round(component.sum_apparent_power() / (self.line_voltage * math.sqrt(3)), 1)

    def current(self, component):
        assert isinstance(component, SwitchBoard) or isinstance(component, Circuit),\
            "Parameter must be SwitchBoard or Circuit!"
        return round(self.current_without_correction(component) / (component.fct * component.fca * component.fcs), 1)

    # def table_line(self):
    def digest(self):
        return dict(tag=self.tag,
                    description=self.description,
                    phases=self.phases,
                    distance=self.distance,
                    active=self.sum_active_power(),
                    reactive=self.sum_reactive_power(),
                    apparent=self.sum_apparent_power(),
                    elements=self.elements)

    def add(self, *elements):
        """Add new load"""
        for element in elements:
            assert (isinstance(element, Circuit) or isinstance(element, SwitchBoard)), \
                "You must can only add circuits or boards to a board."
            assert (self != element), "You cannot add a switchboard to yourself."
            assert (element not in self.elements), "The element already exists in this switchboard."
            self._elements[element.tag] = element

    ################
    ################
    def quantity_elements(self):
        return len(self.elements)

    # PUBLIC METHODS
    # def add(self, element):
    #     assert (isinstance(element, Circuit) or isinstance(element, SwitchBoard)),\
    #         "You must can only add circuits or boards to a board."
    #     assert (self != element), "You cannot add a switchboard to yourself."
    #     assert (element not in self.elements), "The element already exists in this switchboard."
    #     self._elements[element.tag] = element

    def copy(self):
        new = self.__class__(*self.parameters())
        for element in self.elements:
            instance = self.elements[element]
            new.add(instance.copy())
            # copy_instance = instance.__class__(*instance.parameters())
            # new.add(copy_instance)
        return new

    def delete(self, item=None):
        if item is None:
            del self
        else:
            del self.elements[item.tag]

    def sum_powers(self):
        """Totalize active power, reactive power and apparent power"""
        sum_active = sum([self.elements[item].sum_active_power() for item in self.elements])
        sum_apparent = sum([self.elements[item].sum_apparent_power() for item in self.elements])
        sum_reactive = sum([self.elements[item].sum_reactive_power() for item in self.elements])
        return round(sum_active, 2), round(sum_apparent, 2), round(sum_reactive, 2)

    def sum_currents(self):
        active, apparent, reactive = self.sum_powers()
        active_current, apparent_current, reactive_current = 0, 0, 0
        phase_voltage = self.line_voltage / math.sqrt(3)
        if self._phases == 1:                                                   # One phase
            active_current = active / phase_voltage
            apparent_current = apparent / phase_voltage
            reactive_current = reactive / phase_voltage
        elif self._phases == 2:                                                 # Two phases
            active_current = active / self.line_voltage
            apparent_current = apparent / self.line_voltage
            reactive_current = reactive / self.line_voltage
        elif self._phases == 3:                                                 # Three phases
            active_current = active / (self.line_voltage * math.sqrt(3))
            apparent_current = apparent / (self.line_voltage * math.sqrt(3))
            reactive_current = reactive / (self.line_voltage * math.sqrt(3))
        elif self._phases == 4:
            active_current = active / (3 * phase_voltage)                       # Three phases
            apparent_current = apparent / (3 * phase_voltage)
            reactive_current = reactive / (3 * phase_voltage)
        return round(active_current, 2), round(apparent_current, 2), round(reactive_current, 2)

    def current_division(self, component):
        circuit_current = self.current(component)
        if component.phases == 1:
            division = [circuit_current, 0, 0]
        elif component.phases == 2:
            division = [circuit_current, circuit_current, 0]
        else:
            division = [circuit_current, circuit_current, circuit_current]
        return division

    def distribution_board(self):
        # assert (self.quantity_elements() > 0), "The Switchboard has no elements to calculate!"
        matrix_current, table = [], []
        if self.quantity_elements() > 0:
            for element in self.elements:
                component = self.elements[element]
                item = component.digest()
                item.update({'phase_voltage': self.phase_voltage(component)})
                item.update({'average_power_factor': self.average_power_factor()})
                table.append(item)
                matrix_current.append(self.current_division(component))
                # table.append([item, self.phase_voltage(component), component.average_power_factor()])
            # Calculate balanced current matrix from unbalanced current matrix
            # Build table from balanced's loads
            aux = equilibrium(matrix_current)
            for index, current in enumerate(aux):
                table[index].update({'current': current})
        return table

    # def convert_table_to_tuple(self, table):
    #     return [ (value) for key, value in table.items()]

    def attributes(self, parameter=None):
        parameters = {
                "tag": self.tag,
                "label": self.label,
                "description": self.description,
                "line_voltage": self.line_voltage,
                "phases": self.phases,
                "distance": self.distance,
                "demand_factor": self.demand_factor,
                "fct": self.fct,
                "fca": self.fca,
                "fcs": self.fcs,
            }
        try:
            if parameter is not None:
                return json.dumps(parameters[parameter])
        except (KeyError, NameError):
            raise Exception("Error at parameters!")
        return json.dumps(parameters)

    # def format(self, parameter=None):
    #     parameters = {
    #             "tag": "^\w{0,10}$",
    #             "label": "^\w{0,10$",
    #             "description": "^\w{0,10$",
    #             "line_voltage": "^\w{0,10$",
    #             "phases": "^\w{0,10$",
    #             "distance": "^\w{0,10$",
    #             "demand_factor": "^\w{0,10$",
    #             "fct": "^\w{0,10$",
    #             "fca": "^\w{0,10$",
    #             "fcs": "^\w{0,10$",
    #         }
    #     try:
    #         if parameter is not None:
    #             return json.dumps(parameters[parameter])
    #     except (KeyError, NameError):
    #         raise Exception("Error at parameters!")
    #     return json.dumps(parameters)
