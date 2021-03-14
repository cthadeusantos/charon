from abc import ABC, abstractmethod
from math import tan, acos


class Load(ABC):
    """
    That's a abstract class to create a LOAD.
    You never call this class
    """
    counter = 1     # Static variable
    @abstractmethod
    def __init__(self, input_power=0.0, power_factor=0.95, tag=None, idt=None):
        """
        Constructor to load
        :raises ValueError: if input_power or power_factor are invalids
        """
        assert (input_power > 0), "input power must be a non-negative number"
        assert (0 < power_factor <= 1), "power factor must be greater than 0 until 1"
        self._tag = tag if tag is not None else str(Load.counter)
        self.idt = idt
        self._input_power = input_power
        self._power_factor = power_factor
        self._qty = 1
        Load.counter += 1

    @property
    def tag(self):
        """Return the circuit tag(descriptor)"""
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    @property
    def input_power(self):
        """Return the active power's load"""
        return self._input_power

    @input_power.setter
    def input_power(self, value):
        self._input_power = value

    @property
    def power_factor(self):
        """Return the power factor's load"""
        return self._power_factor

    @power_factor.setter
    def power_factor(self, value):
        self._power_factor = value

    @property
    def qty(self):
        """Return quantity load"""
        return self._qty

    @qty.setter
    def qty(self, value):
        self._qty = value

    @property
    def specie(self):
        """ Return load type """
        return type(self).__name__

    def active_power(self):
        """Return the active power's load"""
        return self.input_power

    def apparent_power(self):
        """Return the apparent power's load"""
        return self.active_power() / self.power_factor

    def reactive_power(self):
        """Return the reactive power's load"""
        return self.active_power() * tan(acos(self.power_factor))

    def delete(self):
        """ Delete load """
        del self

    @abstractmethod
    def properties(self):
        """ Return load properties """
        pass


class Specific(Load):
    """Class to define a Specific Load"""
    def __init__(self, input_power=1.0, power_factor=1.0, tag=None, idt=None):
        super().__init__(input_power, power_factor, tag, idt)
        self._tag = "Specific_" + self._tag
        
    def properties(self):
        """the Specific's properties"""
        return {
            'tag': self.tag,
            'input_power': self.input_power,
            'power_factor': self.input_power,
        }


class Lighting(Load):
    """Class to define a Lighting Load"""
    def __init__(self, input_power=1.0, power_factor=1.0, qty=1, tag=None, idt=None):
        super().__init__(input_power, power_factor, tag, idt)
        self._tag = "Lighting_" + self._tag
        assert (qty > 0 == (int(qty) - qty)), "Quantity must be integer greater than 0"
        self._qty = qty

    def properties(self):
        """the Lighting's properties"""
        return {
            'tag': self.tag,
            'input_power': self.input_power,
            'power_factor': self.input_power,
            'qty': self.qty,
        }

    def active_power(self):
        """Return the input power's lighting"""
        return self.input_power * self.qty


class Motor(Load):
    def __init__(self, input_power=1.0, power_factor=1.0, efficiency=1.0, unit_type='HP', tag=None, idt=None):
        """Motor constructor"""
        super().__init__(input_power, power_factor, tag, idt)
        self._tag = "Motor_" + self._tag
        try:
            if unit_type == "#":
                raise SyntaxError
            unit_type = unit_type.lower()
        except (SyntaxError, AttributeError):
            raise Exception("Motor's unit type must be HP or CV")
        assert (0 < efficiency <= 1), "efficiency must be greater than 0 until 1"
        assert (unit_type == 'hp' or unit_type == 'cv'), "Motor's unit type must be HP or CV"
        unit_value = {'hp': 0, 'cv': 1}
        self._efficiency = efficiency
        self._unit_type = unit_value[unit_type]

    @property
    def efficiency(self):
        return self._efficiency

    @efficiency.setter
    def efficiency(self, value):
        self._efficiency = value

    @property
    def unit_type(self):
        """Return unit power's type"""
        return self._unit_type

    @unit_type.setter
    def unit_type(self, value):
        self._unit_type = value

    def mechanical_power(self):
        """Return the motor's mechanical power"""
        return round(self.input_power * 745.7, 2) if self.unit_type else round(self.input_power * 735.5, 2)

    def active_power(self):
        """Return the motor's active power"""
        return round(self.mechanical_power() / self.efficiency, 2)

    def properties(self):
        """the motor's properties"""
        return {
            "tag": self._tag,
            "input_power": self._input_power,
            "power_factor": self._input_power,
            "efficiency": self._efficiency,
            "unit_type": self._unit_type,
        }


class Socket(Load):
    def __init__(self, input_power=1.0, power_factor=1.0, qty=1, tag=None, idt=None):
        super().__init__(input_power, power_factor, tag, idt)
        self._tag = "Socket_" + self._tag
        assert (qty > 0 == (int(qty) - qty)), "Quantity must be integer greater than 0"
        self._qty = qty

    def active_power(self):
        """Return the input power's lighting"""
        return self.input_power * self.qty

    def properties(self):
        """the motor's properties"""
        return {
            "tag": self._tag,
            "input_power": self.input_power,
            "power_factor": self.power_factor,
            "qty": self.qty,
        }
